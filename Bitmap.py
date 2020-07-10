import xml.etree.ElementTree as ET
import numpy as np
import sys, json, pickle, time


tree = ET.parse("hans.xml")
root = tree.getroot()
np.set_printoptions(threshold=sys.maxsize)


class DictionaryHandler():
  def __init__(self):
    self.debates = {}
    self.speakers = {}
    
  def checkDebate(self, debateName):
    key = self.debates.get(debateName)
    if key == None:
      dictionaryLength = len(self.debates)+1
      self.debates.setdefault(debateName, dictionaryLength)
      return dictionaryLength
    else:
      return key
    
  def checkSpeaker(self, speakerName):
    key = self.speakers.get(speakerName)
    if key == None:
      dictionaryLength = len(self.speakers)+1
      self.speakers.setdefault(speakerName, dictionaryLength)
      return dictionaryLength
    else:
      return key

      
  def writeDebatesDictionary(self, filename): 
    with open(filename, 'wb') as f:      
        pickle.dump(self.debates, f, pickle.HIGHEST_PROTOCOL)
  
  def writeSpeakersDictionary(self, filename):
    with open(filename, 'wb') as f:
        pickle.dump(self.speakers, f, pickle.HIGHEST_PROTOCOL)     
  

  
  
class Bitmap(DictionaryHandler):
  def __init__(self, rowSize, columnSize):
    self.array = np.zeros((rowSize, columnSize),dtype=bool) 
    
  def printArray(self):
    print(self.array) 
  
  def writeToJsonFile(self):
    with open('bitmap.json', 'w') as f:
      json.dump(self.array.tolist(), f) 
  
  def createBitmap(self, debateName, speakerName):
    self.array[debateName][speakerName] = 1
  
