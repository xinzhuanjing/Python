# class MetaClassA(type):pass
# class MetaClassB(MetaClassA):pass

# class NewObject(metaclass=MetaClassB):pass

# FORMT_STR = "{0:<30} __class__: {1:<30} __mro__: {2}"

# print(FORMT_STR.format("MetaClassA",str(MetaClassA.__class__), str(MetaClassA.__mro__)))
# print(FORMT_STR.format("MetaClassB",str(MetaClassB.__class__), str(MetaClassB.__mro__)))
# print(FORMT_STR.format("NewObject",str(NewObject.__class__), str(NewObject.__mro__)))

# ######################################################################################


# class Mymeta(type):
#     def __new__(cls, class_name, class_bases, class_dic):
#         print("This is in __new__")
#         return super(Mymeta, cls).__new__(cls, class_name, class_bases, class_dic)

#     def __init__(self, class_name, class_bases, class_dic):
#         print("This is in __init__ in Mymeta")
#         print(self)
#         print("Name: %s" % class_name)
#         print("Bases: %s" % class_bases)
#         print("Attrs: %s" % class_dic)
#         super(Mymeta, self).__init__(class_name, class_bases, class_dic)

#     def echo(self):
#         print("This is echo in Mymeta")

# def __init__(self):
#     self.i_a = 0
#     self.i_b = 0

# def add(self, a, b):
#     return a + b

# Test = Mymeta("Test", (object, ), dict(data_a=10, data_b=10, __init__=__init__, add=add))
# print("Type: %s" % type(Test))


# ######################################################################################


# class Mymeta(type):
#     def __new__(cls, class_name, class_bases, class_dic):
#         print("This is in __new__")
#         return super(Mymeta, cls).__new__(cls, class_name, class_bases, class_dic)

#     def __init__(self, class_name, class_bases, class_dic):
#         print("This is in __init__ in Mymeta")
#         print(self)
#         print("Name: %s" % class_name)
#         print("Bases: %s" % class_bases)
#         print("Attrs: %s" % class_dic)
#         super(Mymeta, self).__init__(class_name, class_bases, class_dic)

#     def echo(self):
#         print("This is echo in Mymeta")

# class Test(object, metaclass=Mymeta):

#     data_a=10
#     data_b=10

#     def __init__(self):
#         self.i_a = 0
#         self.i_b = 0

#     def add(self, a, b):
#         return a + b

# print("Type: %s" % type(Test))

# ######################################################################################

# class Mymeta(type):
#     def __new__(cls, class_name, class_bases, class_dic):
#         print("This is in __new__")
#         return super(Mymeta, cls).__new__(cls, class_name, class_bases, class_dic)

#     def __init__(self, class_name, class_bases, class_dic):
#         print("This is in __init__ in Mymeta")
#         super(Mymeta, self).__init__(class_name, class_bases, class_dic)

#     def echo(self):
#         print("This is echo in Mymeta")

# class Test(object, metaclass=Mymeta):

#     data_a=10
#     data_b=10

#     def __init__(self):
#         self.i_a = 0
#         self.i_b = 0

#     def add(self, a, b):
#         return a + b

# test_a = Test()
# print("{0:<60}{1}".format("Attrs of Mymeta:", dir(Mymeta)))
# print("{0:<60}{1}".format("Attrs of instance of Mymeta:", dir(Test)))
# print("{0:<60}{1}".format("Attrs of instance of Test:", dir(test_a)))


# ######################################################################################
# def record_factory(cls_name, field_names):
#     try:
#         field_names = field_names.replace(',', ' ').split()
#     except AttributeError:
#         pass
#     field_names = tuple(field_names)

#     def __init__(self, *args, **kwargs):
#         attrs = dict(zip(self.__slots__, args))
#         attrs.update(kwargs)
#         for name, value in attrs.items():
#             setattr(self, name, value)

#     def __iter__(self):
#         for name in self.__slots__:
#             yield getattr(self, name)

#     def __repr__(self):
#         values = ', '.join('{}={!r}'.format(*i) for i
#                            in zip(self.__slots__, self))
#         return '{}({})'.format(self.__class__.__name__, values)

#     cls_attrs = dict(__slots__ = field_names,
#                      __init__  = __init__,
#                      __iter__  = __iter__,
#                      __repr__  = __repr__)

#     return type(cls_name, (object,), cls_attrs)

# Dog = record_factory('Dog', 'name weight owner')
# rex = Dog('Rex', 30, 'Bob')
# print(rex)

# rex.weight = 20
# print(rex)


# ######################################################################################

def add_minus(op):

    if op == "+":
        class Add:
            def __call__(self, a, b):
                return a + b

        return Add

    if op == "-":
        class Minus:
            def __call__(self, a, b):
                return a - b

        return Minus

add = add_minus("+")
minus = add_minus("-")

print("A + B: %s" % add()(1,2))
print("A - B: %s" % minus()(1,2))
