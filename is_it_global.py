from pprint import pprint
import re  # find and run re.py
import globals_and_locals
from globals_and_locals import Dog, ANIMAL, MAX_SIZE

pprint(globals())

print(f"globals_and_locals.MAX_SIZE: {globals_and_locals.MAX_SIZE}")
print(f"globals_and_locals.ANIMAL: {globals_and_locals.ANIMAL}")

d = Dog()
