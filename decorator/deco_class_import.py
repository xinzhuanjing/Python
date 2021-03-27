# class Test:

#     def __init__(self):
#         print("This is in __init__")
#         pass

#     def __call__(self, func):
#         print("This is in __call__")
#         def inter(a, b):
#             print("This is in inter")
#             ret = func(a, b)
#             return a + b - ret

#         return inter

# @Test()
# def deb(a, b):
#     return 1


# ##############



# class Test:

#     def __init__(self, func):
#         print("This is in __init__")
#         self.func = func

#     def __call__(self, a, b):
#         print("This is in __call__")
#         ret = self.func(a, b)
#         return a + b - ret

# @Test
# def deb(a, b):
#     return 1


# #############


# class Test:

#     def __init__(self, par1):
#         print("This is in __init__")
#         self.par1 = par1

#     def __call__(self, func):
#         print("This is in __call__")

#         if self.par1:
#             print("This is par1 = True")
#             def inter1(a, b):
#                 print("This is in inter1")
#                 ret = func(a, b)
#                 return a + b - ret
#             return inter1
#         else:
#             print("This is par1 = False")
#             def inter2(a, b):
#                 print("This is in inter2")
#                 ret = func(a, b)
#                 return a + b - ret + 1
#             return inter2


# @Test(True)
# def deb(a, b):
#     return 1

# @Test(False)
# def deb1(a, b):
#     return 1
