#This Program returns grade depending on the number received as input by the user 
print("Check Your Score Grade Here")
Score = float(input("Enter A Score : "))
if Score >= 70 and Score <= 100:
    print("Your Grade Is A")
elif Score >=0 and Score <=39:
    print("Your Grade Is F")  
else:
    print("Score Received Is Out Of Bound")      