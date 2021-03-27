# class TestA:
#     pass

# class TestB(TestA):
#     pass

# print(type(TestA))
# print(type(TestB))
# print(type(TestA()))
# print(type(TestB()))

# ###################
# FORMT_STR = "{0:<30} Type: {1:<30} __mro__: {2}"

# print(FORMT_STR.format("type",str(type(type)), str(type.__mro__)))
# print(FORMT_STR.format("object",str(type(object)), str(object.__mro__)))

# ##################

# class TestA:
#     pass


# class TestB:
#     pass


# class TestC(TestA, TestB):

#     attr_test = "This is a test"

#     def echo(self, test_echo):
#         print(test_echo)

# def echo(self, test_echo):
#     print(test_echo)
# new_class_TestC = type("TestC", (TestA, TestB), {"attr_test": "This is a test", "echo": echo})

# print(TestC.__name__)
# TestC().echo("Echo")
# new_class_TestC().echo("Echo")
# print(new_class_TestC.__name__)

# ######################
# build-in type

# FORMT_STR = "{0:<20} Id: {1:<20} Type: {2:<20} Value: {3:<20} __class__: {4:<20} __mro__: {5}"

# print(FORMT_STR.format("int", id(int), str(type(int)), str(int), str(int.__class__), str(int.__mro__)))
# print(FORMT_STR.format("str", id(str), str(type(str)), str(str), str(str.__class__), str(str.__mro__)))
# print(FORMT_STR.format("list", id(list), str(type(list)), str(list), str(list.__class__), str(list.__mro__)))
# print(FORMT_STR.format("dict", id(dict), str(type(dict)), str(dict), str(dict.__class__), str(dict.__mro__)))
# print(FORMT_STR.format("set", id(set), str(type(set)), str(set), str(set.__class__), str(set.__mro__)))
# print(FORMT_STR.format("tuple", id(tuple), str(type(tuple)), str(tuple), str(tuple.__class__), str(tuple.__mro__)))
# print(FORMT_STR.format("float", id(float), str(type(float)), str(float), str(float.__class__), str(float.__mro__)))
# print(FORMT_STR.format("bytearray", id(bytearray), str(type(bytearray)), str(bytearray), str(bytearray.__class__), str(bytearray.__mro__)))
# print(FORMT_STR.format("memoryview", id(memoryview), str(type(memoryview)), str(memoryview), str(memoryview.__class__), str(memoryview.__mro__)))


# class TestA:
#     pass

# class TestB(TestA):
#     pass

# print("\n\n")
# print(FORMT_STR.format("TestA", id(TestA), str(type(TestA)), str(TestA), str(TestA.__class__), str(TestA.__mro__)))
# print(FORMT_STR.format("TestB", id(TestB), str(type(TestB)), str(TestB), str(TestB.__class__), str(TestB.__mro__)))

# ##############
