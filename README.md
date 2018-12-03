# cipher.py

cipher.py is a simple cipher program that loops through rotations of 1 to 25,
with a customizable starting rot and customizable step.

by default cipher.py uses a starting position of 13 and a step of 25, making it
a simple caesar cipher.

## How it works

```bash
python cipher.py --start 4 --step 3 "foobar"
# output: kwzprl

python cipher.py --decode --start 4 --step 3 "kwzprl"
# output: foobar
```

since there are 25 different starting positions, and 25 possible steps, that
gives us 625 different positions that the cipher can be in. (25x25)

cipher.py has command line options, see `python cipher.py --help` for more
usage information.
