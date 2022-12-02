# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 06:08:25 2022

@author: Marie-Anne Melis
"""

import os   
import pandas as pd

os.chdir('D:/Studie/AdventOfCode/2022/day2')


filename = "day2.txt"

colnames=['opponent','me']
raw_gamedata= pd.read_csv("day2.txt", names = colnames,  header=None,  sep=' ')

myscore = 0


def drawpoints(x):
    value = 0
    if x == "X": 
        value = 1
    elif x == "Y":
        value=2
    elif x=="Z":
        value=3
        
    return value

#my horribly inefficient code part 1

def pointsforresult(data):
    points=0
    #gelijkspel
    if (data["opponent"] == "A" and data["me"] == "X") or \
        (data["opponent"] == "B" and data["me"] == "Y") or \
            (data["opponent"] == "C" and data["me"] == "Z"):
                points = 3
    if (data["opponent"] == "A" and data["me"] == "Z") or \
        (data["opponent"] == "C" and data["me"] == "Y") or \
            (data["opponent"] == "B" and data["me"] == "X"):
                points = 0
    if (data["opponent"] == "C" and data["me"] == "X") or \
        (data["opponent"] == "B" and data["me"] == "Z") or \
            (data["opponent"] == "A" and data["me"] == "Y"):
                points = 6


    
    return points



for index, row in raw_gamedata.iterrows():
    print(row["me"])
    #point for draw
    myscore += drawpoints(row["me"])
    #points for result
    myscore += pointsforresult(row)
    
print(myscore)


 
        
