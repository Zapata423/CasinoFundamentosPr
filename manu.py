# Proyecto: Análisis de exportaciones por región

# Elaborado por:
"""
Manuela Uribe Chavarriaga
Samuel Muñoz Restrepo
Juan Pablo Quintero Roldan
"""

# Librería para realizar gráficas
import matplotlib.pyplot as plt


"""
Lista de 4 posiciones.
La posición 0 representa las toneladas exportadas a América del Norte
La posición 1 representa las toneladas exportadas a Europa
La posición 2 representa las toneladas exportadas a Asia
La posición 3 representa las toneladas exportadas a Latinoamérica
"""
exportaciones = [0, 0, 0, 0]


# Opción 1: Registrar volumen inicial de exportaciones.
# Permite ingresar los valores iniciales de toneladas exportadas para cada región.
def registrarExportaciones():

    print("Registro de exportaciones")

    america = float(input("Ingrese toneladas de América del Norte: "))
    europa = float(input("Ingrese toneladas de Europa: "))
    asia = float(input("Ingrese toneladas de Asia: "))
    latinoamerica = float(input("Ingrese toneladas de Latinoamérica: "))

    # Validación para evitar valores negativos o mayores al tope establecido.
    if america < 0 or europa < 0 or asia < 0 or latinoamerica < 0:
        print("Error: no se permiten valores negativos.")

    elif america > 5000 or europa > 5000 or asia > 5000 or latinoamerica > 5000:
        print("Error: ningún valor puede superar 5000 toneladas.")

    else:
        exportaciones[0] = america
        exportaciones[1] = europa
        exportaciones[2] = asia
        exportaciones[3] = latinoamerica

        print("Datos registrados correctamente.")


# Opción 2: Consultar volumen actual de exportaciones
# Muestra los datos almacenados en la lista en forma de cuadrícula, organizados
def consultarExportaciones():

    print("-------------------------------")
    print("AN:", exportaciones[0], "| EU:", exportaciones[1])
    print("-------------------------------")
    print("AS:", exportaciones[2], "| LA:", exportaciones[3])
    print("-------------------------------")


# Opción 3: Actualizar exportaciones de una región específica
# Permite modificar el valor de toneladas exportadas de una sola región
def actualizarExportaciones():

    print("Actualizar exportaciones")
    print("1. América del Norte")
    print("2. Europa")
    print("3. Asia")
    print("4. Latinoamérica")

    region = int(input("Seleccione la región: "))
    nuevo = float(input("Ingrese el nuevo valor en toneladas: "))

    # Control de errores: no se aceptan valores negativos ni mayores a 5000.
    if nuevo < 0:
        print("Error: no se permiten valores negativos.")

    elif nuevo > 5000:
        print("Error: el valor no puede superar 5000 toneladas.")

    else:
        if region == 1:
            exportaciones[0] = nuevo
            print("Dato actualizado correctamente.")

        elif region == 2:
            exportaciones[1] = nuevo
            print("Dato actualizado correctamente.")

        elif region == 3:
            exportaciones[2] = nuevo
            print("Dato actualizado correctamente.")

        elif region == 4:
            exportaciones[3] = nuevo
            print("Dato actualizado correctamente.")

        else:
            print("Región inválida.")


# Opción 4: Comparar exportaciones entre regiones.
# Identifica cuál región tiene mayor y menor volumen exportado.
def compararExportaciones():

    regiones = ["América del Norte", "Europa", "Asia", "Latinoamérica"]

    # Aquí el programa empieza suponiendo que el primer valor de la lista es el mayor y también el menor
    mayor = exportaciones[0]
    menor = exportaciones[0]
    regionMayor = regiones[0]
    regionMenor = regiones[0]

    # El ciclo for recorre todas las posiciones de la lista y actualiza esos datos si encuentra uno mayor o menor
    for i in range(len(exportaciones)):

        if exportaciones[i] > mayor:
            mayor = exportaciones[i]
            regionMayor = regiones[i]

        if exportaciones[i] < menor:
            menor = exportaciones[i]
            regionMenor = regiones[i]

    print("Región con mayor exportación:", regionMayor, "con", mayor, "toneladas")
    print("Región con menor exportación:", regionMenor, "con", menor, "toneladas")


# Opción 5: Simular incremento de exportaciones
# Calcula un nuevo valor aplicando un porcentaje de aumento a una región seleccionada.
def simularIncremento():

    print("Simular incremento")
    print("1. América del Norte")
    print("2. Europa")
    print("3. Asia")
    print("4. Latinoamérica")

    region = int(input("Seleccione la región: "))
    porcentaje = float(input("Ingrese el porcentaje de incremento: "))

    # Validaciones para evitar errores lógicos
    if region < 1 or region > 4:
        print("Región inválida.")

    elif porcentaje < 0:
        print("Error: el porcentaje no puede ser negativo.")

    elif porcentaje > 100:
        print("Error: el porcentaje no puede superar el 100%.")

    else:
        valorActual = exportaciones[region - 1]
        nuevoValor = valorActual + (valorActual * porcentaje / 100)

        print("Valor actual:", valorActual)
        print("Nuevo valor simulado:", nuevoValor)


# Opción 6: Clasificación de regiones según volumen exportado.
# Clasifica una región como bajo, medio o alto volumen.
def clasificarRegion():

    print("Clasificación de regiones")
    print("1. América del Norte")
    print("2. Europa")
    print("3. Asia")
    print("4. Latinoamérica")

    region = int(input("Seleccione la región: "))

    if region < 1 or region > 4:
        print("Región inválida.")

    else:
        valor = exportaciones[region - 1]

        if valor < 500:
            print("Bajo volumen")

        elif valor <= 1500:
            print("Volumen medio")

        else:
            print("Alto volumen")


# Opción 7: Actualización masiva.
# Duplica el valor de todas las regiones usando un ciclo for.
def actualizarMasivamente():

    for i in range(len(exportaciones)):
        exportaciones[i] = exportaciones[i] * 2

    print("Todos los valores fueron duplicados correctamente.")


# Opción 8: Cargar datos desde archivo
# Lee un archivo llamado datos.txt y actualiza la lista con los valores encontrados
def cargarDesdeArchivo():

    archivo = open("datos.txt", "r")
    # la "r" abre el archivo datos.txt en modo lectura
    contenido = archivo.read()

    datos = contenido.split(",")
    # split(",") separa el contenido cada vez que encuentra una coma
    archivo.close()

    # Verifica que el archivo tenga exactamente cuatro datos.
    if len(datos) == 4:

        valor1 = float(datos[0])
        valor2 = float(datos[1])
        valor3 = float(datos[2])
        valor4 = float(datos[3])

        if valor1 < 0 or valor2 < 0 or valor3 < 0 or valor4 < 0:
            print("Error: el archivo contiene valores negativos.")

        else:
            exportaciones[0] = valor1
            exportaciones[1] = valor2
            exportaciones[2] = valor3
            exportaciones[3] = valor4

            print("Datos cargados correctamente desde el archivo.")

    else:
        print("Error: el archivo debe contener exactamente 4 valores.")


# Opción 9: Graficar exportaciones.
# Muestra los datos de la lista en una gráfica de barras.
def graficar():

    regiones = ["América Norte", "Europa", "Asia", "Latinoamérica"]

    plt.bar(regiones, exportaciones)
    ## Crea una gráfica de barras.
    # "regiones" representa los nombres que aparecerán en el eje X.
    # "exportaciones" representa los valores numéricos que aparecerán en el eje Y.
    plt.title("Exportaciones por región")
    plt.xlabel("Regiones")
    plt.ylabel("Toneladas exportadas")
    plt.show()
     # Cierra la gráfica para que el menú continúe funcionando
    plt.close()


# Menú principal del sistema
# El ciclo while mantiene el programa activo hasta que el usuario elija salir.
while True:

    print(" ")
    print("Menú principal")
    print("1. Registrar volumen inicial de exportaciones")
    print("2. Consultar volumen actual de exportaciones")
    print("3. Actualizar exportaciones de una región específica")
    print("4. Comparar exportaciones entre regiones")
    print("5. Simular incremento de exportaciones")
    print("6. Clasificación de regiones según su volumen exportado")
    print("7. Actualización masiva")
    print("8. Cargar datos desde archivo")
    print("9. Graficar exportaciones")
    print("10. Salir del sistema")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        registrarExportaciones()

    elif opcion == 2:
        consultarExportaciones()

    elif opcion == 3:
        actualizarExportaciones()

    elif opcion == 4:
        compararExportaciones()

    elif opcion == 5:
        simularIncremento()

    elif opcion == 6:
        clasificarRegion()

    elif opcion == 7:
        actualizarMasivamente()

    elif opcion == 8:
        cargarDesdeArchivo()

    elif opcion == 9:
        graficar()

    elif opcion == 10:
        print("Fin del sistema.")
        break

    else:
        print("Opción inválida.")
