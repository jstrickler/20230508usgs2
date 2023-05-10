
class fauxrange:

    def __init__(self, *values):
        if len(values) == 1:
            self._start, self._stop, self._step = 0, *values, 1
        elif len(values) == 2:
            self._start, self._stop, self._step = *values, 1
        elif len(values) == 3:
            self._start, self._stop, self._step = values
        else:
            raise TypeError("Arguments must be from 1 to 3 integers")

        # make range checking function
        end_value = self._stop
        if self._step > 0:
            self._out_of_range = lambda x: x >= self._stop
        else:
            self._out_of_range = lambda x: x <= end_value

    def __next__(self):
        next_value = self._start
        
        if self._out_of_range(next_value):
            raise StopIteration

        self._start += self._step
        return next_value

    def __iter__(self):
        return self

print(f"list(fauxrange(10): {list(fauxrange(10))}")
print(f"list(fauxrange(1, 11): {list(fauxrange(1, 11))}")
print(f"list(fauxrange(5, 51, 5): {list(fauxrange(5, 51, 5))}")
print(f"list(fauxrange(10, 0, -1): {list(fauxrange(10, 0, -1))}")
print(f"list(fauxrange(8, 23, 2): {list(fauxrange(8, 23, 2))}")
print(f"list(fauxrange(50, 4, -5): {list(fauxrange(50, 4, -5))}")

