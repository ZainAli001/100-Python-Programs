import cmath
a,b,c= input("Enter Number a, b , c = ").split()
# b= int(input("Enter Number b = "))
# c= int(input("Enter Number c = "))

# quardatic eq = ax**2 + bx + c = 0
# a != 0

# for discriminant
d = (int(b)**2) - (4*int(a)*int(c))

root1 = (-int(b) - cmath.sqrt(d))/2*int(a)
root2 = (-int(b) + cmath.sqrt(d))/2*int(a)
print(root1)
print(root2)