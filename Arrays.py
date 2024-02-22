#!/usr/bin/env python
# coding: utf-8

# ## Quiz 1

# In[26]:


myExpenses = [
    ["January", 2200],
    ["Febuary", 2350],
    ["March", 2600],
    ["April", 2130],
    ["May", 2190],
]


# In[27]:


print(myExpenses[1][1] - myExpenses[0][1])


# In[28]:


expenses_firstquarter = 0
for index in range(3):
    expenses_firstquarter += myExpenses[index][1]
print(expenses_firstquarter)


# In[29]:


found = False
for expense in myExpenses:
    if expense[1] == 2000:
        found = True
        print(expense[0])
if not found:
    print("Not Found")


# In[35]:


myExpenses.append(["June", 1980])


# In[39]:


for expense in myExpenses:
    if expense[0] == "April":
        expense[1] -= 200
print(myExpenses)


# ## Quiz 2

# In[88]:


heros=['spider man','thor','hulk','iron man','captain america']


# In[89]:


print(len(heros))


# In[90]:


heros.insert(len(heros), 'black panther')
print(heros)


# In[91]:


heros.remove('black panther')
heros.insert(heros.index('hulk') + 1, 'black panther')
print(heros)


# In[92]:


dir(heros)


# In[93]:


heros.sort()
print(heros)


# In[94]:


heros[1:3] = ["doctor strange"]


# In[95]:


print(heros)


# ## Quiz 3

# In[107]:


numList = []
maxnum = int(input("Input a max number for you odd number list: "))
for num in range(0, maxnum):
    numList.append(num + 1)
print(numList)    
for i in numList:
    if i % 2 == 0:
        numList.remove(i)
print(numList)
    


# In[109]:


odd_numList = []
maxnum = int(input("Input a max number for you odd number list: "))
for i in range(1,maxnum + 1):
    if i % 2 == 1:
        odd_numList.append(i)
        
print(odd_numList)


# In[110]:


my_list = [1,2,3,4]
itr = iter(my_list)
for x in itr:
    print(x, end=" ")


# In[ ]:




