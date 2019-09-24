# use of methods
# The user needs to be able to make a deposit
# The user needs to be able to pull money out
# The user needs to be able to pay a bill
# The program needs to track the money in the bank
# The user needs to be able to look up their balance
# The program needs to keep running until the user decides to quit the program.

current_bank_balance = []

def start():
	print("Hello and welcome to the bank")
	main_menu()


def main_menu():
	print("Here are our menu options")
	user_input = input("Please select from the following menu choices: 1: Deposit, 2: Balance, 3: Withdraw, 4: Make a bill payment, 5: Quit ")
	if user_input == "1":
		deposit()
	elif user_input == "2":
		balance()
	elif user_input == "3":
		withdraw()
	elif user_input == "4":
		pay_bill()
	elif user_input == "5":
		print("Please come again")
	else:
		print("That is not a valid option, please try again")
		main_menu()	

def deposit():
	deposit_amount = input("How Much Would You Like to Deposit? ")
	current_bank_balance.append(float(deposit_amount))
	print(f"You have deposited ${deposit_amount}")
	deposit_subchoice()


def deposit_subchoice():
	user_choice = input("Would you like to make another deposit? or return to the main menu? Deposit, Main, Quit ")
	if user_choice == "Deposit":
		deposit()
	elif user_choice == "Main":
		main_menu()
	elif user_choice == "Quit":
		print("Please come again")
	else:
		print("That is not a valid option, please try again")
		deposit_subchoice()


def balance():
	print(f"Here is your current balance ${float(sum(current_bank_balance)):.2f}")
	main_menu()
	

def withdraw():
	print("hi from withdraw")
	


def pay_bill():
	print("hi from pay_bill")
	



start()