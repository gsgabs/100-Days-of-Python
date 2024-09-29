#heads or tail game

import random

heads = 1
tail = 0
while 1:
    n = random.randint(0, 1)
    if n == 1:
        print("heads")
    elif n == 0:
        print("tail")
