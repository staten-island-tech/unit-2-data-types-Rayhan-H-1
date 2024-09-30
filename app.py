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


""" def find_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


number = int(input("Enter a number: "))


factors = find_factors(number)
print(f"The factors of {number} are: {factors}") """


""" food = "pizza:"
name = "Spongebob:"
adjective = "joyful:"
noun = "ballon:"
verb1 = "walking:"
verb2 = "Jumping: "
verb3 = "running:"


madlib = f"It was {food} day at school, and {name} was super {adjective} for lunch. \
But when they went outside to eat, a {noun} stole their {food}! \
{name} chased the {noun} all over school. They {verb1}, {verb2}, and {verb3} through the playground. \
Then they tripped on their {noun} and the {noun} escaped! Luckily, {name}'s friends were willing to share their {food} with them."



print(madlib)
 """

def greatest_common_factor(num1, num2):
   
    if num1 < num2:
        smaller = num1
    else:
        smaller = num2

   
    gcf = 1

    for i in range(1, smaller + 1):
    
        if num1 % i == 0 and num2 % i == 0:
            gcf = i

    return gcf


num1 = 88
num2 = 64444848
result = greatest_common_factor(num1, num2)
print(f"The greatest common factor of {num1} and {num2} is: {result}")

