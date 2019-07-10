#importing needed packages
import random as rd 
import pandas as pd
import getpass as ps
import time as t

#definign list of users and database
app_list = []

database_df = pd.DataFrame(app_list, columns = ['user_name', 'password', 'name', 'birth_day', 'email', 'phone', 'zip_code', 'gender'])

#defining activities list to later generate it for user in random
indoor_list = ['Reading', 'Netflix','Board games','Ice Skating','Bowling','Treasure Hunting','Mini Golf','Basketball' ]
outdoor_list = ['Running','Soccer','StreetBall','Volleyball','Hiking','Rowing','Gardening','BBQ','Picnic','Golf']

#defining diary list and database 
diary_list = []
diary_df = pd.DataFrame(diary_list, columns = ['feelings','thoughts','activity'])


#function for new user
def new_user():
    u_name = input("Enter your user name: ")
    pswd = ps.getpass("Password: ")
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    birth_day = input("Please enter your birthday as (MM/DD/YY): ")
    email = input("Please enter your email: ")
    phone = input("Please enter your phone number: ")
    zip_code = input("Please enter your ZIP code: ")
    gender = input("Please enter your gender: ")
    print("Account created!")
    app_list.append({"user_name" : u_name,
                     "password" : pswd,
                     "first_name" : first_name,
                     "last_name" : last_name,
                     "birth_day" : birth_day,
                     "email" : email,
                     "phone" : phone,
                     "zip_code" : zip_code,
                     "gender" : gender})
    
    
    
#exisitng user definitoon
def old_user():
        u_name = input("Enter your user name: ")
        pswd = ps.getpass("Password: ")
        if str(u_name) in str(user_data['user_name']) and str(pswd) in str(user_data['password']):
            print(f"""Login successful!\n Welcome {u_name}! """)
           
            displayMenu()
        else:
            print("User doesn't exist or wrong password!")
            
            
#menu display method 
def displayMenu():
    print(f"""\n\n\nWelcome to Explonding! \nFamily bonding, reinvented! \n\nToday is {t.ctime()}""")
    
    #defining actions on screen
    print('\t1)Check my Schedule \n\t2)See my family chatroom \n\t3)See interests \n\t4)Go to your diary \n\t0)Exit')
    displayAct()
    
 #actions on the menu method   
def displayAct():
    action = input("Choose what you would like to do: \n")
    if str(action) == str(1): #schedules
        print(f"""\n This is your schedule app it will remind you of current time and schedules  \n\t\tThe current time is {t.ctime()}""")
        goBack()
    elif str(action) ==str(2): #family chat room
        print("\n This is your family chatroom\nHere you can chat with your family members\n\n Server Is Waiting For Incoming Connection.... \n0)Go Back")
        goBack()
    elif str(action) == str(3): #interest actions defintion
        print("These are the two types of interests. Please choose which one you want: \n1)Indoor \n2)Outdoor\n0)Go back")
        inter_act = input("choose what to do ")
        if str(inter_act) == str(1): #definition of indoor and outdoor acivities
            print("You prefer indoor activity \nPlease choose from the following: \n\t1)Random indoor activity \n\t2)Add activity to list \n\t0)Go Back")
            indoor = input("Enter your choice: ")
            if str(indoor) == str(1):
                print(rd.choice(indoor_list)) #generate random actiivity
                goBack()
            elif str(indoor) == str(2):
                indoor_add = input("What activity would you like to add? ")
                indoor_list.append(indoor_add) #append activity entered by user to indoor list
                print(f"""{indoor_add} was successfully added to the list. You can use it next time to generate random activity!""")
                goBack()
            else:
                goBack()
        elif str(inter_act) == str(2):  #define list to create an actions for outdoors and generate randomization
            print("You prefer outdoor activity \nPlease choose from the following: \n\t1)Random ourdoor activity \n\t2)Add activity to list \n\t0)Go Back")
            outdoor = input("Enter your choice:")
            if str(outdoor) == str(1):
                print(rd.choice(outdoor_list)) #generate random actiivity
                goBack()
            elif str(outdoor) == str(2):
                outdoor_add = input("What activity would you like to add? ")
                indoor_list.append(outdoor_add) #append activity entered by user to indoor list
                print(f"""{outdoor_add} was successfully added to the list. You can use it next time to generate random activity!""")
                goBack()
            else:
                goBack()
        else:
            displayMenu()
    elif str(action) == str(4): #diary room
        print("This is your diary. Here you can enter your thoughts and feelings! \n\t1)Write in your diary\n\t0)go back ")
        diary_activity = input("Enter your choice: ")
        if str(diary_activity) == str(1):
            diary_input()
            goBack()
        else:
            goBack()
    else:
        print("Good bye! See you again!")
        quit

        
#going back to menu method    
def goBack():
    go_back = input("Press 0 to go back ")
    if str(go_back) == str(0):
        displayMenu()

#funtion for diary input
def diary_input():
    feelings = input("How do you feel? (ex.happy, neutral, sad) ")
    thoughts = input(f"""Tell us more why you feel {feelings}(ex. Whats bothering you): """)
    activity = input("How was your activity? ")
    print("Thank for sharing with us your thoughts and felings. It is always good to talk to someone ")
    
    #appentding user  feeling info to the diary_list
    
    diary_list.append({"feelings" : feelings,
                      "thoughts" : thoughts,
                      "activity" : activity})
    

      
#defining if user is new or old and processing tp menu 
while True:
    user = input("""

Welcome to Explonding!

If you are a existing user, input 'Log In'

If you are a new user, input 'Register' 
""")

    if user.lower() == "register" :
        new_user() # runs predefined user function
        user_data = database_df.append(app_list, ignore_index = True)
        displayMenu()
        break
        
    elif user.lower() == "log in":
        old_user()
        break
    else:
        print("Wrong input! Please enter 'Log In' or 'Register'")
    
    
    