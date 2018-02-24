#!/usr/bin/env python3
import os
import argparse
from fpl_reader import read_playlist


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    return parser.parse_args()


def main():
    args = parse_args()

    with open(args.path, 'rb') as handle:
        data = handle.read()
        playlist = read_playlist(data)
        print(playlist)


if __name__ == '__main__':
    main()
