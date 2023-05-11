from president import President

p = President(16)
print(f"p: {p}")
print(f"p.first_name: {p.first_name}")
print(f"p.last_name: {p.last_name}")

plist = [President(1), President(26)]
print(f"plist: {plist}")

print(f"President.__init__: {President.__init__}")
print(f"President.ANIMAL: {President.ANIMAL}")

print(dir(p))

attributes = sorted([a for a in dir(p) if not a.startswith('_')])
print(f"attributes: {attributes}")
print()

names = ['first_name', 'last_name']
for name in names:
    value = getattr(p, name)     #  getattr(obj, attribute_name)
    print(f"value: {value}")
    
x = getattr(names, 'append', lambda *args: print("WHAT HO?"))
x('party')
print(f"names: {names}")

print(f"hasattr(names, 'append'): {hasattr(names, 'append')}")

obj = None
if hasattr(obj, 'close'):
    obj.close()

def bark(self):
    print("woof! woof!")

setattr(President, 'bark', bark)

p.bark()     #  look up "bark" in type(p) 

class Foo(President, list):
    pass

print(f"Foo.mro(): {Foo.mro()}")

class A:   # inherits from 'object'
    def beep(self):
        print("beep beep")

class B(A):  # inheritance
    def __init__(self, ClassFoo, ClassBar) -> None:  # composition
        super().__init__()

    def honk(self):
        print("honk honk")

class C(B):
    pass

class D(C):
    pass

d = D()
d.beep()
d.honk()













