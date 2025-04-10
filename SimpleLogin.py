#Simple login that stores data per runtime 
enter_email = input("Enter Your Email : ")
enter_password =  input("Enter Your Password : ")

confirm_email = input("ReEnter Your Email : ")
confirm_password = input("ReEnter Your Password : ")

if enter_email == confirm_email and enter_password == confirm_password:
    print("Logged In Successfully")
else:
    print("Wrong Login Details") 