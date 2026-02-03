#I can only code python btw
#This is the fibonacci sequence
print("Fibonacci")
num1 = 0
num2 = 1
entries = 0
print(1)
while entries < 500:
  print(num1 + num2)
  num2 = num1 + num2
  num1 = num2 - num1
  entries = entries + 1
print("That's it for now, change the number in asterisks in 'while entries < *500*:' to make it longer")
