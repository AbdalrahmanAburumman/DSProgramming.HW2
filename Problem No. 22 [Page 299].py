#!/usr/bin/env python
# coding: utf-8

# In[16]:


def Sp(str1):  #SM:String permutations
    
    if len(str1)==1:
        return [str1]
    
    perm = Sp(str1[1:]) #recursive function call
    firstLetter = str1[0] 
    result=[] # empty list to fill it with the permutations
    
    for i in perm:
        for j in range(len(i)+1):
            result.append(i[j:]+firstLetter+i[:j])
    return result

strprem=input("enter 3 length string with curly brackets:") # the string that we want to permutate

if len(strprem)==5:
    fixedStr=strprem[1:-1] #the string after deleting the curly brackets
    fixedResult=Sp(fixedStr) # calling the function to compute the permutations

        
    print("{",fixedResult[0],",",fixedResult[1],",",fixedResult[2],",",fixedResult[3],",",fixedResult[4],",",fixedResult[5],"}")


else:
    print("the length is not 3")
    

    


# In[ ]:





# In[ ]:




