year = int(input("Enter Year = "))

# leap year 366 --->once in 4 years

if year %400==0 and year%100 ==0:
    print(f"{year} Leap year")
elif year % 4 == 0 and year %100!=0:
    print(f"{year} Leap year")
else:
    print(f"{year} is not a  Leap year")
