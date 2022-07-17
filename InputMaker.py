#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 00:21:24 2022

@author: alessandro
"""

import pandas as pd
import matplotlib
from random import randrange 
a=pd.read_csv(r'abcnews-date-text.csv') 
f=a['headline_text']
contatore=0
wordstart=0
word=''
lenghts=[['hreal2',112495],['vreal2',207423],['creal2',377452]]
startpoint=randrange(lenghts[2][1],2*lenghts[2][1])
#startpoint=0
print(len(f))
word=[]
l=0
for x in range(len(f)):

  for char in '-.,\n':
        contents=f[x].replace(char,' ')
  contents=contents.lower()
  z=contents.split()
  for h in range(len(z)):
      if(wordstart>startpoint):
          
          if(contatore==lenghts[l][1]):
              assert(len(word)==contatore)
              parola=''
              for b in range(contatore):
                  parola=parola+' '+word[b]
                  if(b%100==0):parola=parola+'\n'
              for char in '-.,\n':
                  contents2=parola.replace(char,' ')
              contents2=contents2.lower()
              parole=contents2.split()
              assert(len(parole)==lenghts[l][1]),len(parole)
              c=0
              for p in parole:c+=1
              print('parole '+str(c))
              file = open(lenghts[l][0], "w")
              file.write(parola)
              file.close()
              
              print('saved '+ str(lenghts[l][0])+' with '+str(contatore)+' words')
              contatore=0
              l+=1
              word=[]
              if(l==len(lenghts)):break
          else:
              word.append(z[h])
              contatore+=1
      else:wordstart+=1
  if(l==len(lenghts)):break
print('finish')