class TestA:

    def __init__(self):
        self.a = 10

        self._b = 20

        self.__c = 30

        self.__d_ = 40

        self.__e__ = 50

class_instance = TestA()

print(class_instance.__dict__)
