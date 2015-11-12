# FPL Format Documentation

The FPL playlist is a 32-bit little-endian word-oriented binary file format
that stores track file locations and track metadata. It was created by Peter
Pawlowski, the author of foobar2000. It is intentionally undocumented by the
foobar2000 project with the following disclaimer presented [(source)][0]:

> The FPL format is not meant to be interchangeable with other software or
> editable by users. Its primary design goals are carrying all necessary track
> information (metadata, last seen modification time, etc.) between foobar2000
> sessions while remaining as fast to read and write as possible, since
> reading/writing FPL files bottlenecks app startup and shutdown with large
> Media Library or playlists. Making the FPL format user-editable would
> introduce massive startup/shutdown delays for certain users.
> 
> Additionally, the format is strictly tied to foobar2000 track information
> caching architecture; potential design changes in that area in future
> foobar2000 versions will inevitably require a new non-backwards-compatible
> revision of the FPL format.

This project is an effort to reverse engineer, document, and implement a
parser for this format. Previous efforts have been made (see References at the
end of this document) but they do not seem to be complete.

## Compatibility

This project intends to support playlists created by foobar2000 v0.9.1 and
newer. If you create a playlist file that can't be parsed correctly, please
get in touch.

## Playlist

The following fields make up a complete 'playlist', in order:

    0. magic        (16 bytes)
    1. meta_size    (4 bytes)
    2. meta         ($meta_size bytes)
    3. track_count  (4 bytes)
    4. track(s)     ($track_count 'track' fields, which are variable-sized)

### magic

The 'magic' field is a 16-byte magic number. It is always set to the
following hexadecimal values:

    E1 A0 9C 91 F8 3C 77 42 85 2C 3B CC 14 01 D3 F2

### meta_size

The 'meta_size' field informs the reader how many bytes are filled by the
variable-sized 'meta' field.

### meta

The 'meta' field is a variable-sized concatenation of null-terminated strings.
Its size is given by the value in the 'meta_size' field. A track will use
key:value pairs as a means to provide track metadata; the track filename, key
names, and value data are all stored in the 'meta' field. This field appears
to be deduplicated and if more than one track shares a metadata string, each
will point to the same 'meta' offset.

### track_count

The 'track_count' informs the reader of how many tracks are represented in the
variable-sized track field.

### track(s)

The following fields make up a complete 'track', in order:

    0.  flags               (4 bytes)
    1.  file_name_offset    (4 bytes)
    2.  subsong_index       (4 bytes)
    3.  file_size           (4 bytes)
    4.  unk2                (4 bytes)
    5.  file_time           (8 bytes)
    6.  duration            (8 bytes)
    7.  rpg_album           (4 bytes)
    8.  rpg_track           (4 bytes)
    9.  rpk_album           (4 bytes)
    10. rpk_track           (4 bytes)
    11. entry_count         (4 bytes)
    12. entries             (4 * $entry_count bytes)
    13. padding             (optional, 64 bytes)

#### track.flags

Based on experimentation, 'flags' might be a collection of bits that indicate
the existence of certain attributes for a track depending on whether the bit
is set or not. These are the bits we think we understand:

0x01: When set, indicates the track has metadata. If this bit is unset, the
reader should assume this track has been completely read. Only the
'file_name_offset' and 'subsong_index' fields will be present, and the 'track'
field will conclude after 'subsong_index'.

0x04: When set, indicates the presence of 64 bytes of unknown purpose
following the 'entries' field. When unset, the 'track' field concludes
directly following 'entries'.

Other flags that have been seen but whose purpose remains a mystery:

    0x02    (1.3.8-missing-meta.fpl)
    0x10    (1.3.9-discontiguous-pkeys.fpl)
    0x40    (1.3.9-discontiguous-pkeys.fpl)

#### track.file_name_offset

The 'file_name_offset' field informs the reader of the offset (in bytes) from
the start of the 'meta' field at which the null-terminated string containing
the track's file name or location can be found.

#### track.subsong_index

The 'subsong_index' is used to identify the track's subsong, which is needed
in situations where a single file contains multiple songs.

#### track.file_size

The 'file_size' field contains the size of the track's file in bytes.

#### track.unk2

Not sure what this field does.

#### track.file_time

The 'file_time' field contains the last-modified time of the track file. It is
represented in 64-bit Windows Ticks, which is the count of 100-nanosecond
intervals that have elapsed since 12:00:00 midnight, January 1, 0001 (0:00:00
UTC on January 1, 0001, in the Gregorian calendar.

#### track.duration

The 'duration' field contains the playtime of the track in seconds. This is in
64-bit Windows Ticks like the 'file_time' field.

#### track.rpg_album, track.rpg_track, track.rpk_album, track.rpk_track

The 'rp{g,k}_{album,track}' fields contain replaygain and replaygain peak
information for the album and track respectively. These are floating-point
values.

#### track.entry_count

The 'entry_count' counts the number of keys and values that follow in the
'entries' field. Each key and value is 4 bytes each, so the current 'track'
field concludes 4*entry_count bytes after the entry_count (unless the optional
padding bytes are present).

#### track.entries

The 'entries' field is 4*entry_count bytes long. It is a collection of key and
value pairs that are comprised of offsets into the 'meta' field. The key's
offset points to the key's name, and the value's offset points to the value's
data.  The name and data are both null-terminated strings in the 'meta' field.

The following fields make up an 'entries' field, in order:

    0. primary_key_count    (4 bytes)
    1. secondary_key_count  (4 bytes)
    2. secondary_key_offset (4 bytes)
    4. primary_keys         (4 * 2 * $primary_key_count bytes)
    5. unk5                 (4 bytes)
    6. primary_values       (4 * $primary_key_count bytes)
    7. secondary_keys       (4 * 2 * $secondary_key_count bytes)

##### primary_key_count

The 'primary_key_count' field indicates the number of primary key:value
relationships that exist. This field can be used to calculate the length of
the upcoming 'primary_keys' and 'primary_values' fields.

##### secondary_key_count

The 'secondary_key_count' field indicates the number of secondary key_value
relationships that exist. This field can be used to calculate the length of
the upcoming 'secondary_keys' field.

##### secondary_key_offset

The 'secondary_key_offset' field identifies the offset of the start of the
'secondary_keys' field. The offset is given in 32-bit words, not bytes.

##### primary_keys 

The 'primary_keys' field is comprised of two 32-bit words for each primary key
counted by the 'primary_key_count' field.

The first word contains an integer starting at zero and increasing for each
subsequent key. The purpose of the leading integer is not fully understood.
It's incrementation may be discontiguous - gaps in the count have been
observed.

The second word contains an offset (in bytes) starting at the beginning of the
'meta' field at which a null-terminated string may be found. This string is
the key's name.

##### unk5 

The 'unk5' field is a single 32-bit word that hasn't served a purpose, but it
has so far always been a continuation of the first-word increment that occurs
in the preceding series of primary keys.

##### primary_values 

The 'primary_values' field is a series of 32-bit words. There will be one word
for each of the primary keys counted by 'primary_key_count'. Each contains an
offset (in bytes) starting at the beginning of the 'meta' field at which a
null-terminated string can be found. This string is the data that should be
associated with the primary key of the same key index.

In the event of a discontiguous count of the 'primary_keys' leading word, the
absent value will cause a duplication of the previous 'primary_values' field
in order to fill the gap. Example of discontiguity starting from the beginning
of the 'primary_keys' field:

    0,k0, 1,k1, 2,k2, 4,k4, unk5, v0, v1, v2, v2, v4

Notice that 3,k3 is missing from 'primary_keys',  and therefore v2 is
duplicated to fill the gap.

To assemble a primary key:value, the key name should be taken by following the
offset found in the 'primary_keys' field, and the value data should be taken
by following the offset found in the corresponding word in the
'primary_values' field.

##### secondary_keys

The 'secondary_keys' field is comprised of pairs of 32-bit words, one pair per
key:value set. The start of this field will be located at the position
indicated by the 'secondary_key_offset' which is an offset (in 32-bit words)
from the start of the 'primary_keys' field.

The first word is an offset (in bytes) from the beginning of the 'meta' field
at which a null-terminated string can be found. This string is the key name.

The second word operates similarly and provides the location of the value data
for this key.

#### padding

If a track contains padding, it is always 64 bytes, and its presence is
indicated by bit 0x04 in the 'flags' field. The purpose of the 'padding' field
is currently unknown.

# References

Earlier implementations and discussion:

* [tetrisfrog's fplreader repo on Github][1]
* [Discussion on hydrogenaudio forums][2]

[0]: https://www.foobar2000.org/FAQ#other_questions
[1]: https://github.com/tetrisfrog/fplreader
[2]: https://www.hydrogenaud.io/forums/index.php?showtopic=43673

