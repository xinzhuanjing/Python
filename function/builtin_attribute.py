# def test():
#     pass

# print(dir(test))

# ##################

# def test(a:int, b:str, c) -> int:
#     print("a: %s" % a)
#     print("b: %s" % b)
#     print("c: %s" % c)

#     return a

# print(test.__annotations__)


# ##################

# def test(a:int, b:str, c):
#     print("a: %s" % a)
#     print("b: %s" % b)
#     print("c: %s" % c)

# print("type of test: %s" % type(test))
# print("type of test: %s" % test.__class__)
# print("type of function class object: %s" % test.__class__.__class__)
# print("inheriting of function class object: %s" % str(test.__class__.__mro__))


# ###################


# def test():
#     a = 1
#     c = 2
#     d = 3

#     def inter():
#         b = a + 1
#         e = c

#     print(inter.__closure__)
#     print(type(inter.__closure__))

#     for i in inter.__closure__:
#         print(i.cell_contents)

# test()
# print(test.__closure__)


# ######################

# def test():
#     pass

# print(test.__code__)


# #######################

# def test(a, b=1, c=2, *args, m=1, n, **kwargs):
#     pass

# print(test.__defaults__)


# #####################

# def test():
#     pass

# test.a = 1
# test.b = 1

# print(dir(test))
# print(test.__dict__)


# ####################

# def test():
#     test.a = 1
#     test.b = 1

# print(dir(test))
# print(test.__dict__)
# test()
# print(dir(test))
# print(test.__dict__)


# ######################

# def test():
#     '''doc'''
#     pass

# print(test.__doc__)


# ####################

# a = 1
# b = 1

# class t: pass

# def test():
#     pass

# print(test.__globals__)
# test.__globals__ = {}

# #######################


# def test(a, b=1, c=1, *args, m=1, n, p=1, **kwargs):
#     pass

# print(test.__kwdefaults__)


# ######################


# def test():
#     pass

# print(test.__module__)

# #####################

# def test():
#     pass

# print(test.__name__)


# ######################


# def test():
#     pass

# print(test.__qualname__)

# #######################

# def test(a, b, c=1, *args, m=1, n, **kwargs):
#     '''function built-in attributes study'''

#     p = 1
#     q = 1

#     sum_data = a + b

#     return sum_data

# print(dir(test))


# #######################