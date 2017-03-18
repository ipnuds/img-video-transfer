import os
import shutil
import exifread
from PIL import Image
from PIL.ExifTags import TAGS
import datetime
import sys

# mmc_dir = r'E:'
# destination_dir = r'D:\Personal\test'

mmc_dir = sys.argv[1]
destination_dir = sys.argv[2]

def get_minimum_creation_time(exif_data):
    mtime = "?"
    if 306 in exif_data and exif_data[306] < mtime: # 306 = DateTime
        mtime = exif_data[306]
    if 36867 in exif_data and exif_data[36867] < mtime: # 36867 = DateTimeOriginal
        mtime = exif_data[36867]
    if 36868 in exif_data and exif_data[36868] < mtime: # 36868 = DateTimeDigitized
        mtime = exif_dcopy[36868]
    return mtime

for dirname, dirnames, filenames in os.walk(mmc_dir):
    for filename in filenames:
    	if os.path.splitext(filename)[1] == '.JPG':
    		try:
    			img = Image.open(r'%s\%s' %(dirname,filename))
    		except Exception, e:
    			print "Skipping '%s' due to exception: %s"%(filename, e)
    			continue
    		date_taken_with_time = get_minimum_creation_time(img._getexif())
    		only_date_taken = date_taken_with_time.split()[0].replace(":","-")
    		img_folder = destination_dir + "\\Images"+ "\\"+only_date_taken
    		if not os.path.exists(img_folder):
    			os.makedirs(img_folder)
    		shutil.copy(r'%s\%s' %(dirname,filename), img_folder)
    	if os.path.splitext(filename)[1] == '.MTS':
    		t = os.path.getmtime(r'%s\%s' %(dirname,filename))
    		t = datetime.datetime.fromtimestamp(t)
    		video_date =  str(t).split()[0]
    		video_folder = destination_dir+"\\Videos"+"\\"+ video_date
    		if not os.path.exists(video_folder):
    			os.makedirs(video_folder)
    		shutil.copy(r'%s\%s' %(dirname,filename), video_folder)