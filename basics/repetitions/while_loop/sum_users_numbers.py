print("How many numbers should I sum up?")
n = int(input())

while n >= 0:
  print(f"Print enter number {n} of {n}:")
  n=int(input())
  n -= 1

#Solution choice
print("How many numbers should I sum up?")
n = int(input())
sum = 0
total = 0
while sum < n:
  print("Please enter number", sum, "of", n, ":")
  number = int(input())
  total = total + number
  sum = sum + 1
print("The answer is", total)