print("===============================================================")
print("BIENVENIDO A LA HERRAMIENTA DE CUENTAS PARA TU LISTA DE MERCADO")
print("===============================================================")
print("                                                               ")
print("Para salir o terminar presiona 0")
print("                                                               ")

lista = []
i = 1

while i > 0:
    i = int(input("Digite el precio del producto $: "))
    lista.append(i)
print(lista)
sumList = sum(lista)
print("--------------------------------------------------------------")
print("Tu lista va en los $",sumList)
print("--------------------------------------------------------------")
