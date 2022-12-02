# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 06:08:25 2022

@author: Marie-Anne Melis
"""

import os   
import pandas as pd

os.chdir('D:/Studie/AdventOfCode/2022/day2')


filename = "day2.txt"

colnames=['opponent','instruction']
raw_gamedata= pd.read_csv("day2.txt", names = colnames,  header=None,  sep=' ')

myscore = 0

#my horribly inefficient code part 2

def pointsforresult(instruction):
    points=0
    if instruction == "Y":
        points = 3
    elif instruction == "Z":
        points=6
    
    return points



def whichcard (data):
    cardvalue = 0
    
    if (data["opponent"] == "A" and data["instruction"] == "X"):
        cardvalue=3
    elif data["opponent"] == "A" and data["instruction"] == "Y":
        cardvalue=1
    elif data["opponent"] == "A" and data["instruction"] == "Z":
        cardvalue=2
        
    if (data["opponent"] == "B" and data["instruction"] == "X"):
        cardvalue=1
    elif data["opponent"] == "B" and data["instruction"] == "Y":
        cardvalue=2
    elif data["opponent"] == "B" and data["instruction"] == "Z":
        cardvalue=3
        
    if (data["opponent"] == "C" and data["instruction"] == "X"):
        cardvalue=2
    elif data["opponent"] == "C" and data["instruction"] == "Y":
        cardvalue=3
    elif data["opponent"] == "C" and data["instruction"] == "Z":
        cardvalue=1
    
    
    return cardvalue

#x is loose, y is draw, z = win

for index, row in raw_gamedata.iterrows():

    #point for card
    myscore += whichcard(row)
    #points for result
    myscore += pointsforresult(row["instruction"])
    
print(myscore)


 
        
