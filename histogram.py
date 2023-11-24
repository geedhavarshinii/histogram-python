def histogram(num):
      # Convert given number to list of integers
      lst = list(map(int, str(num)))
      # Iterate through the list to print the number as a string
      for i in num:
          print(i * str(i))

#num = input("Enter a number: ")
num = 345
histogram(num)
