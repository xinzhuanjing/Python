def test_internal_deco(func):
    print('This is test internal deco')
    return func

def rule_of_import(func):

    test_a = 10
    test_b = 11

    print("This is rule of import")

    @test_internal_deco
    def add():

        func()

        test_c = test_a + test_b
        return test_c

    return add


@rule_of_import
def echo():
    print("This is echo")