
def uncallable():

    test_a = 10
    test_b = 11

    result = 0

    def add():

        test_c = test_a + test_b

        return test_c

    result = add()

    print("{0:<60}{1}".format("add.__code__.co_freevars:", add.__code__.co_freevars))
    print("{0:<60}{1}".format("add.__code__.co_varnames:", add.__code__.co_varnames))
    print("{0:<60}{1}".format("add.__closure__:", add.__closure__))
    print("{0:<60}{1}".format("add.__closure__[0].cell_contents:", add.__closure__[0].cell_contents))
    print("{0:<60}{1}".format("add.__closure__[1].cell_contents:", add.__closure__[1].cell_contents))

    return result


print("Add:%s" % uncallable())


print("{0:<60}{1}".format("uncallable.__code__.co_freevars:", uncallable.__code__.co_freevars))
print("{0:<60}{1}".format("uncallable.__code__.co_varnames:", uncallable.__code__.co_varnames))
print("{0:<60}{1}".format("uncallable.__closure__:", uncallable.__closure__))



# add.__code__.co_freevars:                                   ('test_a', 'test_b')
# add.__code__.co_varnames:                                   ('test_c',)
# add.__closure__:                                            (<cell at 0x00000207E1838FD8: int object at 0x00007FF8A7A9A2B0>, <cell at 0x00000207E1857288: int object at 0x00007FF8A7A9A2D0>)
# add.__closure__[0].cell_contents:                           10
# add.__closure__[1].cell_contents:                           11
# Add:21
# uncallable.__code__.co_freevars:                            ()
# uncallable.__code__.co_varnames:                            ('result', 'add')
# uncallable.__closure__:                                     None