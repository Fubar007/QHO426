print("How many bars should be charged?")
bars = int(input())
b = 0
while b < bars:
  b += 1
  print("Charging ", "\u2666"*b)

print("The battery is fully charged!")