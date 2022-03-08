print("What phrase do you see?")
answer = input()

print("\nReversing...\nThe phrase is ", end="")
for i in range(len(answer) - 1, -1, -1):
     print(answer[i], end="")

