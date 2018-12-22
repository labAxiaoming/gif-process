# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 21:14:01 2018

@author: Administrator
"""
from PIL import Image, ImageSequence
import os
#im=Image.open('test.gif')

files=os.listdir('fig/')


gif=[]
for file in files:
    gifi=Image.open('fig/'+file)
    gif.append(gifi)
#gif.save('gif.gif')
gif[0].save('gif.gif',save_all=True, append_images=gif[1:])

    

