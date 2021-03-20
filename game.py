from printing_service import printing_out


def play():
    try:
        num1 = int(input("Write the first number: "))
        num2 = int(input("Write the second number: "))
        printing_out(num1, num2)
    except ValueError:
        print("Something went wrong")
