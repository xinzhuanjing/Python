class T:

    def __init__(self, data):
        self.data = data

    def __eq__(self, a):
        print("This is in __eq__")

        if self.data == a.data:
            return True;
        else:
            return False

if __name__ == "__main__":

    a = T(1)
    b = T(1)

    print(a == b)
