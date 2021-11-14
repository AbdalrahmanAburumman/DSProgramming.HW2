#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("the password must be between 6-20 charecters and contains 1 upperclass 1 lower-class and a number at least")
password=input("password:")
upper=0
lower=0
num=0
lst=[1,2,3,4,5,6,7,8,9]

for i in password:
    if i.isupper():
        upper=upper+1
    if i.islower():
        lower=lower+1
    if i in lst:
        num=num+1
if len(password)<6 or len(password)>20:
    print("password is too short or too long")
if upper<1 or lower<1 or num<1:
    print("password is invalid")   
    
    


# In[ ]:





# In[ ]:




