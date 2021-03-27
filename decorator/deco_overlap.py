def deco1(func):
    print("This is in deco1")
    return func


def deco2(func):

    print("This is in deco2")

    def inter(a, b):
        func(a, b)
        return a + b

    return inter

@deco2
@deco1
def test(a, b):
    print("a + b = %s" % (a + b))

test(1, 999)