# class B:
#     pass

# print("__class__ B:   %s" % B.__class__)
# print("__class__ B(): %s" % B().__class__)

# ##############################################

# class B:
#     pass

# print("__name__ B:   %s" % B.__name__)
# print("__name__ B(): %s" % B().__class__.__name__)

# ###########################################


# class B:

#     def __del__(self):
#         print("delete")

#     def echo(self):
#         print("echo")

# b = B()
# b.echo()
# del b
# b.echo()

# ######################################

# class B:

#     def __del__(self):
#         print("delete")

#     def echo(self):
#         print("echo")

# b = B()
# b.echo()
# b1 = b
# del b1
# b.echo()

# #################################

# from memory_profiler import profile


# class A(object):
#     def __init__(self, x):
#         self.x = x


# @profile
# def main():
#     f = [A(523825) for i in range(2000000)]


# if __name__ == '__main__':
#     main()

# #################################

# from memory_profiler import profile

# class A(object):

#     __slots__=('x')

#     def __init__(self, x):
#         self.x = x

# @profile
# def main():
#     f = [A(523825) for i in range(200000)]

# if __name__ == '__main__':
#     main()


# ##########################

# class A(object):

#     def __init__(self, x):
#         self.x = x

# class B(object):

#     __slots__=('x')

#     def __init__(self, x):
#         self.x = x

# print("dir A: %s" % dir(A))
# print("dir B: %s" % dir(B))

# b = B(1)

# if '__dict__' in dir(b):
#     print("yes")
# else:
#     print("no")

# B.t=1
# b.y = 10


# #############################

# class Test:
#     pass

# print(Test.__module__)


# #############################

# class Test:
#     pass

# print(Test.__qualname__)


# #############################


# class MyType(type):

#     def __instancecheck__(cls, instance):
#         print("Class Object: %s" % cls)
#         print("Class Instance: %s" % instance)

#         if instance.__class__ == cls:
#             return True
#         return False


# class A(metaclass=MyType):
#     pass

# print(isinstance(1, A))


# #############################


# class MyType(type):

#     def __subclasscheck__(cls, new_class):
#         print("Class Object: %s" % cls)
#         print("Class new_class: %s" % new_class)

#         if cls in new_class.__mro__:
#             return True
#         return False


# class A(metaclass=MyType):
#     pass

# class B(A):
#     pass

# print(issubclass(B, A))


# #############################


# import abc


# class Base1(abc.ABC):

#     @abc.abstractmethod
#     def my_protocol1(self):
#         pass

#     @classmethod
#     def __subclasshook__(cls, subclass):
#         print(cls)
#         print(subclass)
#         if cls is Base1:
#             if any("my_protocol1" in B.__dict__ for B in subclass.__mro__):
#                 return True

#         return NotImplemented

#     def echo1(self):
#         pass


# class Base2(abc.ABC):

#     @classmethod
#     def __subclasshook__(cls, subclass):
#         print(cls)
#         print(subclass)

#         if cls is Base2:
#             if any("my_protocol2" in B.__dict__ for B in subclass.__mro__):
#                 return True

#         return NotImplemented

#     def echo2(self):
#         pass


# class Test:

#     def my_protocol1(self, a, b):
#         pass

#     def my_protocol2(self, a, b, c, d, e):
#         pass

# print("Test is the subclass of Base1: %s" % issubclass(Test, Base1))
# print("Test is the subclass of Base2: %s" % issubclass(Test, Base2))
# print("-")
# test = Test()
# print("test is the instance of Base1: %s" % isinstance(test, Base1))
# print("test is the instance of Base2: %s" % isinstance(test, Base2))
# print("-")
# print(Test.__mro__)


# ###################

# class Test:
#     pass

# class Test1(Test):
#     pass

# class Test2(Test):
#     pass

# class Test3(Test1):
#     pass

# print(Test.__subclasses__())


# #################


