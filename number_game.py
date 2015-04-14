import random

winning_guess = random.randint(1,100)
print "Let's play! You have 5 tries to guess a number between 1 and 100."

for times in range (0, 5):
	user_guess = raw_input("Guess a number.  ")
	user_guess = int(user_guess)
	if user_guess == winning_guess:
		print" You win!"
	elif user_guess < winning_guess:
		print "You need to guess higher."
	elif user_guess > winning_guess:
		print "You need to guess lower."
print "You lose! You got %d guesses The answer was %s" %(times +1, winning_guess)
