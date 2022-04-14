#蒙特卡罗
from random import random
from math import sqrt
d = 1000
h = 0.0
for i in range(1,d+1):
    x,y = random(),random()
    dist = sqrt(x**2+y**2)
    if dist <= 1.0:
        h = h + 1
pi = 4 * (h/d)
print('pi值是{}'.format(pi))
