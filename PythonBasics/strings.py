#!/usr/bin/env python
# coding: utf-8

# In[4]:


lst = []
for i in range (0,10):
    lst.append(input())


# In[5]:


lst.sort()
print(lst)
lst.sort(reverse = True)
print(lst)


# In[10]:


print("Original Strings")
print(lst)
for i in range (0,10):
    lst[i] = lst[i][::-1]
print("Reverse Strings")
print(lst)


# In[ ]:




