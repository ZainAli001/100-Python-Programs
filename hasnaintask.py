my_str = "hasnain"
count_char ={}

for i in my_str:
    if i not in count_char:
        count_char[i] = 1
    else:
        count_char[i] +=1

result_str = ''
for char, count in count_char.items():
    result_str += f"{char}{count}"
print(result_str)