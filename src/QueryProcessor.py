from concurrent.futures import process
from .pre import Preprocessor
from .boolean import BooleanQuery
from .prox import ProximityQuery

class QueryProcessor():
    
    def __init__(self):
        pass

    def ProcessQuery(self,query):
        if query != "":
                p = Preprocessor("F:\IR\Assignment 01\Abstracts")
                p.PreprocessingChain()
                tokens = query.split()
                
                try:
                    if len(tokens)>2 and '/' == tokens[2][0]:
                        prox = ProximityQuery(p.PositonalIndex)
                        result_set = prox.ProcessProximityQuery(query)
                    else:
                        b = BooleanQuery(p.dictionary, p.postings, p.noOfDocs)
                        result_set,processingCost = b.ProcessQuery(query)
                except:
                    return ["Error in query string, try again"]

                print(result_set)
                return (result_set,processingCost)
