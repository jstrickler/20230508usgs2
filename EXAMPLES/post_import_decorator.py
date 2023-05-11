from  functools import cache
from random import randint
from geometry import circle_area

circle_area_cached = cache(circle_area)

# like
# @cache
# def func():
#     ...

for _ in range(10000):
    result = circle_area_cached(randint(1, 50))

print(circle_area_cached.cache_info())