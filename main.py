def histogram(num):
    lst = list(map(int, str(num)))
    for i in lst:
        print(i*str(i))
        
num = input("Enter a number: ")
histogram(num)