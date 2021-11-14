#!/usr/bin/env python
# coding: utf-8

# In[21]:


#this program counts the vowels and consonants in an english sentence
def VCcounter(EngSentence):
    EngSentence=str(input("enter an english sentence:"))
    vowelCount=0
    consCount=0
    vowels=['i','a','u','e','o','A','U','E','O','I']
    spChar='!@#$%^&*_-~`.,></?|\/' # all special charecters

    for i in EngSentence:
        if i in vowels:
            vowelCount=vowelCount+1
        if i not in vowels:
            if i not in spChar:
                consCount=consCount+1


# In[11]:


type(spChar)


# In[ ]:





# In[ ]:




