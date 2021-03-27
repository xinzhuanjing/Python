print("This is in foo.t1.abs_import")
print("__name__: %s" % __name__)

import importlib

test_a = importlib.import_module("foo.a")
print("test_a: %s" % test_a)
test_b = importlib.import_module("foo.t2.b")
print("test_b: %s" % test_b)
