#!/usr/bin/env python
# coding: utf-8

# In[16]:


def digit_count(number):
    zeroCount=0
    evenCount=0
    oddCount=0
    strNum=str(number)
    strNumInt=strNum.split(".")[0]
    
    
    for i in strNumInt:
        if int(i)==0:
            zeroCount=zeroCount+1
        elif int(i)%2==0:
            evenCount=evenCount+1
        elif int(i)%2!=0:
            oddCount=oddCount+1
    tup=(zeroCount,evenCount,oddCount)
    print(tup)
    
digit_count(23045.76)


# In[ ]:





# In[ ]:




