# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, 
# For example, 32 + 42 = 9 + 16 = 25 = 52. 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.Find the product abc. 

def is_pythagorean(a, b, c):
    return a**2 + b**2 == c**2

SUM =1000

for a in range(1,500):
    for b in range(a+1, 500):
        c = SUM - a - b
        if is_pythagorean(a, b, c):
            if a + b + c == SUM:
                print(a * b * c)
