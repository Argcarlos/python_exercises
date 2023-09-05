# import mathstuff

# the same

# from mathstuff import natural_sum

import mathstuff as math


def total(numbers):
    s = 0
    for number in numbers:
        s += number
    return s


def natural_sum(last_number):
    if last_number < 1:
        return last_number

    result = 0
    for number in range(1, last_number + 1):
        result += number

    return result


def recursive_natural_sum(last_number):
    if last_number < 1:
        return last_number

    return last_number + recursive_natural_sum(last_number - 1)


print_hello = lambda: print('Hello, World!')


def check_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


# ----------#

text = 'Hello, {name}'


# -------------#
def total2(*args):
    print(type(args))

    t = 0
    for arg in args:
        t += arg

    return t


def items(**kwargs):
    print(type(kwargs))

    for key, value in kwargs.items():
        print(f"{key} : {value}")


def main():
    global text

    print(total([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    # last_number = int(input('up to which number would you like to calculate the sum?\n- '))

    # print(natural_sum(last_number))

    # last_number = int(input('up to which number would you like to calculate the sum?\n- '))

    # print(recursive_natural_sum(last_number))

    print_hello()

    numbers = [1, 2, 5, 4, 7, 88, 12, 15, 55, 77, 95]

    even_numbers = filter(check_even, numbers)

    print(list(even_numbers))

    numbers = [1, 2, 5, 4, 7, 88, 20, 24, 12, 15, 55, 77, 95]

    even_numbers = filter(lambda number: True if number % 2 == 0 else False, numbers)

    print(list(even_numbers))

    text = text.format(name='Carlos')
    print(text)

    print(total2(1, 2, 3, 4, 5))

    items(
        Apple=10,
        Orange=8,
        Grape=35
    )

    last_number = int(input('up to which number would you like to calculate the sum?\n- '))

    # print(mathstuff.natural_sum(last_number))

    # print(natural_sum(last_number))

    print(math.natural_sum(last_number))


if __name__ == '__main__':
    main()
