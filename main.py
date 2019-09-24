import os
import sys
import time
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




    
        # if len(listF)!=0:
        #     for file in listF:
        #         if file.endswith((".jpg",".png",".gif",".exif",".tiff",".bmp",".svg")):
        #             os.rename(pathDownloads+"Temp",pathDownloads+"Images/"+file)



    def process(self,event):
        print(event.src_path)
        fileName=event.src_path.replace(pathDownloads,"")
        os.rename(pathDownloads+fileName,pathDownloads+".Temp/"+fileName)
        self.sort()

        # if "*.png" in event.src_path:
        #    fileName=event.src_path.replace(pathDownloads,"")
        #    os.rename(pathDownloads+fileName,pathDownloads+"Images/"+fileName)

        # elif "*.mp4" in event.src_path:
        #    fileName=event.src_path.replace(pathDownloads,"")
        #    os.rename(pathDownloads+fileName,pathDownloads+"Videos/"+fileName)

        # elif "*.pdf" in event.src_path:
        #    fileName=event.src_path.replace(pathDownloads,"")
        #    os.rename(pathDownloads+fileName,pathDownloads+"Documents/"+fileName)   

        # elif ".zip" in event.src_path:
        #    fileName=event.src_path.replace(pathDownloads,"")
        #    os.rename(pathDownloads+fileName,pathDownloads+"ZipFiles/"+fileName)




        #print(event.src_path)

    def on_created(self,event):
        self.process(event)



folders=["Videos","Images","Documents","Others"]
pathDownloads="/home/"+sys.argv[1]+"/Downloads/"


if not os.path.exists(pathDownloads+"log.txt"):
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