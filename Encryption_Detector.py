import os
from datetime import datetime
import time
import random


class _File:#help class that save the file name,lastmodified date and text
    def __init__(self, name, lastmodified, txt):
        # type: (object, object, object) -> object
        self.name = name;
        self.lastmodified = lastmodified
        self.txt = txt

    def tostring(self):
        print (self.name)
        print (self.lastmodified)
        print (self.txt)


def update_file(f1):#help func that updates the file text,lastmodified date and name
    for x in fileslist:
        if x.name == f1.name:
            x.lastmodified = f1.lastmodified
            x.txt = f1.txt
            return


def update_all_files():#help func that updates all the files in the library (updates theres names,dates and txts)
    fileslist = []
    for file in os.listdir(location):
        if file.endswith(".txt"):
            lastmodified = os.stat(file).st_mtime
            lastmodified = datetime.fromtimestamp(lastmodified)
            with open(file) as f1:
                txt = f1.readlines()
                txt = [x.strip() for x in txt]
                temp = _File(str(file), lastmodified, txt)
                fileslist.append(temp)


def check_all():#help func that checks for every file if someone encrypted him
    fileslisttmp = []
    for file in os.listdir(location):
        if file.endswith(".txt"):
            lastmodified = os.stat(file).st_mtime
            lastmodified = datetime.fromtimestamp(lastmodified)
            with open(file) as f1:
                txt = f1.readlines()
                txt = [x.strip() for x in txt]
                temp = _File(str(file), lastmodified, txt)
                fileslisttmp.append(temp)
    for x in fileslist:
        for _filetmp in fileslisttmp:
            if x.name == _filetmp.name:
                if (x.lastmodified != _filetmp.lastmodified):
                    ans = check_dif(_filetmp.txt)
                    if not ans:
                        print("Oh no someone touch ur files")
                        exit(0)
                    else:
                        update_file(x)


def check_dif(f1):#help func that checks for quarter random lines if they doesn't encrypted
    for i in range (0,len(f1)/4+1):#We Test only quarter randoms line
        x=(int)(random.random() * len(f1))
        tmp=f1[x]
        for word in tmp:
            try:
                word.encode('utf-8')
            except UnicodeDecodeError:
                return False
    return True



location = os.getcwd()  # get present working directory location here
fileslist = []  # list of files
for file in os.listdir(location):
    if file.endswith(".txt"):#save only the txt files
        lastmodified = os.stat(file).st_mtime
        lastmodified = datetime.fromtimestamp(lastmodified)
        with open(file) as f1:
            txt = f1.readlines()
            txt = [x.strip() for x in txt]
            temp = _File(str(file), lastmodified, txt)
            fileslist.append(temp)
if not fileslist:
    print ("Your library doesn't contains txt files")
    exit(0)
print("Starting to monitor")
while (True):
    check_all()
    time.sleep(15)
