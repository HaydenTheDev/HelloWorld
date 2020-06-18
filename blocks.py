
#  if Statements
name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
if age >= 18:
    print("{0} old is enough to vote!".format(name))