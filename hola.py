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

productos={}
total_precio=0
cantidad_productos=0

def agregar_producto():
    global total_recio ,cantidad_productos
nombre_producto=input("ingrese el nombre del producto:")
precio_producto=float(input("ingrese el precio del producto:"))
productos[nombre_producto]=precio_producto
total_precio+=precio_producto
cantidad_productos+=1
print(f"producto agregado:{nombre_producto}-precio: ${precio_producto:.2f}")

