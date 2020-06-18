
#  if Statements
name = input("Please enter your name: ")
age = int(input("How old are you, {0}?".format(name)))
if age >= 18:
    print("{0} old is enough to vote!".format(name))
else:
    print("Sorry! {0}you are not of age to vote.".format(name))
if age < 18:
    print("Please come back in {0} years.".format(18 - age))
elif age == 900:
    print("Sorry, Yoda, you die in return of the jedi.")
else:
    print("you are old enough to vote")
    print("please out an X in the box")