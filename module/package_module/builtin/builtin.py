print("Main: type of __builtins__:       %s" % type(__builtins__))
print("Main: value of __builtins__:      %s" % __builtins__)
print("Main: Instance check:             %s" % isinstance(__builtins__, type(__builtins__)))
print("Main: id of __builtins__:         %s" % id(__builtins__))
print("Main: id of __builtins__.__dict__ %s" % id(__builtins__.__dict__))

import package_attribute
