import random
import math

#Taking inputs
lower = int(input("Enter Lower bound:"))

#Taking inputs
upper = int(input("Enter Upper Bound:"))

#generating random number between the lower and upper
x = random.randint(lower, upper)
print("\n\tYou've only ", 
	round(math.log(upper - lower + 1, 2)),
	" chances to guess the integer!\n")

#Initializing the number of guesses.
count = 0

# for calculation of minimum number
# guess depends upon range 
while count < math.log(upper - lower + 1,2):
    count += 1

    # taking gussing number as a print
    guess = int(input("Guess a number:"))

    # condition testing 
    if x == guess:
        print("conguratulation you did it in",
              count, "try")
        
        # once gussed, loop will break
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You guessed too high!")

# If gussing is more than required guesses,
#show this output.
if count >= math.log(upper - lower +1,2,):
    print("\nThe number is %d" % x)
    print("\Better Luck Next time!")
    