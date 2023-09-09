from accountdetail import *

# A website descirbes te ocation of well maintained mountain bike routes across the Peak District. To have access
# to the website, users must login with an email address and 8-character passwoord. You have been asked to write 
# a small program that checks the email adddress and 8 character password mach the ones that are sstored in the program
# your program sould make use of the account details and only allow customers to atttempt their username and password four
# times after tat the login program will end. Only allow access to the website if both the email addres and passowrd are correct.

# first I will create a variable named "attempts" and assign it the value of 4 
attempts = 0
while attempts <= 4 :
    userEmail = input("To get the location for these bike routes please enter your email: ")
    userPassword = input("password: ")
    if userEmail == emailAddress and userPassword == password:
        print(location)
        break
    else:
        print("Try again")
        attempts += 1
