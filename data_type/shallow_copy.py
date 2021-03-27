# a = [1, 2, 3, [1, 2, 3], (1, 2, 3), {1: 1}]
# b = list(a)

# print("id:                           %s" % id(1))
# print("id of a[0]:                   %s" % id(a[0]))
# print("id of a[3][0]:                %s" % id(a[3][0]))
# print("id of a[4][0]:                %s" % id(a[4][0]))
# print("id of a[5][1]:                %s" % id(a[5][1]))
# print("id of a[5][1] key:            %s" % id(list(a[5].keys())[0]))


# ###################

# a = [1, "abc", {1: 2}, 3.0, bytes(2), bytearray(2), (1, 2, 3)]

# b = list(a)

# print("a[0] id: %s" % id(a[0]))
# print("b[0] id: %s" % id(b[0]))
# print("a[1] id: %s" % id(a[1]))
# print("b[1] id: %s" % id(b[1]))
# print("a[2] id: %s" % id(a[2]))
# print("b[2] id: %s" % id(b[2]))
# print("a[3] id: %s" % id(a[3]))
# print("b[3] id: %s" % id(b[3]))
# print("a[4] id: %s" % id(a[4]))
# print("b[4] id: %s" % id(b[4]))
# print("a[4] id: %s" % id(a[5]))
# print("b[4] id: %s" % id(b[5]))
# print("a[6] id: %s" % id(a[6]))
# print("b[6] id: %s" % id(b[6]))


# #################

# import copy

# a = [1, "abc", {1: 2}, 3.0, bytes(2), bytearray(2), (1, 2, 3)]

# c = copy.copy(a)

# print("a[0] id: %s" % id(a[0]))
# print("c[0] id: %s" % id(c[0]))
# print("a[1] id: %s" % id(a[1]))
# print("c[1] id: %s" % id(c[1]))
# print("a[2] id: %s" % id(a[2]))
# print("c[2] id: %s" % id(c[2]))
# print("a[3] id: %s" % id(a[3]))
# print("c[3] id: %s" % id(c[3]))
# print("a[4] id: %s" % id(a[4]))
# print("c[4] id: %s" % id(c[4]))
# print("a[4] id: %s" % id(a[5]))
# print("c[4] id: %s" % id(c[5]))
# print("a[6] id: %s" % id(a[6]))
# print("c[6] id: %s" % id(c[6]))


# #################

# a = [1, "abc", {1: 2}, 3.0, bytes(2), bytearray(2), (1, 2, 3)]

# d = a[:]

# print("a[0] id: %s" % id(a[0]))
# print("d[0] id: %s" % id(d[0]))
# print("a[1] id: %s" % id(a[1]))
# print("d[1] id: %s" % id(d[1]))
# print("a[2] id: %s" % id(a[2]))
# print("d[2] id: %s" % id(d[2]))
# print("a[3] id: %s" % id(a[3]))
# print("d[3] id: %s" % id(d[3]))
# print("a[4] id: %s" % id(a[4]))
# print("d[4] id: %s" % id(d[4]))
# print("a[4] id: %s" % id(a[5]))
# print("d[4] id: %s" % id(d[5]))
# print("a[6] id: %s" % id(a[6]))
# print("d[6] id: %s" % id(d[6]))

# #######################

# import copy

# a = [1, "abc", 3.0, bytes(2), (1, 2, 3)]

# c = copy.deepcopy(a)

# print("a[0] id: %s" % id(a[0]))
# print("c[0] id: %s" % id(c[0]))
# print("a[1] id: %s" % id(a[1]))
# print("c[1] id: %s" % id(c[1]))
# print("a[2] id: %s" % id(a[2]))
# print("c[2] id: %s" % id(c[2]))
# print("a[3] id: %s" % id(a[3]))
# print("c[3] id: %s" % id(c[3]))
# print("a[4] id: %s" % id(a[4]))
# print("c[4] id: %s" % id(c[4]))


# #############

# import copy

# a = [1, "abc", 3.0, bytes(2), (1, 2, 3), (1, 2, 3, [1, 2, 3])]

# c = copy.deepcopy(a)

# print("a[5] id: %s"    % id(a[5]))
# print("c[5] id: %s"    % id(c[5]))
# print("-")
# print("a[0] id:    %s" % id(a[0]))
# print("a[5][3] id: %s" % id(a[5][0]))
# print("c[5][3] id: %s" % id(c[5][0]))
# print("-")
# print("a[5][3] id: %s" % id(a[5][3]))
# print("c[5][3] id: %s" % id(c[5][3]))

# ###############

import copy

class T:
    def __init__(self):
        print(self.__class__)

def F(m, n):
    print("This is in F")
    return m + n

a = [T, T(), F, F(1, 2)]

b = copy.copy(a)

c = copy.deepcopy(a)

print("a[0] id: %s" % id(a[0]))
print("b[0] id: %s" % id(b[0]))
print("c[0] id: %s" % id(c[0]))
print("a[1] id: %s" % id(a[1]))
print("b[1] id: %s" % id(b[1]))
print("c[1] id: %s" % id(c[1]))
print("a[2] id: %s" % id(a[2]))
print("b[2] id: %s" % id(b[2]))
print("c[2] id: %s" % id(c[2]))
print("a[3] id: %s" % id(a[3]))
print("b[3] id: %s" % id(b[3]))
print("c[3] id: %s" % id(c[3]))
