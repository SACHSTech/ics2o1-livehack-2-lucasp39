"""
********************************************************
Filename:       problem1.py
Description:    Calculate speeding fines
Author:         Pei.L
Created On:     23/02/2021
********************************************************
"""
print("******Speed Limit Calculator******")

#ask user for speed limit and recorded speed
speed_limit = int(input("What is the speed limit?: "))
speed = int(input("How fast was your recorded speed?: "))
print("")

#fine prices 
fine_1_to_20 = 100
fine_21_to_30 = 270
fine_31_plus = 570

#print fines
speed_difference = speed - speed_limit
if speed_difference <= 0:
  print("Congratulations, you are within the speed limit!")
elif speed_difference >= 1 and speed_difference <= 20:
  print("You are speeding and your fine is $" +str(fine_1_to_20) + ".")
elif speed_difference >= 21 and speed_difference <= 30:
  print("You are speeding and your fine is $" +str(fine_21_to_30) + ".")
else:
  print("You are speeding and your fine is $" +str(fine_31_plus) + ".")