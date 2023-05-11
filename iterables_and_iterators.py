
colors = ['coral', 'kiwi', 'yellow']

# x = next(colors)  a list is not an iterabor, so this fails

color_iter = iter(colors)
x = next(color_iter)
print(f"x: {x}")
x = next(color_iter)
print(f"x: {x}")
x = next(color_iter)
print(f"x: {x}")
print('-' * 60)

ecolors = enumerate(colors)
print(f"ecolors: {ecolors}")
print(f"next(ecolors): {next(ecolors)}")
print(f"next(ecolors): {next(ecolors)}")
for i, color in ecolors:
    print(i, color)
print()

ecolors = enumerate(colors)
e_iter = iter(ecolors)
print(ecolors is e_iter)

class CountDown:
    def __init__(self, start_value):
        self._start_value = start_value

    def __iter__(self):
        return self

    def __next__(self):
        if self._start_value == -1:
            raise StopIteration()
        current_value = self._start_value
        self._start_value -= 1
        return current_value

c = CountDown(10)
for num in c:
    print(num)
print('-' * 60)

for num in c:
    print(num)

with open('DATA/mary.txt') as mary_in:
    line1 = next(mary_in)
    print(f"line1: {line1}")
    for raw_line in mary_in:
        line = raw_line.rstrip()
        print(line)
print()





