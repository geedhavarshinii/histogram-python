#Write a Python program to count the number of occurrences of a specific character in a string.

def char_count(input_string, given_char):
    count = 0
    for char in input_string:
        if (char == given_char):
            count+=1
    return count

#receiving the input from the user
input_str = input("Enter a string: ")
while True:
    specified_char = input("Enter the characted to be counted: ")
    if (specified_char.isalnum()):
        break
    else:
        print("Enter a valid character")
result = char_count(input_str,specified_char)
print("The number of occurences of the specified character in the given string is ", result)