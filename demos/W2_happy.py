h = input("Are you happy?")
k = input("Do you know it?")
if h.lower() == "yes" and k.lower() == "yes":
  print("Clap your hands!")
elif h.lower() == "yes" and k.lower() == "no":
  print("Show your happiness!")
else:
  print("Help is available. Talk to me!")

#.lower() . upper() - used to capital and lower case( case sensitive)  If you don't these function, the answer will be capital sensitive