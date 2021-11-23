# To get year (integer input) from the user
# This is my first explanation
print("Başarılar herkese")
year = int(input("Enter a year: "))

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))



# by burcu

sayı= int(input("Lütfen bir sayı giriniz:"))
  if (sayı % 4 == 0 and sayı % 100 != 0) or sayı%400==0:
    print(sayı,"sayısı artık yıldır:",True)
    break
  else:
    print(sayı,"sayısı artık yıl değildir:",False)