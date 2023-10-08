# https://replit.com/join/bdaqpzidfk-javiergarza12

import random

def discounts():
  print("Walmart autopay service")
  print("Enter the price of the unit")
  price = float(input())
  print("Now enter the category indicated by the label (a, b or c)")
  category = input()
  if category == "a":
    print("category a has a 10% discount")
    print("enter the amount of units")
    units = int(input())
    if int(units) > 10:
      print("Good, another 5% discount")
      disc15 = (float(price)*float(units))*(float(15/100))
      totalprice2discounts = (float(price)*float(units))-(float(disc15))
      print("Total price is",totalprice2discounts)
    elif int(units) < 10:
      disc10 = (float(price))*(float(units))*(float(10/100))
      totalprice = (float(price)*float(units))-(float(disc10))
      print("Total price is",totalprice)
  if category == "b":
    print("category b has a 5% discount")
    print("enter the amount of units")
    units2 = int(input())
    if int(units2) > 10:
      print("Good, another 5% discount")
      discc10 = (float(price)*float(units2))*(float(10/100))
      totalprice2discount = (float(price)*float(units2))-(float(discc10))
      print("Total price is",totalprice2discount)
    elif int(units2) < 10:
      disc5 = (float(price))*(float(units2))*(float(5/100))
      totalprice2 = (float(price)*float(units2))-(float(disc5))
      print("Total price is",totalprice2)
  if category == "c":
    print("category a has a 2% discount")
    print("enter the amount of units")
    units3 = int(input())
    if int(units3) > 10:
      print("Good, another 5% discount")
      disc7 = (float(price)*float(units3))*(float(7/100))
      totalprice2discountss = (float(price)*float(units3))-(float(disc7))
      print("Total price is",totalprice2discountss)
    elif int(units3) < 10:
      disc2 = (float(price))*(float(units3))*(float(2/100))
      totalprice3 = (float(price)*float(units3))-(float(disc2))
      print("Total price is",totalprice3)

  discounts()

def exercise():
  print("I´m your new digital coach")
  print("Please enter your weigh in kilograms (what the heck is a pound)")
  weigh = float(input())
  print("And now tell me the time you spend doing an exercise (in minutes)")
  time = int(input())
  print("Enter the exercise")
  print("Note here are the exercises I can calculate")
  print("running, cycling, swimming, jumping, walking")
  ex = input()
  if ex == "running":
    print("Okay, let me calculate")
    calories = (float(weigh)*(float(1.03)))
    total = float(calories)*(int(time)*float(0.2))
    print("total calories burned",total)
  if ex == "walking":
    print("Okay, let me calculate")
    calories2 = (float(weigh)*(float(0.73)))
    total2 = float(calories2)*(int(time)*float(0.68))
    print("total calories burned",total2)
  if ex == "cycling":
    print("Okay, let me calculate")
    calories3 = (float(weigh)*(float(2.2)))
    total3 = float(calories3)*(int(time)*float(0.049))
    print("total calories burned",total3)
  if ex == "jumping":
    print("Okay, let me calculate")
    calories = (float(weigh)*(float(1.53)))
    total = float(calories)*(int(time)*float(0.3))
    print("total calories burned",total)
  if ex == "swimming":
    print("Okay, let me calculate")
    calories = (float(weigh)*(float(1.25)))
    total = float(calories)*(int(time)*float(0.112))
    print("total calories burned",total)

exercise()

def studenten():
  print("Enter the name of the student")
  student = input()
  print("Enter student grade")
  grade = int(input())
  return student, grade
  
print("How many students are in the class?")
students = int(input())
studenti = []
grades = []

for _ in range(students):
  student, grade = studenten()
  studenti.append(student)
  grades.append(grade)
print(studenti)
print(len(studenti))
for w in range(len(studenti)):
  student = studenti[w]
  grade = grades[w]
  print("Student",student,"Grade",grade)
for grade in grades:
  if grade < 60:
    print("A student has failed")
  elif grade > 60:
    print("A student has passed")
average = sum(grades) / len(grades)
print("classroom average",average)
max = max(grades)
min = min(grades)
print("Higest note",max,"lowest note",min)

def roleplay():
  dice1 = random.randint(1,20)
  dice2 = random.randint(1,20)
  dice3 = random.randint(1,20)
  
  print("Ready for the adventure player?")
  print("Welcome to starships")
  print("Choose your role: 1.- Pirate 2.- Mercenary 3.- Assasin")
  choose = input()
  if choose == "1":
    print("You are a pirate: main weapon sword")
    print("You are close to another ship and you attack, how does it goes?")
    print("You roled the dice")
    print(dice1)
    if (dice1) < 12:
      print("The other ship result victorious and stole your things, you lose")
    else:
      print("You win and stole all their things")
  
  if choose == "2":
    print("You are a mercenary: main weapon axe")
    print("You are payed to kill a player, how does it goes?")
    print("You roled the dice")
    print(dice2)
    if dice2 < 8:
      print("The other player killed you and lost the contract and your things")
    elif dice2 < 14:
      print("Player managed to escape and you lost the contract")
    else:
      print("You succesfully killed the player and earned a lot of money")
    
  if choose == "3":
    print("You are an assasin: main weapon knife")
    print("You are about to destroy an enemy team, how does it goes?")
    print("You roled the dice")
    print(dice3)
    if (dice3) < 15:
      print("You failed the attack, other team noticed and easily killed you")
    else:
      print("You manage to take down everyone and get a lot of things")
      
roleplay()
