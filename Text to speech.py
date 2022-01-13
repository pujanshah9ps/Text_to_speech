#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pyttsx3


# In[1]:


import pyttsx3

frnd = pyttsx3.init()
speech = input("say something!!")
frnd.say(speech)
frnd.runAndWait()

