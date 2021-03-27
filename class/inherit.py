# class Base1(object):
#     def __init__(self, base1):
#         self.base1 = base1
#         print("Class: %s" % self.__class__.__name__)
#         print("Base1: %s" % self.base1)

# class Base2(object):
#     def __init__(self, base2):
#         self.base2 = base2
#         print("Class: %s" % self.__class__.__name__)
#         print("Base2: %s" % self.base2)

# class Child(Base1, Base2):
#     pass

# instance_of_child = Child("init Child")

# #########################################

# class Base1(object):
#     def __init__(self, base1):
#         self.base1 = base1
#         print("Class: %s" % self.__class__.__name__)
#         print("Base1: %s" % self.base1)

# class Base2(object):
#     def __init__(self, base2):
#         self.base2 = base2
#         print("Class: %s" % self.__class__.__name__)
#         print("Base2: %s" % self.base2)

# class Child(Base1, Base2):

#     def __init__(self, v1, v2, v3):

#         print("V3: %s" % v3)

# instance_of_child = Child(1, 2, 3)


# #################################

# class Base1(object):
#     def __init__(self, base1):
#         self.base1 = base1
#         print("Class: %s" % self.__class__.__name__)
#         print("Base1: %s" % self.base1)

# class Base2(object):
#     def __init__(self, base2):
#         self.base2 = base2
#         print("Class: %s" % self.__class__.__name__)
#         print("Base2: %s" % self.base2)

# class Child(Base1, Base2):

#     def __init__(self, v1, v2, v3):

#         Base1.__init__(self, v1)
#         Base2.__init__(self, v2)

#         print("V3: %s" % v3)

# instance_of_child = Child(1, 2, 3)

# print(instance_of_child.base1)
# print(instance_of_child.base2)


# ####################################

# import abc

# class MyABCMeta(abc.ABCMeta):

#     def __new__(cls, name, base, attr):
#         print(cls.__name__)

#         return super(MyABCMeta, cls).__new__(cls, name, base, attr)

#     def echo(self):
#         print("test")

# def echo(self):
#     print(self.__class__)

# Test = MyABCMeta("Test", (object,), dict(echo=echo))

# instance_test = Test()
# instance_test.echo()
# print(type(Test))


# ##############

# import abc

# print(type(abc.ABC))
# print(abc.ABC.__mro__)

# ###################################

# import abc

# class A(abc.ABC):

#     def echo(self):
#         print("A: test")

# print(type(A))
# A().echo()

# class B(metaclass=abc.ABCMeta):

#     def echo(self):
#         print("B: test")

# print(type(B))
# B().echo()

# ##############################


# import abc

# class A(abc.ABC):

#     @abc.abstractmethod
#     def echo(self):
#         print("A: test")

# print(type(A))
# A().echo()


# ###########################


# import abc

# class T: pass

# print(set(dir(abc.ABC)) - set(dir(T)))

# print(abc.ABC.__slots__)
# print(abc.ABC.__abstractmethods__)


# ############################

# import abc

# class A(abc.ABC):

#     @abc.abstractmethod
#     def echo(self): pass
#     @abc.abstractmethod
#     def echo2(self): pass

# print(A.__abstractmethods__)

# class B(A):
#     def echo(self):
#         print('B: test')
#     def echo2(self):
#         print('B: test')

# print(B.__abstractmethods__)

# class C(A):
#     def echo(self):
#         print('C: test')

# print(C.__abstractmethods__)

# C()

# ###############################

# import abc

# class A(metaclass=abc.ABCMeta):
#     pass

# class T: pass

# print(set(dir(A)) - set(dir(T)))


# ########################



# def test_abstractmethod(funcobj):
#     funcobj.__isabstractmethod__ = True
#     return funcobj

# class TestABCMeta(type):

#     def __new__(mcls, name, bases, namespace, **kwargs):
#         cls = super().__new__(mcls, name, bases, namespace, **kwargs)
#         # Compute set of abstract method names
#         abstracts = {name
#                      for name, value in namespace.items()
#                      if getattr(value, "__isabstractmethod__", False)}
#         for base in bases:
#             print(base)
#             for name in getattr(base, "__abstractmethods__", set()):
#                 print(name)
#                 value = getattr(cls, name, None)
#                 if getattr(value, "__isabstractmethod__", False):
#                     abstracts.add(name)
#         cls.__abstractmethods__ = frozenset(abstracts)

#         return cls


# class A(metaclass=TestABCMeta):

#     @test_abstractmethod
#     def echo(self): pass
#     @test_abstractmethod
#     def echo2(self): pass

# print(A.__abstractmethods__)

# class B(A):

#     def echo(self):
#         print('B: test')

# print(B.__abstractmethods__)

# B()


# class A:

#     def echo(self):
#         self.__class__.a = 10

# A().echo()

# print(A.a)

# ####################################

# def test_abstractmethod(funcobj):
#     funcobj.__isabstractmethod__ = True
#     return funcobj

# class TestABCMeta(type):

#     def __new__(mcls, name, bases, namespace, **kwargs):
#         cls = super().__new__(mcls, name, bases, namespace, **kwargs)
#         # Compute set of abstract method names
#         abstracts = {name
#                      for name, value in namespace.items()
#                      if getattr(value, "__isabstractmethod__", False)}
#         for base in bases:
#             print(base)
#             for name in getattr(base, "__abstractmethods__", set()):
#                 print(name)
#                 value = getattr(cls, name, None)
#                 if getattr(value, "__isabstractmethod__", False):
#                     abstracts.add(name)
#         cls.__abstractmethods__ = frozenset(abstracts)

#         return cls


# class A(metaclass=TestABCMeta):

#     def __new__(cls, *args, **kwargs):

#         if getattr(cls, "__isabstractmethod__", True):
#             if len(cls.__abstractmethods__) != 0:
#                 print("__abstractmethods__ attribute is not empty")

#                 raise TypeError("Can't instance %s" % cls.__abstractmethods__)
#             else:
#                 print("__abstractmethods__ attribute is empty")
#                 return super().__new__(cls)

#         else:
#             print("Hasn't __abstractmethods__ attribute")
#             return super().__new__(cls)


#     @test_abstractmethod
#     def echo(self): pass
#     @test_abstractmethod
#     def echo2(self): pass

# print(A.__abstractmethods__)

# class B(A):

#     def echo(self):
#         print('B: test')
#     def echo2(self):
#         print('B: test')

# print(B.__abstractmethods__)

# B()

# class C(A): pass

# C()


# ##################################

# class D(object):
#     pass

# class E(object):
#     pass

# class F(object):
#     pass

# class C(D, F):
#     pass

# class B(E, D):
#     pass

# class A(B, C):
#     pass

# print(A.__mro__)

# ############################

# class Base:
#     def __init__(self):
#         print('Base.__init__')

# class A(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print('A.__init__')

# class B(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print('B.__init__')

# class C(A, B):
#     def __init__(self):
#         A.__init__(self)
#         B.__init__(self)
#         print('C.__init__')


# C()

# ###########################


# class Base:
#     def __init__(self):
#         print('Base.__init__')


# class A(Base):
#     def __init__(self):
#         super().__init__()
#         print('A.__init__')


# class B(Base):
#     def __init__(self):
#         super().__init__()
#         print('B.__init__')


# class C(A, B):
#     def __init__(self):
#         super().__init__()
#         print('C.__init__')


# C()

# ###########################


# def mysuper(cls, inst):
#     mro = inst.__class__.mro()
#     return mro[mro.index(cls) + 1]


# class Base:
#     def __init__(self):
#         print('Base.__init__')


# class A(Base):
#     def __init__(self):
#         print(type(mysuper(A, self)))
#         mysuper(A, self).__init__(self)
#         print('A.__init__')


# class B(Base):
#     def __init__(self):
#         mysuper(B, self).__init__(self)
#         print('B.__init__')


# class C(A, B):
#     def __init__(self):
#         mysuper(C, self).__init__(self)
#         print('C.__init__')


# C()