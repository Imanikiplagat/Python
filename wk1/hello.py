x =int(input("Enter an integer x "))
y =int(input("Enter an integer y "))
operation =input("Choose an operation (+,-,*,/):")

if operation == '+':
    result = x + y
    answer =f"You chose addition: {result}"
elif operation == '-':
    result = x - y
    answer =f"You chose subtraction: {result}"
elif operation == '*':
    result = x * y
    answer =f"You chose multiplication: {result}"
if operation == '/':
    if y !=0:  
     result = x / y
     answer =f"You chose division: {result}"
    else:
       answer=f"Math error! Undefined"
print(answer)
