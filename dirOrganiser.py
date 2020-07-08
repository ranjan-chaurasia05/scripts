#!/usr/bin/env python3
import os
import shutil
import random

folderPath = os.environ['HOME']+'/Downloads/'
files = os.listdir(folderPath)

def createAndMove(dirName, file):
    if not os.path.isdir(folderPath+dirName):
        os.mkdir(folderPath+dirName)

    sourceFile = folderPath+file
    destinationFile = folderPath + dirName + os.sep + file
    if os.path.exists(destinationFile):
        _file = os.path.splitext(file)[0]+str(random.randrange(100))+os.path.splitext(file)[1]
        shutil.move(sourceFile, folderPath+_file)
    else:
        shutil.move(sourceFile, destinationFile)

for i in files:
    if os.path.isdir(i):
        pass

    extension = os.path.splitext(i)[1]
    if extension == '.sql':
        createAndMove('databases', i)
    elif extension == '.pdf':
        createAndMove('pdfs', i)
    elif extension == '.php':
        createAndMove('codes', i)
    elif (extension.upper() == '.CSV' or extension.upper() == '.XLS'):
        createAndMove('excels', i)
    elif extension == '.docx':
        createAndMove('docs', i)
    elif extension == '.jpg':
        createAndMove('pictures', i)
