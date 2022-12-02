# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 06:08:25 2022

@author: Marie-Anne Melis
"""

import os   
import pandas as pd

os.chdir('D:/Studie/AdventOfCode/2022/day2')


filename = "day2.txt"

colnames=['draw']
raw_gamedata= pd.read_csv("day2.txt", names = colnames,  header=None)
raw_gamedata['draw'] = raw_gamedata['draw'].str.replace(" ", "")

#both represent card
myscore = 0
#2b second value is instruction
myinstructionscore = 0


dict_cards = {'AX': 4, 'AY': 8, 'AZ': 3 ,\
              'BX': 1, 'BY': 5, 'BZ': 9,\
              'CX': 7, 'CY': 2, 'CZ': 6}

#2b x=loose, y=draw, z=win

dict_instructions = {'AX': 3, 'AY': 4, 'AZ': 8 ,\
              'BX': 1, 'BY': 5, 'BZ': 9,\
              'CX': 2, 'CY': 6, 'CZ': 7}   
    
    

for index, row in raw_gamedata.iterrows():

    #point for draw
    myscore += dict_cards.get(row["draw"])
    #points for result
    myinstructionscore += dict_instructions.get(row["draw"])

    
print(myscore)
print(myinstructionscore)


 
        
