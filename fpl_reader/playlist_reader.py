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
    def __init__(self):
        super(Track, self).__init__()
        self.flags = None
        self.subsong_index = None
        self.file_name = None
        self.file_size = None
        self.file_time = None
        self.duration = None
        self.rpg_album = None
        self.rpg_track = None
        self.rpk_album = None
        self.rpk_track = None
        self.primary_keys = {}
        self.secondary_keys = {}

def read_track(track_no, meta_io, index_io):
    track = Track()
    track.flags = index_io.read_s32_le()
    file_name_offset = index_io.read_u32_le()
    with meta_io.peek(file_name_offset):
        track.file_name = meta_io.read_to_zero()
    track.subsong_index = index_io.read_u32_le()
    if track.flags & 1 == 0:
        # e.g. stream that was never played, so it has no meta
        return track
    track.file_size = index_io.read_s32_le()
    unk2 = index_io.read_s32_le()

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
    unk5 = entries[secondary_key_offset - 1]

    track.primary_keys = {}
    real_key = 0
    for i in range(primary_key_count):
        # Primary keys not guaranteed to be contiguous. In this case, reuse
        # the previous key.
        if entries[3+real_key*2] == i:
            key_offset = entries[3+real_key*2+1]
            real_key += 1
            with meta_io.peek(key_offset):
                key = meta_io.read_to_zero()
        elif i == 0:
            raise RuntimeError('Missing first primary key, what now?')

        # Primary values seem to be contiguous even if the keys are not
        value_offset = entries[3+2*primary_key_count+1+i]
        with meta_io.peek(value_offset):
            value = meta_io.read_to_zero()

        # foobar2000's properties window duplicates and concatenates the value
        # when discontiguous keys are detected; we do not.
        track.primary_keys[key] = value

    track.secondary_keys = {}
    for i in range(secondary_key_count):
        key_offset = entries[3+secondary_key_offset+i*2]
        value_offset = entries[3+secondary_key_offset+i*2+1]
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
