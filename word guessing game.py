import random
# Libary that we use in order to choose
# on random words from a list of words

name = input(("What is your name?"))

# here the user is asked to enter the first name 

print("Good Luck !", name)

words = ['man', 'can', 'fan',
         'computer', 'math','phy',
         'chem','bio' 'water','player']

# Function will choose one random
# word from this list of words
word = random.choice(words)

print("Guess the characters")

guesses = ''

# any number of turns can be used here 
turns = 12

while turns > 0:
    
    # count the number of items a user fails
    failed = 0

    # all characters from the input
    # words taking one at a time.
    for char in word:

        # comparing that character with 
        # the character in guesses
        if char in guesses:
            print(char, end=" ")


        else:
            print("_")

            # for every failure will be 
            # incremented in faliure
            failed += 1

    if failed == 0:
    # user will win the game if failure is 0
    # and 'you win' will be again as output 
     print("You Win")
    
    # this print the correct word
     print("The word is:", word)
    break

# if the user has input wrong alphabet then
# it will ask to enter the anothe number 
print()
guess = input("guess a character:")

# every input character will be stored in guesses
guesses += guess

# check input with the character in word
if guess not in word:

    turns -= 1

    # if the character doesn't match the word 
    # then "wrong" will be given as output
    print("Wrong!")


    # this will print the number of 
    # turns left for the user
    print("You have", + turns, 'more guesses')

    if turns == 0:
        print("You Loose")
