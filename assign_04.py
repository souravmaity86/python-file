# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 21:35:30 2022

@author: Sourav Maity
"""

#q1 Find the largest number from the given list, use for loop.

numbers = [12, 75, 150, 180, 145, 525, 50]
l=numbers[0]
for i in numbers:
     if i>l:
         l=i
print(f" largest  no:{l}")
# Q2
#Print all the even number between (1, 12).
for i in range(1,12):
    if i%2==0:
        print(f" the even is : {i}")
#q3 Calculate the sum of all numbers from 1 to a given number  
a= int(input(" enter your range:"))
sum=1
for i in range(a+1):
    if i!=1:
        sum=sum+i
print(f"sum of all the numbers:{sum}")
#q4 Write a program to display only those numbers from a list that satisfy the following conditions

#The number must be divisible by five

#If the number is greater than 150, then skip it and move to the next number

#If the number is greater than 500, then stop the loop

numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i%5==0:
        print(f" {i} is divisible by 5")
    elif  i>150:
        continue
    print(f" the number {i} is less than  150 ")
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:  
    if  i>500:
        break
    print(f" the number {i} is less than range")

#q5 Print the given list in reverse order.

list1 = [10, 20, 30, 40, 50]
print(f"original list{list1}")
list1.reverse()
print(f"reverse of the list{list1}")
list1 = [10, 20, 30, 40, 50]
start = len(list1) - 1
reversed_list = [list1[i] for i in range(start, -1, -1)]
print(reversed_list)









