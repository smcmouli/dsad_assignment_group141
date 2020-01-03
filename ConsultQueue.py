# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 18:04:00 2020

"""
from PatientRecord import PatientRecord
import csv
from io import StringIO
        
class ConsultQueue:    
 
    def __init__(self): 
        print('__init__')
                
    def registerPatient(self, name, age): 
        print('registerPatient')
        
    def enqueuePatient(self, PatId): 
        print('enqueuePatient')
        
    def nextPatient(self): 
        print('nextPatient')
        
    def dequeuePatient(self, PatId): 
        print('dequeuePatient')
        
    def readCurrentPatients(inputfile):
         with open(inputfile, newline='') as csvfile:
          rowreader = csv.reader(csvfile, delimiter=',')
          global count
          count=0
          p=[]
          for row in rowreader:
             prow=PatientRecord(row[1],row[0],count)
             p.append(prow)
             count=count+1
         return p;
    
    def readNewPatients(inputfile):
        with open(inputfile, newline='') as csvfile:
         rowreader = csv.reader(csvfile, delimiter=':')
         global count
         p=[]
         for newrow in rowreader:
             newf= StringIO(newrow[1])
             colreader = csv.reader(newf, delimiter=',')
             for row in colreader:
                  prow=PatientRecord(row[1],row[0],count)
                  p.append(prow)
                  count=count+1                 
        return p;
    
    def writePatients(outputFile,newList,origList):
        
        def writeNewPatients(outputFile,newList): 
             f= open(outputFile,"w+")
             f.write("---- new patient entered--------------- \r\n")
             for patient in newList:
                 f.write("Patient details: "+repr(patient)+"\r\n")
             f.close
        writeNewPatients(outputFile,newList)   
      
        writeNewPatients(outputFile , newList)
        global count
        f=open(outputFile,"a+")
        f.write("---- initial queue --------------- \r\n")
        f.write("No of patients added: "+str(count)+"\r\n")  
        f.write("Refreshed queue:  \r\n")
        for patient in origList:
             f.write(repr(patient)+"\r\n")
        f.write("---------------------------------------------- \r\n")
        f.close
          
      
         

       
    if __name__== "__main__":
      origList=readCurrentPatients("inputPS5a.txt")
      newList=readNewPatients("inputPS5b.txt")
      origList.extend(newList)    
      #registerPatient for all entries in origList
      #For each patient origList, call enqueuePatient
      #recreate Heap
      #write to output file
      writePatients("outputPS5b.txt",newList,origList)
      #invoke nextPatient for each
      #deque after invoking nextPatient
      
      
   
   
      
