print("How many mountains should I display?")
n = int(input())
for n in range(n, 0, -1):
  print("""
           __
          /  \\_  
         /^    \\
        /  ^    \\_
      _/ ^ ^     ^\\
     /  ^     ^    \\


     """)
print("Done!")

# Solution choice:

# Ask user for number of mountains
print("How many mountains should I display?")
mountains = int(input())

# Display mountains
print("\nDisplaying...")

for i in range(mountains):
    print("""
           __
          /  \\_  
         /^    \\
        /  ^    \\_
      _/ ^ ^     ^\\
     /  ^     ^    \\


     """)
print("Done!")