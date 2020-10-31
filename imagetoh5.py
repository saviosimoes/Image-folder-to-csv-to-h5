#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 23:06:51 2020

@author: savio
"""

import cv2
import datetime as dt
import h5py
import matplotlib.pyplot as plt
import matplotlib.pylab as plb
import numpy as np
import os
import pandas as pd
from glob import glob

def proc_images():
    """
    Saves compressed, resized images as HDF5 datsets
    Returns
        data.h5, where each dataset is an image or class label
        e.g. X23,y23 = image and corresponding class label
    """
    start = dt.datetime.now()
    # ../input/
    PATH = os.path.abspath(os.path.join('/home/savio/Desktop/final project/224by224product', 'test inputs'))
    # ../input/sample/images/
    SOURCE_IMAGES = os.path.join(PATH, "sample", "images")
    # ../input/sample/images/*.png
    images = glob(os.path.join(SOURCE_IMAGES, "*.jpg"))
    # Load labels
    labels = pd.read_csv('combined_csv.csv')
       
    # Set the disease type you want to look for
    #disease="Infiltration"
    
    # Size of data
    NUM_IMAGES = len(images)
    HEIGHT = 256
    WIDTH = 256
    CHANNELS = 3
    SHAPE = (HEIGHT, WIDTH, CHANNELS)
    
    with h5py.File('test_data.h5', 'w') as hf: 
        for i,img in enumerate(images):            
            # Images
            image = cv2.imread(img)
            image = cv2.resize(image, (WIDTH,HEIGHT), interpolation=cv2.INTER_CUBIC)
            Xset = hf.create_dataset(
                name='X'+str(i),
                data=image,
                shape=(HEIGHT, WIDTH, CHANNELS),
                maxshape=(HEIGHT, WIDTH, CHANNELS),
                compression="gzip",
                compression_opts=9)
            # Labels
            base = os.path.basename(img)
            finding = labels["Finding Labels"][labels["Image Index"] == base].values[0]
            yset = hf.create_dataset(
                name='y'+str(i),
                shape=(1,),
                maxshape=(None,),
                compression="gzip",
                compression_opts=9)
            end=dt.datetime.now()
            print("\r", i, ": ", (end-start).seconds, "seconds", end="")
            
print(proc_images())            