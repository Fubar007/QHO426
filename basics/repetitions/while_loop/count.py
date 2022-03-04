print("How many live cables must I avoid?")
live_cables = int(input())
lc = 0
while lc < live_cables:
  lc += 1
  print(f"Avoiding...Done {lc} live cable avoided!")
print("All lives cable have been avoided")