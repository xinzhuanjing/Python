# class Test:

#     def __init__(self):
#         pass

#     def __call__(self, func):
#         print("This is in __call__")
#         def inter(a, b):
#             ret = func(a, b)
#             return a + b - ret

#         return inter

# @Test()
# def deb(a, b):
#     return 1

# ret = deb(1, 2)
# print(ret)


# ##############



# class Test:

#     def __init__(self, func):
#         print(func.__name__)
#         self.func = func

#     def __call__(self, a, b):
#         print("This is in __call__")
#         ret = self.func(a, b)
#         return a + b - ret

# @Test
# def deb(a, b):
#     return 1

# ret = deb(1, 2)
# print(ret)


# #############


# class Test:

#     def __init__(self, par1):
#         self.par1 = par1

#     def __call__(self, func):
#         print("This is in __call__")

#         if self.par1:
#             def inter1(a, b):
#                 ret = func(a, b)
#                 return a + b - ret
#             return inter1
#         else:
#             def inter2(a, b):
#                 ret = func(a, b)
#                 return a + b - ret + 1
#             return inter2


# @Test(True)
# def deb(a, b):
#     return 1

# ret = deb(1, 2)
# print(ret)

# @Test(False)
# def deb1(a, b):
#     return 1

# ret = deb1(1, 2)
# print(ret)


