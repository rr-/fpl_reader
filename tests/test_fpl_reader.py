#!/bin/python3
import os
import datetime
import fpl_reader


def get_file(file_name):
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, 'rb') as handle:
        return handle.read()



def test_0_9_1():
    playlist = fpl_reader.read_playlist(get_file('1.0.3.fpl'))
    assert len(playlist.tracks) == 3
    t = playlist.tracks

    assert t[0].flags == 1
    assert t[0].subsong_index == 0
    assert t[0].file_name == b'file://C:\\Users\\Public\\Music\\Sample Music\\Kalimba.mp3'
    assert t[0].file_size == 8414449
    assert t[0].file_time == datetime.datetime(2009, 7, 14, 5, 32, 31)
    assert t[0].duration == 347.99126984126985
    assert t[0].primary_keys == {
        b'date': b'2008',
        b'title': b'Kalimba',
        b'artist': b'Mr. Scruff',
        b'band': b'Mr. Scruff',
        b'album': b'Ninja Tuna',
        b'genre': b'Electronic',
        b'publisher': b'Ninja Tune',
        b'composer': b'A. Carthy and A. Kingslow',
        b'comment': b'Ninja Tune Records',
    }
    assert t[0].secondary_keys == {
        b'tagtype': b'id3v2|id3v1',
        b'codec': b'MP3',
        b'mp3_stereo_mode': b'stereo',
        b'codec_profile': b'CBR',
        b'encoding': b'lossy',
        b'bitrate': b'192',
        b'samplerate': b'44100',
        b'channels': b'2',
    }

    assert t[1].flags == 1
    assert t[1].subsong_index == 0
    assert t[1].file_name == b'file://C:\\Users\\Public\\Music\\Sample Music\\Maid with the Flaxen Hair.mp3'
    assert t[1].file_size == 4113874
    assert t[1].file_time == datetime.datetime(2009, 7, 14, 5, 32, 31)
    assert t[1].duration == 169.65331065759636
    assert t[1].primary_keys == {
        b'date': b'2008',
        b'artist': b'Slovak Radio Symphony Orchestra',
        b'band': b'Richard Stoltzman',
        b'album': b'Fine Music, Vol. 1',
        b'genre': b'Classical',
        b'conductor': b'Kirk Trevor',
        b'composer': b'Claude Debussy',
        b'comment': b'Navona Records',
    }
    assert t[1].secondary_keys == {
        b'tagtype': b'id3v2|id3v1',
        b'codec': b'MP3',
        b'mp3_stereo_mode': b'stereo',
        b'codec_profile': b'CBR',
        b'encoding': b'lossy',
        b'bitrate': b'192',
        b'samplerate': b'44100',
        b'channels': b'2',
    }

    assert t[2].flags == 1
    assert t[2].subsong_index == 0
    assert t[2].file_name == b'file://C:\\Users\\Public\\Music\\Sample Music\\Sleep Away.mp3'
    assert t[2].file_size == 4842585
    assert t[2].file_time == datetime.datetime(2009, 7, 14, 5, 32, 31)
    assert t[2].duration == 200.53004535147392
    assert t[2].primary_keys == {
        b'date': b'2004',
        b'title': b'Sleep Away',
        b'artist': b'Bob Acri',
        b'band': b'Bob Acri',
        b'album': b'Bob Acri',
        b'genre': b'Other',
        b'composer': b'Robert R. Acri',
        b'comment': b'Blujazz Productions',
    }
    assert t[2].secondary_keys == {
        b'tagtype': b'id3v2|id3v1',
        b'codec': b'MP3',
        b'mp3_stereo_mode': b'stereo',
        b'codec_profile': b'CBR',
        b'encoding': b'lossy',
        b'bitrate': b'192',
        b'samplerate': b'44100',
        b'channels': b'2',
    }


def test_1_0_3():
    playlist = fpl_reader.read_playlist(get_file('1.0.3.fpl'))
    assert len(playlist.tracks) == 3
    t = playlist.tracks

    assert t[0].flags == 1
    assert t[0].subsong_index == 0
    assert t[0].file_name == b'file://C:\\Users\\Public\\Music\\Sample Music\\Kalimba.mp3'
    assert t[0].file_size == 8414449
    assert t[0].file_time == datetime.datetime(2009, 7, 14, 5, 32, 31)
    assert t[0].duration == 347.99126984126985
    assert t[0].primary_keys == {
        b'date': b'2008',
        b'title': b'Kalimba',
        b'artist': b'Mr. Scruff',
        b'band': b'Mr. Scruff',
        b'album': b'Ninja Tuna',
        b'genre': b'Electronic',
        b'publisher': b'Ninja Tune',
        b'composer': b'A. Carthy and A. Kingslow',
        b'comment': b'Ninja Tune Records',
    }
    assert t[0].secondary_keys == {
        b'tagtype': b'id3v2|id3v1',
        b'codec': b'MP3',
        b'mp3_stereo_mode': b'stereo',
        b'codec_profile': b'CBR',
        b'encoding': b'lossy',
        b'bitrate': b'192',
        b'samplerate': b'44100',
        b'channels': b'2',
    }

    assert t[1].flags == 1
    assert t[1].subsong_index == 0
    assert t[1].file_name == b'file://C:\\Users\\Public\\Music\\Sample Music\\Maid with the Flaxen Hair.mp3'
    assert t[1].file_size == 4113874
    assert t[1].file_time == datetime.datetime(2009, 7, 14, 5, 32, 31)
    assert t[1].duration == 169.65331065759636
    assert t[1].primary_keys == {
        b'date': b'2008',
        b'artist': b'Slovak Radio Symphony Orchestra',
        b'band': b'Richard Stoltzman',
        b'album': b'Fine Music, Vol. 1',
        b'genre': b'Classical',
        b'conductor': b'Kirk Trevor',
        b'composer': b'Claude Debussy',
        b'comment': b'Navona Records',
    }
    assert t[1].secondary_keys == {
        b'tagtype': b'id3v2|id3v1',
        b'codec': b'MP3',
        b'mp3_stereo_mode': b'stereo',
        b'codec_profile': b'CBR',
        b'encoding': b'lossy',
        b'bitrate': b'192',
        b'samplerate': b'44100',
        b'channels': b'2',
    }

    assert t[2].flags == 1
    assert t[2].subsong_index == 0
    assert t[2].file_name == b'file://C:\\Users\\Public\\Music\\Sample Music\\Sleep Away.mp3'
    assert t[2].file_size == 4842585
    assert t[2].file_time == datetime.datetime(2009, 7, 14, 5, 32, 31)
    assert t[2].duration == 200.53004535147392
    assert t[2].primary_keys == {
        b'date': b'2004',
        b'title': b'Sleep Away',
        b'artist': b'Bob Acri',
        b'band': b'Bob Acri',
        b'album': b'Bob Acri',
        b'genre': b'Other',
        b'composer': b'Robert R. Acri',
        b'comment': b'Blujazz Productions',
    }
    assert t[2].secondary_keys == {
        b'tagtype': b'id3v2|id3v1',
        b'codec': b'MP3',
        b'mp3_stereo_mode': b'stereo',
        b'codec_profile': b'CBR',
        b'encoding': b'lossy',
        b'bitrate': b'192',
        b'samplerate': b'44100',
        b'channels': b'2',
    }


def test_1_1_18():
    playlist = fpl_reader.read_playlist(get_file('1.1.18.fpl'))
    assert len(playlist.tracks) == 3
    t = playlist.tracks

    assert t[0].flags == 1
    assert t[0].subsong_index == 0
    assert t[0].file_name == b'file://C:\\Users\\Public\\Music\\Sample Music\\Kalimba.mp3'
    assert t[0].file_size == 8414449
    assert t[0].file_time == datetime.datetime(2009, 7, 14, 5, 32, 31)
    assert t[0].duration == 348.00326530612244
    assert t[0].primary_keys == {
        b'date': b'2008',
        b'title': b'Kalimba',
        b'artist': b'Mr. Scruff',
        b'album artist': b'Mr. Scruff',
        b'album': b'Ninja Tuna',
        b'genre': b'Electronic',
        b'publisher': b'Ninja Tune',
        b'composer': b'A. Carthy and A. Kingslow',
        b'comment': b'Ninja Tune Records',
    }
    assert t[0].secondary_keys == {
        b'tagtype': b'id3v2.3|id3v1',
        b'codec': b'MP3',
        b'mp3_stereo_mode': b'stereo',
        b'codec_profile': b'CBR',
        b'encoding': b'lossy',
        b'bitrate': b'192',
        b'samplerate': b'44100',
        b'channels': b'2',
    }

    assert t[1].flags == 1
    assert t[1].subsong_index == 0
    assert t[1].file_name == b'file://C:\\Users\\Public\\Music\\Sample Music\\Maid with the Flaxen Hair.mp3'
    assert t[1].file_size == 4113874
    assert t[1].file_time == datetime.datetime(2009, 7, 14, 5, 32, 31)
    assert t[1].duration == 169.66530612244898
    assert t[1].primary_keys == {
        b'date': b'2008',
        b'title': b'Maid with the Flaxen Hair',
        b'artist': b'Richard Stoltzman/Slovak Radio Symphony Orchestra',
        b'album artist': b'Richard Stoltzman',
        b'album': b'Fine Music, Vol. 1',
        b'genre': b'Classical',
        b'conductor': b'Kirk Trevor',
        b'composer': b'Claude Debussy',
        b'comment': b'Navona Records',
    }
    assert t[1].secondary_keys == {
        b'tagtype': b'id3v2.3|id3v1',
        b'codec': b'MP3',
        b'mp3_stereo_mode': b'stereo',
        b'codec_profile': b'CBR',
        b'encoding': b'lossy',
        b'bitrate': b'192',
        b'samplerate': b'44100',
        b'channels': b'2',
    }

    assert t[2].flags == 1
    assert t[2].subsong_index == 0
    assert t[2].file_name == b'file://C:\\Users\\Public\\Music\\Sample Music\\Sleep Away.mp3'
    assert t[2].file_size == 4842585
    assert t[2].file_time == datetime.datetime(2009, 7, 14, 5, 32, 31)
    assert t[2].duration == 200.54204081632653
    assert t[2].primary_keys == {
        b'date': b'2004',
        b'title': b'Sleep Away',
        b'artist': b'Bob Acri',
        b'album artist': b'Bob Acri',
        b'album': b'Bob Acri',
        b'genre': b'Jazz',
        b'composer': b'Robert R. Acri',
        b'comment': b'Blujazz Productions',
    }
    assert t[2].secondary_keys == {
        b'tagtype': b'id3v2.3|id3v1',
        b'codec': b'MP3',
        b'mp3_stereo_mode': b'stereo',
        b'codec_profile': b'CBR',
        b'encoding': b'lossy',
        b'bitrate': b'192',
        b'samplerate': b'44100',
        b'channels': b'2',
    }


def test_1_2_9():
    playlist = fpl_reader.read_playlist(get_file('1.2.9.fpl'))
    assert len(playlist.tracks) == 3
    t = playlist.tracks

    assert t[0].flags == 1
    assert t[0].subsong_index == 0
    assert t[0].file_name == b'file://C:\\Users\\Public\\Music\\Sample Music\\Kalimba.mp3'
    assert t[0].file_size == 8414449
    assert t[0].file_time == datetime.datetime(2009, 7, 14, 5, 32, 31)
    assert t[0].duration == 348.00326530612244
    assert t[0].primary_keys == {
        b'date': b'2008',
        b'title': b'Kalimba',
        b'artist': b'Mr. Scruff',
        b'album artist': b'Mr. Scruff',
        b'album': b'Ninja Tuna',
        b'genre': b'Electronic',
        b'publisher': b'Ninja Tune',
        b'composer': b'A. Carthy and A. Kingslow',
        b'comment': b'Ninja Tune Records',
    }
    assert t[0].secondary_keys == {
        b'tagtype': b'id3v2.3|id3v1',
        b'codec': b'MP3',
        b'mp3_stereo_mode': b'stereo',
        b'codec_profile': b'CBR',
        b'encoding': b'lossy',
        b'bitrate': b'192',
        b'samplerate': b'44100',
        b'channels': b'2',
    }

    assert t[1].flags == 1
    assert t[1].subsong_index == 0
    assert t[1].file_name == b'file://C:\\Users\\Public\\Music\\Sample Music\\Maid with the Flaxen Hair.mp3'
    assert t[1].file_size == 4113874
    assert t[1].file_time == datetime.datetime(2009, 7, 14, 5, 32, 31)
    assert t[1].duration == 169.66530612244898
    assert t[1].primary_keys == {
        b'date': b'2008',
        b'title': b'Maid with the Flaxen Hair',
        b'artist': b'Richard Stoltzman/Slovak Radio Symphony Orchestra',
        b'album artist': b'Richard Stoltzman',
        b'album': b'Fine Music, Vol. 1',
        b'genre': b'Classical',
        b'conductor': b'Kirk Trevor',
        b'composer': b'Claude Debussy',
        b'comment': b'Navona Records',
    }
    assert t[1].secondary_keys == {
        b'tagtype': b'id3v2.3|id3v1',
        b'codec': b'MP3',
        b'mp3_stereo_mode': b'stereo',
        b'codec_profile': b'CBR',
        b'encoding': b'lossy',
        b'bitrate': b'192',
        b'samplerate': b'44100',
        b'channels': b'2',
    }

    assert t[2].flags == 1
    assert t[2].subsong_index == 0
    assert t[2].file_name == b'file://C:\\Users\\Public\\Music\\Sample Music\\Sleep Away.mp3'
    assert t[2].file_size == 4842585
    assert t[2].file_time == datetime.datetime(2009, 7, 14, 5, 32, 31)
    assert t[2].duration == 200.54204081632653
    assert t[2].primary_keys == {
        b'date': b'2004',
        b'title': b'Sleep Away',
        b'artist': b'Bob Acri',
        b'album artist': b'Bob Acri',
        b'album': b'Bob Acri',
        b'genre': b'Jazz',
        b'composer': b'Robert R. Acri',
        b'comment': b'Blujazz Productions',
    }
    assert t[2].secondary_keys == {
        b'tagtype': b'id3v2.3|id3v1',
        b'codec': b'MP3',
        b'mp3_stereo_mode': b'stereo',
        b'codec_profile': b'CBR',
        b'encoding': b'lossy',
        b'bitrate': b'192',
        b'samplerate': b'44100',
        b'channels': b'2',
    }


def test_1_3_8():
    playlist = fpl_reader.read_playlist(get_file('1.3.8.fpl'))
    assert len(playlist.tracks) == 8
    t = playlist.tracks

    assert t[0].flags == 1
    assert t[0].file_name == b'http://stream1.opb.org:80/opbmusic_hbr.mp3'
    assert t[0].subsong_index == 0
    assert t[0].file_size == -1
    assert t[0].file_time == datetime.datetime(2014, 9, 29, 2, 25, 38)
    assert t[0].duration == -1.0
    assert t[0].rpg_album == -1000.0
    assert t[0].rpg_track == -1000.0
    assert t[0].rpk_album == -1.0
    assert t[0].rpk_track == -1.0
    assert t[0].primary_keys == {
        b'genre': b'Alternative',
        b'title': b'opbmusic.org',
    }
    assert t[0].secondary_keys == {
        b'codec': b'MP3',
        b'samplerate': b'44100',
        b'encoding': b'lossy',
        b'bitrate': b'128',
        b'channels': b'2',
        b'mp3_stereo_mode': b'joint stereo',
    }

    assert t[1].flags == 5
    assert t[1].file_name == b'http://sfstream1.somafm.com:8062/'
    assert t[1].subsong_index == 0
    assert t[1].file_size == -1
    assert t[1].file_time == datetime.datetime(2015, 2, 3, 17, 8, 25)
    assert t[1].duration == -1.0
    assert t[1].rpg_album == -1000.0
    assert t[1].rpg_track == -1000.0
    assert t[1].rpk_album == -1.0
    assert t[1].rpk_track == -1.0
    assert t[1].primary_keys == {
        b'url': b'http://SomaFM.com',
        b'genre': b'IDM',
        b'title': b"<-- cliqhop --> blips'n'bleeps backed w/ beats. [SomaFM]",
    }
    assert t[1].secondary_keys == {
        b'codec': b'MP3',
        b'samplerate': b'44100',
        b'encoding': b'lossy',
        b'bitrate': b'128',
        b'channels': b'2',
        b'mp3_stereo_mode': b'stereo',
    }

    assert t[2].flags == 5
    assert t[2].file_name == b'http://sfstream1.somafm.com:8900/'
    assert t[2].subsong_index == 0
    assert t[2].file_size == -1
    assert t[2].file_time == datetime.datetime(2014, 11, 24, 17, 39, 58)
    assert t[2].duration == -1.0
    assert t[2].rpg_album == -1000.0
    assert t[2].rpg_track == -1000.0
    assert t[2].rpk_album == -1.0
    assert t[2].rpk_track == -1.0
    assert t[2].primary_keys == {
        b'url': b'http://somafm.com',
        b'genre': b'Indie Post Rock',
        b'title': b'Digitalis. Analog rock, digitally-affected, to calm the agitated heart. [SomaFM]',
    }
    assert t[2].secondary_keys == {
        b'codec': b'MP3',
        b'samplerate': b'44100',
        b'encoding': b'lossy',
        b'bitrate': b'128',
        b'channels': b'2',
        b'mp3_stereo_mode': b'stereo',
    }

    t[3].flags == 5
    t[3].file_name == b'http://sfstream1.somafm.com:8384/'
    t[3].subsong_index == 0
    t[3].file_size == -1
    t[3].file_time == datetime.datetime(2014, 10, 6, 22, 41, 35)
    t[3].duration == -1.0
    t[3].rpg_album == -1000.0
    t[3].rpg_track == -1000.0
    t[3].rpk_album == -1.0
    t[3].rpk_track == -1.0
    t[3].primary_keys == {
        b'url': b'http://SomaFM.com/',
        b'genre': b'Downtempo House Techno',
        b'title': b'Beat Blender: A late night blend of deep-house & downtempo chill. [SomaFM]',
    }
    t[3].secondary_keys == {
        b'codec': b'MP3',
        b'samplerate': b'44100',
        b'encoding': b'lossy',
        b'bitrate': b'128',
        b'channels': b'2',
        b'mp3_stereo_mode': b'stereo',
    }

    t[4].flags == 5
    t[4].file_name == b'http://ice.somafm.com:80/groovesalad'
    t[4].subsong_index == 0
    t[4].file_size == -1
    t[4].file_time == datetime.datetime(2014, 1, 31, 15, 16, 54)
    t[4].duration == -1.0
    t[4].rpg_album == -1000.0
    t[4].rpg_track == -1000.0
    t[4].rpk_album == -1.0
    t[4].rpk_track == -1.0
    t[4].primary_keys == {
        b'url': b'http://somafm.com',
        b'genre': b'Ambient Chill',
        b'title': b'Groove Salad: a nicely chilled plate of ambient beats and grooves. [SomaFM]',
    }
    t[4].secondary_keys == {
        b'codec': b'MP3',
        b'samplerate': b'44100',
        b'encoding': b'lossy',
        b'bitrate': b'128',
        b'channels': b'2',
        b'mp3_stereo_mode': b'stereo',
    }

    t[5].flags == 5
    t[5].file_name == b'http://sfstream1.somafm.com:7400/'
    t[5].subsong_index == 0
    t[5].file_size == -1
    t[5].file_time == datetime.datetime(2014, 9, 28, 3, 27, 17)
    t[5].duration == -1.0
    t[5].rpg_album == -1000.0
    t[5].rpg_track == -1000.0
    t[5].rpk_album == -1.0
    t[5].rpk_track == -1.0
    t[5].primary_keys == {
        b'url': b'http://somafm.com',
        b'genre': b'Dubstep Dub',
        b'title': b'Future Folk: Indie Folk, Neobilly, Steampunk, Gaslight and the occasional folk classics. [SomaFM]',
    }
    t[5].secondary_keys == {
        b'codec': b'MP3',
        b'samplerate': b'44100',
        b'encoding': b'lossy',
        b'bitrate': b'128',
        b'channels': b'2',
        b'mp3_stereo_mode': b'stereo',
    }

    t[6].flags == 1
    t[6].file_name == b'http://fr6.ah.fm:443/'
    t[6].subsong_index == 0
    t[6].file_size == -1
    t[6].file_time == datetime.datetime(2014, 10, 6, 20, 45, 52)
    t[6].duration == -1.0
    t[6].rpg_album == -1000.0
    t[6].rpg_track == -1000.0
    t[6].rpk_album == -1.0
    t[6].rpk_track == -1.0
    t[6].primary_keys == {
        b'url': b'http://www.AH.FM',
        b'genre': b'Electronic',
        b'title': b'AH.FM - Leading Trance Radio',
    }
    t[6].secondary_keys == {
        b'codec': b'MP3',
        b'samplerate': b'44100',
        b'encoding': b'lossy',
        b'bitrate': b'192',
        b'channels': b'2',
        b'mp3_stereo_mode': b'stereo',
    }

    t[7].flags == 1
    t[7].file_name == b'http://xstream1.somafm.com:7400/'
    t[7].subsong_index == 0
    t[7].file_size == -1
    t[7].file_time == datetime.datetime(2015, 2, 3, 17, 38, 39)
    t[7].duration == -1.0
    t[7].rpg_album == -1000.0
    t[7].rpg_track == -1000.0
    t[7].rpk_album == -1.0
    t[7].rpk_track == -1.0
    t[7].primary_keys == {
        b'url': b'http://somafm.com',
        b'genre': b'Dubstep Dub',
        b'title': b'Future Folk: Indie Folk, Neobilly, Steampunk, Gaslight and the occasional folk classics. [SomaFM]',
    }
    t[7].secondary_keys == {
        b'codec': b'MP3',
        b'samplerate': b'44100',
        b'encoding': b'lossy',
        b'bitrate': b'128',
        b'channels': b'2',
        b'mp3_stereo_mode': b'stereo',
    }


def test_1_3_8_discontiguous_pkeys():
    playlist = fpl_reader.read_playlist(get_file('1.3.8-discontiguous-pkeys.fpl'))
    len(playlist.tracks) == 8
    t = playlist.tracks

    t[0].flags == 17
    t[0].file_name == b'http://stream1.opb.org:80/opbmusic_hbr.mp3'
    t[0].subsong_index == 0
    t[0].file_size == -1
    t[0].file_time == datetime.datetime(2015, 11, 11, 22, 25, 17)
    t[0].duration == -1.0
    t[0].rpg_album == -1000.0
    t[0].rpg_track == -1000.0
    t[0].rpk_album == -1.0
    t[0].rpk_track == -1.0
    t[0].primary_keys == {
        b'genre': b'Alternative',
        b'title': b'opbmusic.org',
    }
    t[0].secondary_keys == {
        b'codec': b'MP3',
        b'samplerate': b'44100',
        b'encoding': b'lossy',
        b'bitrate': b'128',
        b'channels': b'2',
        b'mp3_stereo_mode': b'joint stereo',
    }

    t[1].flags == 85
    t[1].file_name == b'http://sfstream1.somafm.com:8062/'
    t[1].subsong_index == 0
    t[1].file_size == -1
    t[1].file_time == datetime.datetime(2015, 11, 11, 22, 13, 9)
    t[1].duration == -1.0
    t[1].rpg_album == -1000.0
    t[1].rpg_track == -1000.0
    t[1].rpk_album == -1.0
    t[1].rpk_track == -1.0
    t[1].primary_keys == {
        b'url': b'http://SomaFM.com',
        b'genre': b'IDM',
        b'title': b"<-- cliqhop --> blips'n'bleeps backed w/ beats. [SomaFM]",
    }
    t[1].secondary_keys == {
        b'codec': b'MP3',
        b'samplerate': b'44100',
        b'encoding': b'lossy',
        b'bitrate': b'128',
        b'channels': b'2',
        b'mp3_stereo_mode': b'stereo',
    }

    t[2].flags == 85
    t[2].file_name == b'http://sfstream1.somafm.com:8900/'
    t[2].subsong_index == 0
    t[2].file_size == -1
    t[2].file_time == datetime.datetime(2015, 11, 9, 20, 23, 51)
    t[2].duration == -1.0
    t[2].rpg_album == -1000.0
    t[2].rpg_track == -1000.0
    t[2].rpk_album == -1.0
    t[2].rpk_track == -1.0
    t[2].primary_keys == {
        b'url': b'http://somafm.com',
        b'genre': b'Indie Post Rock',
        b'title': b'Digitalis. Analog rock, digitally-affected, to calm the agitated heart. [SomaFM]',
    }
    t[2].secondary_keys == {
        b'codec': b'MP3',
        b'samplerate': b'44100',
        b'encoding': b'lossy',
        b'bitrate': b'128',
        b'channels': b'2',
        b'mp3_stereo_mode': b'stereo',
    }

    t[3].flags == 85
    t[3].file_name == b'http://sfstream1.somafm.com:8384/'
    t[3].subsong_index == 0
    t[3].file_size == -1
    t[3].file_time == datetime.datetime(2014, 10, 6, 22, 41, 35)
    t[3].duration == -1.0
    t[3].rpg_album == -1000.0
    t[3].rpg_track == -1000.0
    t[3].rpk_album == -1.0
    t[3].rpk_track == -1.0
    t[3].primary_keys == {
        b'url': b'http://SomaFM.com/',
        b'genre': b'Downtempo House Techno',
        b'title': b'Beat Blender: A late night blend of deep-house & downtempo chill. [SomaFM]',
    }
    t[3].secondary_keys == {
        b'codec': b'MP3',
        b'samplerate': b'44100',
        b'encoding': b'lossy',
        b'bitrate': b'128',
        b'channels': b'2',
        b'mp3_stereo_mode': b'stereo',
    }

    t[4].flags == 85
    t[4].file_name == b'http://ice.somafm.com:80/groovesalad'
    t[4].subsong_index == 0
    t[4].file_size == -1
    t[4].file_time == datetime.datetime(2015, 11, 11, 19, 34, 52)
    t[4].duration == -1.0
    t[4].rpg_album == -1000.0
    t[4].rpg_track == -1000.0
    t[4].rpk_album == -1.0
    t[4].rpk_track == -1.0
    t[4].primary_keys == {
        b'url': b'http://somafm.com',
        b'genre': b'Ambient Chill',
        b'title': b'Groove Salad: a nicely chilled plate of ambient beats and grooves. [SomaFM]',
    }
    t[4].secondary_keys == {
        b'codec': b'MP3',
        b'samplerate': b'44100',
        b'encoding': b'lossy',
        b'bitrate': b'128',
        b'channels': b'2',
        b'mp3_stereo_mode': b'stereo',
    }

    t[5].flags == 85
    t[5].file_name == b'http://sfstream1.somafm.com:7400/'
    t[5].subsong_index == 0
    t[5].file_size == -1
    t[5].file_time == datetime.datetime(2015, 11, 11, 22, 25, 10)
    t[5].duration == -1.0
    t[5].rpg_album == -1000.0
    t[5].rpg_track == -1000.0
    t[5].rpk_album == -1.0
    t[5].rpk_track == -1.0
    t[5].primary_keys == {
        b'url': b'http://somafm.com',
        b'genre': b'Folk Indie Newgrass',
        b'title': b'Folk Forward: Indie Folk, Alt-folk and the occasional folk classics. [SomaFM]',
    }
    t[5].secondary_keys == {
        b'codec': b'MP3',
        b'samplerate': b'44100',
        b'encoding': b'lossy',
        b'bitrate': b'128',
        b'channels': b'2',
        b'mp3_stereo_mode': b'stereo',
    }

    t[6].flags == 17
    t[6].file_name == b'http://us.ah.fm:443/'
    t[6].subsong_index == 0
    t[6].file_size == -1
    t[6].file_time == datetime.datetime(2015, 11, 11, 22, 25, 11)
    t[6].duration == -1.0
    t[6].rpg_album == -1000.0
    t[6].rpg_track == -1000.0
    t[6].rpk_album == -1.0
    t[6].rpk_track == -1.0
    t[6].primary_keys == {
        b'url': b'http://www.AH.FM',
        b'genre': b'Electronic',
        b'title': b'AH.FM - Leading Trance Radio',
    }
    t[6].secondary_keys == {
        b'codec': b'MP3',
        b'samplerate': b'44100',
        b'encoding': b'lossy',
        b'bitrate': b'192',
        b'channels': b'2',
        b'mp3_stereo_mode': b'stereo',
    }

    t[7].flags == 17
    t[7].file_name == b'file://C:\\Users\\Public\\Music\\Sample Music\\Kalimba.mp3'
    t[7].subsong_index == 0
    t[7].file_size == 8414449
    t[7].file_time == datetime.datetime(2009, 7, 14, 5, 32, 31)
    t[7].duration == 348.00326530612244
    t[7].rpg_album == -1000.0
    t[7].rpg_track == -1000.0
    t[7].rpk_album == -1.0
    t[7].rpk_track == -1.0
    t[7].primary_keys == {
        b'album': b'Ninja Tuna',
        b'album artist': b'Mr. Scruff',
        b'artist': b'Mr. Scruff',
        b'comment': b'Ninja Tune Records',
        b'composer': b'A. Carthy and A. Kingslow',
        b'date': b'2008',
        b'genre': b'Electronic',
        b'publisher': b'Ninja Tune',
        b'title': b'Kalimba',
    }
    t[7].secondary_keys == {
        b'codec': b'MP3',
        b'codec_profile': b'CBR',
        b'samplerate': b'44100',
        b'encoding': b'lossy',
        b'bitrate': b'192',
        b'channels': b'2',
        b'tagtype': b'id3v2.3|id3v1',
        b'mp3_stereo_mode': b'stereo',
    }


def test_1_3_8_missing_meta():
    playlist = fpl_reader.read_playlist(get_file('1.3.8-missing-meta.fpl'))
    len(playlist.tracks) == 2
    t = playlist.tracks

    t[0].flags == 0
    t[0].file_name == b'http://sfstream1.somafm.com:8900/'
    t[0].file_size == None
    t[0].file_time == None
    t[0].subsong_index == 0
    t[0].duration == None
    t[0].rpg_album == None
    t[0].rpg_track == None
    t[0].rpk_album == None
    t[0].rpk_track == None
    t[0].primary_keys == {}
    t[0].secondary_keys == {}

    t[1].flags == 19
    t[1].file_name == b'file://src\\vntools.other\\HCA_decoder\\hca_quality_samples\\sample.wav'
    t[1].file_size == 1341248
    t[1].file_time == datetime.datetime(2014, 9, 12, 18, 52, 29)
    t[1].subsong_index == 0
    t[1].duration == 6.9854375
    t[1].rpg_album == -1000.0
    t[1].rpg_track == -1000.0
    t[1].rpk_album == -1.0
    t[1].rpk_track == -1.0
    t[1].primary_keys == {}
    t[1].secondary_keys == {
        b'bitrate': b'1536',
        b'bitspersample': b'16',
        b'channels': b'2',
        b'codec': b'PCM',
        b'encoding': b'lossless',
        b'samplerate': b'48000',
    }


def test_1_3_9():
    playlist = fpl_reader.read_playlist(get_file('1.2.9.fpl'))
    len(playlist.tracks) == 3
    t = playlist.tracks

    assert t[0].flags == 1
    assert t[0].subsong_index == 0
    assert t[0].file_name == b'file://C:\\Users\\Public\\Music\\Sample Music\\Kalimba.mp3'
    assert t[0].file_size == 8414449
    assert t[0].file_time == datetime.datetime(2009, 7, 14, 5, 32, 31)
    assert t[0].duration == 348.00326530612244
    assert t[0].primary_keys == {
        b'date': b'2008',
        b'title': b'Kalimba',
        b'artist': b'Mr. Scruff',
        b'album artist': b'Mr. Scruff',
        b'album': b'Ninja Tuna',
        b'genre': b'Electronic',
        b'publisher': b'Ninja Tune',
        b'composer': b'A. Carthy and A. Kingslow',
        b'comment': b'Ninja Tune Records',
    }
    assert t[0].secondary_keys == {
        b'tagtype': b'id3v2.3|id3v1',
        b'codec': b'MP3',
        b'mp3_stereo_mode': b'stereo',
        b'codec_profile': b'CBR',
        b'encoding': b'lossy',
        b'bitrate': b'192',
        b'samplerate': b'44100',
        b'channels': b'2',
    }

    assert t[1].flags == 1
    assert t[1].subsong_index == 0
    assert t[1].file_name == b'file://C:\\Users\\Public\\Music\\Sample Music\\Maid with the Flaxen Hair.mp3'
    assert t[1].file_size == 4113874
    assert t[1].file_time == datetime.datetime(2009, 7, 14, 5, 32, 31)
    assert t[1].duration == 169.66530612244898
    assert t[1].primary_keys == {
        b'date': b'2008',
        b'title': b'Maid with the Flaxen Hair',
        b'artist': b'Richard Stoltzman/Slovak Radio Symphony Orchestra',
        b'album artist': b'Richard Stoltzman',
        b'album': b'Fine Music, Vol. 1',
        b'genre': b'Classical',
        b'conductor': b'Kirk Trevor',
        b'composer': b'Claude Debussy',
        b'comment': b'Navona Records',
    }
    assert t[1].secondary_keys == {
        b'tagtype': b'id3v2.3|id3v1',
        b'codec': b'MP3',
        b'mp3_stereo_mode': b'stereo',
        b'codec_profile': b'CBR',
        b'encoding': b'lossy',
        b'bitrate': b'192',
        b'samplerate': b'44100',
        b'channels': b'2',
    }

    assert t[2].flags == 1
    assert t[2].subsong_index == 0
    assert t[2].file_name == b'file://C:\\Users\\Public\\Music\\Sample Music\\Sleep Away.mp3'
    assert t[2].file_size == 4842585
    assert t[2].file_time == datetime.datetime(2009, 7, 14, 5, 32, 31)
    assert t[2].duration == 200.54204081632653
    assert t[2].primary_keys == {
        b'date': b'2004',
        b'title': b'Sleep Away',
        b'artist': b'Bob Acri',
        b'album artist': b'Bob Acri',
        b'album': b'Bob Acri',
        b'genre': b'Jazz',
        b'composer': b'Robert R. Acri',
        b'comment': b'Blujazz Productions',
    }
    assert t[2].secondary_keys == {
        b'tagtype': b'id3v2.3|id3v1',
        b'codec': b'MP3',
        b'mp3_stereo_mode': b'stereo',
        b'codec_profile': b'CBR',
        b'encoding': b'lossy',
        b'bitrate': b'192',
        b'samplerate': b'44100',
        b'channels': b'2',
    }
