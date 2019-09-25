import os
import sys
import time
import getpass
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

class eventHandler(PatternMatchingEventHandler):
    patterns="*"

    def sort(self):
        listF=os.listdir(pathDownloads+".Temp")
        print(listF)
        for file in listF:
            if file.endswith((".jpg",".png",".gif",".exif",".tiff",".bmp",".svg")):
                os.rename(pathDownloads+".Temp/"+file,pathDownloads+"Images/"+file)

            elif file.endswith((".mp4",".flv",".mkv",".webm",".avi",".wmv",".m4v",".svg")):
                os.rename(pathDownloads+".Temp/"+file,pathDownloads+"Videos/"+file)    

            elif file.endswith((".pdf",".csv",".json",".yml",".doc",".txt",".odt",".xlxs",".html",".xml")):
                os.rename(pathDownloads+".Temp/"+file,pathDownloads+"Documents/"+file)

            else:
                os.rename(pathDownloads+".Temp/"+file,pathDownloads+"Others/"+file)   


    def process(self,event):
        if event.src_path.endswith(".part",".cr"):
            filePath=event.src_path.replace(".part","") #Path of the actual file
            fileName=event.src_path.replace(pathDownloads,"") #Just the name of the original file
            fileOriginal=fileName.replace(".part","")
            print(fileName)
            while os.stat(filePath).st_size==0 or os.path.exists(event.src_path):
                print("Downloading......") 
                time.sleep(3)
            print("file downloaded")
            os.rename(pathDownloads+fileOriginal,pathDownloads+".Temp/"+fileOriginal)
            self.sort()

        elif not event.src_path.endswith(".part"):
            time.sleep(1)
            if not os.path.exists(event.src_path+".part"):
                print("smol file")
                fileName=event.src_path.replace(pathDownloads,"")
                print(fileName)
                os.rename(pathDownloads+fileName,pathDownloads+".Temp/"+fileName)
                self.sort()
            # print(filename)
            # time.sleep(3)
            # while
            # os.stat(filename-".part")!=0:
            #     print("yeeeeeeeeeee")
            
            # fileName=event.src_path.replace(pathDownloads,"")
            # os.rename(pathDownloads+fileName,pathDownloads+".Temp/"+fileName)
            # self.sort()

    def on_created(self,event):
        self.process(event)


if __name__ == "__main__":
    folders=["Videos","Images","Documents","Others"]
    pathDownloads=os.path.expanduser("~")+"/Downloads/"


    if not os.path.exists(pathDownloads+".log.txt"):
        with open(pathDownloads+".log.txt",'w') as file:
            os.mkdir(pathDownloads+".Temp")
            for i in range(len(folders)):
                os.mkdir(pathDownloads+folders[i])
            file.write("Initialised Folders")

    #args=sys.argv[1:]

    observer=Observer()
    observer.schedule(eventHandler(),path=pathDownloads)        
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()