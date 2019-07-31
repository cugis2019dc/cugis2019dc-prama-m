# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 10:48:20 2019

@author: STEM
"""



def cadbury(a):
    cadbury = a+10
    
    print(cadbury)
    
cadbury(5)

def cadbury(c):
    cadbury = c**2+5*3
    
    print(cadbury)
cadbury(6)

def cadbury(a):
    cadbury = a+5
    
    print(cadbury)
cadbury(15)

def cadburyBox(a,b,c):
    cadburyBox = a+b+c
    
    print("There are",a,"milk chocolates,",b,"dark chocolates, and",c,
          "white chocolates in this cadbury box with",cadburyBox,"total chocolates.")

cadburyBox(45,13,22)


def cadburyBox(w,d,m):
    print("There is",w,",",d,", and",m,"in the Cadbury box.")
    
cadburyBox("White chocolatle", "Dark chocolate", "Milk chocolate")

cadbury1="dark chocolate"
cadbury2="white chocolate"
cadbury3="milk chocolate"

print("There is",cadbury1,",",cadbury2, ",and",cadbury3,"in the cadbury box.")

#write code to greet a person by their name

a = "Prama"
print("Hello,",a)

name = input("please enter your name")
print("Your name is",name)

print('Enter your age:')
x = input()
print('Your age is '+ x)


print("Your name is", name)

age = input("please entre your age")

print("Thank you. You entered ",age)

ageint = int(age)
ageint

#math calculations / math library
import math

dir(math)

math.pi

math.factorial(2)

math.pow(6,-1/2)

math.gcd(240,345)

#practice

def cubicRoot(a):
    print("The cubic root of", a, "is", math.pow(a,(1/3)))
    
cubicRoot(8)

import math

def cubic(g):
    cubic= math.pow(g, 1/3)
    
    print("The cubic root of", g, "is", cubic)

cubic(8)

import math

print("Please enter your value:")
v = input()
def cubic(v):
   cubic=math.pow(v,(1/3))
    
    
print("The cubic root of", v, "is", cubic)

    
















