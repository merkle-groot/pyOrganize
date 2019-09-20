import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

class eventHandler(PatternMatchingEventHandler):
    patterns="*"

    def process(self,event):
        print(event.src_path)
        if "*.png" in event.src_path:
           fileName=event.src_path.replace(pathDownloads,"")
           os.rename(pathDownloads+fileName,pathDownloads+"Images/"+fileName)

        elif "*.mp4" in event.src_path:
           fileName=event.src_path.replace(pathDownloads,"")
           os.rename(pathDownloads+fileName,pathDownloads+"Videos/"+fileName)

        elif "*.pdf" in event.src_path:
           fileName=event.src_path.replace(pathDownloads,"")
           os.rename(pathDownloads+fileName,pathDownloads+"Documents/"+fileName)   

        elif ".zip" in event.src_path:
           fileName=event.src_path.replace(pathDownloads,"")
           os.rename(pathDownloads+fileName,pathDownloads+"ZipFiles/"+fileName)




        #print(event.src_path)

    def on_created(self,event):
        self.process(event)



folders=["Videos","Images","Documents","ZipFiles"]
pathDownloads="/home/"+sys.argv[1]+"/Downloads/"


if not os.path.exists(pathDownloads+"log.txt"):
    with open(pathDownloads+"log.txt",'w') as file:
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