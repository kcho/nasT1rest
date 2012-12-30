#!/usr/bin/python

import re
import os
import shutil

t1 = re.compile(r'TFL\S*|\S*T1\S*|\S*t1\S*')
rest = re.compile(r'\S*[Rr][Ee][Ss][Tt]\S*')


#data source directory
dataDirectory = os.path.abspath('/volume1/CCNC_MRI/')

#groups to copy
copyGroups=['CHR','NOR']

#target directory
if os.path.isdir('/volume1/2012_12_31') == True:
    targetDirectory = os.path.abspath('/volume1/2012_12_31')
else:
    os.mkdir('/volume1/2012_12_31')
    targetDirectory = os.path.abspath('/volume1/2012_12_31')

for group in copyGroups:
    subjectList = os.listdir(os.path.join(dataDirectory,group))
    for subject in subjectList:
        subfolder = ''.join([item for item in os.listdir(os.path.join(dataDirectory,group,subject)) if re.match('[0-9]|[A-Za-z]',item)])
        imageFolders = os.listdir(os.path.join(dataDirectory,group,subject,subfolder))
        T1 = t1.match(imageFolders)
        REST = rest.match(imageFolders)
        print T1.group()
        print REST.group()



