import os
import shutil
#os.mkdir("c:/Users/skyla/Downloads/Class99")
os.getcwd()
path="c:/Users/skyla/Downloads/Class99/Test.py"
isexists = os.path.exists(path)
print(isexists)
root = os.path.splitext(path)
print("rootpath",root[1])
list = os.listdir()
print(list)

source = "c:/Users/skyla/Downloads/Class99/TestFolder"
destination = "c:/Users/skyla/Downloads/Class99.5"
test = shutil.move(source,destination)
print("After copying the file: ")
print(os.listdir(path))

