
#!/bin/python3

import math
import os
import random
import re
import sys



# First we have to take n as a integeras Input from user

n = int(input()) #n is input parameter

if n % 2 != 0 :                     #after n dividing by if it is ==0 then number is even
    print("Weird")                      #if not equal to zero then it is odd so (!= not                                             #equal to sign)
if n <=5 and n>=2 and n%2 ==0:
    print("Not Weird")

if n<=20 and n>=6 and n %2 ==0:      # hear we use logic
        print("Weird")               #  to excuate multiple conditions at onse conditions 

if n >= 20:
    print("Not Weird")
