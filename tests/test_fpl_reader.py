#!/bin/python3
import os
import datetime
import unittest
import fpl_reader


def get_file(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name), 'rb') as handle:
        return handle.read()

class TestSequenceFunctions(unittest.TestCase):
    def test_138(self):
        playlist = fpl_reader.read_playlist(get_file('1.3.8.fpl'))
        self.assertEqual(len(playlist.tracks), 8)
        t = playlist.tracks

        self.assertEqual(t[0].flags, 1)
        self.assertEqual(t[0].file_name, b'http://stream1.opb.org:80/opbmusic_hbr.mp3')
        self.assertEqual(t[0].subsong_index, 0)
        self.assertEqual(t[0].file_size, -1)
        self.assertEqual(t[0].file_time, datetime.datetime(2014, 9, 29, 2, 25, 38))
        self.assertEqual(t[0].duration, -1.0)
        self.assertEqual(t[0].rpg_album, -1000.0)
        self.assertEqual(t[0].rpg_track, -1000.0)
        self.assertEqual(t[0].rpk_album, -1.0)
        self.assertEqual(t[0].rpk_track, -1.0)
        self.assertEqual(t[0].primary_keys, {
            b'genre': b'Alternative',
            b'title': b'opbmusic.org'})
        self.assertEqual(t[0].secondary_keys, {
            b'codec':           b'MP3',
            b'samplerate':      b'44100',
            b'encoding':        b'lossy',
            b'bitrate':         b'128',
            b'channels':        b'2',
            b'mp3_stereo_mode': b'joint stereo'})

        self.assertEqual(t[1].flags, 5)
        self.assertEqual(t[1].file_name, b'http://sfstream1.somafm.com:8062/')
        self.assertEqual(t[1].subsong_index, 0)
        self.assertEqual(t[1].file_size, -1)
        self.assertEqual(t[1].file_time, datetime.datetime(2015, 2, 3, 17, 8, 25))
        self.assertEqual(t[1].duration, -1.0)
        self.assertEqual(t[1].rpg_album, -1000.0)
        self.assertEqual(t[1].rpg_track, -1000.0)
        self.assertEqual(t[1].rpk_album, -1.0)
        self.assertEqual(t[1].rpk_track, -1.0)
        self.assertEqual(t[1].primary_keys, {
            b'url':   b'http://SomaFM.com',
            b'genre': b'IDM',
            b'title': b"<-- cliqhop --> blips'n'bleeps backed w/ beats. [SomaFM]"})
        self.assertEqual(t[1].secondary_keys, {
            b'codec':           b'MP3',
            b'samplerate':      b'44100',
            b'encoding':        b'lossy',
            b'bitrate':         b'128',
            b'channels':        b'2',
            b'mp3_stereo_mode': b'stereo'})

        self.assertEqual(t[2].flags, 5)
        self.assertEqual(t[2].file_name, b'http://sfstream1.somafm.com:8900/')
        self.assertEqual(t[2].subsong_index, 0)
        self.assertEqual(t[2].file_size, -1)
        self.assertEqual(t[2].file_time, datetime.datetime(2014, 11, 24, 17, 39, 58))
        self.assertEqual(t[2].duration, -1.0)
        self.assertEqual(t[2].rpg_album, -1000.0)
        self.assertEqual(t[2].rpg_track, -1000.0)
        self.assertEqual(t[2].rpk_album, -1.0)
        self.assertEqual(t[2].rpk_track, -1.0)
        self.assertEqual(t[2].primary_keys, {
            b'url':   b'http://somafm.com',
            b'genre': b'Indie Post Rock',
            b'title': b'Digitalis. Analog rock, digitally-affected, to calm the agitated heart. [SomaFM]'})
        self.assertEqual(t[2].secondary_keys, {
            b'codec':           b'MP3',
            b'samplerate':      b'44100',
            b'encoding':        b'lossy',
            b'bitrate':         b'128',
            b'channels':        b'2',
            b'mp3_stereo_mode': b'stereo'})

        self.assertEqual(t[3].flags, 5)
        self.assertEqual(t[3].file_name, b'http://sfstream1.somafm.com:8384/')
        self.assertEqual(t[3].subsong_index, 0)
        self.assertEqual(t[3].file_size, -1)
        self.assertEqual(t[3].file_time, datetime.datetime(2014, 10, 6, 22, 41, 35))
        self.assertEqual(t[3].duration, -1.0)
        self.assertEqual(t[3].rpg_album, -1000.0)
        self.assertEqual(t[3].rpg_track, -1000.0)
        self.assertEqual(t[3].rpk_album, -1.0)
        self.assertEqual(t[3].rpk_track, -1.0)
        self.assertEqual(t[3].primary_keys, {
            b'url':   b'http://SomaFM.com/',
            b'genre': b'Downtempo House Techno',
            b'title': b'Beat Blender: A late night blend of deep-house & downtempo chill. [SomaFM]'})
        self.assertEqual(t[3].secondary_keys, {
            b'codec':           b'MP3',
            b'samplerate':      b'44100',
            b'encoding':        b'lossy',
            b'bitrate':         b'128',
            b'channels':        b'2',
            b'mp3_stereo_mode': b'stereo'})

        self.assertEqual(t[4].flags, 5)
        self.assertEqual(t[4].file_name, b'http://ice.somafm.com:80/groovesalad')
        self.assertEqual(t[4].subsong_index, 0)
        self.assertEqual(t[4].file_size, -1)
        self.assertEqual(t[4].file_time, datetime.datetime(2014, 1, 31, 15, 16, 54))
        self.assertEqual(t[4].duration, -1.0)
        self.assertEqual(t[4].rpg_album, -1000.0)
        self.assertEqual(t[4].rpg_track, -1000.0)
        self.assertEqual(t[4].rpk_album, -1.0)
        self.assertEqual(t[4].rpk_track, -1.0)
        self.assertEqual(t[4].primary_keys, {
            b'url':   b'http://somafm.com',
            b'genre': b'Ambient Chill',
            b'title': b'Groove Salad: a nicely chilled plate of ambient beats and grooves. [SomaFM]'})
        self.assertEqual(t[4].secondary_keys, {
            b'codec':           b'MP3',
            b'samplerate':      b'44100',
            b'encoding':        b'lossy',
            b'bitrate':         b'128',
            b'channels':        b'2',
            b'mp3_stereo_mode': b'stereo'})

        self.assertEqual(t[5].flags, 5)
        self.assertEqual(t[5].file_name, b'http://sfstream1.somafm.com:7400/')
        self.assertEqual(t[5].subsong_index, 0)
        self.assertEqual(t[5].file_size, -1)
        self.assertEqual(t[5].file_time, datetime.datetime(2014, 9, 28, 3, 27, 17))
        self.assertEqual(t[5].duration, -1.0)
        self.assertEqual(t[5].rpg_album, -1000.0)
        self.assertEqual(t[5].rpg_track, -1000.0)
        self.assertEqual(t[5].rpk_album, -1.0)
        self.assertEqual(t[5].rpk_track, -1.0)
        self.assertEqual(t[5].primary_keys, {
            b'url':   b'http://somafm.com',
            b'genre': b'Dubstep Dub',
            b'title': b'Future Folk: Indie Folk, Neobilly, Steampunk, Gaslight and the occasional folk classics. [SomaFM]'})
        self.assertEqual(t[5].secondary_keys, {
            b'codec':           b'MP3',
            b'samplerate':      b'44100',
            b'encoding':        b'lossy',
            b'bitrate':         b'128',
            b'channels':        b'2',
            b'mp3_stereo_mode': b'stereo'})

        self.assertEqual(t[6].flags, 1)
        self.assertEqual(t[6].file_name, b'http://fr6.ah.fm:443/')
        self.assertEqual(t[6].subsong_index, 0)
        self.assertEqual(t[6].file_size, -1)
        self.assertEqual(t[6].file_time, datetime.datetime(2014, 10, 6, 20, 45, 52))
        self.assertEqual(t[6].duration, -1.0)
        self.assertEqual(t[6].rpg_album, -1000.0)
        self.assertEqual(t[6].rpg_track, -1000.0)
        self.assertEqual(t[6].rpk_album, -1.0)
        self.assertEqual(t[6].rpk_track, -1.0)
        self.assertEqual(t[6].primary_keys, {
            b'url':   b'http://www.AH.FM',
            b'genre': b'Electronic',
            b'title': b'AH.FM - Leading Trance Radio'})
        self.assertEqual(t[6].secondary_keys, {
            b'codec':           b'MP3',
            b'samplerate':      b'44100',
            b'encoding':        b'lossy',
            b'bitrate':         b'192',
            b'channels':        b'2',
            b'mp3_stereo_mode': b'stereo'})

        self.assertEqual(t[7].flags, 1)
        self.assertEqual(t[7].file_name, b'http://xstream1.somafm.com:7400/')
        self.assertEqual(t[7].subsong_index, 0)
        self.assertEqual(t[7].file_size, -1)
        self.assertEqual(t[7].file_time, datetime.datetime(2015, 2, 3, 17, 38, 39))
        self.assertEqual(t[7].duration, -1.0)
        self.assertEqual(t[7].rpg_album, -1000.0)
        self.assertEqual(t[7].rpg_track, -1000.0)
        self.assertEqual(t[7].rpk_album, -1.0)
        self.assertEqual(t[7].rpk_track, -1.0)
        self.assertEqual(t[7].primary_keys, {
            b'url':   b'http://somafm.com',
            b'genre': b'Dubstep Dub',
            b'title': b'Future Folk: Indie Folk, Neobilly, Steampunk, Gaslight and the occasional folk classics. [SomaFM]'})
        self.assertEqual(t[7].secondary_keys, {
            b'codec':           b'MP3',
            b'samplerate':      b'44100',
            b'encoding':        b'lossy',
            b'bitrate':         b'128',
            b'channels':        b'2',
            b'mp3_stereo_mode': b'stereo'})

    def test_138_discontiguous_pkeys(self):
        playlist = fpl_reader.read_playlist(get_file('1.3.8-discontiguous-pkeys.fpl'))
        self.assertEqual(len(playlist.tracks), 8)
        t = playlist.tracks

        self.assertEqual(t[0].flags, 17)
        self.assertEqual(t[0].file_name, b'http://stream1.opb.org:80/opbmusic_hbr.mp3')
        self.assertEqual(t[0].subsong_index, 0)
        self.assertEqual(t[0].file_size, -1)
        self.assertEqual(t[0].file_time, datetime.datetime(2015, 11, 11, 22, 25, 17))
        self.assertEqual(t[0].duration, -1.0)
        self.assertEqual(t[0].rpg_album, -1000.0)
        self.assertEqual(t[0].rpg_track, -1000.0)
        self.assertEqual(t[0].rpk_album, -1.0)
        self.assertEqual(t[0].rpk_track, -1.0)
        self.assertEqual(t[0].primary_keys, {
            b'genre': b'Alternative',
            b'title': b'opbmusic.org'})
        self.assertEqual(t[0].secondary_keys, {
            b'codec':           b'MP3',
            b'samplerate':      b'44100',
            b'encoding':        b'lossy',
            b'bitrate':         b'128',
            b'channels':        b'2',
            b'mp3_stereo_mode': b'joint stereo'})

        self.assertEqual(t[1].flags, 85)
        self.assertEqual(t[1].file_name, b'http://sfstream1.somafm.com:8062/')
        self.assertEqual(t[1].subsong_index, 0)
        self.assertEqual(t[1].file_size, -1)
        self.assertEqual(t[1].file_time, datetime.datetime(2015, 11, 11, 22, 13, 9))
        self.assertEqual(t[1].duration, -1.0)
        self.assertEqual(t[1].rpg_album, -1000.0)
        self.assertEqual(t[1].rpg_track, -1000.0)
        self.assertEqual(t[1].rpk_album, -1.0)
        self.assertEqual(t[1].rpk_track, -1.0)
        self.assertEqual(t[1].primary_keys, {
            b'url':   b'http://SomaFM.com',
            b'genre': b'IDM',
            b'title': b"<-- cliqhop --> blips'n'bleeps backed w/ beats. [SomaFM]"})
        self.assertEqual(t[1].secondary_keys, {
            b'codec':           b'MP3',
            b'samplerate':      b'44100',
            b'encoding':        b'lossy',
            b'bitrate':         b'128',
            b'channels':        b'2',
            b'mp3_stereo_mode': b'stereo'})

        self.assertEqual(t[2].flags, 85)
        self.assertEqual(t[2].file_name, b'http://sfstream1.somafm.com:8900/')
        self.assertEqual(t[2].subsong_index, 0)
        self.assertEqual(t[2].file_size, -1)
        self.assertEqual(t[2].file_time, datetime.datetime(2015, 11, 9, 20, 23, 51))
        self.assertEqual(t[2].duration, -1.0)
        self.assertEqual(t[2].rpg_album, -1000.0)
        self.assertEqual(t[2].rpg_track, -1000.0)
        self.assertEqual(t[2].rpk_album, -1.0)
        self.assertEqual(t[2].rpk_track, -1.0)
        self.assertEqual(t[2].primary_keys, {
            b'url':   b'http://somafm.com',
            b'genre': b'Indie Post Rock',
            b'title': b'Digitalis. Analog rock, digitally-affected, to calm the agitated heart. [SomaFM]'})
        self.assertEqual(t[2].secondary_keys, {
            b'codec':           b'MP3',
            b'samplerate':      b'44100',
            b'encoding':        b'lossy',
            b'bitrate':         b'128',
            b'channels':        b'2',
            b'mp3_stereo_mode': b'stereo'})

        self.assertEqual(t[3].flags, 85)
        self.assertEqual(t[3].file_name, b'http://sfstream1.somafm.com:8384/')
        self.assertEqual(t[3].subsong_index, 0)
        self.assertEqual(t[3].file_size, -1)
        self.assertEqual(t[3].file_time, datetime.datetime(2014, 10, 6, 22, 41, 35))
        self.assertEqual(t[3].duration, -1.0)
        self.assertEqual(t[3].rpg_album, -1000.0)
        self.assertEqual(t[3].rpg_track, -1000.0)
        self.assertEqual(t[3].rpk_album, -1.0)
        self.assertEqual(t[3].rpk_track, -1.0)
        self.assertEqual(t[3].primary_keys, {
            b'url':   b'http://SomaFM.com/',
            b'genre': b'Downtempo House Techno',
            b'title': b'Beat Blender: A late night blend of deep-house & downtempo chill. [SomaFM]'})
        self.assertEqual(t[3].secondary_keys, {
            b'codec':           b'MP3',
            b'samplerate':      b'44100',
            b'encoding':        b'lossy',
            b'bitrate':         b'128',
            b'channels':        b'2',
            b'mp3_stereo_mode': b'stereo'})

        self.assertEqual(t[4].flags, 85)
        self.assertEqual(t[4].file_name, b'http://ice.somafm.com:80/groovesalad')
        self.assertEqual(t[4].subsong_index, 0)
        self.assertEqual(t[4].file_size, -1)
        self.assertEqual(t[4].file_time, datetime.datetime(2015, 11, 11, 19, 34, 52))
        self.assertEqual(t[4].duration, -1.0)
        self.assertEqual(t[4].rpg_album, -1000.0)
        self.assertEqual(t[4].rpg_track, -1000.0)
        self.assertEqual(t[4].rpk_album, -1.0)
        self.assertEqual(t[4].rpk_track, -1.0)
        self.assertEqual(t[4].primary_keys, {
            b'url':   b'http://somafm.com',
            b'genre': b'Ambient Chill',
            b'title': b'Groove Salad: a nicely chilled plate of ambient beats and grooves. [SomaFM]'})
        self.assertEqual(t[4].secondary_keys, {
            b'codec':           b'MP3',
            b'samplerate':      b'44100',
            b'encoding':        b'lossy',
            b'bitrate':         b'128',
            b'channels':        b'2',
            b'mp3_stereo_mode': b'stereo'})

        self.assertEqual(t[5].flags, 85)
        self.assertEqual(t[5].file_name, b'http://sfstream1.somafm.com:7400/')
        self.assertEqual(t[5].subsong_index, 0)
        self.assertEqual(t[5].file_size, -1)
        self.assertEqual(t[5].file_time, datetime.datetime(2015, 11, 11, 22, 25, 10))
        self.assertEqual(t[5].duration, -1.0)
        self.assertEqual(t[5].rpg_album, -1000.0)
        self.assertEqual(t[5].rpg_track, -1000.0)
        self.assertEqual(t[5].rpk_album, -1.0)
        self.assertEqual(t[5].rpk_track, -1.0)
        self.assertEqual(t[5].primary_keys, {
            b'url':   b'http://somafm.com',
            b'genre': b'Folk Indie Newgrass',
            b'title': b'Folk Forward: Indie Folk, Alt-folk and the occasional folk classics. [SomaFM]'})
        self.assertEqual(t[5].secondary_keys, {
            b'codec':           b'MP3',
            b'samplerate':      b'44100',
            b'encoding':        b'lossy',
            b'bitrate':         b'128',
            b'channels':        b'2',
            b'mp3_stereo_mode': b'stereo'})

        self.assertEqual(t[6].flags, 17)
        self.assertEqual(t[6].file_name, b'http://us.ah.fm:443/')
        self.assertEqual(t[6].subsong_index, 0)
        self.assertEqual(t[6].file_size, -1)
        self.assertEqual(t[6].file_time, datetime.datetime(2015, 11, 11, 22, 25, 11))
        self.assertEqual(t[6].duration, -1.0)
        self.assertEqual(t[6].rpg_album, -1000.0)
        self.assertEqual(t[6].rpg_track, -1000.0)
        self.assertEqual(t[6].rpk_album, -1.0)
        self.assertEqual(t[6].rpk_track, -1.0)
        self.assertEqual(t[6].primary_keys, {
            b'url':   b'http://www.AH.FM',
            b'genre': b'Electronic',
            b'title': b'AH.FM - Leading Trance Radio'})
        self.assertEqual(t[6].secondary_keys, {
            b'codec':           b'MP3',
            b'samplerate':      b'44100',
            b'encoding':        b'lossy',
            b'bitrate':         b'192',
            b'channels':        b'2',
            b'mp3_stereo_mode': b'stereo'})

        self.assertEqual(t[7].flags, 17)
        self.assertEqual(t[7].file_name, b'file://C:\\Users\\Public\\Music\\Sample Music\\Kalimba.mp3')
        self.assertEqual(t[7].subsong_index, 0)
        self.assertEqual(t[7].file_size, 8414449)
        self.assertEqual(t[7].file_time, datetime.datetime(2009, 7, 14, 5, 32, 31))
        self.assertEqual(t[7].duration, 348.00326530612244)
        self.assertEqual(t[7].rpg_album, -1000.0)
        self.assertEqual(t[7].rpg_track, -1000.0)
        self.assertEqual(t[7].rpk_album, -1.0)
        self.assertEqual(t[7].rpk_track, -1.0)
        self.assertEqual(t[7].primary_keys, {
            b'album':        b'Ninja Tuna',
            b'album artist': b'Mr. Scruff',
            b'artist':       b'Mr. Scruff',
            b'comment':      b'Ninja Tune Records',
            b'composer':     b'A. Carthy and A. Kingslow',
            b'date':         b'2008',
            b'genre':        b'Electronic',
            b'publisher':    b'Ninja Tune',
            b'title':        b'Kalimba'})
        self.assertEqual(t[7].secondary_keys, {
            b'codec':           b'MP3',
            b'codec_profile':   b'CBR',
            b'samplerate':      b'44100',
            b'encoding':        b'lossy',
            b'bitrate':         b'192',
            b'channels':        b'2',
            b'tagtype':         b'id3v2.3|id3v1',
            b'mp3_stereo_mode': b'stereo'})

    def test_138_missing_meta(self):
        playlist = fpl_reader.read_playlist(get_file('1.3.8-missing-meta.fpl'))
        self.assertEqual(len(playlist.tracks), 2)
        t = playlist.tracks

        self.assertEqual(t[0].flags, 0)
        self.assertEqual(t[0].file_name, b'http://sfstream1.somafm.com:8900/')
        self.assertEqual(t[0].file_size, None)
        self.assertEqual(t[0].file_time, None)
        self.assertEqual(t[0].subsong_index, 0)
        self.assertEqual(t[0].duration, None)
        self.assertEqual(t[0].rpg_album, None)
        self.assertEqual(t[0].rpg_track, None)
        self.assertEqual(t[0].rpk_album, None)
        self.assertEqual(t[0].rpk_track, None)
        self.assertEqual(t[0].primary_keys, {})
        self.assertEqual(t[0].secondary_keys, {})

        self.assertEqual(t[1].flags, 19)
        self.assertEqual(t[1].file_name, b'file://src\\vntools.other\\HCA_decoder\\hca_quality_samples\\sample.wav')
        self.assertEqual(t[1].file_size, 1341248)
        self.assertEqual(t[1].file_time, datetime.datetime(2014, 9, 12, 18, 52, 29))
        self.assertEqual(t[1].subsong_index, 0)
        self.assertEqual(t[1].duration, 6.9854375)
        self.assertEqual(t[1].rpg_album, -1000.0)
        self.assertEqual(t[1].rpg_track, -1000.0)
        self.assertEqual(t[1].rpk_album, -1.0)
        self.assertEqual(t[1].rpk_track, -1.0)
        self.assertEqual(t[1].primary_keys, {})
        self.assertEqual(t[1].secondary_keys, {
            b'bitrate': b'1536',
            b'bitspersample': b'16',
            b'channels': b'2',
            b'codec': b'PCM',
            b'encoding': b'lossless',
            b'samplerate': b'48000'})

if __name__ == '__main__':
    unittest.main()
