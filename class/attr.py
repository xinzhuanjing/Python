# for i in dir(type):
#     print(i)

# for i in dir(object):
#     print(i)


# for i in sorted(set(vars(object))):
#     print(i)

# print(object.__class__.__name__)
# print(object.__name__)

# import abc

# class M(metaclass=abc.ABCMeta): pass

# for i in dir(abc.ABCMeta):
#     print(i)

# ######################################################

# class T:
#     pass

# class A:

#     def echo(self):
#         print("This is in A")

# class B(A):

#     def __init__(self):
#         self.b = 10

#     def echo1(self):
#         print("This is in B")

# print("class object T: %s" % T.__dict__)
# print("class object A: %s" % A.__dict__)
# print("class object B: %s" % B.__dict__)

# ######################################################

# class T:
#     pass

# class A:

#     def echo(self):
#         print("This is in A")

# class B(A):

#     def __init__(self):
#         self.b = 10

#     def echo1(self):
#         print("This is in B")

# print("class object B: %s" % B.__dict__)

# del B.echo1
# print("class object B: %s" % B.__dict__)
# del B.echo


# ######################################################

# class A:

#     def echo(self):
#         print("This is in A")

# class B(A):

#     def __init__(self):
#         self.b = 10

#     def echo1(self):
#         print("This is in B")

# print("class object B: %s" % B.__dict__)
# print("instance of B: %s" % B().__dict__)

# #####################################################

# class A:
#     same = 10

#     def echo(self):
#         print("This is in A")

# class B(A):

#     def __init__(self):
#         self.b = 10
#         self.same = 0

#     def echo1(self):
#         print("This is in B")

# b = B()

# print("class object B: %s" % B.__dict__)
# print("instance of B: %s" % b.__dict__)

# print("instance same: id: %s value: %s" % (id(b.same), b.same))
# del b.same
# print("instance same: id: %s value: %s" % (id(b.same), b.same))
# print("class same: id: %s value: %s" % (id(B.same), B.same))

# ####################################################

# class A:
#     same = 10

#     def echo(self):
#         print("This is in A")

# class B(A):

#     def __init__(self):
#         self.b = 10
#         self.same = 0

#     def echo1(self):
#         print("This is in B")

# b = B()

# print("instance of B: %s" % b.__dict__)
# b.c = 1
# print("instance of B: %s" % b.__dict__)


# ##############################################

class B:

    def __dir__(self):
        return [1,2,3]

    def echo1(self):
        print("This is in B")

print("__class__ B:         %s" % B.__class__)
print("B.__class__.__dir__: %s" % sorted(B.__class__.__dir__(B)))
print("dir B:               %s" % dir(B))
print("type.__dir__:        %s" % sorted(type.__dir__(B)))

b = B()
print("__class__ b:         %s" % b.__class__)
print("b.__class__.__dir__: %s" % sorted(b.__class__.__dir__(b)))
print("dir b:               %s" % dir(b))
print("object.__dir__:      %s" % sorted(object.__dir__(b)))