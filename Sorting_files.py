import shutil
import os

#initializing extrensoins
textExtensions = {"txt","pdf", "docx", "xlsx", "ppt"}
imageExtensions = {"jfif", "png", "jpg", "jpeg"}

#Takes concerned path
path = input("Enter the path : ")

#lisitng all files present in the directory
allFiles = os.listdir(path)

extenions = {}
#gathers all extensions of files present in allFiles
for f in allFiles:
    extenions[f] = os.path.splitext(f)[1][1:]

#replaces space with _ in file names
for file in allFiles:
    if " " in file and os.path.isfile(file) == True:
        tempPath = path + "/" + file 
        os.rename(tempPath, tempPath.replace(" ", "_"))

newAllFiles = os.listdir(path)

#Creates folder for repective file types if present
if  any(x in textExtensions for x in extenions.values()) == True and os.path.isdir(path + '\Text Documents') == False:
    os.mkdir(path + "\Text Documents")
if  any(x in imageExtensions for x in extenions.values()) == True and os.path.isdir(path + '\Images') == False:
    os.mkdir(path + "\Images")
if ("exe") in extenions.values() and os.path.isdir(path + '\Applications') == False:
    os.mkdir(path + "\Applications")

#moves individual file to its respective folder
for file in newAllFiles:
    if os.path.splitext(file)[1][1:] in textExtensions:
        shutil.move(path+"\\"+file,path+"\\Text Documents\\"+file)
    if os.path.splitext(file)[1][1:] in imageExtensions:
        shutil.move(path+"\\"+file,path+"\\Images\\"+file)
    if os.path.splitext(file)[1][1:] == "exe":
        shutil.move(path+"\\"+file,path+"\\Applications\\"+file)
