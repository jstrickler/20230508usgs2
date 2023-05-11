

COLORS = []
AIRPORTS = {}
animal = "wolverine"

def spam(value):
    global animal  # VERY NAUGHTY!!
    animal = "coatimundi"
    COLORS.append("kiwi")
    AIRPORTS['RDU'] = "Raleigh-Durham"
    def ham():
        print("in ham: value is", value)  # value is nonlocal
    return ham

h = spam(1234)
h()
print(f"animal: {animal}")

x = "yak"
for x in range(1,11):
    for y in range(10, 101, 10):
        print(y)
    print("in outer loop:", y)
print("at main:", x, y)

fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

target = 'v'
for fruit in fruits:
    if fruit.startswith(target):
        print(fruit)
        break
else:
    print("Not found")

