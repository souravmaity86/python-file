# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 21:05:31 2022

@author: Sourav Maity
"""
#q3
A=int(input(" enter the value{A}:"))
B=int(input(" enter the value{B}:"))
C=int(input(" enter the value{C}:"))
if ((A>B) & (A>C)):
     print("{A} is greatest")
else:
    if ((B>C) & (B>A)):
       print("{B} is greatest") 
    else: 
      print("{C} is greatest") 
#q5
a = 6
b = 10
print( not ( not a == 10 or not b == 10) )
o/p: false
#6.Find the answer as well as find out the reason behind the result? -

#case 1:
A = 5.0
B = 10/2
print(A is B)
#o/P : FLASE
#case 2:
  A = 5.0
  B = int(10/2)
  print(A is B)
  #o/P: FALSE
#case 3:
  A = 5.0
  B = float(10/2)
  print(A is B)
  o/p: FLASE

# the memory allocation is not same
#Q7. Write a program that asks the user to enter a number. You should print out a message to the user, either “That number is divisible by either 3 or 5”, or “That number is not divisible by either 3 or 5”. Be sure to consider the data type of the input you are taking in from the user. Use a single if/else block to solve this problem.

i=int(input(" enter the value:"))
if((i%3==0) or (i%5==0)):
    print(f" the no {i } is divisible by 3 or 5")
else:
    print(f" the no{ i } is not  divisible by 3 or 5")

#q8
#Take user input for length and width. Then calculate the area of rectangle. Also print as per length and width whether its a square of rectangle.
L=int(input(" enter the value of length:"))
B=int(input(" enter the value of breath:"))
if L!=B:
    print(f"this is a rectangle")
else:
    print(f"this is a square")
print(f"the area is {L*B}")



#q9 Take two variable radius_1 and radius_2 and calculate the area of circle_1 and circle_2. Also print which circle has large area. If area is equal then print area is equal.          
 r1=int(input(" enter the value of radius of first circle:"))
 r2=int(input(" enter the value of radius of second circle:"))
 area_2=3.14*r2*r2
 area_1=3.14*r1*r1
 print(f" area of first circle is: {area_1}")
 print(f" area of second  circle {area_2}")
 
 if area_1!=area_2:
     if area_1>area_2:
         print (f"the area of first circle is greater")
     else:
         print (f"the area of second circle is greater")
 else:
     print (f"the area of {area_1} and {area_2} are equal")
    
 #q10
Check whether a year is leap year or not. Use nested if...else to solve this problem. A leap year is exactly divisible by 4 except for century years (years ending with 00). The century year is a leap year only if it is perfectly divisible by 400.        
year = int (input ("Enter any year that is to be checked for leap year: "))
if (year % 4) == 0:

              if (year % 100) == 0:

                             if (year % 400) == 0:

                                            print ("The given year is a leap year")

                             else:

                                            print ("It is not a leap year")

              else:

                             print ("It is not a leap year")

else:     

            print ("It is  a leap year")
    



