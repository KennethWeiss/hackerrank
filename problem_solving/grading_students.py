
import math
import os
import random
import re
import sys

def gradingStudents(grades):
    # Write your code here
    rounded_grades = []
    for grade in grades:
        if grade >= 38:
            difference = 5-(grade%5)
            print(f"Difference is, {difference}!")
            if difference<3:
                print("Modding")
                grade +=difference
        print(grade)
        rounded_grades.append(grade)
    return rounded_grades
 
print(gradingStudents([73,67,38,33]))