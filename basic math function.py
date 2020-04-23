print("1. Add")
print("2. Subtract")
print("3. Multiplication")
print("4. Divide")
choice = int(input("Input your choice\n"))
if choice == 1:
    print(">>>>>>>>  Addition  <<<<<<<<<")
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter a Number: "))
    sum = n1 + n2
    print("Result: ", sum)
elif choice == 2:
    print(">>>>>>>>  Subtraction  <<<<<<<<<")
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter a Number: "))
    minus = n1 - n2
    print("Result: ", minus)
elif choice == 3:
    print(">>>>>>>>  Multiplication  <<<<<<<<<")
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter a Number: "))
    multi = n1 * n2
    print("Result: ", multi)
elif choice == 4:
    print(">>>>>>>>  Division  <<<<<<<<<")
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter a Number: "))
    div = n1 / n2  # '/' gives float answer
    div2 = n1 // n2  # '//' gives integer answer
    print("Result: ", div, div2)
else:
    print("!!!!!!!  Wrong Choice  !!!!!!!!!")
