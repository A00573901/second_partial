#https://replit.com/join/znpvcbrzer-javiergarza12
def health():
  things = int(input("How many things you eat in a day"))
  for i in range(things):
    print("What do you eat normally")
    food=input()
  
  healthy_food = ["fruits", "vegetables", "rice", "beans", "eggs", "meat", "milk", "water", "juice", "food"]
  count = 0
  for food in healthy_food:
    if food in healthy_food:
      count += 1

  if count == 0:
     print("You have a terrible diet, include more healthy things in it.")

  elif count >= 1:
     print("Your diet can improve far more than that, include more healthy food in it")
  elif count >= 4:
     print("You have a good diet but you can improve it.")

  elif count >= 6:
     print("You have an overall healthy diet keep it up!")

health()
