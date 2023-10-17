def mental_health():
  print("I´m a mental health quiz")
  print("I´m going to ask some questions and you have to answer with 'yes' or 'no'")
  stress = input("Have you ever experienced stress?")
  depression = input("Have you feel like you are not yourself lately?")
  anxiety = input("Do you feel likeyou are worring to much about something?")
  food = input("Do you skip foods?")
  if stress and depression and anxiety and food == "yes":
    print("You have a mental health issue, please seek professional help.")
    print("Remember you are important and asking for help isn´t something to be afraid")
  if stress and depression and anxiety and food == "no":
    print("You have an overall good mental health is optimal that you keep up that way!")
  if stress and anxiety == "yes":
    print("Seek for some professional help, remember if you are stressed and feel anxius")
    print("Try to search for a relaxing activity and have some time for yourself")
  elif food and depression == "yes":
    print("Seek for professional help, remember you are important and you need to eat well")
    print("Try to drink enough water and start eating slowly at your own rithm")
  if stress or anxiety == "yes":
    print("Remember that you really matter, seek professional help and dedicate time for yourself")
  if food == "yes":
    print("Seek professional help, remember is not healthy and you need to eat, even if it´s slowly")
  if depression == "yes":
    print("Remember you are important, try doing something outside and seek for help if needed")

mental_health()
