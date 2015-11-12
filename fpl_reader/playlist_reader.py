from fpl_reader.pseudo_object import PseudoObject
from fpl_reader.cool_io import CoolIO
from fpl_reader.windows_time import get_time_from_ticks


class Playlist(object):
    def __init__(self, tracks):
        self.tracks = tracks

    def __repr__(self):
        return ('Playlist([\n'
            + ',\n\n'.join(repr(track) for track in self.tracks)
            + '\n])')

class Track(PseudoObject):
    pass

def read_track(track_no, meta_io, index_io):
    track = Track()
    track.flags = index_io.read_s32_le()
    file_name_offset = index_io.read_u32_le()
    with meta_io.peek(file_name_offset):
        track.file_name = meta_io.read_to_zero()
    track.subsong_index = index_io.read_u32_le()
    track.file_size = index_io.read_s32_le()
    track.unk2 = index_io.read_s32_le()

    if track.unk2 != 0 and track.unk2 != -1:
        print('I bet the file is truncated right after this...!')

    track.file_time = get_time_from_ticks(index_io.read_u64_le())
    track.duration = index_io.read_f64()
    track.rpg_album = index_io.read_f32()
    track.rpg_track = index_io.read_f32()
    track.rpk_album = index_io.read_f32()
    track.rpk_track = index_io.read_f32()
    entry_count = index_io.read_u32_le()
    entries = [index_io.read_u32_le() for i in range(entry_count)]

    primary_key_count, \
    secondary_key_count, \
    secondary_key_offset = entries[0:3]
    track.unk5 = entries[secondary_key_offset - 1]

    track.primary_keys = {}
    for i in range(primary_key_count):
        if entries[3+i*2] != i:
            raise RuntimeError('Corrupt secondary key offset')
        key_offset = entries[3+i*2+1]
        with meta_io.peek(key_offset):
            key = meta_io.read_to_zero()
        value_offset = entries[3+2*primary_key_count+1+i]
        with meta_io.peek(value_offset):
            value = meta_io.read_to_zero()
        track.primary_keys[key] = value

    track.secondary_keys = {}
    for i in range(secondary_key_count):
        key_offset = entries[secondary_key_offset+i*2+primary_key_count]
        value_offset = entries[secondary_key_offset+i*2+primary_key_count+1]
        with meta_io.peek(key_offset):
            key = meta_io.read_to_zero()
        with meta_io.peek(value_offset):
            value = meta_io.read_to_zero()
        track.secondary_keys[key] = value

    if track.flags & 0x04:
        track.padding = index_io.read(64)

    return track


def read_playlist(data):
    magic = b'\xE1\xA0\x9C\x91\xF8\x3C\x77\x42\x85\x2C\x3B\xCC\x14\x01\xD3\xF2'

    tracks = []
    with CoolIO(data) as fh:
        if fh.read(len(magic)) != magic:
            raise RuntimeError('Not a FPL file')
        meta_size = fh.read_u32_le()
        meta = fh.read(meta_size)
        track_count = fh.read_u32_le()

        with CoolIO(meta) as meta_io, \
            CoolIO(fh.read_to_eof()) as index_io:

            for track_no in range(track_count):
                track = read_track(track_no, meta_io, index_io)
                tracks.append(track)

    return Playlist(tracks)
