import random

# premios = {
#     "💎": 10,
#     "⭐": 7,
#     "🍒": 5,
#     "🍋": 3
# }

simbolos = [
    *["🍋"] * 40,
    *["🍒"] * 20,
    *["🍇"] * 10,
    *["🔔"] * 10,
    *["🍀"] * 5,
    "⭐", "⭐",
    "💎"
]

def tragaMonedas(saldo):
    print("")
    print("TRAGAMONEDAS")
    print("-------------------------------")

    while True:
        simbolo1 = random.choice(simbolos)
        simbolo2 = random.choice(simbolos)
        simbolo3 = random.choice(simbolos)

        print("")
        apuesta = int(input("Ingrese su apuesta (Para salir ingrese 0 ): "))
        print("")

        if apuesta > saldo:
            print("")
            print("No tienes suficientes dinero")
            continue
        elif apuesta == 0:
            return saldo
        elif apuesta < 0:
            print("")
            print("Ingrese un numero adecuado")
            continue

        saldo -= apuesta
        print("-------------------------------")
        print(f"| {simbolo1} | {simbolo2} | {simbolo3} |")
        print("-------------------------------")
        print("")


        if simbolo1 == simbolo2 == simbolo3:
            if simbolo1 == "💎":
                print("JACKPOT DE DIAMANTES!!")
                print(f"Usted gana {apuesta * 500}")
                saldo += apuesta * 500

            elif simbolo1 == "⭐":
                print("TRIPLE DE ESTRELLAS!!")
                print(f"Usted gana {apuesta * 100}")
                saldo += apuesta * 100

            elif simbolo1 == "🍇":
                print("TRIPLE DE UVAS!!")
                print(f"Usted gana {apuesta * 25}")
                saldo += apuesta * 25

            elif simbolo1 == "🔔":
                print("TRIPLE DE CAMPANAS!!")
                print(f"Usted gana {apuesta * 10}")
                saldo += apuesta * 10

            elif simbolo1 == "🍒":
                print("TRIPLE DE CEREZAS!!")
                print(f"Usted gana {apuesta * 5}")
                saldo += apuesta * 5

            elif simbolo1 == "🍋":
                print("TRIPLE DE LIMONES !!")
                print(f"Usted gana {apuesta * 2}")
                saldo += apuesta * 2

        elif simbolo1 == simbolo2 or simbolo2 == simbolo3 or simbolo1 == simbolo3:

            if simbolo1 == simbolo2:
                repetido = simbolo1
            elif simbolo2 == simbolo3:
                repetido = simbolo2
            else:
                repetido = simbolo1

            if repetido == "🍋":
                print("Dos limones.")
                print("No ganas nada.")

            elif repetido == "🍒":
                print("Dos cerezas.")
                print("Recuperas lo apostado.")
                saldo += apuesta

            elif repetido == "🍇":
                print("Dos uvas.")
                print(f"Usted gana {apuesta * 2}")
                saldo += apuesta * 2

            elif repetido == "🔔":
                print("Dos campanas.")
                print(f"Usted gana {apuesta * 3}")
                saldo += apuesta * 3

            elif repetido == "🍀":
                print("Dos tréboles.")
                print(f"Usted gana {apuesta * 5}")
                saldo += apuesta * 5

            elif repetido == "⭐":
                print("Dos estrellas.")
                print(f"Usted gana {apuesta * 20}")
                saldo += apuesta * 20

            elif repetido == "💎":
                print("Dos diamantes.")
                print(f"Usted gana {apuesta * 100}")
                saldo += apuesta * 100
        else:
            print("Perdiste, Vuelve a intentarlo")

        print("")
        print(f"Saldo actual: {saldo}")
