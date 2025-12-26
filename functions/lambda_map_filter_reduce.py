from functools import reduce


def multiply_numbers(number):
    return number * 7


def multiply_by_number(number):
    return lambda x: x * number


def multiply(x):
    return x[0] * multiply(x[1:]) if x else 1


my_list = range(1, 13)

multiple_of_7 = list(
    map(
        multiply_numbers,
        my_list,
    )
)

# Different ways to create a list of squares
square_list_1 = list(map(lambda x: x**2, my_list))

square_list_2 = [x**2 for x in my_list]

square_list_3 = []
for num in my_list:
    square_list_3.append(num**2)

# Using lambda to create a function that multiplies by 3
multiply_by_3 = multiply_by_number(3)
multiply_by_3(5)

# Summing the elements of the list using different methods
my_sum = sum(my_list)
my_sum_2 = reduce(lambda x, y: x + y, my_list)

# Multiplying the elements of the list using different methods
multiple_1 = multiply(my_list)
multiple_2 = reduce(lambda x, y: x * y, my_list)

# Filtering even and odd numbers using lambda
evens = list(filter(lambda x: x % 2 == 0, my_list))
odds = list(filter(lambda x: x % 2 != 0, my_list))
# squares = {x:(lambda x: x**x)(x) for x in range(1, 6)}
