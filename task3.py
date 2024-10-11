# passwd_check functon is to check the strenght of password.
def passwd_check(password):
    up_case,l_case,digit,sp,pl=0,0,0,0,0      # up_case=uppercase, l_case=lowercase, sp=special character
    pl=len(password)                          # pl=password lenght
    # check that your password match the criteria for a strong password
    if(pl<8):
        print("please try angain your password is not strong enough it should at least have 8 characters.....")
    else:
        for i in range(0,pl):
            if(password[i].isupper()):
                up_case += 1
            elif(password[i].islower()):
                l_case += 1
            elif(password[i].isdigit()):
                digit += 1
            else:
                sp += 1
    # feedback according to your password
    if (up_case != 0 and l_case != 0 and digit != 0 and sp != 0):
        if (pl >= 12):
            print("The strength of password is strong.\n")
        else:
            print("The strength of password is medium.\n")
    else:
        if (up_case == 0):
            print("Password must contain at least one uppercase character!\n")
        if (l_case == 0):
            print("Password must contain at least one lowercase character!\n")
        if (sp == 0):
            print("Password must contain at least one special character!\n")
        if (digit == 0):
            print("Password must contain at least one digit!\n")
print("******WELCOME TO PASSWORD COMPLEXITY CHECKER*******")
print()
print()
ch=input("Do you want to check the complexity of your password if yes press(y/Y) else press(n/N)to exit....")
if(ch=='y' or ch=='Y'):
   passwd=input("Enter your password to check its strenght.....")   # passwd=password
   passwd_check(passwd)                                             #functon is called to check the password.
elif(ch=='n' or ch=='N'):
    print("*****VISIT US NEXT TIME****")
print()
print("**********THANK YOU FOR YOUR VISIT*********")