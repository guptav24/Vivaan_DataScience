#Vivaan Gupta
#Insurance Project
#1/5/2022

import os
os.system('cls')

#Data for person
age = 28
smoker = 0
sex = 0
bmi = 26.2
num_of_children = 3

#Equation for insurance cost
insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500

#Printing insurance cost
print("This person's insurance cost is "+ str(insurance_cost)+" dollars.")

#Increase in age
age+=4
new_insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
change_in_insurance_cost  = new_insurance_cost-insurance_cost
print("The change in cost of insurance after increasing the age by 4 years is "+ str(change_in_insurance_cost)+" dollars.")

#BMI Change
age = 28
bmi+=3.1
new_insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
change_in_insurance_cost  = new_insurance_cost-insurance_cost
print("The change in cost of insurance after increasing BMI by 3.1 is "+ str(change_in_insurance_cost)+" dollars.")

#Male vs Female Factor
bmi = 26.2
sex = 1
new_insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
change_in_insurance_cost  = new_insurance_cost-insurance_cost
print("The change in estimated cost for being male instead of female is "+str(change_in_insurance_cost)+" dollars.")

#Extra: Smoker
sex = 0
smoker = 1
new_insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
change_in_insurance_cost  = new_insurance_cost-insurance_cost
print("The change in estimated cost for smoking is "+str(change_in_insurance_cost)+" dollars.")

#Extra: Num of children
smoker = 0
num_of_children = 4
new_insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
change_in_insurance_cost  = new_insurance_cost-insurance_cost
print("The change in cost of insurance after increasing the number of children by 1 is "+ str(change_in_insurance_cost)+" dollars.")