#Madlibs Game : This project works basically by taking inputs from the user to complete parts of a story 
PlayerName = input("Enter Player Name Please : ")
print("Welcome ",  PlayerName) 
Name = input("Enter Your Name : ")
try:
	Age = int(input("Enter Your Age : "))
except ValueError:
	print("Invalid input! Please enter a valid integer for your age.")
	Age = 0  # Default age if input is invalid
Height = input("Enter Your Height : ")
Complexion = input("Enter Your Complexion : ")
Country = input("What Country Do You Live In : ")  


#Use of Formatted Strings To Concatenate Integers and Stings Together
MyStory = f"Hi My Name is {Name}. I Am {Age} years old,  I am {Height} in height,  {Complexion} in Complexion and I live in {Country}."
print(MyStory)