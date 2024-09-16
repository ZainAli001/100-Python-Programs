import random
list1 = ["apple","bannana","cherry"]
list2 = list1.copy()
random.shuffle(list2)

combine_data = list(zip(list1,list2))
print(combine_data)