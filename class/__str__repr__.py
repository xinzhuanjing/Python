# class A:

#     def __str__(self):
#         return "A: This is in __str__"

#     def __repr__(self):
#         return "A: This is in __repr__"

# instance_a = A()

# print(str(instance_a))
# print(repr(instance_a))
# print(instance_a)


# #######################


# class A:

#     def __repr__(self):
#         return "A: This is in __repr__"

# instance_a = A()

# print(str(instance_a))
# print(repr(instance_a))
# print(instance_a)


# ########################


# class A:

#     def __str__(self):
#         return "A: This is in __str__"

#     def __repr__(self):
#         return "A: This is in __repr__"

# class B(A):

#     def __str__(self):
#         return "B: This is in __str__"


# instance_b = B()

# print(str(instance_b))
# print(repr(instance_b))
# print(instance_b)


# ################

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# p = Person('Tom',18)
# print('name = {p.name} age = {p.age}'.format(p=p))

# ###################


# class A:

#     def __str__(self):
#         return "A: This is in __str__"

#     def __repr__(self):
#         return "A: This is in __repr__"

# instance_a = A()

# print("{!r}\n{!s}\n{!a}".format(instance_a, instance_a, instance_a))
