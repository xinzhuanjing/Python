def rule_of_import(func):

    test_a = 10
    test_b = 11

    result = 0

    def add():

        func()

        test_c = test_a + test_b

        return test_c

    print("{0:<60}{1}".format("add.__code__.co_freevars:", add.__code__.co_freevars))
    print("{0:<60}{1}".format("add.__code__.co_varnames:", add.__code__.co_varnames))
    print("{0:<60}{1}".format("add.__closure__:", add.__closure__))
    print("{0:<60}{1}".format("add.__closure__[0].cell_contents:", add.__closure__[0].cell_contents))
    print("{0:<60}{1}".format("add.__closure__[1].cell_contents:", add.__closure__[1].cell_contents))
    print("{0:<60}{1}".format("add.__closure__[2].cell_contents:", add.__closure__[1].cell_contents))

    return add


@rule_of_import
def echo():

    print("{0:<60}{1}".format("rule_of_import.__code__.co_freevars:", rule_of_import.__code__.co_freevars))
    print("{0:<60}{1}".format("rule_of_import.__code__.co_varnames:", rule_of_import.__code__.co_varnames))
    print("{0:<60}{1}".format("rule_of_import.__closure__:", rule_of_import.__closure__))


# echo = rule_of_import(echo)