answer = 5
print("Please guess the number between 1 and 10: ")
guess = int(input())

if guess < answer:
    print("Sorry you guessed too low")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it.")
    else:
        print("sorry you didn't guess right")
elif guess > answer:
    print("Sorry you guessed too high")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it.")
    else:
        print("sorry you didn't guess right")
else:
    print("good job!")
