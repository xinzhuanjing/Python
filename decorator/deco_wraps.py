# def wraps_test(func):

#     def func_test():
#         '''This is __doc__ in func test'''
#         print("This is in funct test")

#     return func_test

# @wraps_test
# def echo_test():
#     '''This is __doc__ in echo tes'''
#     print("This is in echo test")

# print("The finally callable object name: %s" % echo_test.__name__)
# print("The finally callable doc: %s" % echo_test.__doc__)

# #####################################
from functools import wraps


def wraps_test(func):

    @wraps(func)
    def func_test():
        '''This is __doc__ in func test'''
        print("This is in funct test")

    return func_test

@wraps_test
def echo_test():
    '''This is __doc__ in echo test'''
    print("This is in echo test")


print("The finally callable object name: %s" % echo_test.__name__)
print("The finally callable doc: %s" % echo_test.__doc__)