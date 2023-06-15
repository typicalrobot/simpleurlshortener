#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pyshorteners


# In[3]:


import pyshorteners


# In[7]:


long_url = input("Please enter URL to shorten: ")


# In[5]:


type_tiny = pyshorteners.Shortener()


# In[8]:


short_url = type_tiny.tinyurl.short(long_url)
 
print("The Shortened URL is: " + short_url)

