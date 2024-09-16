num = int(input("Enter number : "))
sum= 0
if num<0: print("Number is negative")
else:
    for i in range(1,num+1):
        sum += i

print(sum)
