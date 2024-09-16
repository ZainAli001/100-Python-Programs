num = int(input("Enter number = "))
# fact = 1
# if num > 1 :
#     for i in range(1,num+1):
#         fact = fact * i  
    # print(fact)

# using recursion 
# def fact(num):
#     return ((num) * fact(num-1))                      

# res = fact(num)
# print(res)
fact =1
if num > 1:
    for i in range(1,num+1):
        fact = fact*i
print(fact)