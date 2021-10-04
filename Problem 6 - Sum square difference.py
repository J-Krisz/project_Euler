# The sum of the squares of the first ten natural numbers is, 
# The square of the sum of the first ten natural numbers is, 
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$. 
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum. 

square_of_sums = sum([i for i in range(1, 101)]) ** 2
sum_of_squares = sum([i ** 2 for i in range(1, 101)])

print(f"{square_of_sums} - {sum_of_squares} = {square_of_sums - sum_of_squares}")