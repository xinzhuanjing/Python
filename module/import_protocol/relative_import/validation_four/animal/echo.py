import sys
import os

print(sys.path[0])
sys.path.insert(1, sys.path[0].strip("animal"))

import animal.duck as duck
print(duck.name)