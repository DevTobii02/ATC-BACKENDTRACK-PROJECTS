#This Program calculates body mass index of an individual by collecting weight and height as input 
print("Get Your BMI Here")
Weight = float(input("Enter Your Weight : "))
Height = float(input("Enter Your Height : "))
SquaredHeight = Height * Height
BodyMassIndex = Weight / SquaredHeight
print("Your Body Mass Index is : ", BodyMassIndex)