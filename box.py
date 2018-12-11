#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 14:40:21 2018

@author: wangguanzhi
"""

import plotly
plotly.tools.set_credentials_file(username='guanzhi', api_key='afgF8dxssIOl22Foj0Ao')
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd
mydata=pd.read_csv("cleaned_data.csv")
print(mydata[3:4])
#pointposdep = [-0.9,-1.1,-0.6,-0.3]
#pointposarr = [0.45,0.55,1,0.4]
#showLegend = [True,False,False,False]
#mydata["dep_delay_min"].min()
#print(mydata["aircraft_manuf"][3])
temp=[199,1056,1409,1609,2305,4064,4921,5274,5474,6170,7929,8786,9139,9339,10035]
for i in temp:
    mydata["dep_delay_min"][i]=mydata["arr_delay_min"][i]=0
un=[]    
for j in range(0,11595):
    if mydata['aircraft_manuf'][j]=="unkown":
        un.append(j)
print(un)
for k in un:
    mydata["aircraft_manuf"][k]="Other"
    
data = [
    {
        'x': mydata["dep_delay_min"],
        'y': mydata["aircraft_manuf"],
        'name':'DEP',
        'marker': {
            'color': '#3D9970'
        },
        'boxmean': False,
        'orientation': 'h',
        "type": "box",
    },
    {
        'x': mydata["arr_delay_min"],
        'y': mydata["aircraft_manuf"],
        'name': 'ARR',
        'marker':{
            'color': '#FF4136',
        },
        'boxmean': False,
        'orientation': 'h',
        "type": "box",
    }   
]
layout = {
    'xaxis': {
        'title': 'Delay_min',
        'zeroline': False,
    },
    'boxmode': 'group',
}
fig1 = go.Figure(data=data, layout=layout)


py.iplot(fig1, filename = 'box_grouped', validate = False)