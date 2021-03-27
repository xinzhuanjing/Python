__builtins__.__dict__["entry_attr_a"] = 1

import package_attribute

print("__builtins__.__dict__['package_add_attr_b'] = %s" % __builtins__.__dict__["entry_attr_a"])
