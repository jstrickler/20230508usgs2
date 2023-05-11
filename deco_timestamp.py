import logging
from functools import wraps
from datetime import datetime
logging.basicConfig(level=logging.INFO)

def logtimestamp(target):
    # code A here...  decoration time only
    @wraps(target)
    def wrapper(*args, **kwargs):
        # code B here...  whenever target is called
        logging.info("%s called at %s", target.__name__, datetime.now().strftime("%x-%X"))
        temp_args = list(args)
        temp_args[0] = temp_args[0].upper()
        result = target(*temp_args, **kwargs)
        return result

    return wrapper

@logtimestamp
def hello(animal):
    print(f"Hello, world -- I'm a {animal}")

# original_hello = hello
# hello = logtimestamp(hello)


@logtimestamp
def howdy(animal):
    print(f"Howdy, world from the {animal}")

hello("wombat")
hello("snail darter")
howdy("wallaby")
howdy("platypus")
hello("koala")

# for _ in range(3):
#     original_hello()
print(hello.__name__, howdy.__name__)