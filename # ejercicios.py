 #ejercicios.py
# q = 0
# j = 0
# l = 0

# total = 0
# carrito = 0
# findesc = 0

# while True:
#     print("bienvenido al super")
#     op = int(input('''
#             seleccione una opcion
#             1.- comprar
#             2.- mostrar boleta
#             ''' ))

#     match op:
#         case 1:
#             while True:
#                 op = int(input('''
#                         seleccione una opcion 
#                         1.- queso 2000$ 
#                         2.- jamon 4000$
#                         3.- lechuga 2500$
#                         4.- comprar y salir '''))

#                 match op:
#                     case 1:
#                         total += 2000
#                         carrito += 1
#                     case 2:
#                         total += 4000
#                         carrito += 1
#                     case 3:
#                         total += 2500
#                         carrito += 1
#                     case 4:
#                         print("Desea salir")
#                         break

#         case 2:
#             while True:
#                 desc = input("¿Tiene descuento? (si/no): ")
#                 if desc == "si":
#                     cod = input("Ingrese el código del descuento: ")
#                     if cod == "joto":
#                         findesc = total * 10 / 100
#                         break
#                 if desc == "no":
#                     break

#             hola = total - findesc
#             print(f'''
#                  ------0------
#                  El descuento es: {total * 10 / 100}
#                  Total de productos: {carrito}
#                  Total neto: {total}
#                  Total + IVA: {total * 1.19}
#                  Precio a pagar con descuento: {hola}
#                  Gracias por su compra
#                  ¿Desea seguir comprando?
#                  Chauuuu''')

#             op = int(input(''' ¿Desea seguir comprando?
#                           1.- sí
#                           2.- no
#                           '''))

#             if op == 2:
#                 print("Gracias por su compra")
#                 break

# total=0
# bolsa=0
# desc=0

# while True:
#     print("bienvenido a la tienda")
#     op=int(input('''
#                 1.-comprar
#                 2.-mostrar boleta
#                 '''))
#     match op:
#         case 1:
#             while True:
#                 op = int(input('''
#                         selecione una opcion
#                         1.- polera 15000$
#                         2.- pantalon 20000$
#                         3.- poleron 25000$
#                         4.- zapatillas 50000$
#                         5.- comprar y salir
#                             '''))
#                 match op:
#                     case 1:
#                         total+= 15000
#                         bolsa += 1
#                     case 2:
#                         total+= 20000
#                         bolsa+= 1
#                     case 3:
#                         total+= 25000
#                         bolsa+= 1
#                     case 4:
#                         total+= 50000
#                         bolsa+= 1
#                     case 5:
#                         print("desea salir de la compra?")
#                         break

#         case 2:
#             while True:
#                 desc=input("¿tiene descuento? (si/no):")
#                 if desc == "si":
#                     cod = input("ingrese codigo del descuento ")
#                     if cod == "yeah":
#                         desc = total * 10 / 100
#                         break
#                 if desc == "no":
#                     break
#             hello = total - desc
#             print(f'''
#                     ------0------
#                     el descuento es: {total * 10 / 100}
#                     total de productos es: {bolsa}
#                     total neto es: {total}
#                     total + iva: {total * 1.19}
#                     precio a pagar con descuento : {hello}
#                     gracias por su compra
#                     desea seguir comprando?
#                     adiosssss''')
#             op = int(input(''' desea seguir comprando?
#                             1.- si
#                             2.-no
#                             '''))
            
#             if op == 2:
#                 print("gracias por su compra")
#                 break


# total=0
# bolsa=0
# desc=0

# while True:
#     print("bienevenido a la tienda de moda que desea? ")
#     op=int(input(''' seleccione una opcion
#                  1.- comprar
#                  2.- mostrar boleta
#                  '''))
#     match op:
#         case 1:
#             while True:
#                 op=int(input('''
#                              1.- jeans
#                              2.- tops
#                              3.- chaquetas
#                              4.- calzado
#                              5.- salir
#                              '''))
#                 match op:
#                     case 1:
#                         while True:
#                             op=int(input('''
#                                          1.- skinny jeans 15000$
#                                          2.- slim fit jeans 20000$
#                                          3.- regular fit jeans 25000$
#                                          4.- baggy fit jeans 30000$
#                                          5.- volver al menu principal
#                                          '''))
#                             match op:
#                                 case 1:
#                                     total+=15000
#                                     bolsa+=1
#                                 case 2:
#                                     total+=20000
#                                     bolsa+=1
#                                 case 3:
#                                     total+=25000
#                                     bolsa+=1
#                                 case 4:
#                                     total+=30000
#                                     bolsa+=1
#                                 case 5:
#                                     break
#                                 case _:
#                                     print("opcion invalida")
#                 match op:
#                     case 2:
#                         while True:
#                             op=int(input('''
#                                          1.- polo 5000$
#                                          2.- polera 2000$
#                                          3.- guayabera 5000$
#                                          4.- musculosa 3000$
#                                          5.- volver al menu principal
#                                          '''))
#                             match op:
#                                 case 1:
#                                     total+=5000
#                                     bolsa+=1
#                                 case 2:
#                                     total+=2000
#                                     bolsa+=1
#                                 case 3:
#                                     total+=5000
#                                     bolsa+=1
#                                 case 4:
#                                     total+=3000
#                                     bolsa+=1
#                                 case 5:
#                                     break
#                                 case _:
#                                     print("opcion invalida")
#                 match op:
#                     case 3:
#                         while True:
#                             op=int(input('''
#                                          1.- biker jacket 70000$
#                                          2.- blazer 100000$
#                                          3.- bomber jacket 15000$
#                                          4.- sueter 5000$
#                                          5.- volver al menu principal
#                                          '''))
#                             match op:
#                                 case 1:
#                                     total+=70000
#                                     bolsa+=1
#                                 case 2:
#                                     total+=100000
#                                     bolsa+=1
#                                 case 3:
#                                     total+=15000
#                                     bolsa+=1
#                                 case 4:
#                                     total+=5000
#                                     bolsa+=1
#                                 case 5:
#                                     break
#                                 case _:
#                                     print("opcion invalida")
#                 match op:
#                     case 4:
#                         while True:
#                             op=int(input('''
#                                          1.- zapatillas gucci 70000$
#                                          2.- zapatos de vestir 100000$
#                                          3.- botas 15000$
#                                          4.- chalas 3000$
#                                          5.- volver al menu principal
#                                          '''))
#                             match op:
#                                 case 1:
#                                     total+=70000
#                                     bolsa+=1
#                                 case 2:
#                                     total+=100000
#                                     bolsa+=1
#                                 case 3:
#                                     total+=15000
#                                     bolsa+=1
#                                 case 4:
#                                     total+=3000
#                                     bolsa+=1
#                                 case 5:
#                                     break
#                                 case _:
#                                     print("opcion invalida")
#                 match op:
#                     case 5:
#                         break
#         case 2:
#             while True:
#                 desc=input("¿tienes descuento? (si/no):")
#                 if desc == "si":
#                     cod = input("ingrese codigo de descuento ")
#                     if cod == "fashion":
#                         desc = total * 10 / 100
#                         break
#                 if desc == "no":
#                     break
#             gui = total - desc
#             print(f'''
#                   ------0------
#                   el codigo de descuento es {total * 10 / 100}
#                   total de productos es: {bolsa}
#                   total neto es: {total}
#                   total + iva: {total * 1.19}
#                   precio a pagar con descuento : {gui}
#                   gracias por su comprar
#                   desea seguir comprando?
#                   adiosssssss
#                   ''')
#             op=int(input(''' desea seguir comprando?
#                          1. -si
#                          2.- no
#                          '''))
#             if op == 2:
#                 print(" gracias por visitarnos!!!")
#                 break
                                    
                                    
# notas=[7.0,4.6,4.9, 7.0,5.6]
            
# while True:
#     print('''
#           1.- ingresar nota
#           2.- borrar nota
#           3.- mostrar notas
#           4.- sacar promedio, nota mayor y nota menor
#           5.- limpliar todas las notas
#           6.- salir''')
#     op=int(input("seleccione una opcion: "))
#     match op:
#         case 1:
#             n=float(input("por favor ingrese la nota: "))
#             notas.append(n)
#         case 2:
#             for i, nota in enumerate (notas):
#                 print(i+1,".-",nota)
#             borrar=int(input("seleccione la nota a borrar: "))
#             notas.pop(borrar-1)
#         case 3:
#             print(notas)
#         case 4:
#             total=0
#             sumanotas=sum(notas)
#             promedio = sumanotas/len(notas)
#             print("el promedio de notas es:",promedio)
#         case 5:
#             notas.clear()
#         case 6:
#             print("gracias por ver las notas ")
#             break

# def suma_arg(n1,n2):
#     print(n1+n2)

# def suma_ret(n1,n2):
#     print(n1,n2)
#     n1=int(input("ingrese un numero "))

# num1=int(input("ingrese un numero"))
# num2=int(input("ingrese otro numero"))
# suma_arg(num1,num2)
# print(suma_arg_ret(num1,num2))


# def cal_iva(n):
#     return n*1.19

# def cal_desc(precio, porc):
#     return precio*(porc/100)

# productos=[
#     {"nombre":"lapiz","precio":400},
#     {"nombre":"goma","precio":200},
#     {"nombre":"estuche","precio":1600},
# ]

# print(productos[2]["nombre"])

# '''el nombre del articulo lapiz tiene un precio de 400'''
# for item in productos:
#     print(f"el articulo {item["nombre"]} tiene un precio de {item["precio"]}")


# while True:
#     op=int(input(''' seleccione una opcion
#                  1.- agregar articulo
#                  2.- borrar altirculo
#                  3.- actualizar articulo 
#                  4.- mostrar listado de articulos 
#                  5.- actualizar articulo salir
#                  '''))
#     match op:
#         case 1:

#          herramientas=[
#     {"nombre":"martillo","precio":5000},
#     {"nombre":"hierro","precio":15000},
#     {"nombre":"madera","precio":10000},
#     ]

#     print(herramientas)
#     herramienta=input("agrege la herramienta ")
#     precio=int(input("ingrese un precio "))


#     print(herramientas)

#     for key,value in herramientas():
#      print(key,value)

while True:
    try:

        productos=[
        {"nombre":"martillo","precio":5000},
        {"nombre":"hierro","precio":15000},
        {"nombre":"madera","precio":10000},    
        ]

        print('''
              1.- agregar articulo
              2.- borrar articulo
              3.- actualizar articulo
              4.- mostrar listado de articulos
              5.- salir 
              ''')
    op=int(input("seleccione una opcion "))
    match op:
        case 1:
            nombre=input("nombre del articulo")
            precio=int(input("precio del articulo: "))
            productos.append({"nombre":nombre, "precio": precio})
        case 2:
            for n,producto in enumerate(productos):
                print(n+1, producto["nombre"], producto["precio"])
            borrar=int(input("que articulo desea borrar "))
            producto=input("elimine un producto ")
            productos.pop(borrar-1)

        case 3:
            for n,producto in enumerate(productos):
                print(n+1, producto["nombre"], producto["precio"])
                act=int(input(" que articulo desea actualizar? "))
                nombre=input("nombre del articulo : ")
                precio=int(input("precio del articulo "))
                productos[act-1]["nombre"]=nombre
                productos[act-1]["precio"]=precio

        case 4:
            for n,producto in enumerate(productos):
                print(n+1, producto["nombre"], producto["precio"])
        case 5:
            print("chaooooooo")
            break