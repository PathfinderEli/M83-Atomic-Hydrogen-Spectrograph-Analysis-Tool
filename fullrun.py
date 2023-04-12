import subprocess
import os

dirs = ["M83-1","M83-2","M83-3","M83-4","M83-6","M83-7","M83-8","M83-9","M83-10","M83-11","M83-12","M83-13","M83-14","M83-15","M83-16","M83-POS1","M83-POS2"]

home = os.getcwd()

for i in range(len(dirs)):
    os.chdir(dirs[i])
    subprocess.call(['python', "VoigtFit_"+dirs[i]+".py"])
    os.chdir(home)