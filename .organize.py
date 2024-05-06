import os
import shutil

print(os.listdir(os.getcwd()))

dir  = os.getcwd()

pretty = "C:\\Users\\jaowe\\Documents\\Projects\\ELECTRONICS LIBRARY\\JO_LIB.pretty"

print(dir)
for folder in os.listdir(os.getcwd()):
    print(folder)