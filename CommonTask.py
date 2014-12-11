'''
Created on Oct 26, 2012

@author: chrism
'''
import arcpy, os, smtplib, string ,fnmatch,  linecache
import sys

class ScheduledTask():
    def __init__(self, layerName, inst, fileName, message):
        self.LayerName = layerName
        self.Inst = inst
        self.FileName = fileName
        self.Message = message

    #http://stackoverflow.com/questions/1724693/find-a-file-in-python
    @staticmethod
    def findFilesByPattern(namePattern, path):
        result =[]
        for root , dirs, files in os.walk(path):
            for name in files:
                if fnmatch.fnmatch(name,namePattern):
                    result.append(os.path.join(root,name))
        return result


    def SendErrorMail(self):
        SUBJECT = "Error Message from Create Road Events"
        TO = "cmoon@rockyview.ca"
        FROM = "cmoon@rockyview.ca"
        text = "Error occurs in " + self.LayerName + "\n" +  str(self.Inst)
        BODY = string.join((
            "From: %s" % FROM,
            "To: %s" % TO,
            "Subject: %s" % SUBJECT ,
            "",
            text
            ), "\r\n")
        server = smtplib.SMTP("100.1.1.189")
        server.sendmail(FROM, [TO], BODY)
        server.quit()


    def UpdateLogFile(self):
        with open (self.FileName,'r+') as f:
            old = f.read()
            f.seek(0)
            f.write(self.Message + "\n" + "\n" +  old)
            f.close()