import sys
from random import randrange
import itertools
from string import ascii_lowercase as lc, ascii_uppercase as uc


def make_rot(n):
    lookup = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(lookup)


def cipher(argv, start=randrange(1, 26)):
    rotation = itertools.islice(itertools.cycle(range(1, 26)), start, None)
    out = ''
    for char in argv:
        rot = make_rot(next(rotation))
        out += rot(char)
    return out


def decipher(start, ciphertext):
    start = int(start)
    rotation = itertools.islice(itertools.cycle(range(25, 0, -1)), start, None)
    out = ''
    for char in ciphertext:
        rot = make_rot(next(rotation))
        out += rot(char)
    return out


def main():
    try:
        if sys.argv[1] == '-c':
            print(cipher(' '.join(sys.argv[2:]).lower()))
        elif sys.argv[1] == '-d':
            start = sys.argv[2]
            print(decipher(start, ' '.join(sys.argv[3:]).lower()))
    except IndexError:
        print('''\nUsage:

python cipher.py -c             convert from plaintext to ciphertext
python cipher.py -d  <start>    convert from ciphertext to plaintext
''')


if __name__ == "__main__":
    main()
