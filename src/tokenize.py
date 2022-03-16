# import os
# from tkinter import W
# from collections import defaultdict


def intersect(p1,p2):
    answer=[]

    i1=0
    i2=0
    while i1 < len(p1) and i2 < len(p2):
        if p1[i1] == p2[i2]:
            answer.append(p1[i1])
            i1+=1
            i2+=1

        elif p1[i1]<p2[i2]:
            i1+=1
        else:
            i2+=1

    return answer 

def union(p1,p2):
    answer=[]
    i1=0
    i2=0

    while i1 < len(p1) and i2 < len(p2):
        if p1[i1] == p2[i2]:
            answer.append(p1[i1])
            i1+=1
            i2+=1
        elif p1[i1]<p2[i2]:
            answer.append(p1[i1])
            i1+=1
        else:
            answer.append(p2[i2])
            i2+=1

    while i1 < len(p1):
        answer.append(p1[i1])
        i1+=1
    
    while i2 < len(p2):
        answer.append(p2[i2])
        i2+=1
        

    return answer 

def Complement(p,totalDocs):
    answer = []
    for i in range(totalDocs):
        try:
            p.index(i)    
        except:
            answer.append(i)

    return answer

# docs = []
# wordList = []
# unique_words = {}
# docNo = 0

# # for filename in os.listdir("Documents"):
# #     with open(os.path.join("Documents", filename), 'r') as f:
# #         text = f.read()
# #         text = text.lower()
# #         text_words = text.split()
# #         print(filename)
# #         print(text)
# #         docs.append(filename) 
        
# #         print(text_words)

# #         for word in text_words:
# #             if word not in unique_words:
# #                 unique_words[word] = [docNo]  #initializing posting list
# #                 wordList.append(word)
            
# #             elif docNo not in unique_words[word]:
# #                 unique_words[word].append(docNo) #appending posting list
        
# #         docNo+=1

# # print(docs)

# # query = input()
# # query = query.split()

# # print(query)

# # print(intersect(unique_words['drug'],unique_words['new']))
# # print(union(unique_words['drug'],unique_words['new']))
# # print(Complement(unique_words['approach'],len(docs)))


# PositonalInd = {}
# Dno=0
# for filename in os.listdir("Documents"):
#     with open(os.path.join("Documents", filename), 'r') as f:
#         text = f.read()
#         text = text.lower()
#         text_words = text.split()
#         # print(filename)

#         i=0
#         for word in text_words:
#             if word not in [*PositonalInd.keys()]:
#                 PositonalInd[word] = {Dno:[i]}  #initializing posting list
#             elif Dno not in [*PositonalInd[word].keys()]:
#                 PositonalInd[word][Dno] = [i]  #appending posting list
#             else:
#                 PositonalInd[word][Dno].append(i)
#             i+=1

#         Dno+=1

# # print(wordList)
# # print(unique_words)
# print(PositonalInd)


# def docID(plist):
#         return plist[0]

# def position(plist):
#         return plist[1]
    
# def pos_intersect(p1,p2,k):
#         answer = []                                                                     # answer <- ()
#         len1 = len(p1)
#         len2 = len(p2)
#         i = j = 0 
#         while i != len1 and j != len2:                                                  # while (p1 != nil and p2 != nil)
#                 if docID(p1[i]) == docID(p2[j]):
#                         l = []                                                          # l <- ()
#                         pp1 = position(p1[i])                                           # pp1 <- positions(p1)
#                         pp2 = position(p2[j])                                           # pp2 <- positions(p2)
    
#                         plen1 = len(pp1)
#                         plen2 = len(pp2)
#                         ii = jj = 0 
#                         while ii != plen1:                                              # while (pp1 != nil)
#                                 while jj != plen2:                                      # while (pp2 != nil)
#                                         if abs(pp1[ii] - pp2[jj]) <= k:                 # if (|pos(pp1) - pos(pp2)| <= k)
#                                                 l.append(pp2[jj])                       # l.add(pos(pp2))
#                                         elif pp2[jj] > pp1[ii]:                         # else if (pos(pp2) > pos(pp1))
#                                                 break    
#                                         jj+=1                                           # pp2 <- next(pp2)      
#                                 #l.sort()                                               
#                                 while l != [] and abs(l[0] - pp1[ii]) > k :             # while (l != () and |l(0) - pos(pp1)| > k)
#                                         l.remove(l[0])                                  # delete(l[0])
#                                 for ps in l:                                            # for each ps in l
#                                         answer.append([ docID(p1[i]), pp1[ii], ps ])    # add answer(docID(p1), pos(pp1), ps)
#                                 ii+=1                                                   # pp1 <- next(pp1)
#                         i+=1                                                            # p1 <- next(p1)
#                         j+=1                                                            # p2 <- next(p2)
#                 elif docID(p1[i]) < docID(p2[j]):                                       # else if (docID(p1) < docID(p2))
#                         i+=1                                                            # p1 <- next(p1)                                                        
#                 else:
#                         j+=1                                                            # p2 <- next(p2)
#         return answer

# def run_test():
#         print "to be or not to be"
#         to = [ [1,[7,18,33,72,86,231]] , [2,[1,17,74,222,255]] , [4,[8,16,190,429,433]] , [5,[363,367]] , [7,[13,23,191]]]
#         be = [ [1, [17,25]], [4,[17,191,291,430,434]] , [5,[14,19,101]]]
#         print "to: ", to
#         print "be: ", be
#         print "merge result of \"to /1 be\": " , pos_intersect(to, be, 1)
#         print "merge result of \"be /3 to\": " , pos_intersect(be, to, 3)
#         print "merge result of \"to /5 be\": " , pos_intersect(to, be, 5)

# run_test()