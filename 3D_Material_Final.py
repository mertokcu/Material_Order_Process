#!/usr/bin/env python
# coding: utf-8

#Importing the required packages


import pandas as pd 
import math 


# reading the Data 


orders = pd.read_csv("ordersTest.csv")

#calculate due week

orders["dueBy"] = pd.to_datetime(orders["dueBy"]) #seems unnecessary but still did it
orders["dueWeek"] = orders["dueBy"].dt.strftime('%Y_W%V')

#create list of unique materials and weeks

unique_materials = orders["material"].unique().tolist()
unique_weeks = orders["dueWeek"].unique().tolist()

#create empty template material data frame

material_df = pd.DataFrame({'material': unique_materials, 'volume': 0})
material_df = material_df.set_index("material")

#create a empty dictionary to store weekly material volume table 

d = {}
for i in unique_weeks:
    d[i] = material_df.copy()

#created shape functions

def calculateVolumeCube(side):
    return side**3

def calculateVolumeCuboid(side1,side2,side3):
    return side1 * side2 * side3 

def calculateVolumeSphere(radius):
    return (4 * math.pi * (radius**3)/3)
    
def calculateVolumeCylinder(side,radius):
    return math.pi * (radius**2) * side

def calculateVolumeCone(side,radius):
    return (math.pi * (radius**2) * side) / 3 

#process each order to add volumes to material table 

for i in orders.index:

    current_week = orders.loc[i,"dueWeek"]

    current_shape = orders.loc[i,"shape"]

    current_material = orders.loc[i,"material"]

    current_amount = orders.loc[i,"amount"]

    if current_shape == "cube":
        current_volume = calculateVolumeCube(orders.loc[i,"side1"])

    elif current_shape == "cuboid":
        current_volume = calculateVolumeCuboid(orders.loc[i,"side1"],orders.loc[i,"side2"],orders.loc[i,"side3"])

    elif current_shape == "sphere":
        current_volume = calculateVolumeSphere(orders.loc[i,"radius"])

    elif current_shape == "cylinder":
        current_volume = calculateVolumeCylinder(orders.loc[i,"side1"],orders.loc[i,"radius"])

    elif current_shape == "cone":
        current_volume = calculateVolumeCone(orders.loc[i,"side1"],orders.loc[i,"radius"])

    current_volume = current_volume * current_amount 

    d[current_week].loc[current_material,"volume"] += current_volume

#created a csv file for each week

for week in unique_weeks:
    d[week].sort_index().to_csv("material_" + week + ".csv")