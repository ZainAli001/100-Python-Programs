while True:
    num = int(input("Enter Number = "))
    match num:
        case _ if num>0:
            print(f"Number {num} is positive..!")
        case _ if num<0:
            print(f"Number {num} is negative..!")
        case _ if num==0:
            print(f"Number {num} is zero..!")
