
import src.pre as pre
# import pre
import os
import re

class ProximityQuery:

    def __init__(self,PositionalIndex):
        self.PostionalIndex = PositionalIndex

    def get_posting(self,term):
        if term in [*self.PostionalIndex.keys()]:
            return self.PostionalIndex.get(term)
        else:
            print(term +" Not in Vocablary")
            return None

    def get_positions(self,term,docID):
        return self.PostionalIndex[term][docID]

    def posting_intersect(self,t1,t2,k):
        p = pre.Preprocessor()

        t1 = p.Stemming(t1)
        t2 = p.Stemming(t2)
        answer = []

        p1 = self.get_posting(t1)
        p2 = self.get_posting(t2)


        if p1 == None or p2==None:
            return []
        
        p1 = list(p1.keys())
        p2 = list(p2.keys())

        i=j=0 
        while i<len(p1) and j<len(p2):
            if int(p1[i]) == int(p2[j]):
                l = []
                pp1 = self.get_positions(t1,p1[i])
                pp2 = self.get_positions(t2,p2[j])

                plen1 = len(pp1)
                plen2 = len(pp2)
                ii = jj = 0 
                while ii != plen1:                                              # while (pp1 != nil)
                        while jj != plen2:                                      # while (pp2 != nil)
                                if abs(pp1[ii] - pp2[jj]) <= k+1:                 # if (|pos(pp1) - pos(pp2)| <= k)
                                        l.append(pp2[jj])                       # l.add(pos(pp2))
                                elif pp2[jj] > pp1[ii]:                         # else if (pos(pp2) > pos(pp1))
                                        break    
                                jj+=1                                           # pp2 <- next(pp2)      
                        #l.sort()                                               
                        while l != [] and abs(l[0] - pp1[ii]) > k+1:             # while (l != () and |l(0) - pos(pp1)| > k)
                                l.remove(l[0])                                  # delete(l[0])
                        for ps in l:                                            # for each ps in l
                                answer.append([p1[i], pp1[ii], ps ])    # add answer(docID(p1), pos(pp1), ps)
                        ii+=1                                                   # pp1 <- next(pp1)
                i+=1                                                            # p1 <- next(p1)
                j+=1

            elif int(p1[i]) < int(p2[j]):                                       # else if (docID(p1) < docID(p2))
                i+=1                                                            # p1 <- next(p1)                                                        
            else:
                j+=1                 

        return answer

    def ProcessProximityQuery(self,query):
        tokens = query.split()
        k = int(re.sub(r'[^\w\s]','',tokens[2]))
        # print(k)
        result_set = self.posting_intersect(tokens[0],tokens[1],k)

        ret_docs = {}
        for result in result_set:
            docNo = int(result[0])+1  #docNo = doc_index + 1
            if docNo not in ret_docs:
                ret_docs[docNo] = [(result[1],result[2])]
            else:
                ret_docs[docNo].append((result[1],result[2]))

        return ret_docs



# p = pre.Preprocessor('F:\IR\Assignment 01\Abstracts')
# p.PreprocessingChain()
# prox = ProximityQuery(p.PositonalIndex)
# # print(prox.PostionalIndex)
# print(prox.ProcessProximityQuery('neural information /2'))
# print() 
# print(prox.ProcessProximityQuery('feature track /5'))
# print() 
# print(prox.ProcessProximityQuery('novel accurate /2'))