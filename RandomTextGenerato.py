#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 18:50:10 2022

@author: alessandro
"""


from random import randrange 
qcount=0
bcount=0
rcount=0

def Testindici(dizionario,parola,indici):
    contatore=0
    for elemento in dizionario:
        if(elemento[0]==parola):
            assert(elemento[0]==parola and contatore in indici),str(elemento[0])+str(contatore)
        contatore+=1
    print('Testindici Passed')


#Test per ordinamento dizionario l'assert blocca il codice nel momento in cui la k-esima parola del campo parola chiave 
# dell n-esimo elemento è maggiore della  k-esima parola del campo parola chiave dell'elemento in posizione n+1    
def TestSort(dizionario,k):
 for elemento in range(0,len(dizionario)-2):
    for x in range(0,k):
        assert(dizionario[elemento][0][x]<=dizionario[elemento+1][0][x]),str(dizionario[elemento][0][x])+" "+str(dizionario[elemento+1][0][x])
        if(dizionario[elemento][0][x]<dizionario[elemento+1][0][x]):break
 print('TestSort Passed')





def partition2(array,low,high):
    global qcount
    pivot=array[high]
    
    i=low-1
    for j in range(low,high):
        qcount+=1
      
        
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
with open('head2.1') as f:
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
    m=50
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
    quicksort(dizionario,0,len(dizionario)-1)
    TestSort(dizionario,k)
    ####stampa il dizionario
    #for a in dizionario:
        #print (a)
   
    for x in range(0,m-k):
        lista_indici=[]
        lista_indici=indici(dizionario,frase)
        #Testindici(dizionario,frase,lista_indici)
       
        
            
       
        ind=randrange(len(lista_indici))
        
        frase.append(dizionario[lista_indici[ind]][1])
        frase_output.append(dizionario[lista_indici[ind]][1])
        frase.pop(0)
    print(outputString(frase_output))
    
    print("qcount: "+str(qcount))
    print("bcount: "+str(bcount))
    print("rcount: "+str(rcount))    
    print('il dizionario contiene '+str(len(dizionario)))
    
   
    
  
  
  

    
