import math
import sys
from os import rename

# print(sys.version)
# print(sys.version)
print(sys.executable)
test = 5


def greet(who_to_greet):
    greeting = 'Hello, {}'.format(who_to_greet)
    return greeting


print(greet('world'))
