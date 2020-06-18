answer = 5
print("Please guess the number between 1 and 10: ")
guess = int(input())

if guess < answer:
    print("Sorry you guessed too low")
elif guess > answer:
    print("Sorry you guessed too high")
else:
    print("good job!")