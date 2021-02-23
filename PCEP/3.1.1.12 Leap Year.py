year = int(input("Enter a year: "))

if year < 1582:
    print("Not within Gregorian period")
elif year % 4 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Leap Year")
elif year % 400 == 0:
    print("Leap Year")
else:
    print("Common year")
