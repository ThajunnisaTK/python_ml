def check_leap(x):
    if x % 4 == 0:
        if x % 100 == 0:
            if x % 400 == 0:
                print("it is a leap year")
            else:
                print("not a leap year")
        else:
            print("it is a leap year")
    else:
        print("not a leap year")
year = int((input("enter a year")))
check_leap(year)

