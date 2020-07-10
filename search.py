from mpi4py import MPI
from functions import retrieveBitmap, readDebatesDictionary, readSpeakersDictionary
import numpy as np
import sys, time

np.set_printoptions(threshold=sys.maxsize)

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
    
if rank == 0:
    
    bitmap = retrieveBitmap('./bitmaps/finalBitmap4threads.npy')
    
    debatesArray = []

    print('\n \n')
    print('********************* SEARCH ********************* \n')
    
    for i in range(1, size):   
        debateName = input('Input debate name '+str(i)+': ')
        debatesArray.append(debateName)
        comm.send(debateName, dest=i)

else:
   debatesArray = None
   bitmap = None

bitmap = comm.bcast(bitmap, root=0)   

if rank >0:
    
    debatesArray = comm.recv(source=0)
    
    debateNameToDictionary = readDebatesDictionary('./dictionaries/4threads/debatesDictionary4threads.pkl')
    rowToRetrieve = debateNameToDictionary.get(debatesArray) 
    if rowToRetrieve != None:
        rowToRetrieve = rowToRetrieve -1

    bitmapRow = bitmap[rowToRetrieve]
    speakers = readSpeakersDictionary('./dictionaries/4threads/speakersDictionary4threads.pkl')
    
    if len(bitmapRow)>1:
        comm.send(bitmapRow, dest=0)
    else:
        print(debatesArray,' does not exist')
        rowOfZeros = np.zeros((1, len(bitmap[0])),dtype=int)
        comm.send(rowOfZeros, dest=0)
    
    
if rank ==0:
    
    finalArray = np.zeros((2, len(bitmap[0])),dtype=int)
    
    for i in range(1,size):
        myRow = comm.recv(source=i)
        finalArray[i-1] = myRow
      
    remainingRow = np.logical_and.reduce(finalArray).astype(int)

    
    speakers = readSpeakersDictionary('./dictionaries/4threads/speakersDictionary4threads.pkl')
    speakersInDebate = []
    
    for indexPos, k in enumerate(remainingRow):
        if k == 1:
            for name, index in speakers.items():  
                if index == indexPos+1:
                    speakersInDebate.append(name)
    
    
    print('\n The speakers in the ', debatesArray,' debates are: \n', speakersInDebate)

