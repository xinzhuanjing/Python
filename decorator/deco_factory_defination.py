def deco_factory_test(p1, p2):

    if p1 and p2:
        def funct_test1(func):

            print("This is in func_test1")

            def f1():
                print("This is in f1")

                func()

            return f1
        return funct_test1

    elif not p1 and p2:
        def funct_test2(func):

            print("This is in func_test2")

            def f2():
                print("This is in f2")

                func()

            return f2
        return funct_test2

    elif not p1 and not p2:
        def funct_test3(func):

            print("This is in func_test3")

            def f3():
                print("This is in f3")

                func()

            return f3
        return funct_test3

    else:
        def funct_test4(func):

            print("This is in func_test4")

            def f4():
                print("This is in f4")

                func()

            return f4
        return funct_test4


@deco_factory_test(True, True)
def echo1():
    print("This is in echo 1")

@deco_factory_test(False, True)
def echo2():
    print("This is in echo 2")


@deco_factory_test(False, False)
def echo3():
    print("This is in echo 3")


@deco_factory_test(False, True)
def echo4():
    print("This is in echo 4")


echo1()
echo2()
echo3()
echo4()