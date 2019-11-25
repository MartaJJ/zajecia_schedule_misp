#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pulp import *

from ipywidgets import interact, interactive, fixed, interact_manual, Layout, FloatSlider, IntSlider
import ipywidgets as widgets
import pandas as pd


# In[2]:


pradMax = LpProblem("Prad max", pulp.LpMaximize)

prad_R1 = LpVariable('prad_R1', lowBound=0, cat='Continuous')
prad_R2 = LpVariable('prad_R2', lowBound=0, cat='Continuous')
prad_R3 = LpVariable('prad_R3', lowBound=0, cat='Continuous')
prad_R4 = LpVariable('prad_R4', lowBound=0, cat='Continuous')
prad_R5 = LpVariable('prad_R5', lowBound=0, cat='Continuous')

R1=8
R2=6
R3=4
R4=10
R5=8


# In[3]:


style = {'description_width': 'initial'}
prad_R1_slider = FloatSlider(min=0,max = 2, description="prad_R1", style= style )
prad_R2_slider = FloatSlider(min=0,max = 3, description="prad_R1", style= style )
prad_R3_slider = FloatSlider(min=0,max = 4, description="prad_R1", style= style )
prad_R4_slider = FloatSlider(min=0,max = 2, description="prad_R1", style= style )
prad_R5_slider = FloatSlider(min=0,max = 2, description="prad_R1", style= style )


# In[4]:


pradMax += prad_R3, "Z"

pradMax += prad_R1 <=2, "prad_R1"
pradMax += prad_R2 <=3, "prad_R2"
pradMax += prad_R3 <=4, "prad_R3"
pradMax += prad_R4 <=2, "prad_R4"
pradMax += prad_R5 <=2, "prad_R5"
pradMax += prad_R1*R1==prad_R2*R2, "prad_R1R2"
pradMax += prad_R4*R4==prad_R5*R5 , "prad_R4R5"
pradMax += prad_R3==prad_R4+prad_R5, "pradzik"
pradMax += prad_R3==prad_R1+prad_R2, "pp"

pradMax.solve()


# In[5]:


for variable in pradMax.variables():
    print("{} = {}".format(variable.name, variable.varValue))
print(pulp.value(pradMax.objective))


# In[6]:


print("""\nSensitivity Analysis\n
        Name\tConstraint\t\t\tShadow Price\t\tSlack""")
for name, c in pradMax.constraints.items():
    print(str(name).ljust(17), ":", str(c).ljust(33), str(c.pi).ljust(17), str(c.slack).ljust(10))


# In[7]:


prad_R1=prad_R1_slider,
prad_R2=prad_R2_slider,

