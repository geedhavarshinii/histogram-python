#Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
def max_and_min(sequence):
    maximum = max(sequence)
    minimum = min(sequence)

    return maximum, minimum

#lst = [5, 8, 3, 4, 9]

#receiving input from the user
input_sequence = input()
lst = [int(n) for n in input_sequence.split(',')]

max_num, min_num = max_and_min(lst)
print("The maximum number is ", max_num)
print("The minimum number is ", min_num)