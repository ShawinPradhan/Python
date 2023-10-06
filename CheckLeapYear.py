#function to check whether a year is a leap year or not
def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return " is a leap year."
    else:
        return " is not a leap year."

year = int(input("Enter a year: "))

print(f"{year}",check_leap_year(year))

##OUTPUT
##Enter a year: 2002
##2002  is not a leap year.

##Enter a year: 2004
##2004  is a leap year.

