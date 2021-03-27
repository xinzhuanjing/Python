# def test(a, b, c):
#     print("a: %s" % a)
#     print("b: %s" % b)
#     print("c: %s" % c)

# print("position assignment")
# test(1, 2, 3)
# print("keyword assignment")
# test(c=5, b=4, a=1)
# print("mix of position and keyword assignment")
# test(1, b=4, c=5)


# #####################


# def test(a, b=2, c=3):
#     print("a: %s" % a)
#     print("b: %s" % b)
#     print("c: %s" % c)

# print("position assignment")
# test(1)
# print("-")
# test(1, 3, 5)
# print("keyword assignment")
# test(a=1)
# print("-")
# test(b=3, a=1, c=5)
# print("mix of position and keyword assignment")
# test(1, 3, c=5)

# ####################

# def test(a, b=2, c=3, *args):
#     print("a: %s" % a)
#     print("b: %s" % b)
#     print("c: %s" % c)
#     print("args: %s" % str(args))

# print("position assignment")
# test(1, 2, 3, 4, 5, 6)
# print("keyword assignment")
# test(b=2, a=1, c=3)
# print("mix of position and keyword assignment")
# test(1, b=2, c=3)

# #####################

# def test(a, b=2, c=3, *args, d=4, e, f=6, g):
#     print("a: %s" % a)
#     print("b: %s" % b)
#     print("c: %s" % c)
#     print("args: %s" % str(args))
#     print("d: %s" % d)
#     print("e: %s" % e)
#     print("f: %s" % f)
#     print("g: %s" % g)

# print("position assignment before args")
# test(1, 2, 3, 4, 5, 6, e=5, g=7)
# print("keyword assignment before args")
# test(b=2, a=1, c=3, e=5, g=7)
# print("mix of position and keyword assignment before args")
# test(1, b=2, c=3, e=5, g=7, d=4, f=6)


# ######################


# def test(a, b=2, c=3, **kwargs):
#     print("a: %s" % a)
#     print("b: %s" % b)
#     print("c: %s" % c)
#     print("kwargs: %s" % str(kwargs))

# print("position assignment")
# test(1, 2, 3)
# print("keyword assignment")
# test(a=1, b=2, c=3, d=4, e=5, f=6)
# print("mix of position and keyword assignment")
# test(1, d=4, e=5, f=6)

# #######################


# def test(a, b=2, c=3, *args, d=4, e, **kwargs):
#     print("a: %s" % a)
#     print("b: %s" % b)
#     print("c: %s" % c)
#     print("args: %s" % str(args))
#     print("d: %s" % d)
#     print("e: %s" % e)
#     print("kwargs: %s" % kwargs)

# print("position assignment before args")
# test(1, 2, 3, 4, 5, 6, e=5, g=7)
# print("keyword assignment before args")
# test(b=2, a=1, c=3, e=5, g=7)
# print("mix of position and keyword assignment before args")
# test(1, b=2, c=3, e=5, g=7, d=4, f=6)