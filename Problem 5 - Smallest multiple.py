# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. 
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? 

## Brute force
from itertools import count
for i in count(20):
    if all(map(lambda x: i % x == 0, range(1, 21))):
        print(i)
        break

