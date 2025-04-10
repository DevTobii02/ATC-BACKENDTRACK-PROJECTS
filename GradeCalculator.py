#This Program returns grade depending on the number received as input by the user 
print("Check Your Score Grade Here")
Score = float(input("Enter A Score : "))
if Score >= 70 and Score <= 100:
    print("Your Grade Is A")
elif Score >= 60 and Score <= 69.9:
    print("Your Grade Is B")    
elif Score  >= 50 and Score <= 59.9:
    print("Your Grade Is C ")
elif Score >= 45 and Score <= 49.9:
    print("Your Grade Is E")    
elif Score >=0 and Score <=39:
    print("Your Grade Is F")  
else:
    print("Score Received Is Out Of Bound")      