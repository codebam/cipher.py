import sys
from random import randrange
import itertools


def make_rot(n):
    from string import ascii_lowercase as lc, ascii_uppercase as uc
    lookup = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(lookup)


def cipher(argv):
    start = randrange(1, 26)
    rotation = itertools.islice(itertools.cycle(range(1, 26)), start, None)
    out = ''
    for char in argv:
        rot = make_rot(next(rotation))
        out += rot(char)
    return out


def main():
    if len(sys.argv) <= 1:
        print("Not enough arguments")
    else:
        print(cipher(' '.join(sys.argv[1:])))


if __name__ == "__main__":
    main()
