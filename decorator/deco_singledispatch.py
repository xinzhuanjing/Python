from functools import singledispatch


@singledispatch
def show(obj):
    print("Value:{0:<10}Type:{1:<20}Parameter conditions:{2}".format(str(obj), str(type(obj)), "the other"))

# string parameter
@show.register(str)
def _(text):
    print("Value:{0:<10}Type:{1:<20}Parameter conditions:{2}".format(text, str(type(text)), "str"))

# int parameter
@show.register(int)
def _(n):
    print("Value:{0:<10}Type:{1:<20}Parameter conditions:{2}".format(n, str(type(n)), "int"))


# tuple or dict parameter
@show.register(tuple)
@show.register(dict)
def _(tup_dic):
    print("Value:{0:<10}Type:{1:<20}Parameter conditions:{2}".format(str(tup_dic), str(type(tup_dic)), "tuple or dict"))

# list
show([1])
# str
show("test")
# int
show(666)
# tuple
show((1, 2, 3))
# dict
show({"a": "b"})