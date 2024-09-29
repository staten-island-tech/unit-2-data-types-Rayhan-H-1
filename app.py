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

""" 
temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

""" def even_odd(number):
 if number % 2==0:
     return "even"
 else:
     return "odd"
result=even_odd(8-)

print(result) """
""" 
def calculate_tip():
   
    bill = float(input("Enter the bill amount: "))
    
 
    service = input("Enter service quality (bad, okay, good, great): ")
    
 
    tip_percentages = {
        "bad": 0,
        "okay": 15,
        "good": 20,
        "great": 25
    }
    
  
    if service not in tip_percentages:
        return "Invalid service level. Please enter bad, okay, good, or great."
    #I put this code because relasticly a person might not type what is expected.
  
    tip_percentage = tip_percentages[service]
    
  
    tip = (tip_percentage / 100) * bill
  
    return tip

tip = calculate_tip()
print("Your tip amount is:", tip) """

