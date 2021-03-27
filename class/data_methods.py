# class TestA:

#     static_data_a = 10

#     def echo1(self):
#         TestA.static_data_b = 10

# class TestB: pass

# Format = "{0:<60}{1}"
# # Step1
# print(Format.format("+" * 60, "Get Attrib"))
# print(Format.format("Attributes of Class object TestA:", sorted(set(dir(TestA)) - set(dir(TestB)))))
# class_instance = TestA()
# print(Format.format("Attributes of Class instance class_instance:", sorted(set(dir(class_instance)) - set(dir(TestB)))))

# # Step2
# print(Format.format("+" * 60, "Revise Static Data"))
# print(Format.format("TestA.static_data_a:", TestA.static_data_a))
# print(Format.format("class_instance.static_data_a:", class_instance.static_data_a))
# TestA.static_data_a = 0
# print(Format.format("TestA.static_data_a:", TestA.static_data_a))
# print(Format.format("class_instance.static_data_a:", class_instance.static_data_a))

# # Step3
# print(Format.format("+" * 60, "Add Static Data"))
# class_instance.echo1()
# print(Format.format("Attributes of Class object TestA:", sorted(set(dir(TestA)) - set(dir(TestB)))))
# print(Format.format("Attributes of Class instance class_instance:", sorted(set(dir(class_instance)) - set(dir(TestB)))))
# print(Format.format("TestA.static_data_b:", TestA.static_data_b))
# print(Format.format("class_instance.static_data_b:", class_instance.static_data_b))

# # Step4
# TestA.static_data_c = 1000
# print(Format.format("+" * 60, "Add Static Data"))
# print(Format.format("Attributes of Class object TestA:", sorted(set(dir(TestA)) - set(dir(TestB)))))
# print(Format.format("Attributes of Class instance class_instance:", sorted(set(dir(class_instance)) - set(dir(TestB)))))
# print(Format.format("TestA.static_data_c:", TestA.static_data_c))
# print(Format.format("class_instance.static_data_c:", class_instance.static_data_c))

# # Step5
# print(Format.format("+" * 60, "Delete Static Data"))
# del(TestA.static_data_c)
# print(Format.format("Attributes of Class object TestA:", sorted(set(dir(TestA)) - set(dir(TestB)))))
# print(Format.format("Attributes of Class instance class_instance:", sorted(set(dir(class_instance)) - set(dir(TestB)))))



# class TestA:

#     static_data_a = 10

#     def echo(self):
#         self.non_static_data_b = 10


# class TestB: pass

# Format = "{0:<60}{1}"

# # Step1
# print(Format.format("+" * 60, "Get Attrib"))
# print(Format.format("Attributes of Class object TestA:", sorted(set(dir(TestA)) - set(dir(TestB)))))
# class_instance = TestA()
# print(Format.format("Attributes of Class instance class_instance:", sorted(set(dir(class_instance)) - set(dir(TestB)))))

# # Step2
# print(Format.format("+" * 60, "Add attrib for class instance"))
# class_instance.echo()
# print(Format.format("Attributes of Class object TestA:", sorted(set(dir(TestA)) - set(dir(TestB)))))
# print(Format.format("Attributes of Class instance class_instance:", sorted(set(dir(class_instance)) - set(dir(TestB)))))

# # Step3
# print(Format.format("+" * 60, "Add attrib for class instance"))
# class_instance.non_static_data_c = 10
# print(Format.format("Attributes of Class object TestA:", sorted(set(dir(TestA)) - set(dir(TestB)))))
# print(Format.format("Attributes of Class instance class_instance:", sorted(set(dir(class_instance)) - set(dir(TestB)))))
# print(Format.format("class_instance.non_static_data_c:", class_instance.non_static_data_c))

# # Step4
# print(Format.format("+" * 60, "Revise attrib for class instance"))
# class_instance.non_static_data_c = 0
# print(Format.format("class_instance.non_static_data_c:", class_instance.non_static_data_c))

# # Step5
# print(Format.format("+" * 60, "Delete attrib for class instance"))
# del(class_instance.non_static_data_c)
# print(Format.format("Attributes of Class object TestA:", sorted(set(dir(TestA)) - set(dir(TestB)))))
# print(Format.format("Attributes of Class instance class_instance:", sorted(set(dir(class_instance)) - set(dir(TestB)))))



# class TestA:

#     static_data_a = 10

#     def echo1(self):
#         TestA.static_data_b = 10

#     def echo2(self):
#         self.static_data_b = 100


# class TestB: pass

# Format = "{0:<60}{1}"

# # Step1
# print(Format.format("+" * 60, "Get Attrib"))
# print(Format.format("Attributes of Class object TestA:", sorted(set(dir(TestA)) - set(dir(TestB)))))
# class_instance = TestA()
# print(Format.format("Attributes of Class instance class_instance:", sorted(set(dir(class_instance)) - set(dir(TestB)))))

# # Step2
# print(Format.format("+" * 60, "Change the same name static data through class instance"))
# class_instance.echo1()
# print(Format.format("Attributes of Class object TestA:", sorted(set(dir(TestA)) - set(dir(TestB)))))
# print(Format.format("Attributes of Class instance class_instance:", sorted(set(dir(class_instance)) - set(dir(TestB)))))
# class_instance.echo2()
# print(Format.format("Attributes of Class object TestA:", sorted(set(dir(TestA)) - set(dir(TestB)))))
# print(Format.format("Attributes of Class instance class_instance:", sorted(set(dir(class_instance)) - set(dir(TestB)))))
# print(Format.format("TestA.static_data_b:", TestA.static_data_b))
# print(Format.format("class_instance.static_data_b:", class_instance.static_data_b))

# # Step3
# print(Format.format("+" * 60, "Change the same name static data through class instance"))
# class_instance.static_data_a = 0
# print(Format.format("Attributes of Class object TestA:", sorted(set(dir(TestA)) - set(dir(TestB)))))
# print(Format.format("Attributes of Class instance class_instance:", sorted(set(dir(class_instance)) - set(dir(TestB)))))
# print(Format.format("TestA.static_data_b:", TestA.static_data_b))
# print(Format.format("class_instance.static_data_b:", class_instance.static_data_b))

# # Step4
# print(Format.format("+" * 60, "Delete the same name static data through class instance"))
# del(class_instance.static_data_b)
# print(Format.format("Attributes of Class object TestA:", sorted(set(dir(TestA)) - set(dir(TestB)))))
# print(Format.format("Attributes of Class instance class_instance:", sorted(set(dir(class_instance)) - set(dir(TestB)))))
# print(Format.format("TestA.static_data_b:", TestA.static_data_b))
# print(Format.format("class_instance.static_data_b:", class_instance.static_data_b))







# ##################################################

# class TestA:

#     def echo(self):
#         print("This is in echo")

#     @staticmethod
#     def echo1():
#         print("This is in echo1")

# class TestB: pass

# Format = "{0:<60}{1}"
# # Step1
# print(Format.format("+" * 60, "Get Attrib"))
# print(Format.format("Attributes of Class object TestA:", sorted(set(dir(TestA)) - set(dir(TestB)))))
# class_instance = TestA()
# print(Format.format("Attributes of Class instance class_instance:", sorted(set(dir(class_instance)) - set(dir(TestB)))))

# # Step2
# print(Format.format("+" * 60, "Revise Static Method"))
# TestA.echo1()
# class_instance.echo1()
# TestA.echo1 = "This is revised echo1"
# print(TestA.echo1)
# print(class_instance.echo1)

# # Step3
# print(Format.format("+" * 60, "Revise non-Static Method"))
# TestA.echo(class_instance)
# TestA.echo = "This is revised echo"
# print(TestA.echo)
# print(class_instance.echo)

# # Step4
# print(Format.format("+" * 60, "Add Static Method"))
# @staticmethod
# def echo2(a):
#     print(a)

# TestA.echo2 = echo2
# print(Format.format("Attributes of Class object TestA:", sorted(set(dir(TestA)) - set(dir(TestB)))))
# print(Format.format("Attributes of Class instance class_instance:", sorted(set(dir(class_instance)) - set(dir(TestB)))))
# TestA.echo2("This is in echo2")
# class_instance.echo2("This is in echo2")

# # Step5
# print(Format.format("+" * 60, "Add non-Static Method"))
# def echo3(self, a):
#     print(a)

# TestA.echo3 = echo3
# print(Format.format("Attributes of Class object TestA:", sorted(set(dir(TestA)) - set(dir(TestB)))))
# print(Format.format("Attributes of Class instance class_instance:", sorted(set(dir(class_instance)) - set(dir(TestB)))))

# TestA.echo3(class_instance, "This is in echo3")
# class_instance.echo3("This is in echo3")

# # Step6
# print(Format.format("+" * 60, "Delete Method"))

# del(TestA.echo3)
# del(TestA.echo2)

# print(Format.format("Attributes of Class object TestA:", sorted(set(dir(TestA)) - set(dir(TestB)))))
# print(Format.format("Attributes of Class instance class_instance:", sorted(set(dir(class_instance)) - set(dir(TestB)))))




# class TestA:

#     def echo(self):
#         print("This is in echo")

#     @staticmethod
#     def echo1():
#         print("This is in echo1")

# class TestB: pass

# Format = "{0:<60}{1}"
# # Step1
# print(Format.format("+" * 60, "Get Attrib"))
# print(Format.format("Attributes of Class object TestA:", sorted(set(dir(TestA)) - set(dir(TestB)))))
# class_instance = TestA()
# print(Format.format("Attributes of Class instance class_instance:", sorted(set(dir(class_instance)) - set(dir(TestB)))))

# # Step2
# print(Format.format("+" * 60, "Revise Static Method"))
# TestA.echo1()
# class_instance.echo1()
# class_instance.echo1 = "This is revised echo1"
# TestA.echo1()
# print(class_instance.echo1)

# # Step3
# print(Format.format("+" * 60, "Revise non-Static Method"))
# TestA.echo(class_instance)
# class_instance.echo = "This is revised echo"
# TestA.echo(class_instance)
# print(class_instance.echo)

# # Step4
# print(Format.format("+" * 60, "Add non-Static Method"))
# def echo3(self, a):
#     print(a)

# class_instance.echo3 = echo3
# print(Format.format("Attributes of Class object TestA:", sorted(set(dir(TestA)) - set(dir(TestB)))))
# print(Format.format("Attributes of Class instance class_instance:", sorted(set(dir(class_instance)) - set(dir(TestB)))))

# class_instance.echo3(class_instance, "This is in echo3")

# # Step5
# print(Format.format("+" * 60, "Delete Method"))

# del(class_instance.echo3)
# del(class_instance.echo)

# print(Format.format("Attributes of Class object TestA:", sorted(set(dir(TestA)) - set(dir(TestB)))))
# print(Format.format("Attributes of Class instance class_instance:", sorted(set(dir(class_instance)) - set(dir(TestB)))))
