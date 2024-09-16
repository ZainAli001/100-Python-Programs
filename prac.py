num= 1496
max_num = 0
while num > 0:
    digit= num % 10 #6
    if digit > max_num:
        max_num = digit
    num //=10 # 149

print(max_num)

