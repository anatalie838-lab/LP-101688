import os 

os.system("cls")

number1 = float(input("digite um numero:" ))
number2 = float(input("digite um numero:" ))

print ((number1 + number2) / 2)
print (number1 + number2)
print (number1*number2)

if number1 > number2:
    print(f"o numero maior é {number1} e o menor é {number2}")
else:
    print(f"o numero maior é {number2} e o menor é {number1}")    