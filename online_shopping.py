def online_shopping():
  print("Thanks for using Chop-a-zon!")
  print("Please enter the total of your purchase")
  totalp = int(input())
  if totalp < 100:
    print("Today you are getting a 5% discount!")
    print("Do you have a membership with us?")
    yesno = input()
    if yesno == "yes":
      print("Great another 5% discount")
      tota = float(totalp)*float(10/100)
      total1 = float(totalp)-float(tota)
      print("Your total is",total1)
    if yesno == "no":
      print("Ok, let´s continue")
      tota = float(totalp)**float(5/100)
      total1 = float(totalp)-float(tota)
      print("Your total is",total1)
  
  if totalp > 100:
    print("Today you are getting a 10% discount!")
    print("Do you have a membership with us?")
    yesno1 = input()
    if yesno1 == "yes":
      print("Great another 5% discount")
      totab = float(totalp)*float(15/100)
      total3 = float(totalp)-float(totab)
      print("Your total is",total3)
    if yesno1 == "no":
      print("Ok, let´s continue")
      totab2 = float(totalp)*float(10/100)
      total2 = float(totalp)-float(totab2)
      print("Your total is",total2)
online_shopping()
