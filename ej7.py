base = int(input("Introduce la base mayor o igual a 2: "))
numero = int(input("Escriba un número: "))

def edit(numero, base):
    if base < 2:
        print("Esta base no está permitida")
    elif base > 36:
        print(numero)
    else:
        while numero > 0:
            resto = numero % base
            if resto >= 10:
                letra = chr(ord('A') + resto - 10)
                print(letra, end='')
            else:
                print(resto, end='')
            numero = numero // base