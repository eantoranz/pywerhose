# What is pywerhose?

- It is a library to generate powers one after the other. Ex: 2<sup>2</sup>, 2<sup>3</sup>, 3<sup>2</sup>, 2<sup>4</sup>, 5<sup>2</sup>, 3<sup>3</sup>, 2<sup>5</sup>....

# examples

## Generate the first 7 powers:
```
from pywerhose import Generator

generator = Generator()
generator.next() # (2, 2, 4)
generator.next() # (2, 3, 8)
generator.next() # (3, 2, 9)
generator.next() # (2, 4, 16)
generator.next() # (5, 2, 25)
generator.next() # (3, 3, 27)
generator.next() # (2, 5, 32)
```

## Generate powers not considering 2 or 3 as bases
```
from pywerhose import Generator

generator = Generator(min_base = 4)
generator.next() # (4, 2, 16)
generator.next() # (5, 2, 25)
generator.next() # (6, 2, 36)
generator.next() # (7, 2, 49)
generator.next() # (4, 3, 64)
generator.next() # (9, 2, 81)
```

## Generate powers discarding squares
```
from pywerhose import Generator

generator = Generator(min_power = 3)
generator.next() # (2, 3, 8)
generator.next() # (2, 4, 16)
generator.next() # (3, 3, 27)
generator.next() # (2, 5, 32)
generator.next() # (2, 6, 64)
generator.next() # (3, 4, 81)
generator.next() # (5, 3, 125)
generator.next() # (2, 7, 128)
```

## Generate powers of multiples of 5
```
from pywerhose import Generator

generator = Generator(min_base = 5, step = 5)
generator.next() # (5, 2, 25)
generator.next() # (10, 2, 100)
generator.next() # (5, 3, 125)
generator.next() # (15, 2, 225)
generator.next() # (5, 4, 625)
generator.next() # (10, 3, 1000)
```

## Generate powers starting at a given point
```
from pywerhose import Generator

generator = Generator(start_from = 1000)
generator.next() # (10, 3, 1000)
generator.next() # (2, 10, 1024)
generator.next() # (33, 2, 1089)
generator.next() # (34, 2, 1156)
```

## Generate powers in reverse
```
from pywerhose import Generator

generator = Generator(start_from = 1000)
generator.next() # (31, 2, 961)
generator.next() # (30, 2, 900)
generator.next() # (29, 2, 841
generator.next() # (28, 2, 784)
generator.next() # (3, 6, 729)
```

# TODO
- Package/Publish it.

# Licensing
The package is released under the terms of GPLv3.

Copyright (c) 2022 Edmundo Carmona Antoranz

