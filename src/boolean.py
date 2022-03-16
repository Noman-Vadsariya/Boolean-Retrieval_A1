# from code import interact
# from src.pre import Preprocessor
import pre
# import src.pre as pre


class BooleanQuery:
    def __init__(self, Dictionary, Postings, totalDocs):
        self.Postings = Postings
        self.Dictionary = Dictionary
        self.totalDocs = totalDocs

    def get_posting(self, term):
        if term in [*self.Postings.keys()]:
            return self.Postings[term]
        else:
            print(term + " Not in Vocablary")
            return []

    def get_posting_size(self, term):
        if term in [*self.Dictionary.keys()]:
            return self.Dictionary[term]
        else:
            print(term + " not in vocablary")
            return -1

    def intersect(self, p1, p2):
        answer = []

        i1 = 0
        i2 = 0
        while i1 < len(p1) and i2 < len(p2):
            if p1[i1] == p2[i2]:
                answer.append(p1[i1])
                i1 += 1
                i2 += 1

            elif p1[i1] < p2[i2]:
                i1 += 1
            else:
                i2 += 1

        return answer

    def union(self, p1, p2):
        answer = []
        i1 = 0
        i2 = 0

        while i1 < len(p1) and i2 < len(p2):
            if p1[i1] == p2[i2]:
                answer.append(p1[i1])
                i1 += 1
                i2 += 1
            elif p1[i1] < p2[i2]:
                answer.append(p1[i1])
                i1 += 1
            else:
                answer.append(p2[i2])
                i2 += 1

        while i1 < len(p1):
            answer.append(p1[i1])
            i1 += 1

        while i2 < len(p2):
            answer.append(p2[i2])
            i2 += 1

        return answer

    def complement(self, p):
        answer = []
        for i in range(self.totalDocs):
            if i not in p:
                answer.append(i)

        return answer

    def ProcessQuery(self, query):

        processingCost = 0  # no of DocIDs traversed

        p = pre.Preprocessor()
        tokens = query.split()

        for i in range(len(tokens)):
            tokens[i] = p.Stemming(tokens[i])

        if (len(tokens)) == 1:
            processingCost = self.get_posting_size(tokens[0])
            tempResult = self.get_posting(tokens[0])

        elif (len(tokens)) == 2 and tokens[0].upper() == "NOT":
            processingCost = self.totalDocs - self.get_posting_size(tokens[1])
            tempResult = self.complement(self.get_posting(tokens[1]))

        else:
            i = 0
            tempResult = None
            while i < len(tokens):

                if tokens[i].upper() == "AND":
                    if tempResult is None:
                        if i - 2 >= 0 and tokens[i - 2] == "NOT":
                            p1 = self.complement(self.get_posting(tokens[i - 1]))
                        else:
                            p1 = self.get_posting(tokens[i - 1])

                    if tokens[i + 1] == "NOT" and i + 2 < len(tokens):
                        p2 = self.complement(self.get_posting(tokens[i + 2]))
                        i += 2
                    else:
                        p2 = self.get_posting(tokens[i + 1])
                        i += 1

                    if tempResult is None:
                        tempResult = p1

                    print(len(tempResult))
                    print(len(p2))
                    processingCost += min(len(tempResult), len(p2))
                    tempResult = self.intersect(tempResult, p2)
                    print(processingCost)
                    # print(temp)
                    # print()

                elif tokens[i].upper() == "OR":
                    if tempResult is None:
                        if i - 2 >= 0 and tokens[i - 2] == "NOT":
                            p1 = self.complement(self.get_posting(tokens[i - 1]))
                        else:
                            p1 = self.get_posting(tokens[i - 1])

                    if tokens[i + 1] == "NOT" and i + 2 < len(tokens):
                        p2 = self.complement(self.get_posting(tokens[i + 2]))
                        i += 2
                    else:
                        p2 = self.get_posting(tokens[i + 1])
                        i += 1

                    if tempResult is None:
                        tempResult = p1

                    # print(len(temp))
                    # print(len(p2))
                    processingCost += len(tempResult) + len(
                        p2
                    )  # at max processing cost can be this
                    tempResult = self.union(tempResult, p2)
                    print(processingCost)  # at min will be 0
                    # print(temp)
                    # print()
                i += 1

        result = [i + 1 for i in tempResult]
        return (result, processingCost)


# p = pre.Preprocessor("F:\IR\Assignment 01\Documents")
p = pre.Preprocessor('Abstracts')
p.PreprocessingChain()
b = BooleanQuery(p.dictionary, p.postings, p.noOfDocs)
print(b.totalDocs)
# print(b.get_posting('temporal'))
# print(b.get_posting('deep'))
# print(b.get_posting('learning'))
print()


print(b.ProcessQuery("image AND restoration"))
print()
print(b.ProcessQuery("deep AND learning"))
print()
print(b.ProcessQuery("autoencoders"))
print()
print(b.ProcessQuery("temporal AND deep AND learning"))
print()
print(b.ProcessQuery("time AND Series"))
print()
print(b.ProcessQuery("time AND series AND classification"))
print()
print(b.ProcessQuery("time AND series OR classification"))
print()
print(b.ProcessQuery("pattern"))
print()
print(b.ProcessQuery("pattern AND clustering"))
print()
print(b.ProcessQuery("pattern AND clustering AND heart"))
print()
