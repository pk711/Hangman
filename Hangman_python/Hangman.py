import random, os
from re import A
from art import stages, logo
from wordList import words

print(logo)
def randomWord():
    word = random.choice(words).lower()
    return word

def currWord(word, guesses):
    currWord = ""
    for letter in word:
        if letter in guesses:
            currWord += letter
        else:
            currWord += "_"
    return currWord

def main(word):
    usedLetters = []
    guesses = len(stages)-1
    print ("The word is " + str(len(word)) + " letters long.")

    while True:
        if guesses !=0:
            print("\nYou have " + str(guesses) + " lives left.")
            print("\nCurrent word: " + currWord(word, usedLetters))
            print("\nUsed letters:" + str(usedLetters))
            guess = input("Enter your guess:").lower()[0]
            os.system('cls') # clears the terminal

            if guess not in usedLetters:
                usedLetters.append(guess)

            if currWord(word, usedLetters) == word:
                print("\nCurrent word: " + currWord(word, usedLetters))
                print("\nYou win! The word was: " + word)
                break
            else:
                if guess in word:
                    print("\nCorrect guess!")
                else:
                    print("The letter '" + guess + "' is not in the word.")
                    guesses -= 1
        else:
            print("\nYou run out of lives. The correct word was: " + word)
            break
        print(stages[guesses])

while True:
    word = randomWord()
    main(word)
    if input("\nWould you like to continue? Y/N ").lower().startswith("n"):
        os.system('cls')
        break
    