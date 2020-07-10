from mpi4py import MPI
from functions import retrieveBitmap, readDebatesDictionary, readSpeakersDictionary
import numpy as np
import sys, time , cProfile, io, pstats,psutil, memory_profiler

# def profile(fnc):
    
#     """A decorator that uses cProfile to profile a function"""
    
#     def inner(*args, **kwargs):
        
#         pr = cProfile.Profile()
#         pr.enable()
#         retval = fnc(*args, **kwargs)
#         pr.disable()
#         s = io.StringIO()
#         sortby = 'cumulative'
#         ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
#         ps.print_stats()
#         print(s.getvalue())
#         return retval

#     return inner

@profile
def allocate():

    bitmap = retrieveBitmap('./bitmaps/finalBitmap4threads.npy')

    debatesArray = []

    debateName =[]
    debateName.append('opening: TUESDAY, 8 MAY 1979')
    debateName.append('debates: ALLEGED OMISSION OF WORDS FROM OFFICIAL REPORT OF SENATE DEBATES (HANSARD)')

    print('\n \n')
    print('********************* SEARCH ********************* \n')

    # for i in range(2):   
    #     debateName = input('Input debate name '+str(i)+': ')
    #     debatesArray.append(debateName)

    # debatesArray = comm.recv(source=0)

    
    debateNameToDictionary = readDebatesDictionary('./dictionaries/4threads/debatesDictionary4threads.pkl')
    rowToRetrieve = debateNameToDictionary.get(debateName[0])
    rowToRetrieve2  =debateNameToDictionary.get(debateName[1])
    if rowToRetrieve != None:
        rowToRetrieve = rowToRetrieve -1
        rowToRetrieve2 = rowToRetrieve2 -1

    bitmapRow = bitmap[rowToRetrieve]
    bitmapRow2 = bitmap[rowToRetrieve2]
    speakers = readSpeakersDictionary('./dictionaries/4threads/speakersDictionary4threads.pkl')


    dictionaryRow = []
    dictionaryRow2 = []

    if len(bitmapRow)>1:
        dictionaryRow = bitmapRow
    else:
        print(debatesArray[0],' does not exist')
        rowOfZeros = np.zeros((1, len(bitmap[0])),dtype=int)
        dictionaryRow = rowOfZeros
        
    if len(bitmapRow2)>1:
        dictionaryRow2 = bitmapRow2
    else:
        print(debatesArray[1],'2 does not exist')
        rowOfZeros = np.zeros((1, len(bitmap[0])),dtype=int)
        dictionaryRow2 = rowOfZeros



    # finalArray = np.zeros((2, len(bitmap[0])),dtype=int)
    finalArray = []
    finalArray.append(dictionaryRow)
    finalArray.append(dictionaryRow2)

    remainingRow = np.logical_and.reduce(finalArray).astype(int)


    speakers = readSpeakersDictionary('./dictionaries/4threads/speakersDictionary4threads.pkl')
    speakersInDebate = []
    startTime = time.time()
    for indexPos, k in enumerate(remainingRow):
        if k == 1:
            for name, index in speakers.items():  
                if index == indexPos+1:
                    speakersInDebate.append(name)
    print('speaker search time', time.time() - startTime)
    print('\n The speakers in the ', debatesArray,' debates are: \n', speakersInDebate)

allocate()