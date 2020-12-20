# Numbers are: 1859,161
# Result is 299299
import random

with open('day_01.txt') as file:
    list_01 = []
    for line in file:
        stripped_line = line.rstrip()
        list_01.append(stripped_line)

numbers = list(map(lambda x: int(x), list_01))


def get_2020():
    while True:
        num1 = random.choice(numbers)
        num2 = random.choice(numbers)
        num3 = random.choice(numbers)
        sum = num1 + num2 + num3
        if sum == 2020:
            print(f'Numbers are: {num1},{num2},{num3}')
            result = (num1 * num2)*num3
            print(f'Result is {result}')
            break


get_2020()
