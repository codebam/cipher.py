import argparse
import itertools
from random import randrange
from string import ascii_lowercase as lc, ascii_uppercase as uc


def make_rot(n):
    lookup = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(lookup)


def cipher(text, start=13, step=25):
    rotation = itertools.islice(
        itertools.cycle(range(1, 26)), start-1, None, step)
    out = ''
    for char in text:
        rot = make_rot(next(rotation))
        out += rot(char)
    return out


def decipher(ciphertext, start=13, step=25):
    rotation = itertools.islice(
        itertools.cycle(range(25, 0, -1)), start-1, None, step)
    out = ''
    for char in ciphertext:
        rot = make_rot(next(rotation))
        out += rot(char)
    return out


def main():
    parser = argparse.ArgumentParser(description='Cipher or Decipher text.')
    parser.add_argument(
        '-e',
        '--encode',
        action='store_true',
        help='encode text to ciphertext (default)')
    parser.add_argument(
        'text',
        metavar='text',
        type=str,
        nargs='+',
        help='a string of text to cipher or decipher')
    parser.add_argument(
        '-d',
        '--decode',
        dest='cipher',
        default=cipher,
        action='store_const',
        const=decipher,
        help='decode ciphertext')
    parser.add_argument(
        '--start',
        default=13,
        dest='start',
        type=int,
        help='set the rotation starting position (default: 13 caesar)')
    parser.add_argument(
        '--step',
        default=25,
        dest='step',
        type=int,
        help='set the step for each character (default: 1)')

    args = parser.parse_args()
    print(args.cipher(' '.join(args.text), start=args.start, step=args.step))


if __name__ == "__main__":
    main()
