""" userinput=input("enter sentence:")

def countwords(sentence):
    words=sentence.split(" ") 
    num=len(words)
    return num
print(f"the number of words is:{countwords(userinput)}")

print(userinput) """

"""  day_of_week = input("what day is it? ")
if day_of_week == "thursday":
    print("correct")
else:
    print("incorrect") """


temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold')