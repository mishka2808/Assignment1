"""
Created on Thu May  5 17:54:40 2022
@author: Mish
Assignment 1
Question 3
"""
debtFund0 = 100000.00   #Rands... Float incase of cents being needed
interestRate = 0.065/12 #Float again cause of decimal place... interest% /12 months / 100 so I can just multiply and add it to the initial amount
monthlyRepayment1k = 1000.00 
monthlyRepayment2k = 2000.00
monthlyRepayment3k = 3000.00
monthlyRepayment4k = 4000.00 
month = 1               #for a loop for the 5x12 months total

newcash1karr = [100000.00] #creating a list to store all the cash amounts
newcash2karr = [100000.00]
newcash3karr = [100000.00]
newcash4karr = [100000.00]

n = 0 #n is going to be useful when I need to select the previous element of the array in order to redo calculations and fill in the next element of the array properly
#otherwise its going to be repeated with the first element in the array, and is going to give the same result over the 60 months

"""Idea for how it's calculated:
newcash = debtfund0 - monthlyrepayment 
interest_repayment = newcash*interestRate
new_bankbalance = newcash + interest_repayment ---> your new debtfund
append the new_bankbalance into the newcash list
"""

while month<60:     #the loop is going to run for the 60 months
    newcash1 = newcash1karr[n] - monthlyRepayment1k 
    interest_repayment1 = newcash1*interestRate
    new_bankbalance1 = newcash1 + interest_repayment1
    newcash1karr.append(float(new_bankbalance1))
    
    newcash2 = newcash2karr[n] - monthlyRepayment2k 
    interest_repayment2 = newcash2*interestRate
    new_bankbalance2 = newcash2 + interest_repayment2
    newcash2karr.append(float(new_bankbalance2))
    
    newcash3 = newcash3karr[n] - monthlyRepayment3k 
    interest_repayment3 = newcash3*interestRate
    new_bankbalance3 = newcash3 + interest_repayment3
    newcash3karr.append(float(new_bankbalance3))
    
    newcash4 = newcash4karr[n] - monthlyRepayment4k 
    interest_repayment4 = newcash4*interestRate
    new_bankbalance4 = newcash4 + interest_repayment4
    newcash4karr.append(float(new_bankbalance4))    #easier to do all 4 arrays at once rather than just copy pasting the entire loop for the different cash amounts
    
    month=month+1   #stopping parameter 
    n=n+1           #pushes to the next element in the array so that calculations are done with the newest amount in the array
    

print("Debt with R1K Payments over 5 years: ", newcash1karr)
print(" ")
print("Debt with R2K Payments over 5 years:: ", newcash2karr)
print(" ")
print("Debt with R3K Payments over 5 years:: ",newcash3karr)
print(" ")
print("Debt with R4K Payments over 5 years:: ",newcash4karr)    #just needed to check to see if all the amounts are correctly done.
#The negative amounts won't really matter so there's no reason to remove them and create a whole new loop. I can just set the axe's on the plot to show positive values only

x_axis = [1]    #I was too lazy to fill in the array with the range of 1->60 for the x-axis so I just made a loop to do it for me. I think there's an easier way but I forgot the function.
month_x_axis = 1
while month_x_axis<60:
    month_x_axis= month_x_axis + 1
    x_axis.append(int(month_x_axis))
    
print("The number of months are: ", x_axis)     #needed to check if all 60 months are in

import matplotlib.pyplot as plt

plt.xlabel("Number of Months")
plt.ylabel("Debt")
plt.plot(x_axis, newcash1karr, label = "R1000") 
plt.plot(x_axis, newcash2karr, label = "R2000")
plt.plot(x_axis, newcash3karr, label = "R3000")
plt.plot(x_axis, newcash4karr, label = "R4000")     #labels are required for the lines to be distinguished and for the legend
plt.legend()                                        #adding the legend to the plot
ax = plt.gca()                                      #created a function to manipulate the axe's of the graphs
ax.set_ylim(0,100000)                               #set a y limit so that the negative values we gained from the arrays are cut off
ax.set_xlim(1,60)                                   #set an x limit so it looks neater and less disjointed from the axes  
plt.show()                                          #Done :D

"""
Completed on Wed May 11  18:55:27 2022
"""

