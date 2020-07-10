from mpi4py import MPI
import xml.etree.ElementTree as ET
from Bitmap import Bitmap, DictionaryHandler
import numpy as np
import json, pickle
from functions import writeBitmap, readDebatesDictionary, readSpeakersDictionary, retrieveBitmap

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    tree = ET.parse("hans.xml")
    root = tree.getroot()
    data1 = []
    data = []
    
    H = DictionaryHandler()
    
    H = DictionaryHandler()
    data2 = []
    data2[:] = root.iter('{http://docs.oasis-open.org/legaldocml/ns/akn/3.0}debateSection')
    
    appendLength = len(data2) % 4
    
    boundarySlice = int(len(data2)/4)
    
    debatesData = []
    for i in range(4):  
        if i ==3:
            debatesData.append(data2[boundarySlice*i:(boundarySlice*(i+1)+appendLength)])
        debatesData.append(data2[(i)*boundarySlice:boundarySlice*(i+1)])    
        
    for i in root.iter('{http://docs.oasis-open.org/legaldocml/ns/akn/3.0}debateSection'):
          
        debateNameofInterest =  i.get('name') +': ' + i.find('{http://docs.oasis-open.org/legaldocml/ns/akn/3.0}heading').text  
        
        if debateNameofInterest != None:  
            my1 = H.checkDebate(debateNameofInterest)
        
        for y in i.iter('{http://docs.oasis-open.org/legaldocml/ns/akn/3.0}speech'):
            my2 = H.checkSpeaker(y.get('by'))
             
    H.writeSpeakersDictionary('./dictionaries/4threads/speakersDictionary4threads.pkl') 
    H.writeDebatesDictionary('./dictionaries/4threads/debatesDictionary4threads.pkl')
    
    for k in range(1,4):
        comm.send(debatesData[k], dest=k, tag=1)
     
    speakers = readSpeakersDictionary('./dictionaries/4threads/speakersDictionary4threads.pkl')   
    debates = readDebatesDictionary('./dictionaries/4threads/debatesDictionary4threads.pkl')
    
    
    myBitmap = Bitmap(len(debates), len(speakers))

    for x in debatesData[0]: 
        debateNameofInterest =  x.get('name') +': ' + x.find('{http://docs.oasis-open.org/legaldocml/ns/akn/3.0}heading').text    
        for y in x.iter('{http://docs.oasis-open.org/legaldocml/ns/akn/3.0}speech'):
            my1 = debates.get(debateNameofInterest) 
            my2 = speakers.get(y.get('by'))
            myBitmap.createBitmap(my1-1,my2-1)
            
    rank0Bitmap = (myBitmap.array)
        
    
else:
    data = comm.recv(source=0, tag=1)
    
    speakers = readSpeakersDictionary('./dictionaries/4threads/speakersDictionary4threads.pkl')
    debates = readDebatesDictionary('./dictionaries/4threads/debatesDictionary4threads.pkl')
    
    myBitmap = Bitmap(len(debates), len(speakers))

    for x in data: 
        debateNameofInterest =  x.get('name') +': ' + x.find('{http://docs.oasis-open.org/legaldocml/ns/akn/3.0}heading').text    
        for y in x.iter('{http://docs.oasis-open.org/legaldocml/ns/akn/3.0}speech'):
            my1 = debates.get(debateNameofInterest) 
            my2 = speakers.get(y.get('by'))
            myBitmap.createBitmap(my1-1,my2-1)
    
    array = (myBitmap.array)
    comm.send(array, dest=0)

if rank ==0:
    rank1Bitmap = comm.recv(source=1)
    rank2Bitmap = comm.recv(source=2)
    rank3Bitmap = comm.recv(source=3)
    
    initialOR = np.logical_or(rank1Bitmap, rank2Bitmap, rank3Bitmap).astype(bool)
    finalBitmap = np.logical_or(initialOR, rank0Bitmap).astype(bool)

    print('\n final bitmap using 4 threads: \n', finalBitmap)
    writeBitmap(finalBitmap,'./bitmaps/finalBitmap4threads.npy')
    
     