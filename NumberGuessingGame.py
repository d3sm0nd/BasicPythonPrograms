import random
a = input("Welcome to the Number Guessing Game \n in which You have to set a range between two numbers.\n"
      "Now You have to Guess the number which the Computer has guessed in the minimum numbers of time.Press ENTER to Continue "
          "\n ALL THE BEST :)")


range1 = int(input("Please enter the first starting number :>"))
range2 = int(input("Please enter the second end number :>"))
range_large = range2 + 1
list1 =list(range(range1 , range_large))
#print (list1)
# Now Selecting a random Number from range1 to range2

select_random = random.choice(list1)
#print(select_random)
tries = int(range_large /2)
print("You have {} tries left.".format(tries))

# The System has choosen the random digit Now Loop starts to find the number of Guesses

print("Start Guessing Your Number ;)")
guesses = 1
guess = int(input("Please Enter Your Guessed Number Here:"))
tries = tries - 1
print("You have {} tries left".format(tries))

while True:


    if guess == select_random:
        print("CONGRATULATIONS You are Great \n You Guessed It right")
        print("You have guessed it in {} guesses.".format(guesses))
        print("You guessed the number within the tries")
        break

    elif tries == 0:
        print("Game Over You have Zero Tries :(")
        break

    elif guess > select_random:
       print("Hnnn It seems you are guessing number larger than my number Please try Again ")
       guesses = guesses + 1
       guess = int(input("Please Enter Your Guessed Number Again:"))
       tries = tries - 1
       print("You have {} tries left".format(tries))


    elif guess < select_random:
        print("Hnnn It seems you are guessing number smaller than my number Please try Again ")
        guesses = guesses + 1
        guess = int(input("Please Enter Your Guessed Number Again:"))
        tries = tries - 1
        print("You have {} tries left".format(tries))

    elif guess > range_large:
        print("Please Select the Number Only within the range you have selected.")
        guesses = guesses + 1
        guess = int(input("Please Enter Your Guessed Number Again:"))
        tries = tries - 1
        print("You have {} tries left".format(tries))

