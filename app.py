userinput=input("enter sentence:")

def countwords(sentence):
    words=sentence.split(" ") 
    num=len(words)
    return num
print(f"the number of words is:{countwords(userinput)}")

print(userinput)
