# Program Name: Ramirez_Jose_M07-FP.py
# Author: Jose Ramirez
# Summary: A program to add trainers and their new enrollees, depending on how many enrolling, 
#          they will be seperated into 3 categories but in Python3

trainers = []
enrollees = []

for i in range (0, 15):
    Names = input ("Enter Trainer name: ") 
    trainers.append (Names)
    Enrollments = int (input ("How many enrollments: ")) 
    enrollees.append (Enrollments)
category =[0, 0, 0]
  
for i in enrollees:
    if (i >= 0 and i <= 5):
        category[0] = category[0] + 1 
    elif (i >= 6 and i <= 10):
        category[1] = category[1] + 1 
    elif (i >= 11 and i <= 15):
        category[2] = category[2] + 1 
      
for i in range (0, 3):
    print ("Total enrollments in Category", (i + 1), "are", category[i])