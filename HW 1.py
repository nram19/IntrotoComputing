#!/usr/bin/env python
# coding: utf-8

# In[1]:


colors = ['red', 'purple', 'yellow', 'black', 'white']
print(colors)


# In[4]:


nums = list(range(30, 63, 3))
print(nums)


# In[15]:


weather = {
    "Sunny": "play",
    "Rainy": "watching TV",
    "Cloudy": "walk"
}
print(weather)
weather.update({"snowy": "ski"})
print(weather)


# In[28]:


grade = 69
if grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
else:
    print('F')
    

