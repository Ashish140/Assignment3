#!/usr/bin/env python
# coding: utf-8

# In[1]:


def modfunct(a,b):
    try:
        Div = a // b
        print("Valid result :", Div)
    except:
        print ("Invalid denominator")

modfunct(6,3)
modfunct(4,0)


# In[2]:


class Countries:
    def __init__(self,con1,con2):
        self.con1 = con1
        self.con2 = con2
class Verbs:
    def __init__(self,v1,v2,):
        self.v1 = v1
        self.v2 = v2
        
class Obj:
    def __init__(self,o1,o2):
        self.o1 = o1
        self.o2 = o2
        
c = Countries ("Americans","Indians")            
v = Verbs("Play","Watch")
o = Obj("Baseball","Cricket")
print(c.con1 + ' ' +v.v1+ ' '+o.o1)
print(c.con1 + ' ' +v.v1+ ' '+o.o2)
print(c.con1 + ' ' +v.v2+ ' '+o.o1)
print(c.con1 + ' ' +v.v2+ ' '+o.o2)
print(c.con2 + ' ' +v.v1+ ' '+o.o1)
print(c.con2 + ' ' +v.v1+ ' '+o.o2)
print(c.con2 + ' ' +v.v2+ ' '+o.o1)
print(c.con2 + ' ' +v.v2+ ' '+o.o2)


# In[2]:


import numpy as np
l = np.array([1,2,3,4])
m = 4
np.vander(l,m)


# In[ ]:




