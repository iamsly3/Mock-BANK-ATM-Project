#register
#- first name, last name,email and password
#-generated user account

#login
#- account number  and password

#Bank operations

#initializating the system

database = {} # dictionary
import random
availableBalance = 100

def init():

    print("Welcome to bankPHP")

    
    haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n" ))

    if(haveAccount == 1):
           
        login()
    elif(haveAccount == 2):
           
        register()
    else:
         print("You have selected an invalid option")
         init()

def login():

    print("Login to your account")

    
   
    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("what is your password \n")


    for accountNumber, userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)
            else:     
                   print('Invalid account or password')
                   
    login()

    

def register():
    print("*****Please Register *****")

    email = input("What is your email address \n")
    first_name = input("What is your first name? \n")
    last_name = input("what is your last name? \n")
    password = input( "create a password \n")
    
    accountNumber = generateAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password, accountNumber]

    print("Your account has been created")
    print("== ==== ====== ====== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print("== ==== ===== ===== ===")

    login()
    #return database

def bankOperation(user):
    print("Welcome %s %s " % (user[0], user[1]))
    
    selectedOption = int(input("what would you like to do? (1) Deposit (2)Withdrawal (3) Logout (4) Exit \n"))

    if(selectedOption == 1):
        depositOperation()
    elif(selectedOption == 2):
        withdrawalOperation()  
    elif(selectedOption == 3):
        logout()  
    elif(selectedOption == 4):
        exit()
    else:
        print("Invalid option selected")
        bankOperation(user)

def withdrawalOperation():
    withdrawalAmount = int(input("How much would you like to withdraw? \n"))
    balance = availableBalance - withdrawalAmount
    print("take your cash $ %d" % withdrawalAmount)
    print("Available Balance $ %d" % balance)
    print("Would you like to do something else? \n")
    
    #print("withdrawal amount")

def depositOperation():
    depositAmount = int(input("How  much would you like to Deposit? \n"))
    balance = availableBalance + depositAmount
    print('Deposit Amount $ %d' % depositAmount)
    print("Available Balance $ %d" % balance)
    print("Would you like to do something else? \n")
    
    #print("Deposit Amount \n")
    
def generateAccountNumber():
    #print("account number generated")
    return random.randrange(1111111111,9999999999)

def logout():
    login()

#print(generateAccountNumber())

## Actual Banking System ####

init()