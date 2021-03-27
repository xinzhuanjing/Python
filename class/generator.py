# def gen_test(a, b):

#     yield a + b

# gen = gen_test(1, 2)
# print("Class Instance Type:        %s" % type(gen))
# print("Class Object Type:          %s" % type(gen.__class__))
# print("Class Object __mro__:       %s" % str(gen.__class__.__mro__))
# print("Attributes Of Class Object: %s" % dir(gen.__class__))

# ##############

# def gen_test(a, b):

#     print("Debug point 1")
#     yield a + b
#     print("Debug point 2")

# import inspect
# import traceback

# gen = gen_test(1, 2)

# print("Stat:            %s" % inspect.getgeneratorstate(gen))
# print("Output:          %s" % next(gen))
# print("Stat:            %s" % inspect.getgeneratorstate(gen))
# try:
#     print("Output:          %s" % next(gen))
# except:
#     print(traceback.format_exc())

# print("Stat:            %s" % inspect.getgeneratorstate(gen))

# #############

# def gen_test(a, b):

#     print("Debug point 1")
#     yield a + b
#     print("Debug point 2")
#     c = yield
#     print("Debug point 3")
#     yield a + b + c
#     print("Done")

# import inspect
# import traceback

# gen = gen_test(1, 2)

# print("Stat:            %s" % inspect.getgeneratorstate(gen))
# print("---")
# print("Next:            %s" % next(gen))
# print("Stat:            %s" % inspect.getgeneratorstate(gen))
# print("---")
# print("Next:            %s" % next(gen))
# print("Stat:            %s" % inspect.getgeneratorstate(gen))
# print("---")
# print("Send:            %s" % gen.send(3))
# print("---")

# try:
#     print("Output:          %s" % next(gen))
# except:
#     print(traceback.format_exc())

# print("Stat:            %s" % inspect.getgeneratorstate(gen))

# #############

# def gen_test(a, b):

#     print("Debug point 1")

#     yield "a + 1 = %s" % (a + 1)

#     print("Debug point 2")

#     yield "b + 1 = %s" % (b + 1)

#     print("Debug point 3")

#     yield "a + b = %s" % (a + b)

#     print("Debug point 4")
#     print("Done")


# import inspect
# import traceback

# gen = gen_test(1, 2)

# print("Start:          %s" % inspect.getgeneratorstate(gen))
# print("---")
# print("Next:           %s" % next(gen))
# print("Stat:           %s" % inspect.getgeneratorstate(gen))
# print("---")
# print("Next:           %s" % next(gen))
# print("Stat:           %s" % inspect.getgeneratorstate(gen))
# print("---")
# print("Next:           %s" % next(gen))
# print("Stat:           %s" % inspect.getgeneratorstate(gen))
# print("---")

# try:
#     print("Next:           %s" % gen.send(4))
# except:
#     print(traceback.format_exc())

# print("Stat:           %s" % inspect.getgeneratorstate(gen))

# #############

# def gen_test(a, b):

#     print("Debug point 1")
#     c = yield
#     print("c: %s" % c)

#     print("Debug point 2")
#     d = yield
#     print("d: %s" % d)

#     print("Debug point 3")
#     e = yield
#     print("e: %s" % e)

#     print("Debug point 4")
#     f = yield
#     print("e: %s" % e)

#     print("Debug point 5")
#     print("Done")


# import inspect
# import traceback

# gen = gen_test(1, 2)

# print("Start:          %s" % inspect.getgeneratorstate(gen))
# print("---")
# print("Next:           %s" % next(gen))
# print("Stat:           %s" % inspect.getgeneratorstate(gen))
# print("---")
# print("Send:           %s" % gen.send(1))
# print("Stat:           %s" % inspect.getgeneratorstate(gen))
# print("---")
# print("Send:           %s" % gen.send(2))
# print("Stat:           %s" % inspect.getgeneratorstate(gen))
# print("---")
# print("Send:           %s" % gen.send(3))
# print("Stat:           %s" % inspect.getgeneratorstate(gen))
# print("---")

# try:
#     print("Send:           %s" % gen.send(4))
# except:
#     print(traceback.format_exc())

# print("Stat:           %s" % inspect.getgeneratorstate(gen))


# #########


# def gen_test(a, b):

#     print("Debug point 1")
#     c = yield "a + b = %s" % (a + b)
#     print("c: %s" % c)

#     print("Debug point 2")
#     d = yield "a + b + c = %s" % (a + b + c)
#     print("d: %s" % d)

#     print("Debug point 3")
#     e = yield "a + b + d = %s" % (a + b + d)
#     print("e: %s" % e)

#     print("Debug point 4")
#     f = yield "a + b + e = %s" % (a + b + e)
#     print("f: %s" % f)

#     print("Debug point 5")
#     print("Done")


# import inspect
# import traceback

# gen = gen_test(1, 2)

# print("Start:          %s" % inspect.getgeneratorstate(gen))
# print("---")
# print("Next:           %s" % next(gen))
# print("Stat:           %s" % inspect.getgeneratorstate(gen))
# print("---")
# print("Send:           %s" % gen.send(1))
# print("Stat:           %s" % inspect.getgeneratorstate(gen))
# print("---")
# print("Send:           %s" % gen.send(2))
# print("Stat:           %s" % inspect.getgeneratorstate(gen))
# print("---")
# print("Send:           %s" % gen.send(3))
# print("Stat:           %s" % inspect.getgeneratorstate(gen))
# print("---")

# try:
#     print("Send:           %s" % gen.send(4))
# except:
#     print(traceback.format_exc())

# print("Stat:           %s" % inspect.getgeneratorstate(gen))