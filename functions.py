import json, numpy as np, pickle            

def retrieveBitmap(filename):
    return np.load(filename)
                   
def writeBitmap(bitmap, filename):
    np.save(filename, bitmap)
        
        
def readDebatesDictionary(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)
    
    
def readSpeakersDictionary(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)
    