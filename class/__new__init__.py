# class TestA:

#     def __new__(cls, *argv, **kwargs):
#         print("This is in __new__")

#         print("Class object name: %s, type: %s, __mro__: %s" % (cls.__name__, cls.__class__, cls.__mro__))
#         print("Argv: %s" %(str(argv)))

#         for k,v in kwargs.items():
#             print("Key: %s, Value: %s" % (k, v))

#     def __init__(self, a, b, c, d, e, f):
#         print("This is in __init__")
#         print("Par: a, Value: %s" % a)
#         print("Par: b, Value: %s" % b)
#         print("Par: c, Value: %s" % c)
#         print("Par: d, Value: %s" % d)
#         print("Par: e, Value: %s" % e)
#         print("Par: f, Value: %s" % f)


# test_a = TestA(1,2,3, d=5, e=6, f=7)

# ######################################################################################


# class TestA:

#     def __new__(cls, *argv, **kwargs):
#         print("This is in __new__")

#         print("Class object name: %s, type: %s, __mro__: %s" % (cls.__name__, cls.__class__, cls.__mro__))
#         print("Argv: %s" %(str(argv)))

#         for k,v in kwargs.items():
#             print("Key: %s, Value: %s" % (k, v))

#         return super(TestA, cls).__new__(cls)

#     def __init__(self, a, b, c, d, e, f):
#         print("This is in __init__")
#         print("Par: a, Value: %s" % a)
#         print("Par: b, Value: %s" % b)
#         print("Par: c, Value: %s" % c)
#         print("Par: d, Value: %s" % d)
#         print("Par: e, Value: %s" % e)
#         print("Par: f, Value: %s" % f)

#     def echo(self):
#         print("Echo")


# test_a = TestA(1,2,3, d=5, e=6, f=7)
# print(dir(test_a))

# ######################################################################################

# class Mymeta(type):
#     def __new__(cls, a, b, c):
#         return super(Mymeta, cls).__new__(cls, a, b, c)

#     def echo(self):
#         print("Echo")

#     def __init__(self, class_name, class_bases, class_dic):
#         print(self)
#         print("Name: %s" % class_name)
#         print("Bases: %s" % class_bases)
#         print("Attrs: %s" % class_dic)
#         super(Mymeta, self).__init__(class_name, class_bases, class_dic)

# meta_a = Mymeta("Test", (object, ), dict(data_a=10, data_b=10))


# ######################################################################################

# class TestA:

#     def __new__(cls, a, b, c):
#         print("This is in __new__")

#         print("Class object name: %s, type: %s, __mro__: %s" % (cls.__name__, cls.__class__, cls.__mro__))

#         print("a in __new__: %s" %a)
#         print("b in __new__: %s" %b)
#         print("c in __new__: %s" %c)

#         return super(TestA, cls).__new__(cls)

#     def __init__(self, a, b, c, d, e, f):
#         print("This is in __init__")
#         print("Par: a, Value: %s" % a)
#         print("Par: b, Value: %s" % b)
#         print("Par: c, Value: %s" % c)
#         print("Par: d, Value: %s" % d)
#         print("Par: e, Value: %s" % e)
#         print("Par: f, Value: %s" % f)


# test_a = TestA(1,2,3)