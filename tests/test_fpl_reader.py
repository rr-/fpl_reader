#!/bin/python3
import os
import unittest
import fpl_reader


def get_file(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name), 'rb') as handle:
        return handle.read()

class TestSequenceFunctions(unittest.TestCase):
    def test_w1(self):
        playlist = fpl_reader.read_playlist(get_file('w1.fpl'))
        self.assertEqual(8, len(playlist.tracks))

if __name__ == '__main__':
    unittest.main()
