# class Test:

#     A = 10

#     def __init__(self):
#         self.a = 1

#     def __getattribute__(self, item):
#         print("This is in __getattribute__")
#         return object.__getattribute__(self, item)

# print("Instance: a = %s" % Test().a)
# print("Instance: A = %s" % Test().a)
# print("Class: A = %s" % Test.A)


# ####

# class Test:

#     A = 10

#     def __init__(self):
#         self.a = 1

#     def __getattribute__(self, item):
#         print("This is in __getattribute__")
#         return object.__getattribute__(self, item)

# hasattr(Test(), "a")
# getattr(Test(), "A")

# ####

# class Test:

#     def __init__(self):
#         self.a = 1

#     def __getattribute__(self, item):
#         print("This is in __getattribute__")
#         if item not in super(Test, self).__getattribute__("__dict__"):
#             print("item: %s is not in __dict__" % item)
#             raise AttributeError
#         return super(Test, self).__getattribute__(item)

#     def __getattr__(self, item):
#         print("This is __getattr__")


# print("Instance: a = %s" % Test().a)
# print("Instance: b = %s" % Test().b)

# ####

# class Test:

#     def __init__(self):
#         self.a = 1

#     def __getattribute__(self, item):
#         print("This is in __getattribute__")
#         if item not in super(Test, self).__getattribute__("__dict__"):
#             print("item: %s is not in __dict__" % item)
#             raise AttributeError
#         return super(Test, self).__getattribute__(item)

#     def __getattr__(self, item):
#         print("This is __getattr__")


# hasattr(Test(), "b")
# getattr(Test(), "c")


# #####

# class Test:

#     def __init__(self):
#         self.a = 1

#     def __setattr__(self, name, value):
#         print("This is __setattr__, name=%s, value=%s" % (name, value))
#         self.__dict__[name] = value

# test = Test()
# test.a = 2
# test.b = 1


# ######

# class Test:

#     def __init__(self):
#         self.a = 1

#     def __setattr__(self, name, value):
#         print("This is __setattr__, name=%s, value=%s" % (name, value))
#         super(Test, self).__setattr__(name, value)

# test = Test()
# test.a = 2
# test.b = 1


# #######

# class Test:

#     def __init__(self):
#         self.a = 1

#     def __setattr__(self, name, value):
#         print("This is __setattr__, name=%s, value=%s" % (name, value))
#         super(Test, self).__setattr__(name, value)

# test = Test()
# setattr(test, "a", 2)
# setattr(test, "b", 1)


# ######


# class Test:

#     def __init__(self):
#         self.a = 1

#     def __delattr__(self, item):
#         print("This is __delattr__, item=%s" % item)
#         self.__dict__.pop(item)

# test = Test()

# del test.a
# print(test.__dict__)


# ######

# class Test:

#     def __init__(self):
#         self.a = 1

#     def __delattr__(self, item):
#         print("This is __delattr__, item=%s" % item)
#         super(Test, self).__delattr__(item)

# test = Test()

# del test.a
# print(test.__dict__)


