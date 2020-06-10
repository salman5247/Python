#!/usr/bin/env python
# coding: utf-8

# In[13]:


# create a list manually 

Students= ['Rahul','salman','vinood','ravi']


# In[14]:


print(Students)


# In[15]:


# to view the data type
type(Students)


# In[18]:


print(Students[0:3])


# In[19]:


Students.append('gagan')
print(Students)


# In[20]:


print(Students)
Students.insert(2,'Adil')
print(Students)


# In[21]:


#Delete the list element at index 2
del Students[2]
print(Students)


# In[22]:


#Automatically remove the last element
Students.pop()
print(Students)


# In[25]:


#to shift a list element to a variable 
y=Students.pop(1)
print(y)


# In[26]:


Students


# In[39]:


#Slicing of the list elements
New_students= ['Arjun','Salman','Daman','Mani']
print(New_students[0:4:2])


# In[42]:


# to make a list ranginging from 1-20 quickly at a difference of 3
a_list= list(range(1,20,3))
print(a_list)


# In[43]:


#to print number at even index
print(a_list[::2])


# In[44]:


unsorted_list=[2,5,7,2,9,12,77,131,29]


# In[45]:


sorted(unsorted_list)


# In[46]:


sorted_list=sorted(unsorted_list)


# In[47]:


sorted_list


# In[48]:


unsorted_list.sort()


# In[49]:


unsorted_list


# In[ ]:




