import sys
import os

sys.path.insert(1, os.path.dirname(__file__))

print("This is in __init__")
import duck
print("This is in __init__: %s" % duck.name)