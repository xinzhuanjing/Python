def factory_deco(flag):

    if flag:

        def flag_true(func):
            def true_test():
                print("Flag is true")

            return true_test
        return flag_true

    else:

        def flag_false(func):
            def false_test():
                print("Flag is false")

            return false_test
        return flag_false

@factory_deco(True)
def echo_flag():
    pass

