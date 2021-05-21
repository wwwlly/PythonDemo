# -*- coding: UTF-8 -*-
import os
import sys

encode_path = os.path.abspath("D:\libwebp-1.1.0-windows-x64\bin\cwebp.exe")
webp_path = os.path.abspath("G:\userPhotoWebp") # webp图片路径
png_path = os.path.abspath("G:\userPhoto") # png图片路径
  
def encode():
  "批量png转webp"
  if not os.path.exists(webp_path):
    os.mkdir(webp_path)
 
  for f in os.listdir(png_path):
    res_f = str(f).replace(".png", ".webp")
    #print str(f)
    #print res_f
    #print os.path.join(png_path, f)
    #print os.path.join(webp_path, res_f)
    cmd = "{0} {1} -o {2}".format("cwebp", os.path.join(png_path, f), os.path.join(webp_path, res_f))
    #print cmd
    os.system(cmd)
  return
#encode()

def rename(path):
  "批量改文件名"
  for f in os.listdir(path):
    if os.path.isfile(os.path.join(path, f)) == True:
	  new_name = str(f).replace("@2x", "")
	  print new_name
	  os.rename(os.path.join(path, f), os.path.join(path, new_name))
  return
rename(webp_path)