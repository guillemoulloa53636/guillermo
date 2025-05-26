# def comprar():
#      c=int(input("comprar "))
# def tipo():
#      t=int(input("seleccione tipo de prenda "))
# def pagar():
#      p=int(input("ir a pagar "))
# def boleta():
#      b=int(input("mostrar boleta "))
# def salir():
#      s=int(input("salir de la tienda "))


# total = 0
# bolsa = 0

# while True:
#     print("\n'''Seleccione una opción'''"
#           "\n1.- Comprar"
#           "\n2.- Mostrar boleta"
#           "\n3.- Salir")
#     try:
#         op = int(input("Opción: "))
#     except ValueError:
#         print("Por favor ingresa un número válido.")
#         continue

#     match op:
#         case 1:
#             while True:
#                 print("\n'''Seleccione una categoría:'''"
#                       "\n1.- Pantalones"
#                       "\n2.- Tops"
#                       "\n3.- Accesorios"
#                       "\n4.- Calzado"
#                       "\n5.- Volver al menú principal")

#                 try:
#                     categoria = int(input("Opción: "))
#                 except ValueError:
#                     print("Por favor ingresa un número válido.")
#                     continue

#                 if categoria == 5:
#                     break

#                 def post_compra():
#                     print(f"\n🛍️ Total parcial: ${total} | Artículos: {bolsa}")
#                     salir = input("¿Deseas salir de esta sección? (s/n): ").lower()
#                     return salir == 's'

#                 match categoria:
#                     case 1:
#                         while True:
#                             print("\n1.- Pantalón slim fit 20000$"
#                                   "\n2.- Pantalón recto 30000$"
#                                   "\n3.- Pantalón skinny 15000$"
#                                   "\n4.- Shorts 20000$"
#                                   "\n5.- Volver")
#                             try:
#                                 opc = int(input("Opción: "))
#                             except ValueError:
#                                 print("Entrada inválida.")
#                                 continue

#                             match opc:
#                                 case 1:
#                                     total += 20000
#                                     bolsa += 1
#                                 case 2:
#                                     total += 30000
#                                     bolsa += 1
#                                 case 3:
#                                     total += 15000
#                                     bolsa += 1
#                                 case 4:
#                                     total += 20000
#                                     bolsa += 1
#                                 case 5:
#                                     break
#                                 case _:
#                                     print("Producto inválido")
#                                     continue

#                             if post_compra():
#                                 break

#                     case 2:
#                         while True:
#                             print("\n1.- Polera pique 15000$"
#                                   "\n2.- Polera lisa 10000$"
#                                   "\n3.- Polera deportiva 20000$"
#                                   "\n4.- Polera de CR7 1000000$"
#                                   "\n5.- Volver")
#                             try:
#                                 opc = int(input("Opción: "))
#                             except ValueError:
#                                 print("Entrada inválida.")
#                                 continue

#                             match opc:
#                                 case 1:
#                                     total += 15000
#                                     bolsa += 1
#                                 case 2:
#                                     total += 10000
#                                     bolsa += 1
#                                 case 3:
#                                     total += 20000
#                                     bolsa += 1
#                                 case 4:
#                                     total += 1000000
#                                     bolsa += 1
#                                 case 5:
#                                     break
#                                 case _:
#                                     print("Producto inválido")
#                                     continue

#                             if post_compra():
#                                 break

#                     case 3:
#                         while True:
#                             print("\n1.- Reloj 25000$"
#                                   "\n2.- Pulsera 1000$"
#                                   "\n3.- Pulsera de plata 10000$"
#                                   "\n4.- Cadena 5000$"
#                                   "\n5.- Volver")
#                             try:
#                                 opc = int(input("Opción: "))
#                             except ValueError:
#                                 print("Entrada inválida.")
#                                 continue

#                             match opc:
#                                 case 1:
#                                     total += 25000
#                                     bolsa += 1
#                                 case 2:
#                                     total += 1000
#                                     bolsa += 1
#                                 case 3:
#                                     total += 10000
#                                     bolsa += 1
#                                 case 4:
#                                     total += 5000
#                                     bolsa += 1
#                                 case 5:
#                                     break
#                                 case _:
#                                     print("Producto inválido")
#                                     continue

#                             if post_compra():
#                                 break

#                     case 4:
#                         while True:
#                             print("\n1.- Zapatillas Puma 45000$"
#                                   "\n2.- Zapatos de vestir 60000$"
#                                   "\n3.- Chalas 3000$"
#                                   "\n4.- Botas 80000$"
#                                   "\n5.- Volver")
#                             try:
#                                 opc = int(input("Opción: "))
#                             except ValueError:
#                                 print("Entrada inválida.")
#                                 continue

#                             match opc:
#                                 case 1:
#                                     total += 45000
#                                     bolsa += 1
#                                 case 2:
#                                     total += 60000
#                                     bolsa += 1
#                                 case 3:
#                                     total += 3000
#                                     bolsa += 1
#                                 case 4:
#                                     total += 80000
#                                     bolsa += 1
#                                 case 5:
#                                     break
#                                 case _:
#                                     print("Producto inválido")
#                                     continue

#                             if post_compra():
#                                 break

#                     case _:
#                         print("Opción inválida")

#         case 2:
#             print(f'''
# ------ BOLETA ------
# Total de artículos: {bolsa}
# Total neto: ${total}
# Total con IVA (19%): ${round(total * 1.19, 2)}
# Gracias por su compra.
# --------------------
# ''')

#         case 3:
#             print("Saliendo del programa... ¡Hasta luego!")
#             break

#         case _:
#             print("Opción inválida")
