"""
# While Loop
# For in --key differences in 'for in' loop clearly defined start and finish to loop
# While--while loops don't stop on a list and has to be told to stop(sentinal value)

"""
# nums = list(range(1,100))
#   print(nums)

# ####for in loop


# for num in nums:  <--- to print out the list of numbers
#     print(num)


# # while len(nums) > 0:       <-- length of nums is great than 0
# #     print(nums.pop())      <--iterates over list and pops off the value--starts at 99 and goes to 1
#-------------------------------------------------------------------------
def guessing_game():                  # fucntion name guessing game
    while True:                       # while True ( don't know where you want it to stop)
        print('What is your guess?')  # print what is your guess
        guess = input()               # stored guess in a variable --input is a function and stores whatever we put in (sets a prompt and stores what we type)
        
        if guess == '42':             # if guess is equal to 42 (user guess ) 
            print('You correctly guessed it')  # you got it right basically
            return False                       # Will stop the program here (stop the loop)
        else:
            print(f'No, {guess} is not the anwer try again\n')   # print format No and then what ever number the guess- is not the answer '\n new line ' 
                
guessing_game()                
