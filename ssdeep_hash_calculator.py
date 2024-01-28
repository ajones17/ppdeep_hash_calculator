import os
import ssdeep
import pathlib
from datetime import datetime
import sys

currentDateAndTime = str(datetime.now())
with open('ssdeepoutput.txt', 'a') as fd:
    fd.write("%s\n" + currentDateAndTime)
    fd.close
print("The current date and time is ", currentDateAndTime)

dirName = "./Documents/"
listOfFiles = list()

for (dirpath, dirnames, filenames) in os.walk(dirName):
    for filename in filenames:
        listOfFiles += [os.path.join(dirpath, filename)]

for elem in listOfFiles:
    filesizestr = str(os.path.getsize(elem))
    elemstr = str(elem)

    #Test to see if file is readable
    path2 = os.access(elemstr, os.R_OK)
    print("Boolean permission validation:", path2)
    h1 = ssdeep.hash_from_file(elemstr)
    print(elemstr + "|" + filesizestr + "|" + h1)
    with open('ssdeepoutput.txt', 'a') as fd:
        fd.write('\n' + elemstr + "|" + filesizestr + "|" + h1)
    fd.close
    endDateAndTime = str(datetime.now())
    print("Procedure ended at ", endDateAndTime)
    with open('ssdeepout.txt', 'a') as fd:
        fd.write('\n' + endDateAndTime)

