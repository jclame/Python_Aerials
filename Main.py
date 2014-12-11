#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ChrisM
#
# Created:     03/12/2014
# Copyright:   (c) ChrisM 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os, fnmatch, arcpy, CommonTask, time
from datetime import datetime

vTargetImage = "Database Connections\\sa@Imagery2014.sde\\Imagery2014.DBO.Seed"
vLogFile = r"E:\Aerial_DB\Imagery2014Log.txt"

def MosaicImages(filePath, target):
    try:

        arcpy.Mosaic_management(filePath, target,  "LAST", "FIRST", "", "", "NONE", "0", "NONE")
        print "Successfully Done" + filePath + " processed time:" + str(datetime.now().strftime("%Y-%m-%d %H %M %S"))

    except Exception as inst:
        ST = CommonTask.ScheduledTask(filePath , inst , vLogFile , arcpy.GetMessages())
        ST.SendErrorMail()
        ST.UpdateLogFile()


if __name__ == '__main__':

    fileNames = []
    fileNames = CommonTask.ScheduledTask.findFilesByPattern("*.ecw", r'E:\ImageFolder' )

    vCount = 0
    for name in fileNames:

        print "Process " + name
        vCount = vCount + 1

        MosaicImages(name,vTargetImage)
        print str(vCount) + " are processed out of " + str(len(fileNames))


    print str(len(fileNames)) + " files were succcessfuly Done"



