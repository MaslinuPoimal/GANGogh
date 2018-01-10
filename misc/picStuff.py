"""
A script designed to 1) resize all of the downloaded images to desired dimension (DEFAULT 64x64 pixels) and 2) rename images in folders from 1.png to n.png for ease of use in training
"""

import os
import scipy.misc
import random

root='/home/mykyta/DL4CVProject/images'

PATH = os.path.normpath('/home/mykyta/DL4CVProject/smallimages/')

blacklist = ['flower-painting', 'landscape']

for subdir, dirs, _ in os.walk(root):
    for style in dirs:
        if len(style) < 1:
            continue

        if style in blacklist:
            continue

        subfolder = PATH+'/'+style

        print('Writing to: '+subfolder)

        if not os.path.isdir(subfolder):
            print('creating subfolder '+subfolder)
            os.makedirs(subfolder)
        
        i = 0
        for _, _, files in os.walk(root+'/'+style):
            for source in files: 
                print(source)
                try:
                    image = scipy.misc.imread(root+'/'+style+'/'+source)
                    image = scipy.misc.imresize(image,(64,64))
                    scipy.misc.imsave(subfolder + '/' + str(i) + '.png',image)
                    i+=1
                except Exception:
                    print('missed image: ' + root+'/'+style+'/'+source)
