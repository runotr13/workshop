# To get year (integer input) from the user
# This is my first explanation
print("Başarılar herkese")
year = int(input("Enter a year: "))

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} is a leap year".format(year))
            print("Onur hoca çok güzel liderlik yapıyor bütün liderlikleri alsın")
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))
print("merhabalar arkadaşlar")
