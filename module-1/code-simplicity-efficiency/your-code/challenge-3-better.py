"""
You are presented with an integer number larger than 5. Your goal is to identify the longest side
possible in a right triangle whose sides are not longer than the number you are given.

For example, if you are given the number 15, there are 3 possibilities to compose right triangles:

1. [3, 4, 5]
2. [6, 8, 10]
3. [5, 12, 13]

The following function shows one way to solve the problem but the code is not ideal or efficient.
Refactor the code based on what you have learned about code simplicity and efficiency.
"""


def longest_side(max_length):
    max_hypotenuse = 0
    for a in range(1, max_length):
        for b in range(a, max_length):
            c = (a**2 + b**2)**0.5  # calculate the hypotenuse
            if c <= max_length and c > max_hypotenuse:  # check if c is valid and longer than previous max
                max_hypotenuse = c
    return int(max_hypotenuse)

max_length = int(input("What is the maximal length of the triangle side? Enter a number: "))
print("The longest side possible is", longest_side(max_length))