#Write a Python function to check whether a number is divisible by another number

def divisible_or_not(num, divisor):
    if (divisor == 0):
        print("Division by zero is not possible.")
    elif (num%divisor == 0):
        print("The given number is divisible.")
    else:
        print("The given number is not divisible.")

#receiving the input from the user
number = int(input("Enter the number to be checked for divisibility: "))
divisor_num = int(input("Enter the divisor: "))
divisible_or_not(number, divisor_num)