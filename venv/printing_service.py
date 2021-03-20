def view_information():
    print("""
    An extended project "FizzBuzz" made by:
    
    Wojciech Jasiewicz
    """)


def view_rules():
    print("""
    
    1. Then write 2 numbers which will be the range
    3. Do not try to write letters or any other characters, just numbers
    4. Your range will be written on the screen
    5. Divisors of 3  will be replaced by Fizz
       Divisors of 5  will be replaced by Buzz
       Divisors of 15 will be replaced by FizzBuzz
    6. You will come back to main menu
    """)


def printing_out(num1, num2):
    if num1 < num2:
        print_numbers(num1, num2 + 1)
    else:
        print_numbers(num2, num1 + 1)


def print_numbers(smaller, bigger):
    for number in range(smaller,bigger):
        if number % 15 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
