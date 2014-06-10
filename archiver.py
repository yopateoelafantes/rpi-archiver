from tkinter.messagebox import showinfo

class cmdArchiver():
    def onEncode(archiveFormatType,archiveFileLocation,window=False):
        data = open(archiveFileLocation,'r')
        for each_line in data:
            encodedFile = each_line.encode(archiveFormatType)
            print(encodedFile)
            if window == True:
                showinfo(title="Archived File: "+archiveFileLocation,message=str(encodedFile))
    def onDecode(archiveFormatType,archiveFileLocation,window=False):
        data = open(archiveFileLocation,'rb')
        for each_line in data:
            decodedFile = each_line.decode(archiveFormatType)
            print(decodedFile)
            if window == True:
                showinfo(title="Unarchived File: "+archiveFileLocation,message=str(decodedFile))
        for each_line in data:
            decodedFile = each_line.encode(archiveFormatType)
            print(decodedFile)
            if window == True:
                showinfo(self,messag=decodedFile)
    if __name__ == "__main__":
        aoru = input("Archive or Unarchive? >>")
        fileLocation = input("File Location >>")
        print("Types:\tutf8,\tutf16,\tlatin1")
        archiveType = input("Archive Type >>")
        if aoru == "Archive":
            onEncode(archiveType,fileLocation)
        elif aoru == "Unarchive":
            onDecode(archiveType,fileLocation)
