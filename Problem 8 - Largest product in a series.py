# The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832. 
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

with open("Problem 8 - Largest product in a series", "r") as f:
    numbers = [int(digit) for digit in f.read() if digit != "\n"]

def largest_product(series, start=0, end=13):
    """
    Takes an array of numbers and returns the largest product of 13 consecutive numbers
    :param series: iterable
    :param start: first index of the slice
    :param end: last index of the slice
    :return: largest prod of 13 consecutive numbers
    """

    output = 0
    temp = 1

    while end < len(series):
        for number in series[start:end]:
            temp *= number

        if temp > output:
            output = temp

        start += 1
        end += 1
        temp = 1

    return f" the largest product of the series is {output}"

print(largest_product(numbers))