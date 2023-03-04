# Historial de una cuenta corriente

operaciones = []  # Lista para almacenar el historial de operaciones
saldo = 0  # Saldo inicial de la cuenta corriente

cuenta_corriente = input("¿Desea abrir una cuenta corriente en el banco? (si/no): ")

if cuenta_corriente == "no":
    print("Usted ha elegido no abrir una cuenta corriente en nuestro banco.")
elif cuenta_corriente == "si":
    print("Debe abonar dinero en su nueva cuenta corriente.")
    dinero_ingresado = int(input("Por favor, ingrese el dinero deseado a abonar: "))
    saldo = dinero_ingresado
    operaciones.append(("abono", dinero_ingresado))

while True:
    operacion = input("¿Qué operación desea realizar? (consultar/retirar/abonar/salir): ")
    
    if operacion == "salir":
        print("Gracias por confiar en nuestro banco.")
        break
    
    elif operacion == "abonar":
        introducir_dinero = float(input("Introduzca el dinero que desea ingresar en su cuenta: "))
        saldo += introducir_dinero
        operaciones.append(("abono", introducir_dinero))
        print("Su saldo es de", saldo, "€")
    
    elif operacion == "consultar":
        print("El saldo de su cuenta es", saldo, "€")
    
    elif operacion == "retirar":
        retirar_dinero = float(input("Introduzca el dinero que desea retirar de su cuenta: "))
        if saldo >= retirar_dinero:
            saldo -= retirar_dinero
            operaciones.append(("retiro", retirar_dinero))
            print("Al retirar la cantidad de", retirar_dinero, "€, su saldo ha disminuido a un total de", saldo, "€")
        else:
            print("No tiene suficiente saldo para retirar esa cantidad.")
    
    else:
        print("Operación no válida. Por favor, elija entre consultar, retirar, abonar o salir.")
    
    if len(operaciones) > 0:
        suma_operaciones = sum([op[1] for op in operaciones])
        media_operaciones = suma_operaciones / len(operaciones)
        if media_operaciones > 10:
            print("La media del importe de los movimientos es superior al mínimo solicitado.")
        else:
            print("La media del importe de los movimientos es inferior al mínimo solicitado.")