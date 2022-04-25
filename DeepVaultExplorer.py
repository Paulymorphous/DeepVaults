#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from glob import glob
import cv2
from random import shuffle, choice

image_dir = "C:\\Users\\Paulymorphous\\Pictures\\Clicks\\"


# In[2]:


file_names = []
for path, subdirs, files in os.walk(image_dir):
    for name in files:
        file_names.append(name)
shuffle(file_names)


# In[9]:


prev_image = None 
while True:
    cv2.namedWindow("DeepVault Explorer", cv2.WINDOW_AUTOSIZE)
    
    file_name = choice(file_names)
    image = cv2.imread(image_dir + file_name)
    image = cv2.resize(image, (1920, 1080))
    cv2.imshow('DeepVault Explorer', image)
  
    
    key_press = cv2.waitKey(0)
    if key_press == ord('q'):
        print("Q pressed, Exiting.")
        break
    
    
        
    
cv2.destroyAllWindows()

