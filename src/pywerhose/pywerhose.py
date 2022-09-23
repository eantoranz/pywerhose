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

    def __init__(self, min_base:int = 2, min_power: int = 2, step: int = 1, start_from: int | None = None, reverse: bool = False) -> None:
        self.min_base = min_base
        self.min_power = min_power
        self.step = step
        self.start_from = start_from
        self.reverse = reverse
        
        if reverse and start_from is None:
            raise Exception("Need to setup a value to start from to go in reverse")
        
        # the current list of powers
        self.powers = list[Power]()
        
        if reverse:
            self.setup_powers_down()
            self.next = self.previous_power
        else:
            self.setup_powers_up()
            self.next = self.next_power

    def setup_powers_up(self):
        if self.start_from is None:
            starting_power = Power(self.min_base, self.min_power)
            self.powers.append(starting_power)
        else:
            # need to setup all appropriate powers necessary
            base = self.min_base
            log_start_from = math.log(self.start_from)
            max_power, value = self.get_max_power(base, self.start_from, log_start_from) # base^max_power <= start_from
            if value < self.start_from:
                max_power += 1 # make sure to include a power for min_base
            power = max_power
            powers = []
            has_min_base = False
            while True:
                if power < self.min_power:
                    # no need to continue
                    break
                base, value = self.get_max_base(power, self.start_from) # base is already corrected to match min_base and step
                if value < self.start_from:
                    # increase the base so that we are over the value
                    base += self.step
                    value = base ** power
                if not has_min_base and base == self.min_base:
                    has_min_base = True
                _power = Power(base, power, value)
                powers.append(_power)
                power -= 1
            if not has_min_base:
                # Need to include a power with min_base
                powers.append(self.min_base, max_power + 1)
            # now we sort them out
            self.insort_powers(powers)
    
    def setup_powers_down(self):
        # need to setup all appropriate powers necessary
        base = self.min_base
        log_start_from = math.log(self.start_from)
        max_power, value = self.get_max_power(base, self.start_from, log_start_from) # base^max_power <= start_from
        power = max_power
        powers = []
        while True:
            if power < self.min_power:
                break
            base, value = self.get_max_base(power, self.start_from) # base is already corrected to match min_base and step
            if base < self.min_base:
                break
            _power = Power(base, power, value)
            powers.append(_power)
            power -= 1
        # now we sort them out
        self.insort_powers(powers)

    def insort_powers(self, powers: list[Power]) -> None:
        for power in powers:
            if not self.powers or power.value < self.powers[0].value:
                self.powers.insert(0, power)
                continue
            lo = 0
            hi = len(self.powers)
            while True:
                pos = bisect.bisect_left(self.powers, power, lo = lo, hi = hi)
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
                        if self.reverse:
                            power.base -= self.step
                            hi = pos
                        else:
                            power.base += self.step
                            lo = pos
                        power.value = power.base ** power.power
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

    def previous_power(self) -> (int, int, int):
        # look for the table with the highest value
        current_power: Power = self.powers.pop()
        
        # save current value which will be returned.
        power = (current_power.base, current_power.power, current_power.value) # this is what will be returned

        # update values in table
        current_power.base -= self.step
        if current_power.base >= self.min_base:
            current_power.value = current_power.base ** current_power.power
            powers = [current_power]
            self.insort_powers(powers)

        return power

    def get_max_power(self, base: int, limit: int, limit_log: float):
        """
        limit_log is math.log of limit (so that we don't do it over and over again)
        limit is passed down for verification
        """
        power = int(math.floor(limit_log / math.log(base)))
        result = base ** power

        # the following lines are for verification purposes, can be deleted once I have made sure they work
        if result > limit:
            raise Exception(f"BUG: get_max_power(base={base}, limit={limit}, limit_log={limit_log}): {base}^{power} > limit")
        if result * base <= limit:
            raise Exception(f"BUG: get_max_power(base={base}, limit={limit}, limit_log={limit_log}): {base}^({power}+1) is <= limit")

        return power, result

    def get_max_base(self, power: int, limit: int):
        """
        Return max value of base so that base^power <= limit

        Value of base _has_ to match min_base/step configuration
        """
        base = int(math.floor(math.pow(limit, 1.0 / power)))
        value = base ** power

        # the following lines are for verification purposes, can be deleted once I have made sure they work
        if value > limit:
            # rounding error
            base -= self.step
            value = base ** power
        if value > limit:
            raise Exception(f"BUG: get_max_base(power={power}, limit={limit}): {base}^{power} > limit")
        if ((base + 1) ** power < limit):
            # rounding error
            base += 1
            value = base ** power
        if ((base + 1) ** power < limit):
            raise Exception(f"BUG: get_max_base(power={power}, limit={limit}): {base+1}^({power}) is < limit")

        if self.step > 1:
            # let's adjust power so that it matches configuration
            mod = (base - self.min_base) % self.step
            if mod > 0:
                base -= mod
                value = base ** power

        return base, value
