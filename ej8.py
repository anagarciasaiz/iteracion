import tabulate

def analizar_cadena():
    separador = input("Introduce el separador que desea utilizar: ")
    cadena = input("Introduce un texto para analizar: ")
    subcadenas = cadena.split(separador)
    tabla = []
    
    for i, subcadena in enumerate(subcadenas):
        tabla.append([i+1, subcadena])
    
    headers = ["Numero", "Subcadena"]
    print(tabulate.tabulate(tabla, headers, tablefmt="fancy_grid", showindex=False))