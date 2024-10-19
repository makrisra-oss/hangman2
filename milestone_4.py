"""Milestone 4"""
import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        
        self.word = random.choice(word_list)
        print(self.word)

        self.word_guessed = ['_' for char in self.word]

        self.num_letters = len(set(self.word))
        print(self.num_letters)

        self.num_lives = num_lives
        print(f"Num lives:", self.num_lives)

        self.word_list = word_list
        print(self.word_list)

        self.list_of_guesses = []
        print(self.list_of_guesses)



    # def make_guess(self, letter):
    #     for i, char in enumerate(self.word):
    #         if char == letter:
    #             self.word_guessed[i] = letter
    #     return self.word_guessed

    def check_guess(self, guess):
        if guess in self.word:
            print("Good guess! {guess} is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            num_lives -= 1
            print("Sorry, {letter} is not in the word.")
            print("You have {num_lives} lives left.")



    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ").lower()
            if guess != len(guess) == 1 and guess.isdigit():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                print(self.list_of_guesses)
        
    # def play(self):
    #     index = 0
    #     self.list_of_guesses = []

    #     while '_' in self.word_guessed:
    #         print(' '.join(self.word_guessed))
    #         guess = input("Guess a letter: ").lower()
    #         if len(guess) == 1 and guess.isalpha():
    #             self.make_guess(guess)
            
    #         else:
    #             print("Please enter a single letter.")

    #     print("Congratulations! You've guessed the word:", self.word)

    #     print(self.word_guessed)

        

word_list = ['apple', 'banana', 'cherry']
game = Hangman(word_list)
#game.check_guess(guess)
game.ask_for_input()
print(game.num_letters)

#make_guess > check_guess. Have an if statement making sure the guess is in the word
