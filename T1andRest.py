#!/usr/bin/python

import re
import os
import glob
import shutil

t1Comp = re.compile(r'TFL\S*|\S*(?<!S)T1\S*|\S*(?<!s)t1\S*')
restComp = re.compile(r'\S*[Rr][Ee][Ss][Tt]\S*')
dataDirectory = os.path.abspath('/volume1/CCNC_MRI')
#dataDirectory = os.path.abspath('/Users/mav88/Dropbox/python/exampleNas')

#groups to copy
copyGroups=['CHR','NOR']

#targetDirectory = os.path.abspath('/Users/mav88/Dropbox/python/nasTarget')

#target directory
if os.path.isdir('/volume1/2012_12_31') == True:
    targetDirectory = os.path.abspath('/volume1/2012_12_31')
else:
    os.mkdir('/volume1/2012_12_31')
    targetDirectory = os.path.abspath('/volume1/2012_12_31')

noT1=[]
noREST=[]
for group in copyGroups:
    groupDirectory = os.path.join(dataDirectory,group)
    subjectList = glob.glob(groupDirectory+'/'+ group +'[0-9][0-9]_[A-Z][A-Z][A-Z]')
    for subject in subjectList:
        subjectName = os.path.basename(subject)
        subfolder = glob.glob(subject+'/[A-Za-z0-9]*')
        subfolder = [item for item in subfolder if os.path.isdir(item)==True]
        if len(subfolder) > 1:
            answer = raw_input('\n\n{0} has more than 1 subfolders\nChoose one between \n1=\t\t{1}\n2=\t\t{2}\n == '.format(
                    subject,subfolder[0],subfolder[1]))
            if answer == "1":
                subfolder = subfolder[0]
            elif answer =="2":
                subfolder = subfolder[1]
            else:
                print 'this subject is skipped'
                continue


        #imageFolders = os.listdir(os.path.abspath(''.join(subfolder)))
        imageFolders = glob.glob(''.join(subfolder)+'/[A-Za-z0-9]*')
        T1Copy=[]
        RESTCopy=[]
        for i in imageFolders:
            T1 = ''.join(t1Comp.findall(i))
            REST = ''.join(restComp.findall(i))
            if REST:
                if len(glob.glob(i+'/*')) > 4000:
                    os.makedirs(targetDirectory+'/'+subjectName+'/'+'REST')
                    dest =  os.path.join(targetDirectory,subjectName,'REST')
                    os.system('cp -r {0} {1}'.format(i,dest))

                    RESTCopy.append(i)

            if T1:
                if len(glob.glob(i+'/*')) > 208 and len(glob.glob(i+'/*')) < 220:
                    os.makedirs(targetDirectory+'/'+subjectName+'/'+'T1')
                    destT =  os.path.join(targetDirectory,subjectName,'T1')
                    os.system('cp -r {0} {1}'.format(i,destT))
                    T1Copy.append(i)
        if T1Copy==[]:
            print '{} has no T1'.format(subject)
            noT1.append(subject)
        if RESTCopy==[]:
            print '{} has no REST'.format(subject)
            noREST.append(subject)


print noT1,'\n\n\n'
print noREST








