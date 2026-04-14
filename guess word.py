import random

words = ["apple", "car", "computer", "program", "school", "python", "keyboard"]

secret_word = random.choice(words)
guessed_letters = []
attempts = 8

print("🎮 Welcome to 'Guess the Word'!")

while attempts > 0:
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print("\nWord:", display)

    if "_" not in display:
        print("🎉 You guessed the word:", secret_word)
        break

    guess = input("Enter a letter OR whole word: ").lower()

    if guess == secret_word:
        print("🎉 You guessed the word:", secret_word)
        break

    if len(guess) > 1:
        attempts -= 1
        print("❌ Wrong word! Attempts left:", attempts)
        continue


    if guess in guessed_letters:
        print("⚠️ You already used this letter")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Correct!")
    else:
        attempts -= 1
        print("❌ Wrong! Attempts left:", attempts)

if attempts == 0:
    print("💀 You lost! The word was:", secret_word)
