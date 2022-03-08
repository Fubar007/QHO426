print("What level of brightness is required?")
lvl = int(input())
if lvl % 2 == 0:
  print("Adjusting brightness...")
for lvl in range(2, lvl, 2):
  print(f"Beep's brightness level:{lvl}", "*" * lvl)
  print(f"Bop's brightness level:{lvl}", "*" * lvl)



#Solution choice:

print("What level of brightness is required?")
lvl = int(input())
print("Adjusting brightness...\n")
for i in range(2, lvl +1, 2):
  print(f"Beep's brightness level:{i}", "*" * i)
  print(f"Bop's brightness level:{i}", "*" * i)
