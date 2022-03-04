print("How many bars should be charged?")
bars = int(input())
b = 0
while b < bars:
  b += 1
  print(f"Charging ", "\u2666"*bars)
print("\nThe battery is fully charged!")