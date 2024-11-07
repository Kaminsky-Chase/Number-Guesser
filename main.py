import random

print("""
Welcome to Number Guessser!
This is were you make a number range from least 
to greatest and try to guess the correct number.
""")

while True:
    try:
        firstNumber = int(input("Enter your Least number: "))
        secondNumber = int(input("Enter your Greater number: "))

        if firstNumber < secondNumber:
            print("Thank you for inputing your range!")
            break
        else:
            print("Invalid: Enter a number or a greator value")

    except ValueError:
        print("Invalid: Enter a number or a greator value")

print(f"\nYou picked {firstNumber} to {secondNumber}.")

randomNumber = random.randint(firstNumber, secondNumber)
guessCount = 0

print("\nGuess a number")

while True:
    try:
        Guess = int(input("Enter your Guess: "))
        guessCount += 1

        if Guess == randomNumber:
            print("\nYou guessed correct!")
            print(f"It took you {guessCount} guesses.")
            break
        elif Guess > secondNumber or Guess < firstNumber:
            print("invalid, number is bigger or smaller then range")
        elif Guess != randomNumber:
            if Guess > randomNumber:
                print("Try Again! You guessed too high")
            elif Guess < randomNumber:
                print("Try Again! You guessed too small")
        else:
            print("Invalid: Enter a number or a greator value")

    except ValueError:
        print("Invalid")