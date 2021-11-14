#!/usr/bin/env python
# coding: utf-8

# In[12]:


print("there is a %5 discount on products due father's day")
print("additional %10 discount if the clinet is a member")
cost= float(input("enter the cost:"))
member=input("is the clinet a member?(yes/no):")
if member=="yes":
    cost= cost- (15/100)*cost
else:
    cost= cost- (5/100)*cost
print(cost)


# In[ ]:





# In[ ]:




