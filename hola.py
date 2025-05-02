# declaracion de variables
# nombre="link"
# edad=58
# ejemplo de concatenacion
# print("hola",nombre, "y su edad es",edad)



#multiplicacion de dos numeros
#n1=int(input("ingrese un numero"))
#n2=int(input ("ingrese un numero"))


#print(n1+n2)

#ingrese 3 numeros y promedielos

#Sprint("ingrese numero")

#n1=int(input())
#n2=int(input())
#n3=int(input())

#print(n1+n2+n3)

#clave=1951
#intentos=3
#contraseña=int(input("ingrese su contraseña"))

#while clave!=contraseña:
   #intentos-=1
#print("quedan",intentos,"intentos")
#print("error; clave invalida")
#contraseña=int(intput("ingrese su contraseña"))
#if intentos==1:

    # break

#if clave==contraseña:
    #print("clave aceptada")
#else:
    #print("sistema bloqueado")

#num=5

#while num!=0:
    #num=int(input("ingrese un numero(cero para salir)"))
    #if num % 2==0:
        #print(f"el numero{num} es par")
#else:

   #print(f"el numero{num} es impar")

#edad=-1

#while (edad <0 or edad >100):
    #edad=int(input("ingresa edad"))
    #if (edad <0 or edad>100):
        #print ("edad, edad fuera de rango{0,100}")
#print("edad ingresa exitosamente")


#numero=int(input("ingrese un numero"))

#if numero % 2 ==0:
    #print(f"el numero{numero} es par")
#else:
    #print(f"el numero{numero} es impar")

    #print("numeros pares:")
#for i in range(1,numero+1,2):
#    print(i)

#productos={}
#total_precio=0
#cantidad_productos=0

#def agregar_producto():
    #global total_recio ,cantidad_productos
#nombre_producto=input("ingrese el nombre del producto:")
#precio_producto=float(input("ingrese el precio del producto:"))
#productos[nombre_producto]=precio_producto
#total_precio+=precio_producto
#cantidad_productos+=1
#print(f"producto agregado:{nombre_producto}-precio: ${precio_producto:.2f}")





#clave correcta predevinida

#clave_correcta="guille_ulloa_vera:"


#while True:

  #clave_ingresada=input("ingrese clave:")
  #if clave_ingresada==clave_correcta:
     #print("clave correcta!, welcome: ")
     #break
  #print("Error. Ingrese clave correcta.")

# algoritmo liviano_pesado_citycar

# iniciamos la variable total
#total=0

# solicitamos el numero de vehiculos

#num=int(input("ingrese el numero de vehiculos:"))


#iteramos desde 1 hasta num
#for i in range(1,num+1):
    #print(f"\nvehiculo #{i}")
    #print("seleccione el tipo de vehiculo:")
    #print("1: auto liviano")
    #print("2: auto pesado")
    #print("3: citycar")

    #auto=int(input("opcion (1-3):"))

    #if auto == 2:
        #print("auto pesado, costo 5000$")
        #total+=5000
    #elif auto == 1:
        #print("auto liviano, costo 3500$")
        #total+=3500
    #elif auto == 3:
        #print("citycar, costo 1500$")
        #total+=1500
    #else:
        #print("error, seleccione una opcion valida")

        #mostrar resultados

#print("\nlas ganancias diarias son $", total)
#print("las ganancias diarias con iva (19%) son $", round(total*1.19, 2))