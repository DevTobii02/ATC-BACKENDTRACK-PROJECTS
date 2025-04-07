print("This Is A Basic Calculator Project")
Number1 = int(input("Enter First Number  : "))
Number2 = int(input("Enter Second Number :  "))
Opeartor = input("Enter Your Operator : ")
if Opeartor == "+":
    Number1 + Number2
    print("The Result Of Your Operation Is : ", Number1 + Number2) 
elif Opeartor == "-":
    Number1 - Number2
    print("The Result Of Your Operation  Is : ", Number1 - Number2)
    if Number1 < Number2:
        Number2 - Number1
        print("The Result Of Your Operation Is : ", Number2 - Number1)
elif Opeartor == "/" : 
    Number1 / Number2
    print("The Result Of Your Operation Is : ",  Number1 / Number2)
elif Opeartor == "*":
    Number1 * Number2
    print("The Result Of Your Operation Is : ", Number1 * Number2)            