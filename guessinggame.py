answer = 5
print("Please guess the number between 1 and 10: ")
guess = int(input())

if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Pleas guess lower")
    guess = int(input())
    if guess == answer:
        print("well done you got it")
    else:
        print("sorry, you have not guesses right")
else:
    print("you got it first try")

# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it right")
#     else:
#         print("sorry, you have not guessed correctly")
# else:
#     print("You got it first try!")

# if guess < answer:
#     print("Sorry you guessed too low")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it.")
#     else:
#         print("sorry you didn't guess right")
# elif guess > answer:
#     print("Sorry you guessed too high")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it.")
#     else:
#         print("sorry you didn't guess right")
# else:
#     print("good job!")
