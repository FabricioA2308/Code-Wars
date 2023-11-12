# https://www.codewars.com/kata/558fc85d8fd1938afb000014

def sum_two_smallest_numbers(numbers):
    numbers.sort()

    return numbers[0] + numbers[1]

# Expected result: 7
print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))