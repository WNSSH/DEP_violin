#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 14:59:40 2018

@author: wangguanzhi
"""
import plotly
plotly.tools.set_credentials_file(username='guanzhi', api_key='afgF8dxssIOl22Foj0Ao')
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd
mydata=pd.read_csv("cleaned_data.csv")
pointposdep = [-0.9,-1.1,-0.6,-0.3]
pointposarr = [0.45,0.55,1,0.4]
showLegend = [True,False,False,False]
#mydata["dep_delay_min"].min()
mydata.columns.values.tolist()
temp=[199,1056,1409,1609,2305,4064,4921,5274,5474,6170,7929,8786,9139,9339,10035]
for i in temp:
    mydata["dep_delay_min"][i]=mydata["arr_delay_min"][i]=0
mydata["rank"]=1
for j in range(len(mydata)):
    if mydata['filed_departuretime_week'][j]=="Mon":
        mydata["rank"][j]=1
    elif mydata['filed_departuretime_week'][j]=="Tue":
        mydata["rank"][j]=2
    elif mydata['filed_departuretime_week'][j]=="Wed":
        mydata["rank"][j]=3
    elif mydata['filed_departuretime_week'][j]=="Thu":
        mydata["rank"][j]=4
    elif mydata['filed_departuretime_week'][j]=="Fri":
        mydata["rank"][j]=5
    elif mydata['filed_departuretime_week'][j]=="Sat":
        mydata["rank"][j]=6
    elif mydata['filed_departuretime_week'][j]=="Sun":
        mydata["rank"][j]=7
mydata=mydata.sort_values('rank')
    
        
data2 = []
'''
for i in range(0,len(pd.unique(df['filed_departuretime_week']))):
    dep = {
            "type": 'violin',
            "x": mydata['filed_departuretime_week'][ (mydata['dep_delay_sig'] == 'True')],
            "y": mydata['dep_delay_min'][ (mydata['dep_delay_sig'] == 'True')] ,
            
'''
for i in range(0,len(pd.unique(mydata['filed_departuretime_week']))):
    trace = {
            "type": 'violin',
            "x": mydata['filed_departuretime_week'][mydata['filed_departuretime_week'] == pd.unique(mydata['filed_departuretime_week'])[i]],
            "y": mydata['dep_delay_min'][mydata['filed_departuretime_week'] == pd.unique(mydata['filed_departuretime_week'])[i]],
            "name": pd.unique(mydata['filed_departuretime_week'])[i],
            "box": {
                "visible": True
            },
            "meanline": {
                "visible": True
            }
        }
    data2.append(trace)

        
fig = {
    "data": data2,
    "layout" : {
        "title": "Departure delay distribution",
        "yaxis": {
            "zeroline": False,
        }
    }
}

py.iplot(fig, filename='violin_dep_updated', validate = False)