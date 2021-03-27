# class TestA:

#     def echo(self):
#         print("The input class name of the instance: %s" % self.__class__.__name__)

# class TestB:

#     def add(t, a, b):
#         t.total = a + b


# test_a = TestA()
# test_b = TestB()

# test_a.echo()
# test_b.add(1, 2)
# print("Sum: %d" % test_b.total)



# class TestA:

#     def echo(self):
#         print("The input class name of the instance: %s" % self.__class__.__name__)

# class TestB:

#     def add(t, a, b):
#         t.total = a + b


# test_a = TestA()
# test_b = TestB()

# test_a.echo()
# TestA.echo(test_a)
# TestA.echo(test_b)

# TestB.add(test_b, 1, 2)
# print("test_b instance, Sum: %d" % test_b.total)

# TestB.add(test_a, 1, 2)
# print("test_a instance, Sum: %d" % test_a.total)



# class TestA:

#     data_a = 10

#     @classmethod
#     def echo(cls):
#         print("The input class name: %s, type: %s" % (cls.__name__, cls.__class__))
#         cls.data_a = 0

# test_a = TestA()
# print("data_a: %d" % test_a.data_a)
# test_a.echo()
# print("data_a: %d" % test_a.data_a)
# print("data_a: %d" % TestA.data_a)


# class TestA:

#     data_a = 10

#     @classmethod
#     def echo(cls):
#         print("The input class name: %s, type: %s" % (cls.__name__, cls.__class__))
#         cls.data_a = 0

# test_a = TestA()
# print("data_a: %d" % test_a.data_a)
# TestA.echo()
# print("data_a: %d" % test_a.data_a)


# class TestA: pass
# class TestB: pass

# def echo(self):
#     print("The input class name of the instance: %s" % self.__class__.__name__)

# TestA.echo = echo

# test_a = TestA()
# test_a.echo()
# TestA.echo(TestB())



# class TestA: pass

# @classmethod
# def echo(cls):
#     print("The input class name: %s, type: %s" % (cls.__name__, cls.__class__))

# TestA.echo = echo

# test_a = TestA()
# test_a.echo()
# TestA.echo()


# class TestA: pass

# @staticmethod
# def echo():
#     print("Test")

# TestA.echo = echo

# test_a = TestA()
# test_a.echo()
# TestA.echo()


# class TestA: pass

# def echo():
#     print("No self")

# def echo1(self):
#     print("The input class name of the instance: %s" % self.__class__.__name__)

# test_a = TestA()
# test_a.echo = echo
# test_a.echo1 = echo1
# print("Attribute of TestA: %s" % dir(TestA))
# test_a.echo()
# test_a.echo1(test_a)


class TestA: pass


@staticmethod
def echo():
    print("Test")

test_a = TestA()
test_a.echo = echo
test_a.echo()
