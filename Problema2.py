"""Función recursiva"""

"""suma"""
def sumar_todo_de_ida(lista, pi, pf, suma_acumulada):
    
    if pi > pf:
        return suma_acumulada
        
    nueva_suma = suma_acumulada + lista[pi]
    
    return sumar_todo_de_ida(lista, pi + 1, pf, nueva_suma)


"""Entradas principales de datos"""

tamano = int(input("¿Cuantos numeros tendra la lista?: "))

mi_lista = []
for i in range(tamano):
    numero = int(input(f"Ingrese el numero para la posicion {i + 1}: "))
    mi_lista.append(numero)
    
print("\nTu lista es:", mi_lista)

pos_inicial = 0
pos_final = len(mi_lista) - 1

resultado = sumar_todo_de_ida(mi_lista, pos_inicial, pos_final, 0)

print("Resultado de la suma:", resultado)