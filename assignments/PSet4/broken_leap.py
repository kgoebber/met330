# This is a program to check to leap year, written in python
#
# By: Kevin Goebbert

year = input("Input a year to determine if the year is a leap year \n"


while (int(year) != -999)

    yr4 = year % 4
    yr100 = year % 100
    yr400 = year % 400

    if (((yr4 = 0.0) and (yr100 != 0.0)) or ((yr100 = 0.0) and (yr400 = 0.0))):
       print("The year you input, "+year+, is a leap year!")
    else:
       print("The year you input, +year+, is NOT a leap year.")

    print()
year = input("Input a year to determine if the year is a leap year \n)
