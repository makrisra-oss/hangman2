
import random

word_list = ["banana", "apple", "pear", "orange", "grapes"]

print(word_list)

word = random.choice(word_list)
print(word)

# while True:
#     print("Guess a letter ")
#     guess = input()
#     if len(guess) == 1 and guess.isalpha():
#         print("successful")
#         if guess in word:
#             print(f"Good guess! {guess} is in the word.")
#         else:
#             print(f"Sorry, {guess} is not in the word. Try again.")
#         break
#     else:
#         print("Invalid letter. Please, enter a single alphabetical character.")


# def check_guess(guess):
#     if guess.lower() in word:
#         print(f"Good guess! {guess.lower()} is in the word.")
#     else:
#         print(f"Sorry, {guess.lower()} is not in the word. Try again.")

# check_guess(guess)

def ask_for_input():
    #Iteratively check
    print('Enter a single letter ')
    guess = input()

    if len(guess) == 1 and guess.isalpha():
        print("Good guess")
    else:
        print("Oops! That is not a valid input.")

    print(guess)

    #Check guess
    def check_guess(guess):
        if guess.lower() in word:
            print(f"Good guess! {guess.lower()} is in the word.")
        else:
            print(f"Sorry, {guess.lower()} is not in the word. Try again.")

    check_guess(guess)

ask_for_input()

x = ('apple', 'banana', 'cherry')
y = enumerate(x)
print(y)