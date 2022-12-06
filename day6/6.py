# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 06:08:25 2022

@author: Marie-Anne Melis
"""

import os   

os.chdir('D:/Studie/AdventOfCode/2022/day6')


filename = "input.txt"
string_list = []

with open(filename, 'r', encoding='utf-8') as file:
    while True:
        char = file.read(1)
        string_list.append(char)
        if not char:
            break


        
#first assignment was chunck size 4       
chunk_size = 14
for i in range(0, len(string_list)):
        chunk = string_list[i:i+chunk_size]
        #check chunk on different chars, if true, num char processed is i + chunk_size
        if len(set(chunk)) == chunk_size:
           print("different",chunk, "num chars", i+chunk_size)
           break
            

