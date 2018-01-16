# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 13:29:31 2018

@author: Bart
"""

import glob, os

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Directory where the data will reside, relative to 'darknet.exe'
path_data = "E:\DATA\Images"

# Percentage of images to be used for the test set
percentage_test = 20;

files = glob.iglob(os.path.join(path_data, "*.txt"))

# Create and/or truncate train.txt and test.txt
file_train = open(os.path.join(path_data,'train.txt'), 'w')
file_test = open(os.path.join(path_data,'test.txt'), 'w')

# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage_test)

for pathAndFilename in files:
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    if counter == index_test:
        counter = 1
        file_test.write(path_data + title + '.tiff' + "\n")
    else:
        file_train.write(path_data + title + '.tiff' + "\n")
        counter = counter + 1