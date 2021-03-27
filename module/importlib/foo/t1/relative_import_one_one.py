print("This is in foo.t1.relative_import_one_one")
print("__name__: %s" % __name__)

import importlib

test_e = importlib.import_module("..a", "foo.pen")
print("test_e: %s" % test_e)
test_f = importlib.import_module(".b", "foo.t2")
print("test_f: %s" % test_f)