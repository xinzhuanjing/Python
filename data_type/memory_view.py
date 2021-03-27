@profile
def test():
    a = bytearray(1024 * 1024 * 10)

    b = a[1024 * 1024: ]



if __name__ == "__main__":
    test()
