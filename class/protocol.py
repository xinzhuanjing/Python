# class PeopleName:

#     def __init__(self):
#         self._names = ["XiaoWang", "ZhangSan", "LiYuan"]

#     def __len__(self):
#         return len(self._names)

#     def __getitem__(self, position):
#         return self._names[position]


# class DogName:

#     def __init__(self):
#         self._names = ["HaShiQi", "TuGou", "TaiDi"]

#     def __len__(self):
#         return len(self._names)

#     def __getitem__(self, position):
#         return self._names[position]


# FORMAT = "{0:<60}{1}"

# peopleName = PeopleName()
# print(FORMAT.format("Length of People Name:", len(peopleName)))
# for name in peopleName:
#     print(FORMAT.format("People Name:", name))

# dogName = DogName()
# print(FORMAT.format("Length of Dog Name:", len(dogName)))
# for name in dogName:
#     print(FORMAT.format("Dog Name:", name))

# #######################################

# class PeopleName:

#     def __init__(self):
#         self._names = ["XiaoWang", "ZhangSan", "LiYuan"]

#     def __len__(self):
#         return len(self._names)

#     def __getitem__(self, position):
#         return self._names[position]

#     def __call__(self, a):
#         return a

# FORMAT = "{0:<60}{1}"

# peopleName = PeopleName()
# print(FORMAT.format("Length of People Name:", len(peopleName)))
# for name in peopleName:
#     print(FORMAT.format("People Name:", name))

# print(FORMAT.format("Output of the function:", peopleName("This is a test")))

# #################################

# class Example():
#     def func1(self):
#         print('Original One')

# def func2():
#     print('Replace One')

# def func3():
#     print('Replace Two')

# instance = Example()
# instance.func1()

# instance.func1 = func2
# instance.func1()
# instance.func1 = func3
# instance.func1()

# ##################################

# class Example():
#     def func1(self):
#         print('Original One')

# def func2(self):
#     print('Replace One')

# def func3(self):
#     print('Replace Two')

# instance = Example()
# instance.func1()

# Example.func1 = func2
# instance.func1()
# Example.func1 = func3
# instance.func1()


# ########################

# class MySeq:

#     TEST_SEQ = ["A", "B", "C", "D", "E", "F", "G"]

#     def __getitem__(self, index):
#         return MySeq.TEST_SEQ[index]

#     def __len__(self):
#         return len(MySeq.TEST_SEQ)

# my_seq = MySeq()

# print(len(my_seq))
# print(my_seq[0])
# print(my_seq[2:6:3])

# #####################
# class MySeq:

#     TEST_SEQ = ["A", "B", "C", "D", "E", "F", "G"]

#     def __getitem__(self, index):
#         return MySeq.TEST_SEQ[index]

# my_seq = MySeq()

# print(my_seq[0])
# print(my_seq[2:6:3])

# #####################

# class MySeq:

#     TEST_SEQ = ["A", "B", "C", "D", "E", "F", "G"]

#     def __len__(self):
#         return len(MySeq.TEST_SEQ)

# my_seq = MySeq()

# print(len(my_seq))

# ######################

# class MySeq:
#     def __getitem__(self, index):
#         return index

# my_seq = MySeq()

# FORMAT = "{0:<10}{1:<60}{2:<10}{3}"
# print(FORMAT.format("Index:", str(my_seq[0]), "Type:", type(my_seq[0])))

# ############################

# class MySeq:
#     def __getitem__(self, index):
#         return index

# my_seq = MySeq()

# FORMAT = "{0:<10}{1:<60}{2:<10}{3}"
# print(FORMAT.format("Index:", str(my_seq[0: 10]), "Type:", type(my_seq[0: 10])))
# print(FORMAT.format("Index:", str(my_seq[1:4:2]), "Type:", type(my_seq[1:4:2])))
# print(FORMAT.format("Index:", str(my_seq[1:4:2, 9]), "Type:", type(my_seq[1:4:2, 9])))
# print(FORMAT.format("Index:", str(my_seq[1:4:2, 7:9]), "Type:", type(my_seq[1:4:2, 7:9])))


# ##################


# class MySeq:

#     TEST_SEQ = ["A", "B", "C"]

#     def __getitem__(self, index):
#         print("Index: %s" % index)
#         return MySeq.TEST_SEQ[index]

# for i in MySeq():
#     print("Data:  %s" % i)


# ##################

# class Foo:

#     def __enter__(self):
#         return 1

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         return True

# with Foo() as handler:
#     print("Returned value Of __enter__: %s" % handler)

# ########################

# class Foo:
#     def __init__(self, name):
#         self.name = name

#     def __enter__(self):
#         print('This is in __enter__')
#         return self

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Exception Type:  %s" % exc_type)
#         print("Exception Value: %s" % exc_val)
#         print("Traceback:       %s" % exc_tb)
#         return True

# with Foo('test') as handler:
#     print("Name:            %s" % handler.name)

# print("Done")


# ########################

# class Foo:
#     def __init__(self, name):
#         self.name = name

#     def __enter__(self):
#         print('This is in __enter__')
#         return self

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Exception Type:  %s" % exc_type)
#         print("Exception Value: %s" % exc_val)
#         print("Traceback:       %s" % exc_tb)
#         return False

# with Foo('test') as handler:
#     print("Name:            %s" % handler.name)
#     1 / 0

# print("Done")

# #######################

# class Foo:
#     def __init__(self, name):
#         self.name = name

#     def __enter__(self):
#         print('This is in __enter__')
#         return self

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Exception Type:  %s" % exc_type)
#         print("Exception Value: %s" % exc_val)
#         print("Traceback:       %s" % exc_tb)
#         return True

# with Foo('test') as handler:
#     print("Name:            %s" % handler.name)
#     1 / 0

# print("Done")

# #################


# import contextlib

# @contextlib.contextmanager
# def test(a, b):

#     print('This is in __enter__')

#     c = a + b

#     yield c

#     print('This is in __exit__')

# with test(1, 2) as handler:
#     print(handler)


# print("Done")

# ################

# import contextlib

# @contextlib.contextmanager
# def test(a, b):

#     print('This is in __enter__')

#     c = a + b

#     yield c

#     print('This is in __exit__')

# with test(1, 2) as handler:
#     print(handler)

#     1 / 0


# print("Done")

# ####################

# class Test:

#     def __call__(self, a, b):
#         return a + b

# test = Test()
# print(test.__call__(1, 2))


# #########

class Test:

    def __call__(self, a, b):
        return a + b

test = Test()
print(test(1, 2))