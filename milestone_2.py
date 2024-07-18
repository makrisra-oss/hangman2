import random

word_list = ["banana", "apple", "pear", "orange", "grapes"]

print(word_list)

word = random.choice(word_list)
print(word)

print('Enter a single letter ')
guess = input()

if len(guess) == 1 and guess.isalpha():
    print("Good guess")
else:
    print("Oops! That is not a valid input.")

print(guess)
