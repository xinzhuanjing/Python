from functools import reduce


def square(x, y):
    return x*y


result = reduce(square, range(1, 5))
print(result)

# 24