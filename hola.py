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

# while True:
#     try:
#         num=int(input("ingrese un numero mayor que 3"))
#         if num>3:
#             break
#     except Exception:
#       print("solo debe ingresar numeros")



# nombre=int(input("ingrese su nombre "))

# print("bienvenido al sistema, que desea comprar")

# cant=int(input("ingrese la cantidad de productos "))
# total=0
# for i in range(cant):
#     print(" ''' cuales productos van a llevar " 
#     "1 .- coca cola $2000" 
#     "2 .- pan $3500" 
#     "3.- queso $2500'''")

# print(input("ingrese su nombre "))

# def tipo(pro1,pro2,pro3,pro4):
# =int(input("ingrese el tipo de producto"),pro1,pro2,pro3,pro4)
#     pro1=int(input("ingrese el producto:  "))
#     pro2=int(input("ingrese otro producto:  "))
#     pro3=int(input("ingrese otro producto"))
#     pro4=int(input("ingrese otro producto"))
#     print("El resultado de la suma de los productos es", pro1+pro2+pro3+pro4)

#  def tipo():
#      while True:
#          op=int(input('''Seleccione una opcion
#                       1.- pan
#                      2.- fideos
#                      3.- tomates
#                      4.- coca cola
#                      5.- Salir
#                      '''))
 

# def compras(pro1,pro2,pro3):
#     print("El resultado de la compra es", pro1+pro2+pro3)

# def compra():
#     pro1=int(input("ingrese el producto:  "))
#     pro2=int(input("ingrese otro producto:  "))
#     pro3=int(input("ingrese otro producto"))
    # print("El resultado de la suma de los productos es", pro1+pro2+pro3)





#  def nombre():
#  nombre=int(input("Ingrese su nombre"))
#  print("bienvenido", nombre)

# def cantproductos():
#     p1=int(input("Ingrese un producto"))
#     p2=int(input("Ingrese otro producto"))
#     p3=int(input("ingrese otro producto"))
#     print("El resultado de la cant es", p1+p2+p3)
# def carrito():
#     n1=int(input("Ingrese un carrito"))
# def producto():
#      while True:
#          op=int(input('''Seleccione una opcion
#                       1.- pan
#                      2.- fideos
#                      3.- tomates
#                      4.- coca cola
#                      5.- Salir
#                      '''))
 
# def suma():
#     p1=int(input("Ingrese un producto"))
#     p2=int(input("Ingrese otro producto"))
#     p3=int(input("Ingrese otro producto"))
#     print("El resultado de la suma",p1+p2+p3)

 
# def calcu():
#     while True:
#         op=int(input('''Seleccione una opcion
#                     1.- ingrese su nombre
#                     2.- carrito
#                     3.- ingrese producto
#                     4.- sumar precios
#                     5.- Salir
#                     '''))

#         match op:
#             case 1:
#                 print("ingrese su nombre")
#                 nombre()
#             case 2:
#                 print("carrito")
#                 carrito()
#             case 3:
#                 print("ingrese producto")
#                 producto()
#             case 4:
#                 print("sumar precios")
#                 divi()
#             case 5:
#                 print("Salir")
#                 break
#             case _:
#                 print("Opcion invalida")




# cant=int(input("Ingrese el número de alumnos "))

# if cant <=5:

#  cantnotas=int(input("ingrese cantidad de notas del alumno 1 "))
# suma=0
# for j in range(cant):
#      print(f"Ingrese la nota numero {j+cantnotas }")
#      nota=float(input())
#      cantnotas=suma+nota
# suma=nota/cantnotas

# print(f"El promedio es {j+nota} ")

# if cant <=4:
#     print("alumno 1 aprobo")
# else:
#      print("alumno 1 reprobo")