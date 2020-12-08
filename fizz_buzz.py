#!/usr/bin/env python3 

number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print("fizz-buzz")
elif number % 3 == 0:
    print("fizz")
elif number % 5 == 0:
    print("buzz")
else:
    print(number)
    

'''
Fizz buzz is a game in which the following rules apply
- any number which is divisible by 3 is replaced with fizz
- any number which is divisible by 5 is replaced with buzz
- any number which is divisible by both 3 and 5 is replaced with fizz-buzz
- any other number is just the number itself
'''
