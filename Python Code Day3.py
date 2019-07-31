# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 10:29:28 2019

@author: STEM
"""

def cadburyBox(a,b,c):
    cadburyBox = a+b+c
    
    print("There are",a,"milk chocolates,",b,"dark chocolates, and",c,
          "white chocolates in this cadbury box with",cadburyBox,"total chocolates.")

cadburyBox(6,5,8)

cadbury1="Milk Chocolate"
cadbury2="Dark Chocolate"
cadbury3="White Chocolate"

Cadburymilk = 6
Cadburydark = 5
Cadburywhite = 8

print(cadbury1, "has" ,Cadburymilk, "," ,cadbury2, "has" ,Cadburydark, ",and" ,cadbury3, "has" ,Cadburywhite,)

#dict
chocolate1 = {"cadburymilk":5}
chocolate2 = {"cadburydark":8}
chocolate3 = {"cadburywhite":3}


print(chocolate1, chocolate2, chocolate3)

chocolatebox = {"cadburymilk":5,"cadburydark":8,"cadburywhite":3}

print(chocolatebox)

#pratice dict

students = {"steve is male":32, "lia is female":28, "vin is male":45, "katie is female":38}
print(students)

#list

studentlist =[["steve",32,"M"] , ["lia",28,"F"] , ["vin",45,"male"],["katie",38,"female"]]
print(studentlist)

student = [students, studentlist]
print(student)

#pandas

import pandas

dir(pandas)

studentdf = pandas.DataFrame(studentlist,columns=("name","age","gender"))
studentdf

chocolateboxlist = [["cadbury white",5], ["cadbury dark",8], ["cadbury milk",10]]
cadburyboxdf = pandas.DataFrame(chocolateboxlist,columns=("chocolate","quantity"))
cadburyboxdf

studentdf["name"]
studentdf["age"]
cadburyboxdf["quantity"]
cadburyboxdf["chocolate"]

#create a dataframe of student information 

newstudentlist =[["steve",52,"male"],["lia",28,"female"],["vin",45,"male"],["katie",38,"female"]]
newstudentlist

import pandas

dir(pandas)

studentlistdf=pandas.DataFrame(newstudentlist,columns=("Name","Age","Gender"),index=["Person 1","Person 2","Person 3","Person 4"])
studentlistdf

studentlistdf2 =pandas.DataFrame(newstudentlist,index=["1","2","3","4"])
studentlistdf2

import plotly
dir(plotly)

from plotly.offline import plot
import plotly.graph_objs as go

studentbar = go.Bar(x=studentdf["name"],y=studentdf["age"])
plot([studentbar])

import plotly
dir(plotly)

from plotly.offline import plot
import plotly.graph_objs as go

cadburyboxbar = go.Bar(x=cadburyboxdf["chocolate"],y=cadburyboxdf["quantity"])
plot([cadburyboxbar])

titles = go.Layout(title = "Number of Chocolates by Type")

cadburyboxbar=go.Bar(x=cadburyboxdf["chocolate"],y=cadburyboxdf["quantity"])

fig=go.Figure(data=[cadburyboxbar], layout=titles)
plot(fig)


