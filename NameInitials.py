#This Project Generates Name Initials By Taking The First Letter Of Each Name Provided
print("Generate Your Name Initials Here")
FirstName = input("Enter Your First Name : ")
MiddleName = input("Enter Your Middle Name : ")
LastName = input("Enter Your Last Name : ")

NameInitials = FirstName[0] + "." + MiddleName[0] + "." +  LastName[0] + "." 
print("Your Name Initials Is : van", NameInitials)