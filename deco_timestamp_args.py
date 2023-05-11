import logging
from functools import wraps
from datetime import datetime
logging.basicConfig(level=logging.INFO)

def logtimestamp(*, dateonly=False):

    def subdecorator(target):
        # code A here...  decoration time only
        @wraps(target)
        def wrapper(*args, **kwargs):
            # code B here...  whenever target is called
            now = datetime.now()
            if dateonly:
                message = now.strftime("%x")
            else:
                message = f"{target.__name__} called at {now.strftime('%x-%X')}"
            logging.info(message)
            temp_args = list(args)
            temp_args[0] = temp_args[0].upper()
            result = target(*temp_args, **kwargs)
            return result

        return wrapper
    return subdecorator

@logtimestamp(dateonly=False)
def hello(animal):
    print(f"Hello, world -- I'm a {animal}")

@logtimestamp(dateonly=True)
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