"""
Created on Wed Oct  13 09:24:05 2016

File:       testBmi.py    
Date:       10/13/2016
Instructor: Nguyen Thai
Course:     CSC 7014 - The Practice of Computer Programming
Author:     Reshma Kapadnis
Description: A program in which we create a test case to check the BMI class of the given list.
"""

from bmi import BMI###importing our bmi class

def healthStatus(name,age,weight,height_ft,height_inch): ##function for calculating healthstatus for teh given users
    c=BMI(name,age,weight,height_ft,height_inch)
    c.getName()
    c.getStatus()

healthStatus(name='John',age=18,weight=165,height_ft=5,height_inch=9)###user 1

healthStatus(name='Mary',age=25,weight=115,height_ft=5,height_inch=2)##user 2

healthStatus(name='Mark',age=60,weight=135,height_ft=5,height_inch=6)##user 3

