name = input("Enter your name: ")

#len() - function that returns the lenght of string*

if len(name) > 9: 
  print("Your name is way to long to rember. Can I use a nickname please?")
  print("This prints too!")
elif len(name) <= 3:
  print("That is very short - easy to rember")
else:
  print("Your name is pretty short!")
print("Nice to meet you anyway, {}!" .format(name))