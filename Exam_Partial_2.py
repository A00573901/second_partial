#https://replit.com/join/hxbboiaceg-javiergarza12
def ruby():
  print("Ruby daily care programm.")
  print("Enter the actual temperature in Celsius degrees:")
  temp = int(input())
  if temp >= 20 and temp <= 25:
    print("Good conditions.")
  elif temp < 20:
    print("Bring Ruby inside the house!")
  elif temp > 25:
    print("Bring Ruby inside the house and turn on the fan!")

  print("What day is today?")
  day = input()
  if day == "tuesday" or day == "thursday" or day == "saturday":
    print("Water Ruby!")
  elif day == "monday" or day == "wednesday" or day == "friday" or day == "sunday":
    print("You don´t need to water Ruby.")

  print("What is the humidity right now?")
  hum = int(input())
  if hum >= 20 and hum <= 22:
    print("Suitable conditions.")
  elif hum < 20:
    print("You should water Ruby!")
  elif hum > 22 and day == "monday" or day == "wednesday" or day == "friday" or day == "sunday":
    print("It´s not necesary to water Ruby.")
  elif hum > 22 and day == "tuesday" or day == "thursday" or day == "saturday":
    print("Do nothing")
    
ruby()
