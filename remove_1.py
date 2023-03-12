import os

current_dir = os.getcwd()#获取当前python文件所处 dirctory
removedfiles = []
for filename in os.listdir(current_dir): #循环当前路径内所有文件
    if os.path.isfile(filename) and os.path.getsize(filename) == 0 :
        os.remove(filename) #delete the file
        removedfiles.append(filename)

if removedfiles: 
    print(f"Removed file(s): {', '.join(removedfiles)}")