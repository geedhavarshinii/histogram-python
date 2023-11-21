def histogram(num):
    intnum = list(map(int, str(num)))
    for i in intnum:
        times = i
        result = ''
        while times > 0:
            result+=str(i)
            times-=1
        print(result)
num = input("Enter a number: ")
histogram(num)