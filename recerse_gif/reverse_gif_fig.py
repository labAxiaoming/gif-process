# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 21:14:01 2018

@author: Administrator
"""
from PIL import Image, ImageSequence

im=Image.open('test.gif')
if im.is_animated:
    frames = [f.copy() for f in ImageSequence.Iterator(im)]
    
    frames.reverse()
    
    frames[0].save('reverse'+'.gif',save_all=True, append_images=frames[1:])
    
    

