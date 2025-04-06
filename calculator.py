Number1 = int(input("Enter First Number  : "))
Number2 = int(input("Enter Second Number :  "))
Opeartor = input("Enter Your Operator : ")
if Opeartor == "+":
    Number1 + Number2
    print(Number1 + Number2) 
elif Opeartor == "-":
    Number1 - Number2
    print(Number1 - Number2)
    if Number1 < Number2:
        Number2 - Number1
        print(Number2 - Number1)
elif Opeartor == "/" : 
    Number1 / Number2
    print(Number1 / Number2)        