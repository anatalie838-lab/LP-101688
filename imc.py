import os
os.system("cls")
peso = float(input("\nInsira seu peso (em KG): "))
altura = float(input("\nInsira sua altura: "))


peso_vezes_peso = altura * altura 
imc = peso / peso_vezes_peso


if imc >= 40:
    print(f"\nseu imc é {imc: .1f}")
    print(f"\Obesidade III (mórbida)")
elif imc >= 35:
    print(f"\nseu imc é {imc: .1f}")
    print(f"\Obesidade II (mórbida)")   
elif imc 30:
    print(f"\nseu imc é {imc: .1f}")
    print(f"\Obesidade I (mórbida)")   
elif imc 25:
    print(f"\nseu imc é {imc:.1f}")
    print(f"\nlevemente acima do peso")
elif imc 18.6:
    print(f"\nseu imc {imc:.1f}")
    print("\npeso ideal!")
else:
    print(f"\nseu imc é{imc:.1f}")
    print("\nabaixo do peso")

