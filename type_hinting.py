import math
import typing as T

class Dog:
    pass

class Cat:
    pass

class Penguin:
    pass

WashableAnimal = T.Union[Dog,Cat]
print(f"WashableAnimal: {WashableAnimal}")

Number = T.Union[int,float]

user_name: str

user_name = 123
print(f"user_name: {user_name}")

def wash_and_brush(animal: WashableAnimal):
    pass

felix = Cat()
nellie = Dog()
polly = Penguin()


for animal in felix, nellie, polly:
    wash_and_brush(animal)

def circle_area(diameter: Number) -> float:
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    return area

a1 = circle_area(22)
print(f"a1: {a1}")

# a2 = circle_area("42")
# print(f"a2: {a2}")

a3 = circle_area(8.9)
print(f"a3: {a3}")

def process_files(file_names: T.Iterable[str]) -> None:
    for file_name in file_names:
        print(f"processing {file_name}")

f1 = ['foo', 'bar', 'blah']
f2 = 'spam', 'ham'
f3 = (f.upper() for f in f1)

process_files(f1)
process_files(f2)
process_files(f3)

print(f"dir(process_files): {dir(process_files)}")
print()
print(f"process_files.__annotations__: {process_files.__annotations__}")

print(process_files.__annotations__['file_names'])

class A:
    def foo(self, thing: "B") -> None:
        pass

class B:
    def bar(self, other_thing: A) -> None:
        pass


def do_the_thing(value) -> T.Optional[str]:
    if value < 100:
        return "wombat"
    else:
        return None





