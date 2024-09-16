num = input("Enter number : ")
x= len(num)
sum=0
for i in range(x):
    res = int(num[i])**x
    sum+=res
if sum == int(num) : print(f"The Number = {num} is Armstrong")
else : print(f"The Number = {num} is not a Armstrong")
