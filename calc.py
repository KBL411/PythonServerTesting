def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("the denominator cannot be zero")
    return a / b


if "__main__" == __name__:
    print("test for add passed: {}".format(3 == add(1, 2)))
    print("test for substrac passed: {}".format(-1 == subtract(1, 2)))
    print("test for multiply passed: {}".format(2 == multiply(1, 2)))
    print("test for divide passed: {}".format(2 == divide(4, 2)))
