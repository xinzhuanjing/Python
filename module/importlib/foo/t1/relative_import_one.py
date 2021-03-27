print("This is in foo.t1.relative_import_one")
print("__name__: %s" % __name__)

import importlib

test_c = importlib.import_module(".a", "foo")
print("test_c: %s" % test_c)
test_d = importlib.import_module(".t2.b", "foo")
print("test_d: %s" % test_d)