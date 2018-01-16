# -*- coding: utf-8 -*-

"""
This script is to convert the txt annotation files to appropriate format needed by darknet
"""

print("Converting bboxes to VOC format")


import os
from os import walk, getcwd
from PIL import Image


""" Configure Paths"""

mypath = "E:/DATA/labels/"

outpath = "E:/DATA/labelsvoc/"

imagepath = "E:/DATA/Images/"

classes = ["bird", "human"]

if not os.path.isdir(outpath):
     os.mkdir(outpath)

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh

    return (x,y,w,h)


def get_cls_id(cls):
	if cls not in classes:
		exit(0)

	return classes.index(cls)


"""-------------------------------------------------------------------"""
#list_file = open('%s/list.txt'%(outpath), 'w')

""" Get input text file list """
txt_name_list = []

for (dirpath, dirnames, filenames) in walk(mypath):
    txt_name_list.extend(filenames)

    break

""" Process """
for txt_name in txt_name_list:
    """ Open input text files """
    txt_path = mypath + txt_name
    txt_file = open(txt_path, "r")
    lines = txt_file.read().split('\n')   #for ubuntu, use "\r\n" instead of "\n"

    """ Open output text files """
    txt_outpath = outpath + txt_name
    txt_outfile = open(txt_outpath, "w")

    """ Convert the data to YOLO format """
    ct = 0
    print txt_name
    for line in lines:

        elems = line.split(' ')
        if(len(elems) == 5):
            #print elems

            ct = ct + 1
            elems = line.split(' ')
            xmin = elems[0]
            xmax = elems[2]
            ymin = elems[1]
            ymax = elems[3]
            cls = elems[4]
            img_path = str('%s%s.tiff'%(imagepath, os.path.splitext(txt_name)[0]))
            im=Image.open(img_path)
            w= int(im.size[0])
            h= int(im.size[1])
            b = (float(xmin), float(xmax), float(ymin), float(ymax))
            bb = convert((w,h), b)

            txt_outfile.write(str(get_cls_id(cls)) + " " + " ".join([str(a) for a in bb]) + '\n')

    """ Save those images with bb into list"""
    #if(ct != 0):
        #list_file.write('%s%s.jpg\n'%(imagepath, os.path.splitext(txt_name)[0]))

#list_file.close()