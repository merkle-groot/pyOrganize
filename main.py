import os
folders=["Videos","Images","Documents","Apps","Zip Files"]
path="/home/nardog/Downloads/"
if not os.path.exists(path+"log.txt"):
    with open(path+"log.txt",'w') as file:
        for i in range(len(folders)):
            os.mkdir(path+folders[i])
        file.write("Initialised Folders")
        