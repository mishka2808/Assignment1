"""
Created on Thu May 5  10:05:35 2022
@author: Mish
Assignment 1
Question 1
"""
n = int(input ("Input any number :")) #Persons input

#Created a boolian for each case
rem2 = False
rem3 = False
rem5 = False

"""tests to see if a remainder exists for divisor (2,3,5) and if there is no remainder, it is divisible by the specific number
If no remainder exists, the boolians are changed to true to indicate it is divisible""" 

if n%2==0:
     rem2 = True
if n%3==0:
     rem3 = True
if n%5==0:
     rem5 = True 
     
"""#Counting the number of states/combinations of the divisors
2 F T
3 F T
5 F T     
2|3,5> = T{|FF> , |FT> , |TF> , |TT>} + F{|FF> , |FT> , |TF> , |TT>} ...8 states total"""
    
if rem2 == False:               #Else-If statement if n is divisible by 2, in this case, it is not divisible by 2
    if rem3 == False and rem5 == False:
        print("It's not Black or Pink :(") 
    if rem3 == False and rem5 == True:
        print("Pink")
    if rem3 == True and rem5 == False:
        print("Black")
    if rem3 == True and rem5 == True:
        print("BlackPink")
    
else:                           #in this case, n is divisible by 2
    if rem3 == False and rem5 == False:
        print("): kniP ro kcalB ton s'tI")
    if rem3 == False and rem5 == True:
        print("kniP")
    if rem3 == True and rem5 == False:
        print("kcalB")
    if rem3 == True and rem5 == True:
        print("kniPkcalB")
        
"""
Completed on Thu May 5  13:30:35 2022
"""