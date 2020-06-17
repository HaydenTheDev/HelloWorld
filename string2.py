#
#         01234567890123
parrot = "Norwegian Blue"

#  basically its 6 / 2 or 6 / 3
print(parrot[0:6:2])  #  Nre 0 2 4
print(parrot[0:6:3])  #  Nw 0 3

number = "9,223;372:036 854,775;807"
seperator = number[1::4]
print(seperator)

values = "".join(char if char not in seperator else " " for char in number).split()
print([int(val) for val in values])