# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
    return str(n) == str(n)[::-1]

my_list = []

for n_1 in range(100, 1000):
    for n_2 in range(100, 1000):
        result = n_1 * n_2
        if is_palindrome(result):
            my_list.append(result)
print(max(my_list))