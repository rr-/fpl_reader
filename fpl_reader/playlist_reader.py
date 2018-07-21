from fpl_reader.pseudo_object import PseudoObject
from fpl_reader.cool_io import CoolIO
from fpl_reader.windows_time import get_time_from_ticks


class Playlist:
    def __init__(self, tracks):
        self.tracks = tracks

    def __repr__(self):
        return (
            'Playlist([\n'
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


def read_track(meta_io, index_io):
    track = Track()
    track.flags = index_io.read_s32_le()
    file_name_offset = index_io.read_u32_le()
    track.file_name = meta_io.seek(file_name_offset).read_to_zero()
    track.subsong_index = index_io.read_u32_le()
    if track.flags & 1 == 0:
        # e.g. stream that was never played, so it has no meta
        return track
    track.file_size = index_io.read_s64_le()

    track.file_time = get_time_from_ticks(index_io.read_u64_le())
    track.duration = index_io.read_f64()
    track.rpg_album = index_io.read_f32()
    track.rpg_track = index_io.read_f32()
    track.rpk_album = index_io.read_f32()
    track.rpk_track = index_io.read_f32()
    entry_count = index_io.read_u32_le()
    entries = [index_io.read_u32_le() for i in range(entry_count)]

    primary_key_count = entries.pop(0)
    secondary_key_count = entries.pop(0)
    secondary_keys_offset = entries.pop(0)

    primary_key_name_offsets = {}
    for _ in range(primary_key_count):
        key_name_id = entries.pop(0)
        key_name_offset = entries.pop(0)
        primary_key_name_offsets[key_name_id] = key_name_offset
    entries.pop(0)  # unk0
    primary_key_value_offsets = [
        entries.pop(0)
        for _ in range(primary_key_count)
    ]

    track.primary_keys = {}
    last_key_offset = None
    for i in range(primary_key_count):
        # foobar2000's properties window duplicates and concatenates the value
        # when discontiguous keys are detected; we do not.
        last_key_offset = primary_key_name_offsets.get(i, last_key_offset)
        value_offset = primary_key_value_offsets[i]

        if last_key_offset is None:
            raise RuntimeError('Missing first primary key, now what?')

        key = meta_io.seek(last_key_offset).read_to_zero()
        value = meta_io.seek(value_offset).read_to_zero()
        track.primary_keys[key] = value

    assert primary_key_count * 3 + 1 <= secondary_keys_offset
    for i in range(secondary_keys_offset - (primary_key_count * 3 + 1)):
        entries.pop(0)

    track.secondary_keys = {}
    for i in range(secondary_key_count):
        key_offset = entries.pop(0)
        value_offset = entries.pop(0)
        key = meta_io.seek(key_offset).read_to_zero()
        value = meta_io.seek(value_offset).read_to_zero()
        track.secondary_keys[key] = value

    if track.flags & 0x04:
        _padding = index_io.read(64)

    return track


def read_playlist(data):
    magic = b'\xE1\xA0\x9C\x91\xF8\x3C\x77\x42\x85\x2C\x3B\xCC\x14\x01\xD3\xF2'

    tracks = []
    with CoolIO(data) as handle:
        if handle.read(len(magic)) != magic:
            raise RuntimeError('Not a FPL file')
        meta_size = handle.read_u32_le()
        meta = handle.read(meta_size)
        track_count = handle.read_u32_le()

        with CoolIO(meta) as meta_io, CoolIO(handle.read_to_eof()) as index_io:
            for track_no in range(track_count):
                track = read_track(meta_io, index_io)
                tracks.append(track)

    return Playlist(tracks)
