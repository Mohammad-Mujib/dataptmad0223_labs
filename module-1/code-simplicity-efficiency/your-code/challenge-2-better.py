import random
import string

def random_string(length):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))


def batch_string_generator(num_strings, min_length=8, max_length=12):
    if min_length > max_length:
        raise ValueError("Minimum length should be less than or equal to maximum length.")
    return [random_string(random.randint(min_length, max_length)) for _ in range(num_strings)]

min_length = int(input('Enter minimum string length: '))
max_length = int(input('Enter maximum string length: '))
num_strings = int(input('How many random strings to generate? '))

print(batch_string_generator(num_strings, min_length, max_length))
