import random, time

while True:
    try:
        perros=int(input("cuantos perros van a la caza? "))
        while perros<1:
            print("Solo valores enteros positivos")
            perros=int(input("cuantos perros van a la caza? "))
        cuota=3
        pCumplen=0
        for p in range (perros):
            time.sleep(1)
            conejos=random.randint(0,6)
            if conejos>=cuota:
                print(f"El pero {p+1} capturó {conejos} conejos ")
                print("Se ganó un filete")
                pCumplen+=1
            else:
                print(f"El pero {p+1} capturó {conejos} conejos ")
                print("no hay filete para éste perro")
        print(pCumplen," perros llegaron a la cuota")
        print(perros-pCumplen," perros llegaron a la cuota")
        break
    except Exception:
        print("Solo debe poner numeros enteros ")