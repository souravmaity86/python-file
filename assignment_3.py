C:/Users/Sourav Maity/Desktop/ib/data science/inuron/6_3_python_list.pyC:/Users/Sourav Maity/Desktop/ib/data science/inuron/6_3_python_list.py# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 20:58:56 2022

@author: Sourav Maity
"""
#Q1 :Count the number of times iNeuron appears in the string
text = "Welcome to iNeuron, You are a part of FSDS Bootcamp 2 in iNeuron. I hope you are enjoying the course by iNeuron"

print('Number of occurrence of :iNeuron', text.count('iNeuron'))

# Q2. Check if position 5 to 11 ends with the phrase iNeuron. in the string
txt = "Hello, welcome to FSDS 2.0 at iNeuron."

txt.endswith("iNeuron.")
#q3 Write a program that takes your full name as input and displays 
#the abbreviations of the first and middle names 
#except the last name which is displayed as it is. For example,
# if your name is Sunny Bhaveen Chandra, then the output should be S.B.Chandra.
name="Sourav Kumar Maity"
first_name, middle_name, sur_name= name.split(" ")
F1=first_name[0]+'.'
F2=middle_name[0]+'.'

print(f"{F1}{F2}{sur_name}")


#q4Join all items in a list into a string, using a hash(#) character as separator:

LIST = ["My", "name", "is", "Rishav", "Dash"]

LIST1 = '#'.join([str(elem) for elem in LIST])
print(LIST1)
#q5
#Write example for the following string manipulation function,
#isdecimal()
txt = "\Sour99v" 

x = txt.isdecimal() #The isdecimal() method returns True if all the characters are decimals (0-9).

print(x)

# islower()
name= "SOURAV"
print(name.islower()) # check if all the characters are  in lowercase

##isupper()
name= "MAITy"
print(name.isupper()) # check if all the characters are in uppercase 
# isalpha()
name= "MAITy09"
print(name.isalpha()) # check if all the characters are in alphabets
#isnumeric()
name= "77809"
print(name.isnumeric()) # check if all the characters are in numeric
#q6
#Indian PAN card format follows the following formats -

#AYEPC7894X
#ABCDE9999Y Take user input for PAN_CARD and validate as per the above example.
PAN_card=input("enter your PAN NO:")
if PAN_card[0:5].isupper and PAN_card[5:9].isdigit() and PAN_card[9].isupper and  len(PAN_card)==10:
  print(f"user input is correct")
else:
  print("invalid input")
