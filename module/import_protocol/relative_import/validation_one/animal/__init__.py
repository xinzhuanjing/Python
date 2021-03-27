print("This is in __init__")
from . import duck

print("This is in __init__: %s" % duck.name)