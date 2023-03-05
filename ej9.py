import tabulate

def tabla(diccionario):
    table=[]
    for i in range(0, len(diccionario)):
        table.append(list(diccionario[i:i+1]))
    headers=["i", "diccionario", "anterior", "siguiente"]
    print(tabulate.tabulate(table, headers=headers, tablefmt="fancy_grid", showindex=True))

def palabra():
    diccionario=["avion", "tren", "auto", "camion"]
    tabla(diccionario)
    print("\n")
    diccionario.sort()
    print("Ordenadas alfabéticamente: ")
    tabla(diccionario)

# Se llama a la función 'palabra' para mostrar la tabla correspondiente.
palabra()
