# This is deco 1
# This is deco 2
# This is deco 3
# This is test case1
# Callable object
# func test


def deco_1(func):

    print("This is deco 1")

    return func

@deco_1
def test_case1():
    print("This is test case1")

# ###################################

class CallableClass:

    def __call__(self):
        print("Callable object")


def deco_2(func):

    print("This is deco 2")

    return CallableClass()

@deco_2
def test_case2():
    print("This is test case2")

# ###################################

def func_test():
    print("func test")

def deco_3(func):

    print("This is deco 3")

    return func_test

@deco_3
def test_case3():
    print("This is test case3")

# ###################################

def deco_4(func):

    print("This is deco 4")

    def internal_func():

        print("Internal func")

    return internal_func

@deco_4
def test_case4():
    print("This is test case4")



test_case1()
test_case2()
test_case3()
test_case4()