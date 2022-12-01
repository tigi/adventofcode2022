# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 06:08:25 2022

@author: Marie-Anne Melis
"""

import os   
import pandas as pd

os.chdir('D:/Studie/AdventOfCode/2022/day1')


filename = "input1.csv"
elf = 1
df = pd.DataFrame(columns=['elf','calories'])

with open(filename) as elves_data:
   for n, line in enumerate(elves_data, start=1):
       
        if line.rstrip('\n') == '':
            #next elve
            elf += 1
        else:
            new_row = pd.Series({'elf': elf, 'calories': int(line.rstrip('\n'))})
            df=pd.concat([df, new_row.to_frame().T], ignore_index=True)

#calories per elve

df_sum=df.groupby('elf').sum()

#1a - elve with most calories

max_elve = df_sum['calories'].max()
print(max_elve)

##1b - sum calories top 3 elves

sum_top_3 = df_sum.nlargest(3, columns='calories').sum()
print(sum_top_3)



 
        
