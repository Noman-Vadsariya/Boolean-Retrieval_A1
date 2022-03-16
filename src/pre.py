import os
import re
from nltk.stem import PorterStemmer
import json
from pathlib import Path

class Preprocessor:
    def __init__(self,FolderName=None):
        self.docs = []
        self.PositonalIndex = {}
        self.dictionary = {}
        self.postings = {}
        self.noOfDocs = 0
        self.stopwords = []
        self.CollectionDir = str(Path(__file__).parent.resolve()).replace('src',str(FolderName))
        self.DataDir = str(Path(__file__).parent.resolve()).replace('src','data')

    def PreprocessingChain(self):

        if not os.path.isdir(self.DataDir):
            self.LoadStopwordsList()
            self.BuildInvertedIndex()
            self.BuildPositionalIndex()

            os.mkdir(self.DataDir)      #creating data directory for storing and loading indexes
            self.WriteToDisk(self.docs,'Documents')
            self.WriteToDisk(self.dictionary,'Dictionary')
            self.WriteToDisk(self.postings,'Inverted_Index')
            self.WriteToDisk(self.PositonalIndex,'Positional_Index')
        else:
            
            #loading indexes from data directory
            self.docs = self.ReadFromDisk('Documents')
            self.noOfDocs = len(self.docs)                      #total documents in the collections
            self.dictionary = self.ReadFromDisk('Dictionary')
            self.postings = self.ReadFromDisk('Inverted_Index')
            self.PositonalIndex = self.ReadFromDisk('Positional_Index')

    def tokenize(self,text):
        text = text.lower()     #case folding
        # text = re.sub(r',|-',"",text)
        text = re.sub(r'[^\w\s]',' ',text)   #noise removal - replacing all types of [^a-zA-Z0-9] and [^\t\r\n\f] with space for splitting on space
        text = text.split()     #splitting on space
        return text

    def RemoveStopwords(self,tokens):
        SanitizedList = []
        
        for tok in tokens:
            tok = re.sub(r'[^\w\s]','',tok)     # regex for filtering out punctuations
            if tok in self.stopwords:
                continue
            
            SanitizedList.append(tok)

        return SanitizedList

    def isStopword(self,term):
        return term in self.stopwords

    def LoadStopwordsList(self):
        pathToStopwords = str(Path(__file__).parent.resolve()).replace('src',str('Stopwords'))
        for filename in os.listdir(pathToStopwords):
            with open(os.path.join(pathToStopwords, filename), 'r') as f:
                self.stopwords += f.read().splitlines()

            f.close()

        while '' in self.stopwords: self.stopwords.remove('')
        self.stopwords = [x.replace(' ','') for x in self.stopwords]

    def FilterStopwords(self,tokens):
        
        for tok in self.stopwords:
            if tok in tokens:
                tokens.remove(tok)
        
        return tokens
    
    def Stemming(self,token):
        ps = PorterStemmer()
        return ps.stem(token)   

    def BuildInvertedIndex(self):

        files = os.listdir(self.CollectionDir)
        files = [int(x.replace('.txt','')) for x in files]
        files.sort()
        files = [ str(x)+'.txt' for x in files ]

        for filename in files:
            with open(os.path.join(self.CollectionDir, filename), 'r') as f:
                text = f.read()
                text_words = self.tokenize(text)
                # text_words = self.RemoveStopwords(text_words)
                self.docs.append(filename) 
                
                # print(text_words)

                for word in text_words:
                    if not self.isStopword(word):   #Stopwords Removal
                        word = self.Stemming(word)
                        if word not in self.dictionary:
                            self.postings[word] = [self.noOfDocs]  #initializing posting list
                            self.dictionary[word] = 1   #initializing document count
                        
                        elif self.noOfDocs not in self.postings.get(word):
                            self.postings[word].append(self.noOfDocs) #appending posting list
                            self.dictionary[word] += 1  #incrementing document count
                    
                self.noOfDocs+=1

    def BuildPositionalIndex(self):
        
        Dno = 0

        files = os.listdir(self.CollectionDir)
        files = [int(x.replace('.txt','')) for x in files]
        files.sort()
        files = [ str(x)+'.txt' for x in files ]

        for filename in files:
            with open(os.path.join(self.CollectionDir, filename), 'r') as f:
                text = f.read()
                text_words = self.tokenize(text)
                # text_words = self.RemoveStopwords(text_words)

                i=0
                for word in text_words:
                    if not self.isStopword(word):
                        word = self.Stemming(word)
                        if word not in [*self.PositonalIndex.keys()]:
                            self.PositonalIndex[word] = {Dno:[i]}  #initializing posting list
                        elif Dno not in [*self.PositonalIndex[word].keys()]:
                            self.PositonalIndex[word][Dno] = [i]   #appending posting list
                        else:
                            self.PositonalIndex[word][Dno].append(i)
                    i+=1

                # print(self.PositonalIndex.keys())
                Dno+=1
    
    def WriteToDisk(self,index,indexType):
        filename = '\\' + indexType + ".txt"
        with open(self.DataDir + filename, 'w') as filehandle:
            filehandle.write(json.dumps(index))

    def ReadFromDisk(self,indexType):
        filename = '\\' + indexType + ".txt"
        with open(self.DataDir + filename, 'r') as filehandle:
            index = json.loads(filehandle.read())

        return index

# p = Preprocessor('F:\IR\Assignment 01\Documents')
p = Preprocessor('Abstracts')
p.PreprocessingChain()
