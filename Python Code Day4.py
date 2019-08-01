# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 10:11:17 2019

@author: STEM
"""

import pandas
dir(pandas)

import plotly
dir(plotly)

from plotly.offline import plot
import plotly.graph_objs as go

wodf = pandas.read_excel("GISdata.xlsx",sheet_name = "womenOccupation")

womenoccupation = go.Bar(x= wodf["occupation"], y=wodf["women"], marker = {"color": wodf
                        ["women"], "colorscale" : "Picnic"})
plot([womenoccupation])

titles = go.Layout(title = "Percentages of Women in Occupations", 
                   xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text="Occupation",)),
                   yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text="Percentage",)))
fig=go.Figure(data=[womenoccupation], layout=titles)
plot(fig)

plot([womenoccupation])

#cancer cases
import pandas
dir(pandas)

import plotly
dir(plotly)

from plotly.offline import plot
import plotly.graph_objs as go

wodf = pandas.read_excel("GISdata.xlsx",sheet_name = "cancercases")

cancercases = go.Bar(x= wodf["CancerType"], y=wodf["Number"], marker = {"color": wodf
                        ["Number"], "colorscale" : "Sunsetdark"})
plot([cancercases])

titles = go.Layout(title = "Number of Women Affected by Different Cancer Types in 2018", 
                   xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text="CancerType",)),
                   yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text="Number",)))
fig=go.Figure(data=[cancercases], layout=titles)
plot(fig)

plot([cancercases])
