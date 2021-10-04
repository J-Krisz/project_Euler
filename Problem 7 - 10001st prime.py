# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13. 
# What is the 10 001st prime number? 

def is_prime(num):
    factor = 2
    while factor ** 2 <= num:
        if num % factor == 0:
            return False
        factor += 1
    return True


def nth_prime_number(n):
    if n == 1:
        return 2
    count = 1
    num = 1
    while count < n:
        num += 2
        if is_prime(num):
            count += 1
    return num


print(nth_prime_number(10001))
