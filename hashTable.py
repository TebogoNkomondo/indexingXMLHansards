import time, sys
import xml.etree.ElementTree as ET, pickle
from Bitmap import Bitmap
from functions import writeBitmap, readDebatesDictionary, readSpeakersDictionary, retrieveBitmap


class LinkedList:
    class ListNode:
        def __init__(self, value, next = None):
            self.value = value
            self.next = next
        #end __init__
    
    def __init__(self, otherList = None):
        self.head = None
    #end __init__

    def isEmpty(self):
        return self.head == None
    #end isEmpty

    def add(self, value):
        if isinstance(value, LinkedList):
            cursor = value.head
            while cursor is not None:
                self.add(cursor.value)
                cursor = cursor.next
            #end while
        else:
            self.head = LinkedList.ListNode(value, self.head)
        #end if-else
    #end add

    def __str__(self):
        if self.isEmpty():
            return '[]'
        #end if
        listStr = '['
        cursor = self.head
        while cursor is not None:
            listStr += str(cursor.value) + ', '
            cursor = cursor.next
        #end while
        return listStr[0:-2] + ']'
    #end __str__
#end LinkedList

class Node:
    def __init__(self, key, value):
        self.key = key
        self.values = LinkedList()
        self.values.add(value)
        self.right = None
        self.next = None
    # __init__
#end Node

class HashTable:
    def __init__(self):
        self.size = 0
        self.cap = 70
        self.hashmap = [None]*self.cap
    #end __init__

    def hash(self, key):
        hashSum = 0
        for i in range(len(key)):
            hashSum += (i+len(key))**ord(key[i])
            hashSum %= self.cap
        #end for
        return hashSum
    #end hash

    def insert(self, key, value):
        #double the size if it is half the hashTable size
        if self.cap/2 <= self.size:
            self.doubleUp()
        #end if

        self.size += 1
        index = self.hash(key)
        node = self.hashmap[index]
        if node is None:
            self.hashmap[index] = Node(key, value)
            return
        #end if

        prev = node
        while node is not None:
            if node.key == key:
                node.values.add(value)
                return
            #end if
            prev = node
            node = node.next
        #end while
        prev.next = Node(key, value)
    #end insert

    def search(self, key):
        ''' It will return the value associated with the key if found, otherwise it returns None'''
        index = self.hash(key)
        node = self.hashmap[index]
        if node is None:
            return None
        #end if

        while True:
            if node.key == key:
                return node.values
            #end if

            # The list is fully traversed but the key is not found
            if node.next is None:
                return None
            #end if 
            node = node.next
        #end while
    #end search

    def delete(self, key):
        index = self.hash(key)
        node = self.hashmap[index]
        prev = None
        while node is not None and node.key != key:
            prev = node
            node = node.next
        #end while
        if node is None:
            return None
        else:
            self.size -= 1
            result = node.values
            if prev is None:
                self.hashmap[index] = None
            else:
                prev.next = prev.next.next
            #end if-else
            return result
        #end if-else
    #end delete

    def doubleUp(self):
        oldMap = self.hashmap
        self.cap *= 2 #double capacity
        self.hashmap = [None]*self.cap #New hashmap with new capacity

        #Copying everything frofm the old hashmap
        for node in oldMap:
            if node is None:
                continue
            #end if
            cursor = node
            #Traversing the (possible) linked list
            while cursor is not None:
                self.insert(cursor.key, cursor.values)
                cursor = cursor.next
            #end while
        #end for
    #end doubleUp

    def __str__(self):
        if self.size == 0:
            return '{}'
        #end if
        mapStr = '{'
        for i in hashT.hashmap:
            if i != None:
                cursor = i
                while cursor != None:
                    mapStr += cursor.key + ':'+ str(cursor.values)+ ', '
                    cursor = cursor.next
                #end while
            #end if
        #end for

        return mapStr[0:-2] + '}'
    #end __str__
#end HashTable


    # hashT = HashTable()


    # hashT.insert('Can', 1)
    # hashT.insert('Ken', 2)
    # hashT.insert('Tim', 3)
    # hashT.insert('Koti', 4)

    # H = {}
    # H.setdefault('Can', 1)
    # H.setdefault('Ken', 2)
    # H.setdefault('Tim', 3)
    # H.setdefault('Koti', 4)


    # startTime = time.time()
    # print(hashT.search('Tim'))
    # hashtableFinish = time.time() - startTime
    # print('search time for hashtable :', hashtableFinish)
    # print('size of hashtable', sys.getsizeof(hashT))
    # # print(hashT)

    # startTime = time.time()
    # print(H.get('Tim'))
    # dictionaryFinish = time.time() - startTime
    # print('search time for dictionary :', dictionaryFinish)
    # print('size of dictionary', sys.getsizeof(H))
    # # print(H)


    # print('difference :', dictionaryFinish - hashtableFinish)

class DictionaryHandler():
    def __init__(self):
        self.debates = HashTable()
        self.speakers = HashTable()
    
    def checkDebate(self, debateName):
        key = self.debates.search(debateName)
        if key == None:
            # print(self.debates.size)
            dictionaryLength = self.debates.size+1
            self.debates.insert(debateName, dictionaryLength)
            return dictionaryLength
        else:
            return key
    
    def checkSpeaker(self, speakerName):
        key = self.speakers.search(speakerName)
        if key == None:
            dictionaryLength = self.speakers.size+1
            self.speakers.insert(speakerName, dictionaryLength)
            return dictionaryLength
        else:
            return key
        
    def writeDebatesDictionary(self, filename): 
        with open(filename, 'wb') as f:      
            pickle.dump(self.debates, f, pickle.HIGHEST_PROTOCOL)
  
    def writeSpeakersDictionary(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.speakers, f, pickle.HIGHEST_PROTOCOL)     
  


tree = ET.parse("hans.xml")
root = tree.getroot()

data =[]
H = DictionaryHandler()

data[:] = root.iter('{http://docs.oasis-open.org/legaldocml/ns/akn/3.0}debateSection')
startTime = time.time()  
for i in root.iter('{http://docs.oasis-open.org/legaldocml/ns/akn/3.0}debateSection'):
        
    debateNameofInterest =  i.get('name') +': ' + i.find('{http://docs.oasis-open.org/legaldocml/ns/akn/3.0}heading').text  
    
    startTime = time.time()
    if debateNameofInterest != None:  
        my1 = H.checkDebate(debateNameofInterest)
    
    for y in i.iter('{http://docs.oasis-open.org/legaldocml/ns/akn/3.0}speech'):
        my2 = H.checkSpeaker(y.get('by'))
 
          
H.writeSpeakersDictionary('./dictionaries/4threads/speakersDictionary4threadsHash.pkl') 
H.writeDebatesDictionary('./dictionaries/4threads/debatesDictionary4threadsHash.pkl')
print('writing hash table dictionaries: ', time.time() - startTime)

# speakers = readSpeakersDictionary('./dictionaries/4threads/speakersDictionary4threadsHash.pkl')   
# debates = readDebatesDictionary('./dictionaries/4threads/debatesDictionary4threadsHash.pkl')
# print(speakers)
# myBitmap = Bitmap(len(debates), len(speakers))

# for x in data: 
#     debateNameofInterest =  x.get('name') +': ' + x.find('{http://docs.oasis-open.org/legaldocml/ns/akn/3.0}heading').text    
#     for y in x.iter('{http://docs.oasis-open.org/legaldocml/ns/akn/3.0}speech'):
#         my1 = debates.get(debateNameofInterest) 
#         my2 = speakers.get(y.get('by'))
#         myBitmap.createBitmap(my1-1,my2-1)

sumPytbonDic = 0.028041839599609375 + 0.025744199752807617 + 0.03713560104370117 + 0.03438615798950195 +  0.02548837661743164 +0.025799036026000977 + 0.022286415100097656 + 0.025452613830566406 + 0.03402543067932129 + 0.028065919876098633
print(sumPytbonDic/10)
