# Copyright (c) 2022 Edmundo Carmona Antoranz
# Released under the terms of GPLv3

import bisect
import math

class Power:
    """
    A power holds a semi-fixed power, a base and a value
    base ** power = value
    
    The process of _consuming_ a power will make the power increase (or, later, decrease) its
    base/value according to the power being used
    """
    
    def __init__(self, base, power, value = None):
        self.base = base
        self.power = power
        self.value = base ** power if value is None else value
    
    def __lt__(self, other):
        return self.value < other.value

    def __str__(self):
        return f"Power: {self.base}^{self.power} ({self.value})"

class Generator:

    def __init__(self, min_base:int = 2, min_power: int = 2, step: int = 1) -> None:
        self.min_base = min_base
        self.min_power = min_power
        self.step = step
        
        # the current list of powers
        self.powers = list[Power]()
        
        starting_power = Power(min_base, min_power)
        self.powers.append(starting_power)
    
    def insort_powers(self, powers: list[Power]) -> None:
        for power in powers:
            if not self.powers or power.value < self.powers[0].value:
                self.powers.insert(0, power)
                continue
            index = 0
            while True:
                pos = bisect.bisect_left(self.powers, power, lo=index)
                if pos < len(self.powers):
                    old_power = self.powers[pos]
                    if old_power.value == power.value:
                        # we will keep the record with the biggest power in place
                        if old_power.power < power.power:
                            # exchanging values between power and old_power
                            temp = (old_power.base, old_power.power)
                            old_power.power = power.power # told you power is semi-fixed
                            old_power.base = power.base
                            # replacing for new values in temp
                            power.base = temp[0]
                            power.power = temp[1]
                        power.base += self.step
                        power.value = power.base ** power.power
                        index = pos + 1
                    else:
                        self.powers.insert(pos, power)
                        break
                else:
                    self.powers.append(power)
                    break
    
    def next_power(self) -> (int, int, int):
        # look for the table with the lowest value
        current_power: Power = self.powers.pop(0)
        
        # save current value which will be returned.
        power = (current_power.base, current_power.power, current_power.value) # this is what will be returned
        
        # update values in table
        current_power.base += self.step
        current_power.value = current_power.base ** current_power.power
        
        powers = [current_power]
        if (power[0] == self.min_base):
            # need to insert a new table for min_base^(current_power.power+1)
            new_power = Power(self.min_base, current_power.power + 1, power[2] * self.min_base)
            powers.append(new_power)
        
        self.insort_powers(powers)
        
        return power
