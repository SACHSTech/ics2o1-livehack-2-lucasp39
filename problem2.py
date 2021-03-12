"""
********************************************************
Filename:       problem1.py
Description:    Calculate whether 
Author:         Pei.L
Created On:     23/02/2021
********************************************************
"""
print("******Speed Limit Calculator******")

#ask user for side lengths
side1 = int(input("Side 1 Length: "))
side2 = int(input("Side 2 Length: "))
side3 = int(input("Side 3 Length: "))
print ("")

if ((side1+side2) > (side3)) and ((side1+side3) > side2) and ((side2+side3) > (side1)):
  print("A figure with lengths " + str(side1) + ", " + str(side2) + ", and " + str(side3) + " does form a triangle.")
else:
  print("A figure with lengths " + str(side1) + ", " + str(side2) + ", and " + str(side3) + " does NOT form a triangle.")