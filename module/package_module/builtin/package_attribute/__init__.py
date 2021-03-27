print("package_attribute: type of __builtins__: %s" % type(__builtins__))
tmp = list(__builtins__.keys())
tmp.sort()
print("package_attribute: keys of __builtins__: %s" % tmp)
print("package_attribute: id of __builtins__:   %s" % id(__builtins__))

