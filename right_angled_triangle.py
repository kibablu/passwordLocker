#!/usr/bin/env python3 

import math
a = int(input("Enter first number"))
b = int(input("Enter second number"))
c = int(input("Enter third number"))

formula = math.sqrt(a ** 2 + b ** 2)

if c == formula:
    print("It is a right angled triangle")
else:
    print("try again")
