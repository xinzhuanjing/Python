# import sys

# try:
#     sys.exit(0)
# except SystemExit:
#     print("sys exit exception")
# finally:
#     print("finally")

# ########################


# try:
#     while True: pass
# except KeyboardInterrupt:
#     print("Key board exception")
# finally:
#     print("finally")


# #########################

# def myGenerator():
#     try:
#         yield 1
#         yield 2
#     except GeneratorExit:
#         print ("Generator is deleted")

# gen = myGenerator()
# print (next(gen))
# del gen


# #########################

# try:
#     1 / 0
# except Exception:
#     print("Exception")
# finally:
#     print("finally")


# ########################

# class TestException(Exception):
#     pass

# raise TestException("Test")

# ########################


# class TestException(Exception):

#     def __init__(self, error_value):
#         Exception.__init__(self, error_value, "This is a test")

#         self.error_value = error_value

#     def check(self, a, b):

#         if a + b == self.error_value:
#             print("Wrong a , b group")

# try:
#     raise TestException(10)
# except TestException as e:
#     e.check(1, 9)
# finally:
#     print("finally")


# #########################

# raise Exception("test")


# ############################

# class TestException(Exception):
#     pass

# t = None

# try:
#     t = TestException("test")
#     raise t
# except TestException as e:
#     print("e is the Class Instance of TestException:  %s" % isinstance(e, TestException))
#     print("t and e is the actual same class instance: %s" % (t is e))
#     print("the id of t is:                            %s" % id(t))
#     print("the id of e is:                            %s" % id(e))


# ##############################

# class TestException(Exception):
#     pass

# try:
#     raise TestException("test")
# except Exception:
#     print("father exception class")
# except TestException:
#     print("child exception class")


# #############################


# class TestException(Exception):
#     pass

# try:
#     raise TestException("test")
# except TestException:
#     print("child exception class")
# except Exception:
#     print("father exception class")

# #############################


# class TestException(Exception):
#     def __init__(self, input, flag):
#         Exception.__init__(self, input)
#         self.flag = flag

#     def echo(self):
#         if self.flag:
#             print("echo")

# try:
#     raise TestException("test", True)
# except TestException as e:
#     e.echo()


# ######################

# try:
#     print("try")
# except Exception:
#     print("except")
# else:
#     print("else")


# #####################

# try:
#     print("try")
# except Exception:
#     print("except")
# else:
#     print("else")


# ####################


# try:
#     1 / 0
# finally:
#     print("finally")


# ###################

# try:
#     1 / 0
# except Exception:
#     print("except")
# finally:
#     print("finally")

# #################

# try:
#     1 / 0
# except Exception:
#     print("except")
#     raise Exception("test")
# finally:
#     print("finally")

# ##################

# def test():
#     try:
#         1 / 0
#     except Exception:
#         print("except with return")
#         return
#     finally:
#         print("finally")

# test()


# ##################

# assert 'a' == 'A'

# #################

# assert 'a' == 'A', "This is a tets"

# #################

# try:

#     print("try")

#     try:
#         print("internal try")
#         1 / 0
#     finally:
#         print("internal finally")

# except Exception:
#     print("except")
# else:
#     print("else")
# finally:
#     print("finally")


# ####################

# try:
#     print("try")
#     1 / 0
# except Exception:
#     print("except")
#     try:
#         print("internal try")
#         raise Exception("test")
#     finally:
#         print("internal finally")
# else:
#     print("else")
# finally:
#     print("finally")

# #####################

# try:
#     print("try")
# except Exception:
#     print("except")
# else:
#     print("else")
#     try:
#         print("internal try")
#         1 / 0
#     finally:
#         print("internal finally")
# finally:
#     print("finally")


# ####################

# try:
#     print("try")
# except Exception:
#     print("except")
# else:
#     print("else")
# finally:
#     print("finally")
#     try:
#         print("internal try")
#         1 / 0
#     finally:
#         print("internal finally")

# ####################

# import traceback

# try:
#     print("try")
#     1 / 0
# except Exception:
#     print("except")
#     print(traceback.format_exc())
# else:
#     print("else")
# finally:
#     print("finally")