# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 06:08:25 2022s

@author: Marie-Anne Melis
"""

import os   
import pandas as pd

os.chdir('D:/Studie/AdventOfCode/2022/day3')


filename = "input3.txt"

raw_rucksack= pd.read_csv(filename,  header=None)



dict_alphabet = {'a': 1, 'b': 2, 'c': 3 ,\
              'd': 4, 'e': 5, 'f': 6,\
              'g': 7, 'h': 8, 'i': 9, \
              'j': 10, 'k': 11, 'l': 12 ,\
               'm': 13, 'n': 14, 'o': 15, 'p': 16,\
               'q': 17, 'r': 18, 's': 19,\
                  't': 20, 'u': 21, 'v': 22,\
                  'w': 23, 'x': 24, 'y': 25, \
                  'z': 26,\
 'A': 27, 'B': 28, 'C': 29 ,\
               'D': 30, 'E': 31, 'F': 32,\
               'G': 33, 'H': 34, 'I': 35, \
               'J': 36, 'K': 37, 'L': 38 ,\
                'M': 39, 'N': 40, 'O': 41, 'P': 42,\
                'Q': 43, 'R': 44, 'S': 45,\
                   'T': 46, 'U': 47, 'V': 48,\
                   'W': 49, 'X': 50, 'Y': 51, \
                   'Z': 52 }
                  

def split_halfway(string):
    return (string[:int(len(string) / 2)], string[int(len(string) / 2):])

#puzzle 1, corresponding values in 2 compartments rucksack = line input 
sumvalues=0    

for index, row in raw_rucksack.iterrows():

    #split rucksack contents
    stringhalves = split_halfway(row[0])
   
    #get common values and add corresponding integer from dict
    a=list(set(stringhalves[0])&set(stringhalves[1]))

    for i in a:
        sumvalues += dict_alphabet.get(i)
    
print(sumvalues)

#puzzle 2 corresponding values in 3 rucksacks is 3 lines

sumvalues2=0
        
t = raw_rucksack.iterrows()
for (i, row1), (j, row2), (k, row3) in zip(t, t, t):
        
   #get common values and add corresponding integer from dict
    a=list(set(row1[0])&set(row2[0])&set(row3[0]))

    for q in a:

        sumvalues2 += dict_alphabet.get(q)


print(sumvalues2)

 
        

