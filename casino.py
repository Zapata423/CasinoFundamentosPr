from juego1 import dados
from juego2 import tragaMonedas

def menuPrincipal():
    print("")
    print("BIENVENIDO AL CASINO DE ZAPATA")
    while True:
        print("")
        print("-------------------------------")
        print("Menu Principal")
        print("1. Iniciar Seccion")
        print("2. Crear Jugador")
        print("3. Jugar como Invitado")
        print("4. Salir")
        print("-------------------------------")
        print("")

        opcion = input("Ingrese una opción: ")
        print("")
        print("")

        if opcion == "1":
            iniciarSecion()
        elif opcion == "2":
            crearJugador()
        elif opcion == "3":
            saldo = 100000
            menuJuegos(saldo)
        elif opcion == "4":
            print("Gracias por visitarnos, que tengas un feliz dia")
            break
        else:
            print("")
            print("Opcion Invalida")


def menuJuegos(saldo):
    print("")
    while True:
        print("Nuestro Catalogo: ")
        print("")
        print("-------------------------------")
        print("1. Tragamonedas")
        print("2. Ruleta")
        print("3. Blackjack")
        print("4. Dados")
        print("5. Ver saldo")
        print("6. Historial")
        print("7. Volver") 
        print("-------------------------------")
        print("")

        opcion = input("Ingrese una opción: ")
        print("")
        print("")

        if opcion == "1":
            saldo = tragaMonedas(saldo)
        elif opcion == "2":
            ruleta()
        elif opcion == "3":
            blackjack()
        elif opcion == "4":
            saldo = dados(saldo)
        elif opcion == "5":
            saldo()
        elif opcion == "6":
            historial()
        elif opcion == "7":
            return
        else:
            print("")
            print("Opcion Invalida")



    

print(menuPrincipal())

