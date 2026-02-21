import random

print("Welcome to Hangman Game!")
print("-------------------------")

# List of words
word_list = ["python", "computer", "internship", "developer", "programming"]

# Select random word
secret_word = random.choice(word_list)

guessed_letters = []
wrong_attempts = 0
max_attempts = 6

while wrong_attempts < max_attempts:
    
    display_word = ""
    
    # Show guessed letters and underscores
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print("\nWord:", display_word.strip())
    
    # Check if user guessed all letters
    if "_" not in display_word:
        print("Congratulations! You guessed the word correctly:", secret_word)
        break
    
    user_input = input("Enter a letter: ").lower()
    
    if user_input in guessed_letters:
        print("You already guessed that letter.")
    
    elif user_input in secret_word:
        print("Good guess!")
        guessed_letters.append(user_input)
    
    else:
        print("Wrong guess!")
        guessed_letters.append(user_input)
        wrong_attempts += 1
        print("Remaining attempts:", max_attempts - wrong_attempts)

if wrong_attempts == max_attempts:
    print("\nGame Over! The correct word was:", secret_word)