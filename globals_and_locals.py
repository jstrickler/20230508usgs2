from pprint import pprint
import re  # do NOT find and run re.py

MAX_SIZE = 100

globals()['ANIMAL'] = "wildebeest"

class Dog:
    pass

def spam(y):
    z = 98
    print("SPAM!")
    print("locals:", locals())

def main():
    x = 100

    g = globals()
    pprint(g)

    s = g['spam']
    print(f"type(s): {type(s)}")
    s("wombat")

def make_global():
    g['color'] = "blue"
    print(f"color: {color}")

if __name__ == "__main__":
    main()



