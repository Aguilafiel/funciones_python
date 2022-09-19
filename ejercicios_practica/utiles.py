##funciones utiles

# impimir mayor
def imprimir_mayor(numero_1, numero_2):
    print("Funcion imprimir mayor")
    if numero_1 > numero_2:
        print(numero_1 , 'es mayor que' , numero_2)
    else:
        print(numero_2, ' es mayor que' , numero_1)


#promedio
def promedio(numeros):
    print("Funcion promedio")
    resultado = 0
    for numero in numeros: 
        sumatoria_numeros = sum(numeros)
        cantidad_numeros = len(numeros)
        promedio = sumatoria_numeros / cantidad_numeros
        if cantidad_numeros == 0:
            print('No se ingresaron numeros en la lista en la lista')
        else:
            resultado = promedio

    return resultado

#ordenar de menor a mayor
def ordenar(numeros):
    lista_ordenada = sorted(numeros)
    return lista_ordenada

# genera datos para ingresar en una lista
def generar_invitados(cantidad_invitados):
    lista_invitados  = []
    for cantidad in range(cantidad_invitados):
        nombre = str(input('ingrese el nombre de un invitado:'))
        lista_invitados.append(nombre)
        
    return lista_invitados

