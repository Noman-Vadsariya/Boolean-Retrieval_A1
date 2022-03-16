from nltk.stem import PorterStemmer
ps = PorterStemmer()
  
words = ["network", "networks", "networking", "networked","neural","information","features","tracking"]
for w in words:
    print(ps.stem(w))