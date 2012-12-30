#!/usr/bin/python

import re
import os
import shutil

t1 = re.compile(r'TFL\S*|\S*T1\S*|\S*t1\S*')
rest = re.compile(r'\S*[Rr][Ee][Ss][Tt]\S*')


#data source directory
#dataDirectory = os.path.abspath('/volume1/CCNC_MRI')
dataDirectory = os.path.abspath('/Users/mav88/Dropbox/python/exampleNas')

#groups to copy
copyGroups=['CHR','NOR']

targetDirectory = os.path.abspath('/Users/mav88/Dropbox/python/nasTarget')

#target directory
#if os.path.isdir('/volume1/2012_12_31') == True:
#    targetDirectory = os.path.abspath('/volume1/2012_12_31')
#else:
#    os.mkdir('/volume1/2012_12_31')
#    targetDirectory = os.path.abspath('/volume1/2012_12_31')

for group in copyGroups:
    subjectList = os.listdir(os.path.join(dataDirectory,group))
    for subject in subjectList:
        subfolder = os.listdir(os.path.join(dataDirectory,group,subject))
        rightFolder = re.search('CNT|RESEARCH|2011|2012|2010','subfolder')
        print rightFolder



