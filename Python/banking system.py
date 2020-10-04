import random #to generate a random no.
import sys  #to exit the system
accounts=dict()

#main functions
def mainscreen():# To display main screen of project when the function is called.
    global choice #By the GLOBAL ,the variables can be used in the whole project.
    print("\t#################################################")
    print("\t#\tWELCOME TO ONLINE BANKING SYSTEM\t#")
    print("\t#\t\t\t\t\t\t#")
    print("\t#\t\t\t\t\t\t#")
    print("\t#\t\tAPEEJAY SCHOOL\t\t\t#")
    print("\t#\t\t\t\t\t\t#")
    print("\t#\t\t\t\tMADE BY PP    \t#")
    print("\t#################################################")
    print("1.Create an Account")
    print("2.Deposit Money")
    print("3.Withdraw Money")
    print("4.Get Account Information")
    print("5.Modify An account")
    print("6.Close an account")
    print("7.Money Transfer")
    print("8.Exit")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def createaccount():# To create a new account
    global money
    global name
    global age
    global typeofacc
    global accno
    global address
    global phoneno
    global money1
    global name1
    global age1
    global typeofacc1
    global address1
    global phoneno1
    accno=random.randint(111111111111,999999999999)#Generating random account no. for user.
    name=input("Enter name of account holder")
    age=int(input("Enter age of account holder"))
    typeofacc=input("Enter the type of account(C/S)")
    phoneno=input("Enter your phone no.")
    address=input("Enter your address")
    password=input("Enter password for your account")
    money=int(input("Enter the amount of money to be deposited"))
    if type(name)!=str:
        print("INVALID NAME !!")
        name=input("Enter name of account holder again")
    if age<18 or age>99 or type(age)!=int:
        print("INVALID AGE!!!")
        age=int(input("please enter your age again(must be greater than 18 and less than 99)"))
    if type(typeofacc)!=str or len(typeofacc)>1:
        print(" SORRY!WE HAVE NO SUCH TYPE OF ACCOUNTS")
        typeofacc=input("Enter the type of account(C/S) again")
    if len(phoneno)<5 or len(phoneno)>10:
        print("INVALID PHONENO.!!")
        phoneno=int(input("please enter your phone no. again(must be of 5 to 10 characters)"))
    if type(address)!=str:
        print("INVALID ADDRESS!!!")
        address=input("Enter your address again(must not be only numbers)")
    if money>9999999 or money<1:
        print("Please enter a valid amount of money between 1 and 9999999")
        money=int(input("enter the amount of money to be deposited again"))
    for i in accounts:# to check uniqueness of accounts.
        if accounts[i]['phoneno1']==phoneno:
            print("This Phone no. is already linked to an account..")
            phoneno=input("Enter your phone no. again")
    print("Your Account No. is",accno)
    print("CONGRATULATIONS !!!!  Your Account Has Been Created!!")
    accounts[accno]={'name1':name,'age1':age,'password1':password,'typeofacc1':typeofacc,'money1':money,'phoneno1':phoneno,'address1':address}


def depositeamount():# To deposit money in your account
    a=int(input("enter the account no."))
    depo=int(input("enter the amount to be deposited"))
    passw=input("Enter your password")
    if a not in accounts:
        print("There is no such account")
        mainscreen()
    if type(depo)!=int:
        print("invalid entry")
        depo=int(input("enter the amount to be deposited"))
    if passw==accounts[a]['password1']:        
        accounts[a]['money1']+=depo
        print("Thank You ! Your Money has been deposited!!")
    elif passw!=accounts[b]['password1']:
        print("You have entered wrong password")      

def withdrawamount():# To withdraw money from your account
    b=int(input("enter your account no."))
    withdraw=int(input("enter the amount to be withdrawn"))
    passw1=input("Enter your password")
    if b not in accounts:
        print("There is no such account")
        mainscreen()
    if type(withdraw)!=int:
        print("INVALID ENTRY!!")
        withdraw=int(input("enter the amount to be withdrawn again"))
    n=accounts[b]['money1']
    if withdraw>n and passw1==accounts[b]['password1']:
        print("Your Account has insufficient balance!!")
    if passw1==accounts[b]['password1'] and withdraw<n:
        accounts[b]['money1']=n-withdraw
        print("Thank You ! Your money has been withdrawn!")
    elif passw1!=accounts[b]['password1']:
        print("You have entered the wrong password")

        
def accountinformation():# To get information of your account.
    c=int(input("enter your account no."))
    passw2=input("Enter your password")
    if c not in accounts:
        print("There is no such account")
        mainscreen()
    if passw2==accounts[c]['password1']:
        print("Here are your account details:-")
        print("Account Number=",c)
        print("Name of account holder:",str(accounts[c]['name1']))
        print("Age of account holder:",str(accounts[c]['age1']))
        print("Type of account:",str(accounts[c]['typeofacc1']))
        print("Balance:",str(accounts[c]['money1']))
        print("Password:",str(accounts[c]['password1']))
        print("Phone number.:",str(accounts[c]['phoneno1']))
        print("Address:",str(accounts[c]['address1']))
    elif passw2!=accounts[b]['password1']:
        print("You have entered the wrong password")

        
def modifyaccount():# To modify your account.
    f=int(input("Enter the account no."))
    g=str(input("Enter the detail to be modified(name,age,phoneno,address,password)"))
    print("Enter the new",g)
    h=input("")
    m=g+"1"
    passw4=input("Enter your password")
    if f not in accounts:
        print("There is no such account..")
        mainscreen()
    if passw4==accounts[f]['password1']:
        accounts[f][m]=h
        print("Your",g,"has been updated!!")
    elif passw4!=accounts[b]['password1']:
        print("You have entered wrong password")
        
def closeaccount():# To close your account.
    d=int(input("Enter your account number"))
    passw3=input("Enter your password")
    if d not in accounts :
        print("There is no such account")
        mainscreen()
    if passw3==accounts[d]['password1']:
        del accounts[d]
        print("Your account has been closed !!")
    elif passw3!=accounts[b]['password1']:
        print("You have entered the wrong password")

def transfermoney():# to transfer money
    taccno=int(input("Enter the acc no. to which you want to transfer money"))
    saccno=int(input("Enter your acc no."))
    spass=input("Enter your password")
    amounttransfer=int(input("Enter the amount to be transferred"))
    if spass==accounts[saccno]['password1'] and amounttransfer<accounts[saccno]['money1']:
        accounts[taccno]['money1']+=amounttransfer
        accounts[saccno]['money1']-=amounttransfer
        print("Thank You!! Your money has been transferred")
    elif spass==accounts[saccno]['password1'] and amounttransfer>accounts[saccno]['money1']:
        print("You have insufficient balnce to transfer!!")
        print("SORRY !! TRANSFER FAILED!!!!!")
    elif spass!=accounts[saccno]['password1'] and amounttransfer<accounts[saccno]['money1']:
        print("You have entered wrong Password..")

        
while True:# main loop for program(menu driven).
    mainscreen()
    choice=int(input("enter your choice"))
    if choice==1:
        createaccount()
    if choice==2:
        depositeamount()
    if choice==3:
        withdrawamount()
    if choice==4:
        accountinformation()
    if choice==5:
        modifyaccount()
    if choice==6:
        closeaccount()
    if choice==7:
        transfermoney()
    if choice==8:
        sys.exit()






