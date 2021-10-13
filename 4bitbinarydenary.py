"""answer = 0
column = 8
while column >= 1:
    print("Enter bit value: ")
    bit = int(input())
    answer += column * bit
    column = column / 2
print("Decimal value is: ")
print(answer)
"""

print("Player One enter your chosen number: ")
NumberToGuess = int(input())
while NumberToGuess < 1 or NumberToGuess > 10:
      print("Not a valid choice, please enter another number: ")
      NumberToGuess = int(input())
Guess = 0
NumberOfGuesses = 0
while Guess != NumberToGuess and NumberOfGuesses < 5:
    print("Player Two have a guess: ")
    Guess = int(input())
    NumberOfGuesses = NumberOfGuesses + 1

if Guess == NumberToGuess:
    print("Player Two wins")
else:
    print("Player One wins")

