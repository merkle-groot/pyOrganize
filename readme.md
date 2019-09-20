# pyOrganize

An automated folder organizer in Python.</br>
It runs in the background and watches for new files created by the user and moves it to it's folder(Images/Documents/Vides,etc), depending on the extension of the file. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

It needs __watchdog__ module to trigger an event when a new file is created.

```
sudo pip install watchdog
```

### Usage


Run it on your local machine by passing the name of the User Account in Linux.

```
python main.py vishnu
```
where, _vishnu_ is the username of my system.

That's it!


## Adding more file formats

Just copy and edit any of the _if_ statement inside the proccess method in the eventHandler class.

eg, to organise .C files, add this snippet

```

    elif ".c" in event.src_path:
            fileName=event.src_path.replace(pathDownloads,"")
            os.rename(pathDownloads+fileName,pathDownloads+"C_programs"+fileName)   
```


