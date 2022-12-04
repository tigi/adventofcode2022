# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 06:08:25 2022s

@author: Marie-Anne Melis
"""

import os   
import pandas as pd

os.chdir('D:/Studie/AdventOfCode/2022/day4')


filename = "input4.txt"

raw_cleanup= pd.read_csv(filename, delimiter=",", header=None)

def intersect_full(s1,e1,s2,e2):
    intersect = False
    #full intersect
    if s1 >= s2 and e1 <= e2 :
        intersect = True
    if s2 >= s1 and e2 <= e1 :
        intersect = True
        
    return intersect

def intersect_partly(s1,e1,s2,e2):
    intersect = False
    # partly intersect [s1,e1], [s2,e2]
    if s1 <= s2:
        if not e1 < s2 or s1 > e2:
            intersect = True
    else:
        if not e2 < s1 or s2 > e1:
            intersect = True               
    
    return intersect


count_intersect_full=0
count_intersect_partly = 0

for index, row in raw_cleanup.iterrows():
    #it's sunday, this could all be more efficient
    #not today, coffeetime
    elf_s1 = int(row[0].split("-")[0])
    elf_e1 = int(row[0].split("-")[1])
    elf_s2 = int(row[1].split("-")[0])
    elf_e2 = int(row[1].split("-")[1])

    #calculate full and partly intersect
    if (intersect_full(elf_s1,elf_e1,elf_s2,elf_e2)):
        count_intersect_full +=1
    if (intersect_partly(elf_s1,elf_e1,elf_s2,elf_e2)):
        count_intersect_partly +=1    
    
        

