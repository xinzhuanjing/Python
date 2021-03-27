# class Test:

#     def __init__(self, a, b):
#         self.add_a = a
#         self.add_b = b

#     def add(self):
#         return self.add_a + self.add_b

# #####################################
# class ClassTest:

#     def __init__(self):
#         print("This is in ClassTest")

#     def echo(self):
#         print("This is in echo")

# class_object_new_reference = ClassTest
# class_object_new_reference().echo()

# #####################################

# class ClassTest:

#     def __init__(self):
#         print("This is in ClassTest")

#     def echo(self):
#         print("This is in echo")

# def test(cls):
#     print("This is in test")
#     cls().echo()

# test(ClassTest)

# ###################################
# class ClassTest:

#     def __init__(self):
#         print("This is in ClassTest")

#     def echo(self):
#         print("This is in echo")

# def test():
#     print("This is in test")

#     return ClassTest

# class_object = test()
# class_object().echo()

# ##############################
# class ClassTest:

#     def __init__(self):
#         print("This is in ClassTest")

#     def echo(self):
#         print("This is in echo")


# test = {"a": ClassTest}

# test["a"]().echo()

# ##########################

# class ClassTest:

#     def __init__(self):
#         print("This is in ClassTest")

#     def echo(self):
#         print("This is in echo")

#     class InternalTest:

#         def __init__(self):
#             print("InternalTest")

#         def echo(self):
#             print("This is in echo of InternalTest")


# class_instance = ClassTest()
# class_instance.echo()
# class_instance.InternalTest().echo()

# ###########################

# def test():
#     print("This is in test")

#     class ClassTest:

#         def __init__(self):
#             print("This is in ClassTest")

#         def echo(self):
#             print("This is in echo")

#     return ClassTest

# class_object = test()
# class_object().echo()

# ###############################
# class ClassTest:

#     def __init__(self):
#         print("This is in ClassTest")

#     def echo(self):
#         print("This is in echo")

# class_instance_new_reference = ClassTest()
# class_instance_new_reference.echo()

# ###########################
# class ClassTest:

#     def __init__(self):
#         print("This is in ClassTest")

#     def echo(self):
#         print("This is in echo")

# def test(instance):
#     print("This is in test")
#     instance.echo()

# test(ClassTest())

# ############################
# def test():
#     print("This is in test")

#     class ClassTest:

#         def __init__(self):
#             print("This is in ClassTest")

#         def echo(self):
#             print("This is in echo")

#     return ClassTest()

# class_object = test()
# class_object.echo()

# #####################
class ClassTest:

    def __init__(self):
        print("This is in ClassTest")

    def echo(self):
        print("This is in echo")


test = {"a": ClassTest()}

test["a"].echo()
