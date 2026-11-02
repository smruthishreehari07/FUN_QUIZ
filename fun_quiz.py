questions = [

    # EASY
    ["In which direction does the sun rise?", "North", "South", "East", "West", "c"],

    ["How many days are there in a week?", "5", "6", "7", "8", "c"],

    ["Which animal is known as the King of the Jungle?", "Tiger", "Lion", "Elephant", "Leopard", "b"],

    ["How many months are there in a year?", "10", "11", "12", "13", "c"],

    ["Which is the largest animal in the world?", "Elephant", "Giraffe", "Blue Whale", "Shark", "c"],

    # EASY - MEDIUM
    ["Which country is famous for the Eiffel Tower?", "Italy", "France", "Germany", "Spain", "b"],

    ["How many players are there in a cricket team?", "9", "10", "11", "12", "c"],

    ["Which is the fastest land animal?", "Lion", "Cheetah", "Horse", "Deer", "b"],

    ["What do bees produce?", "Milk", "Silk", "Honey", "Wax only", "c"],

    ["Which is the smallest continent?", "Europe", "Australia", "Africa", "South America", "b"],

    # MEDIUM
    ["Which country is known as the Land of the Rising Sun?", "China", "Thailand", "Japan", "South Korea", "c"],

    ["How many rings are there in the Olympic symbol?", "4", "5", "6", "7", "b"],

    ["Which is the largest desert in the world?", "Sahara", "Gobi", "Antarctic Desert", "Arabian Desert", "c"],

    ["Which instrument is used to measure temperature?", "Barometer", "Thermometer", "Speedometer", "Hygrometer", "b"],

    ["Which bird is known for its ability to mimic human speech?", "Eagle", "Parrot", "Sparrow", "Penguin", "b"],

    # HARD
    ["Which is the only mammal capable of true flight?", "Flying squirrel", "Bat", "Ostrich", "Penguin", "b"],

    ["Which is the longest river in the world, according to the commonly cited traditional ranking?", "Amazon", "Nile", "Yangtze", "Mississippi", "b"],

    ["Which country gifted the Statue of Liberty to the United States?", "United Kingdom", "France", "Germany", "Italy", "b"],

    ["What is the currency of Switzerland?", "Euro", "Pound", "Swiss Franc", "Dollar", "c"],

    ["Which is the largest island in the world?", "Madagascar", "Greenland", "Borneo", "New Guinea", "b"]

]

prizes = [1000,5000,10000,15000,20000,25000,30000,35000,40000,45000,50000,55000,60000,65000,70000,75000,80000, 85000,90000, 100000]
i = 0 
print("Welcome to this fun quiz")
import time
time.sleep(2)
x=input("What is your name? ")
y=input(f"Hello {x} are you ready for your first question? (yes/exit) ")
if y=="yes":
    for question in questions:
        print(question[0]) 
        print(f"a. {question[1]}")
        print(f"b. {question[2]}")
        print(f"c. {question[3]}")
        print(f"d. {question[4]}")
        a = input("Enter your answer:")
        if(question[5] == a):
            print("Correct Answer")
            print(f"You won rupees {prizes[i]}")
            i +=1 
        else:
            print(f"oh oh oops Incorrect answer, the correct answer was {question[5]}")
            print("Better luck next time!\nThankyou for playing")  
            print("You won rupees",prizes[i-1]) 
            break
else:
    exit()           