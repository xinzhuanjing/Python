# def func_test():
#     print("This is demo")

# new_reference = func_test
# new_reference()

# ##############################
def foo():
    print('This is foo')

def bar(func):
    print("This is bar")
    func()

bar(foo)

# #############################
# def foo():
#     print('This is foo')

# def bar(func):
#     print("This is bar")
#     return func

# f = bar(foo)
# f()

# ############################
# def foo():
#     print('This is foo')

# dic={'func':foo}

# dic['func']()

# #########################

# def f1():

#     print("This is f1")
#     def f2():
#         print("This is f2")

#         def f3():
#             print("This is f3")

#         f3()

#     f2()


# f1()
