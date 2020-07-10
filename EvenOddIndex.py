from mpi4py import MPI
import xml.etree.ElementTree as ET
from Bitmap import Bitmap, DictionaryHandler
import numpy as np
import json
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

    dates = []
    for i in root.iter('{http://docs.oasis-open.org/legaldocml/ns/akn/3.0}debateSection'):
          
        debateNameofInterest =  i.get('name') +': ' + i.find('{http://docs.oasis-open.org/legaldocml/ns/akn/3.0}heading').text  
        
        if debateNameofInterest != None:  
            my1 = H.checkDebate(debateNameofInterest)
        
        if my1 %2 == 0:
            data1.append(i)
        else: 
            data.append(i)
        
        
        for y in i.iter('{http://docs.oasis-open.org/legaldocml/ns/akn/3.0}speech'):
            my2 = H.checkSpeaker(y.get('by'))
            
            
    H.writeSpeakersDictionary('./dictionaries/EvenOdd/speakersEvenOdd.pkl')
    print('\n', len(dates) , '\n')    
    H.writeDebatesDictionary('./dictionaries/EvenOdd/debatesEvenOdd.pkl')
        
    comm.send(data1, dest=1, tag=1)
    comm.send(data, dest=2, tag=1)

else:
    data = comm.recv(source=0, tag=1)
    
    debates = readDebatesDictionary('./dictionaries/EvenOdd/debatesEvenOdd.pkl')
    speakers = readSpeakersDictionary('./dictionaries/EvenOdd/speakersEvenOdd.pkl')
    
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
    even = comm.recv(source=1)
    odd = comm.recv(source=2)
    
    
    finalBitmap =np.zeros((len(even), len(even[1])),dtype=bool)

    for i in range(len(even)):
        if i %2 == 0:
            finalBitmap[i] = odd[i]
        else: 
            finalBitmap[i] = even[i]
            

    print('Final bitmap Even Odd: \n',finalBitmap ,'\n')
    writeBitmap(finalBitmap,'./bitmaps/finalBitmapEvenOdd.npy')


