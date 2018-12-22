# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 21:14:01 2018

@author: Administrator
"""
from PIL import Image, ImageSequence

im=Image.open('test.gif')




if im.is_animated:
    frames = [f.copy() for f in ImageSequence.Iterator(im)]
    i=0
    for framei in frames:
        
        framei.save('fig/'+str(i)+'.png')
        i+=1
    

