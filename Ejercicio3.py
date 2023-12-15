alimentos = [["A", "B", "C"],[270, 340, 390]]
monedas = [["0", "1", "2"],[10, 50, 100]]
cont=0
opcion=0
bandera=True
while(bandera):
    print("Elegir el producto")
    for i in alimentos[0]:
        print(f"\t{cont}. {i}") #muestra los productos 
        cont +=1
    try: 
        opcion=int(input("\n"))
        if opcion <= len(alimentos[0])-1 and opcion>=0: #len es un contador y se esta utilizando para
            bandera=False                                #para contar lo que hay dentro de la lista
        else:
            raise    #Error para terminar el programa
    except: 
        print("Ingrese un producto valido")
        bandera=True
    finally:
        cont= 0


precioProducto = alimentos[1][opcion] #saber cual es el precio según lo que 
#                                      elegimos en lo anterior
cantidad = 0

while cantidad < precioProducto: #mientas la cantidad de dinero ingresado 
    try:                         #sea menor al precio del prodcuto se ejecuta le programa
        print("Ingrese una moneda unicamente las siguientes")
        for i in monedas[1]:
            print(f"\t {i}")
        monedaIngresada = int(input())
        if monedaIngresada in monedas[1]:  #el in es para ver si lo que ingresamos 
            cantidad += monedaIngresada    #esta dentro de la lista de monedas
        else:
            raise
    except:
        print("Moneda no válida")       #El while se asegura de que una vez se pase 
        continue                        #del precio del producto calcule los vueltos           
#                                        y si no hay se termina el programa
vuelto = cantidad - precioProducto      #ya que pues no vamos a echar una cantidad
#                                        exagerada de monedas si se sabe el valor del productos
#                                        igualmente hay VARIOS TIPOS DE USUARIOS  
#                                        asi que mejor se evitan incovenientes con una condición


if vuelto > 0:                      
    print(f"Vuelto: {vuelto} pesos")
    print("Entregando monedas de vuelto:")
    
    for valorMoneda in sorted(monedas[1], reverse=True): #sorted se utiliza para organizar una lista
        cantidadMonedas = vuelto // valorMoneda
        if cantidadMonedas > 0:
            print(f"{cantidadMonedas} monedas de {valorMoneda} pesos")
            vuelto %= valorMoneda

print("¡Gracias por su compra!")           #En esta ultima parte lo que se hace es:
#                                           los vueltos se dividen en el valor de la moneda
#                                           que se almacena en valorMoneda que es la lista al reves.
#                                           Lo que esta haciendo es como una comparacion entonces almacena
#                                           valorMoneda la lista al reves empezando por 100, por ejemplo si los  
#                                           vueltos son 10 entonces va a ir comparando hasta que  la cantidad de monedas
#                                           se mayor a 0 entonces tendia que ser 10//10 que da 1 y asi
#                                           finaliza el programa 

