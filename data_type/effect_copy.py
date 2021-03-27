# @profile
# def test():
#     a = [1]

#     b = [a] * 1024 * 1024 * 10

#     c = b[1024 * 1024:]

import copy

@profile
def test():
    a = [1]

    b = [a] * 1024 * 1024 * 10

    c = copy.deepcopy(b[1024 * 1024:])


if __name__ == "__main__":
    test()