sentence=input("this is a sentence")

def count(sentence):
    words=sentence.split()
    return len(words)
   
print("number of words in sentence")