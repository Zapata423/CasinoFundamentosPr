import random
def dados(saldo):

    print("")
    print("DADOS")
    while True:
        dado = random.randint(1, 6)
        print("")
        print("-------------------------------")
        print("Seleccione modo de juego")
        print("1. Mitad Superior (4 - 6)")
        print("2. Mitad Inferior (1- 3)")
        print("3. Par")
        print("4. Impar")
        print("5. Numero exacto")
        print("6. Volver")
        print("-------------------------------")
        print("")

        opcion = input("Ingrese una opción: ")
        print("")
        print("")
        
        
        if opcion == "6":
            return saldo
        apuesta = int(input("Ingrese su apuesta: "))

        if apuesta > saldo:
            print("No tienes suficientes dinero")
            continue
        
        if opcion == "5":
            numero = int(input("Elige un número del 1 al 6: "))
            
        print(f"Cayo el numero: {dado}")
        
        if opcion == "1":
            if dado >= 4:
                saldo += apuesta
                print("Ganaste")
            else:
                saldo -= apuesta
                print("Perdiste")
        elif opcion == "2":
            if dado <= 3:
                saldo += apuesta
                print("Ganaste")
            else:
                saldo -= apuesta
                print("Perdiste")   
        elif opcion == "3":
            if dado % 2 == 0:
                saldo += apuesta
                print("Ganaste")
            else:
                saldo -= apuesta
                print("Perdiste") 
        elif opcion == "4":
            if dado % 2 != 0:
                saldo += apuesta
                print("Ganaste")
            else:
                saldo -= apuesta
                print("Perdiste") 
        elif opcion == "5":
            if dado == numero:
                saldo += apuesta * 4
                print("Ganaste, ¡Número exacto!")
            else:
                saldo -= apuesta
                print("Perdiste") 
        else:
            print("")
            print("Opcion Invalida")
        print(f"Saldo actual: {saldo}")
