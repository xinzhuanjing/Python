
# class IterTest:

#     a = [1, 2, 3, 4, 5, 6]

#     def __init__(self):
#         self.index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         try:
#             data = IterTest.a[self.index]

#             self.index += 1

#             return data
#         except IndexError:
#             raise StopIteration


# import traceback

# test = IterTest()

# try:
#     instance_of_iterator = iter(test)
# except:
#     print(traceback.format_exc())

# print(next(test))
# print(next(test))
# print(next(test))
# print(next(test))
# print(next(test))
# print(next(test))
# print(next(test))

# #############


# class IterTest:

#     a = [1, 2, 3, 4, 5, 6]

#     def __init__(self):
#         self.index = 0

#     def __next__(self):
#         try:
#             data = IterTest.a[self.index]

#             self.index += 1

#             return data
#         except IndexError:
#             raise StopIteration

# import traceback

# test = IterTest()

# try:
#     instance_of_iterator = iter(test)
# except:
#     print(traceback.format_exc())

# print(next(test))
# print(next(test))
# print(next(test))
# print(next(test))
# print(next(test))
# print(next(test))
# print(next(test))

# ############


# class IterTest:

#     a = [1, 2, 3, 4, 5, 6]

#     def __init__(self):
#         self.index = 0

#     def __next__(self):
#         try:
#             data = IterTest.a[self.index]

#             self.index += 1

#             return data
#         except IndexError:
#             raise StopIteration

# class NewIter:

#     def __iter__(self):
#         return IterTest()

# import traceback

# test = NewIter()

# try:
#     instance_of_iterator = iter(test)
#     print(next(instance_of_iterator))
#     print(next(instance_of_iterator))
#     print(next(instance_of_iterator))
#     print(next(instance_of_iterator))
#     print(next(instance_of_iterator))
#     print(next(instance_of_iterator))
#     print(next(instance_of_iterator))
# except:
#     print(traceback.format_exc())

# #########

# class IterTest:

#     def __init__(self):
#         self.index = 0

#     def __next__(self):

#         data = 0

#         if self.index < 1:
#             data =  0
#         elif self.index < 3:
#             data =  1
#         else:
#             data =  2

#         self.index += 1

#         if self.index == 6:
#             raise StopIteration

#         return data

# test = IterTest()

# print(next(test))
# print(next(test))
# print(next(test))
# print(next(test))
# print(next(test))
# print(next(test))
# print(next(test))

# #######


# class IterTest():

#     a = [1, 2, 3, 4, 5, 6]

#     def __init__(self):
#         self.index = 0

#     def __iter__(self):

#         while self.index < len(IterTest.a):
#             data = IterTest.a[self.index]

#             self.index += 1

#             yield data

# import traceback

# test = IterTest()

# try:
#     instance_of_iterator = iter(test)
#     print(next(instance_of_iterator))
#     print(next(instance_of_iterator))
#     print(next(instance_of_iterator))
#     print(next(instance_of_iterator))
#     print(next(instance_of_iterator))
#     print(next(instance_of_iterator))
#     print(next(instance_of_iterator))
# except:
#     print(traceback.format_exc())




# ###########

# from collections import abc

# class IterTest(abc.Iterator):

#     a = [1, 2, 3, 4, 5, 6]

#     def __init__(self):
#         self.index = 0

#     def __next__(self):
#         try:
#             data = IterTest.a[self.index] + 10000

#             self.index += 1

#             return data
#         except IndexError:
#             raise StopIteration

# import traceback

# test = IterTest()

# try:
#     instance_of_iterator = iter(test)
#     print(next(instance_of_iterator))
#     print(next(instance_of_iterator))
#     print(next(instance_of_iterator))
#     print(next(instance_of_iterator))
#     print(next(instance_of_iterator))
#     print(next(instance_of_iterator))
#     print(next(instance_of_iterator))
# except:
#     print(traceback.format_exc())

# ############

a = [1, 2, 3, 4, 5, 6]
print(dir(a))
test = iter(a)
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))