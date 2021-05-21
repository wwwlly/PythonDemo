# -*- coding: UTF-8 -*-
import os
import sys

encode_path = os.path.abspath("D:\libwebp-1.1.0-windows-x64\bin\cwebp.exe")
webp_path = os.path.abspath("G:\GitRepository\PythonDemo\webp") # webp图片路径
png_path = os.path.abspath("G:\GitRepository\PythonDemo\png") # png图片路径
  
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
encode()