from collections.abc import Iterable, Sized

colors = ['red', 'blue', 'green']

if hasattr(colors, "__iter__"):
    print("Yep, it's an iterable")

if isinstance(colors, Iterable):
    print("Still an iterable)")

if hasattr(colors, '__len__'):
    print('has a length')

if issubclass(list, Sized):
    print("also has a length")
