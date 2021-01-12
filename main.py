import PIL

from PIL import Image
import os

mywidth = 3024
source_dir = "/Users/Qaswar/Pictures/Test2 CHEM"
destination_dir = "/Users/Qaswar/Desktop/testpics"

def resize_pic(oldpic, newpic,mywidth):
    img = Image.open(oldpic)
    wpercent = (mywidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((mywidth, hsize), PIL.Image.ANTIALIAS)
    img.save(newpic)

def entire_directory(source_dir,dest_dir,width):
    files=os.listdir(source_dir)
    i = 0
    for file in files:
        i+=1
        old_pic = source_dir + "/" + file
        new_pic = dest_dir + "/" + file
        resize_pic(old_pic,new_pic,width)
        print(i,"done")
entire_directory(source_dir,destination_dir,mywidth)