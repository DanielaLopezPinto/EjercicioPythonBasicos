print("---Alza del dolar---")
while True:
    try:
        dias= int(input("Ingrese el número de dias: \n"))
        if dias > 0:
            break  #El break sirve paraalir del bucle si la entrada es válida
        else:
            print("Ingrese un número de dias mayor que 0")
    except ValueError:             #ValueError se utiliza cuando una función espera un valor 
        print("Ingrese un número") #determinado pero recibe otro

precio = [0] * dias

#se hace un por para que el ususario ingrese el precio del dolar de cada dia
#y se va a guardar en la lista

for i in range(dias):
    while True:
        try:
            precio[i]=float(input(f"Ingrese el precio del dolar del dia {i + 1}: "))
            break  
        except ValueError:
            print("Ingrese un número valido")
        
#con esto se muestran los dias y su precio
for j in range(dias):
    print(f"Día {j + 1}: {precio[j]}")


alzaMayor = 0
for i in range(1, dias):
    alza=precio[i]-precio[i-1]
    alzaMayor= max(alzaMayor, alza) #max compara los elementos y muestra el mas grande

if alzaMayor > 0:
    print(f"La mayor alza fue de: {alzaMayor}")
else:
    print("No hubo alzas.")
