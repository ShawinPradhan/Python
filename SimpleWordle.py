import random

# List of words to choose from
word_list = ["apple", "about", "baker", "grape", "cross", "drive"]

# Choose a random word
hidden_word = random.choice(word_list)

# Number of attempts
attempts = 6

# Game loop
while attempts > 0:
    guess = input("Enter your guess: ").lower()
    
    if guess == hidden_word:
        print("Congratulations! You guessed the word:", hidden_word)
        break
    else:
        attempts -= 1
        print(f"Wrong guess. {attempts} attempts left.")
else:
    print("Sorry, you're out of attempts. The word was:", hidden_word)

'''
OUTPUT
Enter your guess: drive
Wrong guess. 5 attempts left.
Enter your guess: apple
Wrong guess. 4 attempts left.
Enter your guess: cross
Wrong guess. 3 attempts left.
Enter your guess: about
Wrong guess. 2 attempts left.
Enter your guess: grape
Wrong guess. 1 attempts left.
Enter your guess: baker
Congratulations! You guessed the word: baker
'''
