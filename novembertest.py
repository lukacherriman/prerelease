Number1 = int(input("Enter a whole number: "))
Number2 = int(input("Enter another whole number: "))

Temp1 = Number1
Temp2 = Number2
while Temp1 != Temp2:
    if Temp1 > Temp2:
        Temp1 = Temp1 - Temp2
    else:
        Temp2 = Temp2 - Temp1

Result = Temp1
print(f"{Result} is GCF of {Number1} and {Number2}")
