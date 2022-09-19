# What is pywerhose?

- It is a library to generate powers one after the other. Ex: 2<sup>2</sup>, 2<sup>3</sup>, 3<sup>2</sup>, 2<sup>4</sup>, 5<sup>2</sup>, 3<sup>3</sup>, 2<sup>5</sup>....

# examples

## Generate the first 7 powers:
```
from pywerhose import Generator

generator = Generator()
generator.next_power() # (2, 2, 4)
generator.next_power() # (2, 3, 8)
generator.next_power() # (3, 2, 9)
generator.next_power() # (2, 4, 16)
generator.next_power() # (5, 2, 25)
generator.next_power() # (3, 3, 27)
generator.next_power() # (2, 5, 32)
```

## Generate powers not considering 2 or 3 as bases
```
from pywerhose import Generator

generator = Generator(min_base = 4)
generator.next_power() # (4, 2, 16)
generator.next_power() # (5, 2, 25)
generator.next_power() # (6, 2, 36)
generator.next_power() # (7, 2, 49)
generator.next_power() # (4, 3, 64)
generator.next_power() # (9, 2, 81)
```

## Generate powers discarding squares
```
from pywerhose import Generator

generator = Generator(min_power = 3)
generator.next_power() # (2, 3, 8)
generator.next_power() # (2, 4, 16)
generator.next_power() # (3, 3, 27)
generator.next_power() # (2, 5, 32)
generator.next_power() # (2, 6, 64)
generator.next_power() # (3, 4, 81)
generator.next_power() # (5, 3, 125)
generator.next_power() # (2, 7, 128)
```

## Generate powers of multiples of 5
```
from pywerhose import Generator

generator = Generator(min_base = 5, step = 5)
generator.next_power() # (5, 2, 25)
generator.next_power() # (10, 2, 100)
generator.next_power() # (5, 3, 125)
generator.next_power() # (15, 2, 225)
generator.next_power() # (5, 4, 625)
generator.next_power() # (10, 3, 1000)
```

# TODO
- Start producing powers from a random number
- Generate them backward

# Licensing
The package is released under the terms of GPLv3.

Copyright (c) 2022 Edmundo Carmona Antoranz

