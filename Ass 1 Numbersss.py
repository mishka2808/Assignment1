"""
Created on Thu May  5 13:55:18 2022
@author: Mish
Assignment 1
Question 2
"""
def is_float(myNumbers): #creates a parameter/definition called "is_float"
    try:                 #trys a specific command, in this case, it checks if myNumbers can be a float
        float(myNumbers)
        return True      #lets the system keep going until
    except ValueError:   #we reach a value that cannot be a float (non-numerical values such as @#% and letters)
        return False     #prevents the system from adding this specific value
    
myNumbers = [] #Empty List made
num = (str(input("Type your numbers. Type * to end "))) #first user input

while not num == "*":                   #loops if num doesnt = *
    if is_float(num):                   #checks to see if the value entered by the user can be a float, if true, then we proceed to
        myNumbers.append(float(num))    #add the value into the array as a float
        print(myNumbers)                #displays the current array (mostly for personal observation and checks if the array is appearing correct)
        num = (str(input("Type your numbers. Type * to end ")))     #restarts the loop with a new user input until "*" is typed
    else:
        print("Is not a valid number.") #the number is not added since it does not meet the requirements of the is_float function (so its not a float and is not added to the array)
        num = (str(input("Type your numbers. Type * to end "))) #restarts the loop until "*" ends the loop
else:
    if num == "*": 
        print("Thank you for the numbers", myNumbers)           #ends the loop
    
import numpy as np

mean = np.mean(myNumbers)
median = np.median(myNumbers)
stdev = np.std(myNumbers)

print("Mean: ", mean)
print("Median: ", median)
print("Standard Deviation: ", stdev)

import matplotlib.pyplot as plt

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.hist(myNumbers)

plt.show()

"""
Completed on Thu May 10  10:35:10 2022
"""
        