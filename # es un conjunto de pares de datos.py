# es un conjunto de pares de datos

# dic={
#     "nombre":"mel broks",
#     "numero": 945453443,
#     "casado":True,
# }

# # print(dic)

# for key,value in dic.items():
#     print(key,value)

# dic["ciudad"]="talca"

# for key,value in dic.items():
#     print(key,value)

# dic["casado"]=False

# for key,value in dic.items():
#     print(key,value)

# frutas={
#     "sandia": 3000,
#     "manzana": 1500,
#     "naranja": 1000
# }
# print(frutas)
# fruta=input("ingrese una fruta ")
# precio=int(input("ingrese el precio "))

# frutas[fruta]=precio

# print(frutas)
# fruta=input("ingrese una fruta ")
# precio=int(input("ingrese el precio "))

frutas={
    "sandia": 4500,
    "pera": 1000,
    "naranja": 1500

}
print(frutas)
fruta=input("ingrese una fruta ")
precio=int(input("ingrese precio "))

frutas[fruta]=precio

print(frutas)
fruta=input("ingrese una fruta ")
precio=int(input("ingrese precio "))

frutas[fruta]=precio

print(frutas)
frutas["sandia"]=5000

for key,value in frutas.items():
    print(key,value)

fruta=input("elimine una fruta ")
frutas.pop(fruta)

print(frutas)




