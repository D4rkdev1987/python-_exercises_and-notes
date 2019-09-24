# """
# While Loop0
# For in --key differences in for in loop clearly defined loop
# While--while loops don't stop on a list and has to be told to stop(sentinal value)

# """
# nums = list(range(1,100))
# # print(nums)

# ####for in loop


# # for num in nums:
# #     print(num)


# # while len(nums) > 0:# length of nums is great than 0
# #     print(nums.pop())

def guessing_game():
    while True:
        print('What is your guess?')
        guess = input() #input is a function and stores whatever we put in
        
        if guess == '42':
            print('You correctly guessed it')
            return False
        else:
            print(f'No, {guess} is not the anwer try again\n')   
                
guessing_game()                
