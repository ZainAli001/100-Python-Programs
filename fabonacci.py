
num = int(input("Enter number = "))
a= 0
b=1
sum_ = 0
for i in range(num):
    print(a,end=" ")
    sum_ = a+b
    a=b
    b=sum_