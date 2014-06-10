"""
@author: lane surface
*this software is free for distrabution without the consent of the author
*required: consent from the author for large redidtribution of the souce code
################################################################################
version 1.0.0
-initial distribution
-main source code and class (srchiveViewer)
-initial archive types (UTF-8,UTF-16,Latin1)
-released in June of 2014 on Github
################################################################################
"""

from tkinter import *
from archiver import cmdArchiver

archiveTypes = ["utf8","utf16","latin1"]

class archiveViewer():
    def onArchiveRequest(archiveFormatType,archiveFileLocation):
        cmdArchiver.onEncode(archiveFormatType,archiveFileLocation,window=True)
    def onUnarchiveRequest(archiveFormatType,archiveFileLocation):
        cmdArchiver.onDecode(archiveFormatType,archiveFileLocation,window=True)
    def onArchiveFormatRequest(self):
        pick = self.var.get()
        print("Archive Format: "+pick)
    def __init__(self):
        root = Tk()
        root.title("RPi-Archiver")
        #frames
        labelFrame = Frame(root)
        entryFrame = Frame(root)
        radiobuttonFrame = Frame(root)
        #labels and buttons
        butt_archive = Button(root,text="Archive",
                              command=(lambda:archiveViewer.onArchiveRequest(self.var.get(),
                                                               entry_fileLocation.get())))
        butt_unarchive = Button(root,text="Unarchive",
                                command=(lambda:archiveViewer.onUnarchiveRequest(self.var.get(),
                                                                   entry_fileLocation.get())))
        label_fileLocation = Label(labelFrame,text="File Location: ",width=15)
        entry_fileLocation = Entry(entryFrame,width=20)
        #radio buttons
        self.var = StringVar()
        for archiveType in archiveTypes:
            Radiobutton(radiobuttonFrame,text=archiveType,
                                             command=self.onArchiveFormatRequest,
                                             variable=self.var,value=archiveType).pack(side=TOP)
        self.var.set(archiveType)
        #pack items
        butt_archive.pack(side=BOTTOM,fill=X)
        butt_unarchive.pack(side=BOTTOM,fill=X)
        radiobuttonFrame.pack(side=BOTTOM)
        labelFrame.pack(side=LEFT)
        entryFrame.pack(side=RIGHT)
        label_fileLocation.pack(side=RIGHT,fill=X)
        entry_fileLocation.pack(side=LEFT,fill=X)
        #initilize root
        root.mainloop()
archiveViewer()
