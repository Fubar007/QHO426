print("What level of brightness is required?")
lvl = int(input())
if lvl % 2 == 0:
  print("Adjusting brightness...")
for lvl in range(0, lvl, 2):
  print(f"Beep's brightness level:{lvl+2}", lvl+2)
  print(f"Bop's brightness level:{lvl+2}", lvl+2)
