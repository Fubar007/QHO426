name = input("Enter your name: ")

#len() - function that returns the lenght of string*
#if, elif, else use :doua puncte, after the cmd line

if len(name) > 9: 
  print("Your name is way to long to rember. Can I use a nickname please?")
  print("This prints too!")
elif len(name) <= 3:
  print("That is very short - easy to rember")
elif name == "Martha":
  print("Why did you say that name?!")
else:
  print("Your name is pretty short!")
print("Nice to meet you anyway, {}!" .format(name))

