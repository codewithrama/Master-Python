#!/usr/bin/env python
# coding: utf-8

# # Digital ATM with Python

# In[1]:


import math, random
 
# function to generate OTP
def generateOTP() :
 
    # Declare a digits variable 
    # which stores all digits
    digits = "0123456789"
    OTP = ""
 
   # length of password can be changed
   # by changing value in range
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
 
    return OTP


# In[2]:


def validate_phone_number(phone_number):
    if len(phone_number) != 10:
        return False
    else :
        return True
       


# In[3]:


import time
import os


print ("⭐Welcome to Rs ATM  ")
time.sleep(2)
print (" ")
print ("What do you want do today ?😍")
print (" ")
print ("Press 1 : Open a Bank Account\n" 
       "Press 2 : Withdrawl Amount\n" 
       "Press 3: Know your balance")

user_input = int(input(" "))
#blocking  invalid user input

if (user_input >=4 or user_input ==0):
    print ("Invalid Input 😔 Try again !")

elif user_input ==1:                                            #open a back account
        phone_num = str(input("Enter your Phone number : "))
        if (validate_phone_number(phone_num) == True):  
                print ('Loading.... Hang on 3 2 1')
                time.sleep(3)
                print ("Successfully 🥳 we saved your phone number in our DataBase")
                time.sleep(2)
                print ('Here is your Personalized OTP, Please Show this in Banking Counter',generateOTP())
                print ("Thank you !!")
                os.system('clear')
           
        else :
            print ("Invalid phone number !😒")
            
elif user_input ==2:                           #Withdrawl Amount
    account_number = str(input("Enter your A/c"))
    if(len(account_number) != 6):
        print ("Our Bank Account no is Max 6 Digits")
    else :
        account_pin= str(input('Enter your Account OTP When you initiated your bank process :'))
        if(len(account_pin) !=4) :
            print('PIN is wrong')
        else :
            amount = str(input('Enter the Amount to Withdraw :  '))
            time.sleep (3)
            print ("Your Amount Withdrawn !")
            print ("Thankyou !")
            
elif user_input ==3:                                  #Withdrawl Amount
    account_number = str(input("Enter your A/c"))
    if(len(account_number) != 6):
        print ("Our Bank Account no is Max 6 Digits")
    else :
        account_pin= str(input('Enter your Account OTP When you initiated your bank process :'))
        if(len(account_pin) !=4) :
            print('PIN is wrong')
        else:
            time.sleep (3)
            print ("Your balance is : ",generateOTP())
            time.sleep (5)
            print ("Thankyou !")
        
        
        
else :
     print ('Machine Failed !')     


# ## 
