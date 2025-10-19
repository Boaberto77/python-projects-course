import os
import random

# Ask to play again
def play_again():
	while True:
		# ask to play again
		user_input = input("Do you want to play again? (yes/no): ").lower()
		# logic for choice
		if user_input in ['yes', "no"]:
			return user_input == "yes"
		else:
			print("Invalid input. Please enter 'yes or 'no'.")

# Determine winner
def determine_winner(user_choice, computer_choice):
	#Determine tie
	if user_choice == computer_choice:
		return "Its a tie!!"
	# Determine user winning
	elif (user_choice == "Rock" and computer_choice == "Scissors") or \
		(user_choice == "Scissors" and computer_choice == "Paper") or \
		(user_choice == "Paper" and computer_choice == "Rock"):
		return "You Win!"
	else:
		return "Computer Wins!"


def get_computer_choice():
	# Have the computer select rock, paper, scissors
	choices = ["Rock", "Paper", "Scissors"]
	return random.choice(choices)

def get_user_choice():
	choices = {1:"Rock", 2:"Paper", 3:"Scissors"}
	try:
		user_input = int(input("Enter 1 for Rock, 2 for Paper, or 3 for Scissors: "))
		if user_input in choices:
			return choices[user_input]
		else:
			print("Invalid Choice. Please try again")
			return get_user_choice()

	except ValueError:
		print("Invalid Input. Please Enter a Number between 1 and 3.")
		return get_user_choice()

# Set up the game
def play_game():
	while True:

		# Clear the screen
		os.system("clear")
		# Get the users choice
		user_choice = get_user_choice()
		# Get the computers choice
		computer_choice = get_computer_choice()

		# User Output
		print(f"You Chose: {user_choice}")
		# Computer output
		print(f"Computer Chose: {computer_choice}")

		# Determine the winner!
		result = determine_winner(user_choice, computer_choice)
		# Print the results
		print(result)

		# end the game
		if not play_again():
			print("Thanks for playing! Goodbye!")
			break


# Play the Game
play_game()