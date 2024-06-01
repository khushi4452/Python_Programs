first = input("first input number:")
operator = input("enter operator  (+,-,*,/,%): ")
second = input("second input number:")

first = int(first)
second = int(second)

if operator == "+":
    print (first + second)

if operator == "-":
    print (first - second)  

if operator == "*":
    print (first + second)

if operator == "/":
    print (first + second)

if operator == "%":
    print (first + second)

else:
    print("invalid operator")



