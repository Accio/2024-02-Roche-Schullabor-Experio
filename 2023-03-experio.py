#!/usr/bin/env python
# coding: utf-8

# # Experio

# ## Aufgabe 1: DNA, RNA, Protein

# In[1]:


dna = 'ATG'
rna = dna.replace('T', 'U')
print(rna)


# In[2]:


dna2 = 'ATGTTTAGGTGT'
rna2 = dna2.replace('T', 'U')
print(rna2)


# In[3]:


dna_liste = ['ATG', 'AGC', 'AGG', 'GAC', 'TGA']
rna_liste = []
for dna in dna_liste:
    rna = dna.replace('T', 'U')
    rna_liste.append(rna)
    
print(rna_liste)


# In[4]:


codes = {'AGC': 'S',
         'AGG': 'A',
         'AUG': 'M',
         'GAC': 'D',
         'UGA': '*'}
eiweiss = ''
for rna in rna_liste:
    aa = codes[rna]
    eiweiss = eiweiss + aa
print(eiweiss)


# In[5]:


patient_dna_liste = ['ATG', 'AGC', 'AGC', 'GAC', 'TGA']
patient_rna_liste = []
for patient_dna in patient_dna_liste:
    patient_rna = patient_dna.replace('T', 'U')
    patient_rna_liste.append(patient_rna)

print(patient_rna_liste)


# In[6]:


patient_eiweiss = ''
for patient_rna in patient_rna_liste:
    patient_aa = codes[patient_rna]
    patient_eiweiss = patient_eiweiss + patient_aa
print(patient_eiweiss)


# ## Aufgabe 2: PK

# In[7]:


import pandas as pd


# In[8]:


zeit = [0, 0.2, 0.4, 0.6, 
        0.8, 1, 1.4, 3.5, 
        5, 8, 9.5]
iv = [0.50, 0.43, 0.36, 0.27, 
      0.22, 0.19, 0.11, 0.02, 
      0.01, 0, 0]
pk_iv = pd.DataFrame({'Zeit': zeit, 'IV': iv})
print(pk_iv)


# In[9]:


import matplotlib.pyplot as plt


# In[10]:


pk_iv.plot.scatter(x="Zeit", y="IV")
plt.show()


# In[11]:


def iv_exp(t, k, C0):
    return C0 * np.exp(-k * t)


# In[12]:


import numpy as np
from scipy.optimize import curve_fit


# In[13]:


popt, pcov = curve_fit(iv_exp, zeit, iv)
xx = np.linspace(0, 10, 1000)
fit_val = iv_exp(xx, *popt)

plt.plot(xx, fit_val)
plt.plot(zeit, iv, 'bo')


# In[14]:


po = [0, 0.09, 0.15, 0.19,
      0.23, 0.24, 0.26, 0.15, 
      0.07, 0.04, 0.01]
pk_iv_po = pd.DataFrame({'Zeit': zeit, 'IV': iv, 'PO': po})
print(pk_iv_po)


# In[15]:


pk_iv_po.plot.scatter(x="Zeit", y="PO")
plt.show()


# ## Aufgabe 3: Studie

# In[16]:


gruppe = ['K', 'K', 'K', 'K', 'V1', 'V1', 'V1', 'V1', 'V2', 'V2', 'V2', 'V2']
vor = [8, 9, 8, 7, 6, 8, 8, 7, 8, 9, 8, 7]
nach = [8, 8, 7, 8, 5, 6, 8, 8, 4, 5, 3, 4]


# In[17]:


studie = pd.DataFrame({'Gruppe': gruppe, 'Vor': vor, 'Nach': nach})
print(studie)


# In[18]:


studie['Unterschied'] = studie['Nach'] - studie['Vor']
print(studie)


# In[19]:


studie.boxplot(column='Unterschied', by='Gruppe')


# In[20]:


studie.boxplot(column='Unterschied', by='Gruppe', grid=False)
plt.axhline(y=0, color='k', linestyle='--')


# In[21]:


studie.plot.scatter('Gruppe', 'Unterschied')
plt.axhline(y=0, color='k', linestyle='--')

