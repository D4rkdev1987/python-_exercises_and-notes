def fizz_buzz(max_num, display_rows):
    if display_rows:
      list_format = []
      def format_number(number_check):
          if num % 5 == 0 and num % 3 == 0:
              return "FizzBuzz"
          elif num % 3 == 0:
              return "Fizz"
          elif num % 5 == 0:
              return "Buzz"
          else:
              return num

      for num in range(1,max_num+1):
          list_format.append(format_number(num))
      
      i = 0
      while i < max_num:
        print(str(list_format[i:i+5]).strip('[]'))
        i +=5
    else:
      for num in range(1,max_num+1):
          if num % 5 == 0 and num % 3 == 0:
              print("FizzBuzz")
          elif num % 5 == 3:
              print("Fizz")
          elif num % 5 == 0:
              print("Buzz")
          else:
              print(num)            

def Is_Int(n):
    try: 
        int(n)
        return True
    except ValueError:
        return False
input_needed = True
user_range = input("Please input how many numbers you'd like to generate, then press ENTER:")

while input_needed:
    if Is_Int(user_range):
        if int(user_range) < 2:
            user_range = input("Please input an integer greater than 1, then press ENTER:")
        else:
            input_needed = False
            user_range = int(user_range)
    else:
        user_range = input("Please input a valid integer, then press ENTER:")

format_toggle = False
format_input = input("Please type 'row' without quotations if you'd like to see a more organized display, otherwise just press ENTER: ").strip().lower()

if format_input == "row":
  print(f"<<ROW DISPLAY FOR {user_range} NUMBERS>>")
  format_toggle = True
else:
  print(f"<<VERTICAL DISPLAY FOR {user_range} NUMBERS>>")

fizz_buzz(user_range, format_toggle)
