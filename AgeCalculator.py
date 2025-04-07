#This Projects calculates users age based on input received as birth year
print("Hi Lets Calculate Your Age For You")
import datetime
date = datetime.datetime.now()
print(date)
print(date.year)
BirthYear = int(input("Enter Your Birth Year : "))
Age = date.year - BirthYear
print(f"Your Are {Age} years of Age")