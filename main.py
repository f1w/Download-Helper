import os
from pathlib import Path
import shutil


def menu():


    files = str(input("What kind of Files do you want to Save? (exe, pdf) Whitespace after every keyword needed: "))

    fileList = files.split(" ")  

    

    dw_path = str(Path.home() / "Downloads")

    home_path = str(Path.home() / "Desktop")


    os.chdir(dw_path)

    

    l = []

    dirlist = []


    for files in os.listdir(dw_path):
        getAfter = os.path.splitext(files)[1]
        getAfter = getAfter.replace(".", "").strip()
        if getAfter not in fileList:
            os.remove(files)    
        else:
            l.append(files)

    os.chdir(home_path)

    for directories in os.listdir(home_path):

        if "DownloadedFiles" not in directories:
            try:
                os.mkdir("DownloadedFiles")
                
            except:
                pass

    os.chdir("DownloadedFiles")

    anotherOne = os.getcwd()

    for objectives in fileList:
        try:
            os.mkdir(objectives+"s")
            dirlist.append(objectives+"s")
        except:
            pass

    os.chdir(dw_path)

    
    for dd in l:
        os.replace(dw_path+"\\"+dd, anotherOne+"\\"+dd)

    os.chdir(anotherOne)

    for folders in os.listdir(anotherOne):
        getBehind = os.path.splitext(folders)[1]
        if getBehind == "":
            pass          
        else:
            getBehind = getBehind.replace(".", "").strip()
            for sadtimes in dirlist:
                if getBehind in sadtimes:
                    os.replace(anotherOne+"\\"+folders, os.getcwd()+"\\"+sadtimes+"\\"+folders)

            




  
    


if __name__ == "__main__":
    
    menu()