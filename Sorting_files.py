import shutil
import os

#initializing extrensoins
textExtensions = ["txt","pdf", "docx", "xlsx", "ppt"]
imageExtensions = ["jfif", "png", "jpg", "jpeg"]
others = ["txt","pdf", "doc", "docx", "xlsx", "ppt", "jfif", "png", "jpg", "jpeg", "exe"]

#Takes concerned path
path = input("Enter the path : ")

#lisitng all files present in the directory
allFiles = os.listdir(path)

extenions = {}
#gathers all extensions of files present in list allFiles
for f in allFiles:
    extenions[f] = os.path.splitext(f)[1][1:]

#Creates folder for particular file type if present
if  any(x in textExtensions for x in extenions.values()) == True and os.path.isdir(path + '\Text Documents') == False:
    os.mkdir(path + "\Text Documents")
if  any(x in imageExtensions for x in extenions.values()) == True and os.path.isdir(path + '\Images') == False:
    os.mkdir(path + "\Images")
if ("exe") in extenions.values() and os.path.isdir(path + '\Applications') == False:
    os.mkdir(path + "\Applications")

tempList = list(set(extenions.values()) - set(others))
if "" in tempList:
    tempList.remove("")

if (tempList not in others) and os.path.isdir(path + '\Others') == False:
    os.mkdir(path + "\Others")


#moves individual file to its respective folder
for key, value in extenions.items():
    if value in textExtensions:
        shutil.move(path+"\\"+key,path+"\\Text Documents\\"+key)
    elif value in imageExtensions:
        shutil.move(path+"\\"+key,path+"\\Images\\"+key)
    elif value == 'exe':
        shutil.move(path+"\\"+key,path+"\\Applications\\"+key)
    elif value in tempList:
        shutil.move(path+"\\"+key,path+"\\Others\\"+key)
        
print("FILES SORTED!")