# FORMAT = "{0:<60}{1}"

# class Override(object):

#     def __init__(self, trust_attr_name):
#         self.trust_attr_name = trust_attr_name

#     def __set__(self, instance, value):
#         print(FORMAT.format("Descriptor:", "Override-set"))
#         print(FORMAT.format("Trust Class Instance:", instance))
#         print(FORMAT.format("Setted Value:", value))
#         print(FORMAT.format("Name:", self.trust_attr_name))

#         try:
#             value = int(value)
#         except Exception:
#             print("Non-int value")
#             raise
#         else:
#             instance.__dict__[self.trust_attr_name] = value

#     def __get__(self, instance, owner):
#         print(FORMAT.format("Descriptor:", "Override-get"))
#         print(FORMAT.format("Trust Class Instance:", instance))
#         print(FORMAT.format("Trust Class Object:", owner))

#         if instance != None:
#             try:
#                 return instance.__dict__[self.trust_attr_name]
#             except Exception:
#                 print("No %s in the trust class instance" % self.trust_attr_name)
#                 return None
#         else:
#             try:
#                 return owner.__dict__[self.trust_attr_name]
#             except Exception:
#                 print("No %s in the trust class object" % self.trust_attr_name)
#                 return None

#     def __delete__(self, instance):
#         print(FORMAT.format("Descriptor:", "Override-delete"))
#         print(FORMAT.format("Trust Class Instance:", instance))

#         del instance.__dict__[self.trust_attr_name]

# class DescriptorTest(object):
#     add_a = Override("add_a")
#     man_b = Override("add_e")

#     def __init__(self):

#         self.man_b = 30
#         self.add_c = 60

# print("================Create instance")
# add = DescriptorTest()
# print("-")
# print(add.__dict__)
# print("================Read")
# print(add.add_a)
# print("-")
# print(add.man_b)
# print("-")
# print(add.add_c)
# print("================Write")
# add.add_a = 0
# print("-")
# add.man_b = 1
# print("-")
# add.add_c = 2
# print(add.__dict__)
# print("================Delete")
# del add.add_a
# print("-")
# del add.man_b
# print("-")
# del add.add_c
# print(add.__dict__)

# ###################

# FORMAT = "{0:<60}{1}"

# class Override(object):

#     def __init__(self, trust_attr_name):
#         self.trust_attr_name = trust_attr_name

#     def __set__(self, instance, value):
#         print(FORMAT.format("Descriptor:", "Override-set"))
#         print(FORMAT.format("Trust Class Instance:", instance))
#         print(FORMAT.format("Setted Value:", value))
#         print(FORMAT.format("Name:", self.trust_attr_name))

#         try:
#             value = int(value)
#         except Exception:
#             print("Non-int value")
#             raise
#         else:
#             instance.__dict__[self.trust_attr_name] = value


# class DescriptorTest(object):
#     add_a = Override("add_a")
#     man_b = Override("add_e")

#     def __init__(self):

#         self.man_b = 30
#         self.add_c = 60

# print("================Create instance")
# add = DescriptorTest()
# print("-")
# print(add.__dict__)
# print("================Read")
# print(add.add_a)
# print("-")
# print(add.man_b)
# print("-")
# print(add.add_c)
# print("================Write")
# add.add_a = 0
# print("-")
# add.man_b = 1
# print("-")
# add.add_c = 2
# print(add.__dict__)
# print("================Delete")
# del add.add_c
# del add.add_e
# del add.add_a

# #################

# FORMAT = "{0:<60}{1}"

# class Override(object):

#     def __init__(self, trust_attr_name):
#         self.trust_attr_name = trust_attr_name

#     def __get__(self, instance, owner):
#         print(FORMAT.format("Descriptor:", "Override-get"))
#         print(FORMAT.format("Trust Class Instance:", instance))
#         print(FORMAT.format("Trust Class Object:", owner))

#         if instance != None:
#             try:
#                 return instance.__dict__[self.trust_attr_name]
#             except Exception:
#                 print("No %s in the trust class instance" % self.trust_attr_name)
#                 return None
#         else:
#             try:
#                 return owner.__dict__[self.trust_attr_name]
#             except Exception:
#                 print("No %s in the trust class object" % self.trust_attr_name)
#                 return None


# class DescriptorTest(object):
#     add_a = Override("add_a")
#     man_b = Override("add_e")

#     def __init__(self):

#         self.man_b = 30
#         self.add_c = 60

# print("================Create instance")
# add = DescriptorTest()
# print("-")
# print(add.__dict__)
# print("================Read")
# print(add.add_a)
# print("-")
# print(add.man_b)
# print("-")
# print(add.add_c)
# print("================Write")
# add.add_a = 0
# print("-")
# # add.man_b = 1
# print("-")
# add.add_c = 2
# print(add.__dict__)
# print("================Delete")
# del add.add_a
# print("-")
# del add.man_b
# print("-")
# del add.add_c
# print(add.__dict__)




# ###################

# FORMAT = "{0:<60}{1}"

# class Override(object):

#     def __init__(self, trust_attr_name):
#         self.trust_attr_name = trust_attr_name

#     def __set__(self, instance, value):
#         print(FORMAT.format("Descriptor:", "Override-set"))
#         print(FORMAT.format("Trust Class Instance:", instance))
#         print(FORMAT.format("Setted Value:", value))
#         print(FORMAT.format("Name:", self.trust_attr_name))

#         try:
#             value = int(value)
#         except Exception:
#             print("Non-int value")
#             raise
#         else:
#             instance.__dict__[self.trust_attr_name] = value

#     def __delete__(self, instance):
#         print(FORMAT.format("Descriptor:", "Override-delete"))
#         print(FORMAT.format("Trust Class Instance:", instance))

#         del instance.__dict__[self.trust_attr_name]

# class DescriptorTest(object):
#     add_a = Override("add_a")
#     man_b = Override("add_e")

#     def __init__(self):

#         self.man_b = 30
#         self.add_c = 60

# print("================Create instance")
# add = DescriptorTest()
# print("-")
# print(add.__dict__)
# print("================Read")
# print(add.add_a)
# print("-")
# print(add.man_b)
# print("-")
# print(add.add_c)
# print("================Write")
# add.add_a = 0
# print("-")
# add.man_b = 1
# print("-")
# add.add_c = 2
# print(add.__dict__)
# print("================Delete")
# del add.add_a
# print("-")
# del add.man_b
# print("-")
# del add.add_c
# print(add.__dict__)


# ###################

# FORMAT = "{0:<60}{1}"

# class Override(object):

#     def __init__(self, trust_attr_name):
#         self.trust_attr_name = trust_attr_name

#     def __get__(self, instance, owner):
#         print(FORMAT.format("Descriptor:", "Override-get"))
#         print(FORMAT.format("Trust Class Instance:", instance))
#         print(FORMAT.format("Trust Class Object:", owner))

#         if instance != None:
#             try:
#                 return instance.__dict__[self.trust_attr_name]
#             except Exception:
#                 print("No %s in the trust class instance" % self.trust_attr_name)
#                 return None
#         else:
#             try:
#                 return owner.__dict__[self.trust_attr_name]
#             except Exception:
#                 print("No %s in the trust class object" % self.trust_attr_name)
#                 return None

#     def __delete__(self, instance):
#         print(FORMAT.format("Descriptor:", "Override-delete"))
#         print(FORMAT.format("Trust Class Instance:", instance))

#         del instance.__dict__[self.trust_attr_name]

# class DescriptorTest(object):
#     add_a = Override("add_a")
#     man_b = Override("add_e")

#     def __init__(self):

#         self.add_c = 60

# print("================Create instance")
# add = DescriptorTest()
# print("-")
# print(add.__dict__)
# print("================Read")
# print(add.add_a)
# print("-")
# print(add.man_b)
# print("-")
# print(add.add_c)
# print("================Write")
# add.add_a = 0
# print("-")
# add.man_b = 1
# print("-")
# add.add_c = 2
# print(add.__dict__)
# print("================Delete")
# del add.add_a
# print("-")
# del add.man_b
# print("-")
# del add.add_c
# print(add.__dict__)

# #############

FORMAT = "{0:<60}{1}"

class Override(object):

    def __init__(self, trust_attr_name):
        self.trust_attr_name = trust_attr_name

    def __delete__(self, instance):
        print(FORMAT.format("Descriptor:", "Override-delete"))
        print(FORMAT.format("Trust Class Instance:", instance))

        del instance.__dict__[self.trust_attr_name]

class DescriptorTest(object):
    add_a = Override("add_a")
    man_b = Override("add_e")

    def __init__(self):

        self.add_c = 60

print("================Create instance")
add = DescriptorTest()
print("-")
print(add.__dict__)
print("================Read")
print(add.add_a)
print("-")
print(add.man_b)
print("-")
print(add.add_c)
print("================Write")
add.add_a = 0
print("-")
add.man_b = 1
print("-")
add.add_c = 2
print(add.__dict__)
print("================Delete")
del add.add_a
print("-")
del add.man_b
print("-")
del add.add_c
print(add.__dict__)