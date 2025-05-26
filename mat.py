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


total=0
bolsa=0

while True:
 print("'''seleccione una opcion'''" \
 " 1.- comprar " \
 " 2.- mostrar boleta " \
 " 3.- salir ")
 try:
         op = int(input("Opción: "))
 except ValueError:
            print("Por favor ingresa un número válido.")
            continue

 match op:
     case 1:
                               while True:


                                ("1.-comprar pantalones'''"
                                "2.-comprar tops'''"
                                "3.-comprar accesorios'''"
                                "4.-comprar calzado" 
                                "5.- volver al menu principal'''")
                                  
                                
                                op=int(input())
    
                                match op:
                                 case 1:
                    
                                        print("'''" 
                                 "1.- pantalon slim fit 20000$"
                                "2.- pantalon recto 30000$"
                                "3.- pantalon skinny 15000$"
                                "4.- shorts 20000$'''")

                                opc=int(input())
                                match opc:
                                    case 1:
                                        total+=20000
                                        bolsa+=1
                                    case 2:
                                        total+=30000
                                        bolsa+=1
                                    case 3:
                                        total+=15000
                                        bolsa+=1
                                    case 4:
                                        total+=20000
                                        bolsa+=1
                                    case 5:
                                      break
                                    case _:
                                      print("Su total parcial es ", total)
                                      print("producto invalido")
     case 2:
 
                                 print("'''" 
                                "1.- polera pique 15000$"
                                "2.- polera lisa 10000$"
                                "3.- polera deportiva 20000$"
                                "4.- polera de cr7 1000000$'''")
                                 opc=int(input())
                                 match opc:
                                     case 1:
                                        total+=15000
                                        bolsa+=1
                                     case 2:
                                        total+=10000
                                        bolsa+=1
                                     case 3:
                                        total+=20000
                                        bolsa+=1
                                     case 4:
                                        total+=1000000
                                        bolsa+=1
                                     case 5:
                                      break
                                     case _:
                                      1
                                      print("producto invalido")

     case 3:
                                 print("'''" 
                                "1.- reloj 25000$"
                                "2.- pulsera 1000$"
                                "3.- pulsera de plata 10000$"
                                "4.- cadena 5000$'''")
                                 opc=int(input())
                                 match opc:
                                     case 1:
                                        total+=25000
                                        bolsa+=1
                                     case 2:
                                        total+=1000
                                        bolsa+=1
                                     case 3:
                                        total+=10000
                                        bolsa+=1
                                     case 4:
                                        total+=5000
                                        bolsa+=1
                                     case 5:
                                      break
                                     case _:
                                      print("producto invalido")


     case 4:
                                 print("'''" 
                                "1.- zapatillas puma 45000$"
                                "2.- zapatos de vestir 60000$"
                                "3.- chalas 3000$"
                                "4.- botas 80000$'''")
                                 opc=int(input())
                                 match opc:
                                     case 1:
                                        total+=45000
                                        bolsa+=1
                                     case 2:
                                        total+=60000
                                        bolsa+=1
                                     case 3:
                                        total+=3000
                                        bolsa+=1
                                     case 4:
                                        total+=80000
                                        bolsa+=1
                                     case 5:
                                      break
                                     case _:
                                      print("producto invalido")
                                      break
                      
                 
                 
     case 2:
                print(f'''
                    ------0------
                    el total de articulos es{bolsa}
                    su total neto es{total}
                    su total mas IVA es{total*1.19}
                    gracias por venir vuelva pronto
                    ------0------''')
     case 3:
                break
     case _:
             print("opcion invalida")
        

     
