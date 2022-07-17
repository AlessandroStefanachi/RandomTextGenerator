#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 19:02:57 2022

@author: alessandro
"""

import math
from random import randrange 
import pandas as pd
qcount=0
bcount=0
rcount=0

def Testindici(dizionario,parola,indici):
    contatore=0
    for elemento in dizionario:
        if(elemento[0]==parola):
            assert(elemento[0]==parola and contatore in indici),str(elemento[0])+str(contatore)
        contatore+=1

def TestSort(dizionario,k):
 for elemento in range(0,len(dizionario)-2):
    for x in range(0,k-1):
        assert(dizionario[elemento][0][x]<=dizionario[elemento+1][0][x]),str(dizionario[elemento][0][x])+" "+str(dizionario[elemento+1][0][x])
        if(dizionario[elemento][0][x]<dizionario[elemento+1][0][x]):break





def partition2(array,low,high):
    global qcount
    pivot=array[high]
    
    i=low-1
    for j in range(low,high):
        qcount+=1
      
        ##
        if(array[j]<pivot):
            i+=1
            swap=array[j]
            array[j]=array[i]
            array[i]=swap
    swap=array[i+1]
    array[i+1]=array[high]
    array[high]=swap
    return i+1


def quicksort( array,i, f):
    
    
    if(i>=f): return
    m=partition2(array,i,f)
    quicksort(array,i,m-1)
    quicksort(array,m+1,f)


def partition(array, i, f):
    global qcount
    
    
    pivot=array[i]
    inf=i
    sup=f+1
    swap=""
    while(1):
       
       while(1):
           inf+=1
           assert (inf<len(array)),"inf vale "+str(inf)+" e ha superato "+str(len(array))+" "+str(sup)
           qcount+=1
           if(array[inf]>pivot or inf==f):break
       while(1):
           sup-=1
           assert (sup<len(array)),"sup vale"+str(sup)+" e ha superato "+str(len(array))
           qcount+=1
           if(array[sup]<=pivot or sup==i):break
       if(inf<sup):
            swap=array[sup]
            array[sup]=array[inf]
            array[inf]=swap
       else: break
    swap=array[i]
    array[i]=array[sup]
    array[sup]=swap
    return sup



    
    
    
    
def ricerca_binaria(array,chiave,i,f):
    global bcount
    if(i>f): 
        return -1
    m=int((f+i)/2)
    if(array[m][0]==chiave):
        return m
    elif(array[m][0]>chiave):
        bcount+=1
        return ricerca_binaria(array,chiave,i,m-1)
    else:
        bcount+=1
        return ricerca_binaria(array,chiave,m+1,f)
    
def indici(array,chiave):
     global rcount
     indici=[]
     i=ricerca_binaria(array,chiave,0,len(array)-1)
     
     indici.append(i)
     inf=i-1
     sup=i+1
     rcount+=1
     while(inf>=0 or sup<len(array)):
     
         if(array[inf%len(array)][0]==chiave and inf>=0):
             rcount+=1
             indici.append(inf)
             inf-=1
         else: inf=-1
         if(array[sup%len(array)][0]==chiave and sup<len(array)):
             rcount+=1
             indici.append(sup)
             sup+=1
         else: sup=len(array)
     
     return indici




def outputString(output):
    frase=""
    for parola in output:
        frase=frase+" "+parola
    return frase

##########################################
#Funzione che riproduce il doubling experiment
def doubling():
    print('start Doubling Experiment')
    global bcount
    global rcount
    global qcount
    lenght=[]
    mcounter=0
    m_results=[[],[],[],[]]
    r_results=[[],[],[],[]]
    m_values=[100000,200000,400000]
    qn=[]
    for t in range(1,5):
        contents=[]
        with open('head2.'+str(t)) as f:
            contents = f.read()
            for char in '-.,\n':
                contents=contents.replace(char,' ')
            contents=contents.lower()
            parole=contents.split()
            k=1
            assert(k<len(parole)),"il numero di parole nel testo è troppo piccolo"
          
            contatore=0
            dizionario=[]
        #genera il dizionario il primo elemento del dizionario è a sua volta un'array contente k parole
        #il secondo elemento è il suffisso
        #il terzo elemento è un'indice associato alla posizione della prima parola presente in parola_chiave nel testo    
            for parola in parole:
                elemento=[]
                parola_chiave=[]
                parola_chiave.append(parole[contatore%len(parole)])
                for x in range(1,k):
                    parola_chiave.append(parole[(contatore+x)%len(parole)])
                elemento.append(parola_chiave)
                elemento.append(parole[(contatore+k)%len(parole)])
                elemento.append(contatore)
                dizionario.append(elemento)
                contatore+=1
                qcount=0
            quicksort(dizionario,0,len(dizionario)-1)
            #for a in dizionario:
               # print (a)
            
            
            for m in m_values:
                bcount=0
                rcount=0
                frase=[]
                frase_output=[]
                for x in range(k):
                    frase.append(parole[x])
                    frase_output.append(parole[x])
            
                for x in range(0,m-k):
                    lista_indici=[]
                    lista_indici=indici(dizionario,frase)
                    #for a in lista_indici:
                        #print(a)
                    
                        
                    
                    ind=randrange(len(lista_indici))
                    frase.append(dizionario[lista_indici[ind]][1])
                    frase_output.append(dizionario[lista_indici[ind]][1])
                    frase.pop(0)
                m_results[mcounter].append(bcount)
                r_results[mcounter].append(rcount) 
                
                print('finito file n '+str(t)+' con m= '+str(m))
            #print(outputString(frase_output))
    
            mcounter+=1
        qn.append(qcount/len(dizionario))
        lenght.append(len(dizionario))       
               
    
    Btable={
      'M/N':m_values,
      '10^5':m_results[0],
      '2x10^5':m_results[1],
      '4x10^5':m_results[2],
      '8x10^5':m_results[3]
      
      }
    b=pd.DataFrame(Btable)
    b.set_index('M/N')
    b.to_csv('./test/doubling/bcount',index=False)
    Rtable={
      'M/N':m_values,
      '10^5':r_results[0],
      '2x10^5':r_results[1],
      '4x10^5':r_results[2],
      '8x10^5':r_results[3]
      
      }
    r=pd.DataFrame(Rtable)
    r.set_index('M/N')
    r.to_csv('./test/doubling/rcount',index=False)
    Qtable={'n':lenght,
           'Qcount/n':qn
            }       
    q=pd.DataFrame(Qtable)
    q.to_csv('./test/doubling/qcount',index=False)
    print('Doubling experiment terminato')
    return b,r,q
###########
#Funzione per testare il modello
def model_comparison():
    m2=[]
    m2.extend(range(100,10100,100))
    global rcount
    global qcount
    global bcount
    datas=[[],[],[]]
    iteration=5
    m=1000
    lenght=[]
    qn=[]
    counter=0
    files=['hreal2','vreal2','creal2']
    for t in files:
        qcount=0
        contents=[]
        with open(t) as f:
            contents = f.read()
            for char in '-.,\n':
                contents=contents.replace(char,' ')
            contents=contents.lower()
            parole=contents.split()
            k=1
            assert(k<len(parole)),"il numero di parole nel testo è troppo piccolo"
            frase=[]
            frase_output=[]
            for x in range(k):
                frase.append(parole[x])
                frase_output.append(parole[x])
            
           
        #genera il dizionario il primo elemento del dizionario è a sua volta un'array contente k parole
        #il secondo elemento è il suffisso
        #il terzo elemento è un'indice associato alla posizione della prima parola presente in parola_chiave nel testo  
        m=1000
        #for it in range(iteration):
        for it in range(iteration):
            contatore=0
            dizionario=[]
            for parola in parole:
                elemento=[]
                parola_chiave=[]
                parola_chiave.append(parole[contatore%len(parole)])
                for x in range(1,k):
                    parola_chiave.append(parole[(contatore+x)%len(parole)])
                elemento.append(parola_chiave)
                elemento.append(parole[(contatore+k)%len(parole)])
                elemento.append(contatore)
                dizionario.append(elemento)
                contatore+=1
            qcount=0
            quicksort(dizionario,0,len(dizionario)-1)
            #for a in dizionario:
               # print (a)
            
            bcount=0
            rcount=0
            for x in range(0,m-k):
                   
                    lista_indici=[]
                    lista_indici=indici(dizionario,frase)
                    #for a in lista_indici:
                        #print(a)
                    
                        
                    
                    
                    ind=randrange(len(lista_indici))
                    
                    frase.append(dizionario[lista_indici[ind]][1])
                    frase_output.append(dizionario[lista_indici[ind]][1])
                    frase.pop(0)
            model_value=1.1918*len(dizionario)*math.log2(len(dizionario))+0.5369*m*math.log2(len(dizionario))+0.0031*m*len(dizionario)
            datas[counter].append((qcount+rcount+bcount)/(model_value))
            print('done '+str(t)+' with m '+str(m))
            m=m*2
            #print(outputString(frase_output))
            
            lenght.append(len(dizionario))
            qn.append(qcount/len(dizionario))
            #TestSort(dizionario)
            
        counter+=1
        
    plot={
      'parole':[1000,2000,4000,8000,16000],
      #'parole':m2,
      'h':datas[0],
      'c':datas[1],
      'v':datas[2]
      
      }    
    t=pd.DataFrame(plot)
    print('model test terminato')
    t.plot(x='parole',logx=True)
    t.to_csv('./test/model_test/model_real22',index=False)
    return t
##########
def ValuePlotter():
    global rcount
    global bcount
    global qcount
    rdatas=[[],[],[]]
    qdatas=[[],[],[]]
    bdatas=[[],[],[]]
    iteration=5
    m=1000
    lenght=[]
    qn=[]
    counter=0
    files=['hcorretto','vcorretto','ccorretto']
    for t in files:
        qcount=0
        contents=[]
        with open(t) as f:
            contents = f.read()
            for char in '-.,\n':
                contents=contents.replace(char,' ')
            contents=contents.lower()
            parole=contents.split()
            k=1
            assert(k<len(parole)),"il numero di parole nel testo è troppo piccolo"
            frase=[]
            frase_output=[]
            for x in range(k):
                frase.append(parole[x])
                frase_output.append(parole[x])
            
           
        #genera il dizionario il primo elemento del dizionario è a sua volta un'array contente k parole
        #il secondo elemento è il suffisso
        #il terzo elemento è un'indice associato alla posizione della prima parola presente in parola_chiave nel testo  
        m=1000
        for it in range(iteration):
            contatore=0
            dizionario=[]
            for parola in parole:
                elemento=[]
                parola_chiave=[]
                parola_chiave.append(parole[contatore%len(parole)])
                for x in range(1,k):
                    parola_chiave.append(parole[(contatore+x)%len(parole)])
                elemento.append(parola_chiave)
                elemento.append(parole[(contatore+k)%len(parole)])
                elemento.append(contatore)
                dizionario.append(elemento)
                contatore+=1
            qcount=0
            quicksort(dizionario,0,len(dizionario)-1)
            #for a in dizionario:
               # print (a)
            
            bcount=0
            rcount=0
            for x in range(0,m-k):
                   
                    lista_indici=[]
                    lista_indici=indici(dizionario,frase)
                    #for a in lista_indici:
                        #print(a)
                    
                        
                   
                    #ind=0 + round((rng(m)/m)*((len(lista_indici)-1)-0))
                    ind=randrange(len(lista_indici))
                    frase.append(dizionario[lista_indici[ind]][1])
                    frase_output.append(dizionario[lista_indici[ind]][1])
                    frase.pop(0)
                   
            rdatas[counter].append(rcount/(m*len(dizionario)))
            bdatas[counter].append(bcount/(m*math.log(len(dizionario),2)))
            qdatas[counter].append(qcount/(len(dizionario)*math.log(len(dizionario),2)))
            print('done '+str(t)+' with m '+str(m))
            m=m*2
            #print(outputString(frase_output))
            
            lenght.append(len(dizionario))
            qn.append(qcount/len(dizionario))
            #TestSort(dizionario)
            #for elemento in dizionario:
        counter+=1
        #    print(elemento)
    rplot={
      'parole':[1000,2000,4000,8000,16000],
      'h':rdatas[0],
      'c':rdatas[1],
      'v':rdatas[2]
      
      }    
    r=pd.DataFrame(rplot)
    r.plot(ylabel='rcount/mn',x='parole',logx=True)
    r.to_csv('./test/plot/rplot',index=False)
    
    qplot={
      'parole':[1000,2000,4000,8000,16000],
      'h':qdatas[0],
      'c':qdatas[1],
      'v':qdatas[2]
      
      }    
    q=pd.DataFrame(qplot)
    q.plot(ylabel='qcount/nlogn',x='parole',logx=True)
    q.to_csv('./test/plot/qplot',index=False)
    
    bplot={
      'parole':[1000,2000,4000,8000,16000],
      'h':bdatas[0],
      'c':bdatas[1],
      'v':bdatas[2]
      
      }    
    b=pd.DataFrame(bplot)
    b.plot(ylabel='bcount/mlogn',x='parole',logx=True)
    b.to_csv('./test/plot/bplot',index=False)
    
    return r,q,b
##########
########le funzioni doubling e ValuePlotter restituiscono 3 data frame accessibili da data[0],data[1] e data[2]
#i data frame sono consultabili direttamente dal variable explorer di spyder
data=model_comparison() 
#Bdata=data[0]
#Rdata=data[1]  
#Qdata=data[2]   
