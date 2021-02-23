# ICS2O1 LiveHack 2

## Instructions
For each of the described problems:
* Complete a flowchart for each described problem (see Google Classroom post)
* Write a python solution to the problem in the appropriate file
* Use proper variable naming
* Use appropriate commenting and include a program header
* Make input and output user friendly.


### Running your code
You can enter the following in the terminal to run your code:  
`python3 problem1.py`  
`python3 problem2.py`  


## Problem 1
Many communities now have “radar” signs that tell drivers what their speed is, in the hope that they will slow down.  You will output a message for a “radar” sign. 
  
The message will display information to a driver based on their speed according to the following table:

| km/h over the speed limit  | Fine  |
|---|---|
| 1 to 20   | $100  |
| 21 to 30  | $270  |
| 31 or above  | $570  |

In addition to the fines above, if the driver is speeding in a construction zone, the fines will be doubled.

#### Input Specification
The user will be prompted for 2 integers:
1. The speed limit
2. The recorded speed of the driver


#### Output specification
If the driver is not speeding, the output should be: `Congratulations, you are within the speed limit!`  
If the driver is speeding, the output should be: `You are speeding and your fine is $F`. where F is the amount of the fine as described in the table above,


#### Sample Run 1  
```
Enter the speed limit: 40 
Enter the recorded speed of the car: 39
Congratulations, you are within the speed limit! 
```

#### Sample Run 2
```
Enter the speed limit: 100 
Enter the recorded speed of the car: 131 
You are speeding and your fine is $570. 
```

#### Sample Run 3 
```
Enter the speed limit: 100 
Enter the recorded speed of the car: 120 
You are speeding and your fine is $100.
```

## Problem 2
Three numbers represent the sides of a triangle when the sum of any two sides is greater than the third side. For example, 3, 4, and 5 are the sides of a triangle because the sum of any pair of sides is bigger than the third side. But 12, 3, and 8 are not sides of a triangle because 3 + 8 = 11 is not greater than 12. 

Write a program to have the user enter three lengths of sides and determine whether the figure is a triangle or not. Do not assume that the side lengths are entered in any particular order.

#### Sample Run 1
```
Welcome to the Triangle Checker
Enter the length of the first side: 3
Enter the length of the second side: 4
Enter the length of the third side: 5
The figure is a triangle.
```

#### Sample Run 2  
```
Welcome to the Triangle Checker
Enter the length of the first side: 12
Enter the length of the second side: 3
Enter the length of the third side: 8
The figure is NOT a triangle
```







