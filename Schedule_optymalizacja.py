#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pulp import *
import pandas as pd
import numpy as np


# In[2]:


godziny = LpProblem("Najtaniej praca",LpMinimize)
mIgor=pulp.LpVariable("mIgor",lowBound=0,upBound=4,cat='Integer')
tIgor=pulp.LpVariable("tIgor",lowBound=0,upBound=4,cat='Integer')
wIgor=pulp.LpVariable("wIgor",lowBound=1,upBound=4,cat='Integer')
tuIgor=pulp.LpVariable("tuIgor",lowBound=0,upBound=4,cat='Integer')
fIgor=pulp.LpVariable("fIgor",lowBound=0,upBound=4,cat='Integer')
saIgor=pulp.LpVariable("saIgor",lowBound=1,upBound=4,cat='Integer')
mMarcin=pulp.LpVariable("mMarcin",lowBound=0,upBound=4,cat='Integer')
tMarcin=pulp.LpVariable("tMarcin",lowBound=0,upBound=4,cat='Integer')
wMarcin=pulp.LpVariable("wMarcin",lowBound=1,upBound=4,cat='Integer')
tuMarcin=pulp.LpVariable("tuMarcin",lowBound=1,upBound=4,cat='Integer')
fMarcin=pulp.LpVariable("fMarcin",lowBound=0,upBound=4,cat='Integer')
saMarcin=pulp.LpVariable("saMarcin",lowBound=0,upBound=4,cat='Integer')
mFranus=pulp.LpVariable("mFranus",lowBound=0,upBound=3,cat='Integer')
tFranus=pulp.LpVariable("tFranus",lowBound=1,upBound=3,cat='Integer')
wFranus=pulp.LpVariable("wFranus",lowBound=0,upBound=3,cat='Integer')
tuFranus=pulp.LpVariable("tuFranus",lowBound=0,upBound=3,cat='Integer')
fFranus=pulp.LpVariable("fFranus",lowBound=0,upBound=3,cat='Integer')
saFranus=pulp.LpVariable("saFranus",lowBound=0,upBound=3,cat='Integer')
mPioter=pulp.LpVariable("mPioter",lowBound=1,upBound=8,cat='Integer')
tPioter=pulp.LpVariable("tPioter",lowBound=0,upBound=8,cat='Integer')
wPioter=pulp.LpVariable("wPioter",lowBound=0,upBound=8,cat='Integer')
tuPioter=pulp.LpVariable("tuPioter",lowBound=0,upBound=8,cat='Integer')
fPioter=pulp.LpVariable("fPioter",lowBound=0,upBound=8,cat='Integer')
saPioter=pulp.LpVariable("saPioter",lowBound=0,upBound=8,cat='Integer')
mAnia=pulp.LpVariable("mAnia",lowBound=1,upBound=10,cat='Integer')
tAnia=pulp.LpVariable("tAnia",lowBound=0,upBound=10,cat='Integer')
wAnia=pulp.LpVariable("wAnia",lowBound=0,upBound=10,cat='Integer')
tuAnia=pulp.LpVariable("tuAnia",lowBound=0,upBound=10,cat='Integer')
fAnia=pulp.LpVariable("fAnia",lowBound=1,upBound=10,cat='Integer')
saAnia=pulp.LpVariable("saAnia",lowBound=0,upBound=10,cat='Integer')
mZuzia=pulp.LpVariable("mZuzia",lowBound=1,upBound=5,cat='Integer')
tZuzia=pulp.LpVariable("tZuzia",lowBound=0,upBound=5,cat='Integer')
wZuzia=pulp.LpVariable("wZuzia",lowBound=0,upBound=5,cat='Integer')
tuZuzia=pulp.LpVariable("tuZuzia",lowBound=0,upBound=5,cat='Integer')
fZuzia=pulp.LpVariable("fZuzia",lowBound=0,upBound=5,cat='Integer')
saZuzia=pulp.LpVariable("saZuzia",lowBound=0,upBound=5,cat='Integer')


# In[3]:


godziny += (mIgor+tIgor+wIgor+tuIgor+fIgor+saIgor)*170+(mMarcin+tMarcin+wMarcin+tuMarcin+fMarcin+saMarcin)*60+(mFranus+tFranus+wFranus+tuFranus+fFranus+saFranus)*80 +(mPioter+tPioter+wPioter+tuPioter+fPioter+saPioter)*200+(mAnia+tAnia+wAnia+tuAnia+fAnia+saAnia)*90 +(mZuzia+tZuzia+wZuzia+tuZuzia+fZuzia+saZuzia)*70 

godziny +=(mIgor+tIgor+wIgor+tuIgor+fIgor+saIgor)+ (mMarcin+tMarcin+wMarcin+tuMarcin+fMarcin+saMarcin)+(mFranus+tFranus+wFranus+tuFranus+fFranus+saFranus) +(mPioter+tPioter+wPioter+tuPioter+fPioter+saPioter)+(mAnia+tAnia+wAnia+tuAnia+fAnia+saAnia) + (mZuzia+tZuzia+wZuzia+tuZuzia+fZuzia+saZuzia)==30
godziny+= mIgor+tIgor+wIgor+tuIgor+fIgor+saIgor <=4 
godziny+= mMarcin+tMarcin+wMarcin+tuMarcin+fMarcin+saMarcin <=4 
godziny += mFranus+tFranus+wFranus+tuFranus+fFranus+saFranus <=3 
godziny += mPioter+tPioter+wPioter+tuPioter+fPioter+saPioter <=8 
godziny += mAnia+tAnia+wAnia+tuAnia+fAnia+saAnia <=10 
godziny += mZuzia+tZuzia+wZuzia+tuZuzia+fZuzia+saZuzia <=5 
godziny += mIgor + mMarcin + mFranus + mPioter + mAnia + mZuzia <=8
godziny += tIgor + tMarcin + tFranus + tPioter + tAnia + tZuzia <=4
godziny += wIgor + wMarcin + wFranus + wPioter + wAnia + wZuzia <=4
godziny += tuIgor + tuMarcin + tuFranus + tuPioter + tuAnia + tuZuzia <=4
godziny += fIgor + fMarcin + fFranus + fPioter + fAnia + fZuzia <=8
godziny += saIgor + saMarcin + saFranus + saPioter + saAnia + saZuzia <=2

godziny.solve()


# In[4]:


tablicaM=[]
tablicaT=[]
tablicaW=[]
tablicaTu=[]
tablicaF=[]
tablicaSa=[]


# In[5]:


print("-------Schedule-------")
for variable in godziny.variables():
    #print ("{} = {}".format(variable.name,variable.varValue))
    wartosc=variable.varValue
    imie=variable.name
    
    if(imie.startswith("m")== 1):
        tablicaM.append(wartosc)
    elif(imie.startswith("t")== 1 and imie.startswith("tu")== 0):
        tablicaT.append(wartosc)        
    elif(imie.startswith("w")== 1):
        tablicaW.append(wartosc)        
    elif(imie.startswith("tu")== 1):
        tablicaTu.append(wartosc)
    elif(imie.startswith("f")== 1):
        tablicaF.append(wartosc)        
    elif(imie.startswith("sa")== 1):
        tablicaSa.append(wartosc)
        


# In[6]:


print("           Ania Franus Igor Pioter Marcin Zuzia\nPoniedzieli: {} \nWtorek:      {}".format(tablicaM,tablicaT))
print("Środa:       {}\nCzwartek:    {}\nPiątek:      {}\nSobota:      {}".format(tablicaW,tablicaTu,tablicaF,tablicaSa))

