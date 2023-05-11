
# this is the decorator
def void(thing_being_decorated):
    return lambda: print("decorators are weird")  # replace function with 42

name = "Guido"
name = void(name)

@void  # decorate hello() function
def hello():
    print("Hello, world")

@void
def howdy():
    print("Howdy, world")

# howdy = void(howdy)

print(hello, type(hello)) # hello is now the integer 42, not a function
print(howdy, type(howdy)) # hello is now the integer 42, not a function
print(x, type(x))
