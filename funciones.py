import json
from tabulate import tabulate


# =========================
# CARGAR ARCHIVO JSON
# =========================

try:
    with open("datos.json", "r") as D:
        data = json.load(D)

except FileNotFoundError:
    print("El archivo datos.json no existe")
    data = {
        "gastos": {
            "comida": [],
            "entretenimiento": [],
            "transporte": []
        }
    }

except json.JSONDecodeError:
    print("El archivo JSON esta dañado")
    data = {
        "gastos": {
            "comida": [],
            "entretenimiento": [],
            "transporte": []
        }
    }


# =========================
# REGISTRAR GASTO
# =========================

def registrar_gasto():

    try:
        Ndatos = int(input("Ingrese numero de datos que vas a ingresar: "))

    except ValueError:
        print("Debes ingresar un numero entero")
        return

    for i in range(Ndatos):

        categoria = input("Ingrese categoria (comida, entretenimiento, transporte): ").lower()

        if categoria not in data["gastos"]:
            print("Categoria invalida")
            continue

        nombre = input("Ingrese el nombre: ")

        try:
            precio = int(input("Ingrese el precio: "))
            cantidad = int(input("Ingrese la cantidad: "))

        except ValueError:
            print("Precio y cantidad deben ser numeros")
            continue

        fecha = input("Ingrese la fecha del gasto: ")

        nuevo_gasto = {
            categoria: nombre,
            "precio": precio,
            "cantidad": cantidad,
            "fecha": fecha
        }

        data["gastos"][categoria].append(nuevo_gasto)

        guardar = input("Ingrese 'S' para guardar o 'C' para cancelar: ").upper()

        if guardar == "S":

            try:
                with open("datos.json", "w") as D:
                    json.dump(data, D, indent=4)

                print("Gasto guardado correctamente")

            except:
                print("Error al guardar el archivo")

        elif guardar == "C":
            print("Se cancelo correctamente")

        else:
            print("Opcion invalida")


# =========================
# LISTAR GASTOS
# =========================

def listargastos():

    opcion = 0

    while opcion != "4":

        print("\n====================")
        print("     LISTAR GASTOS")
        print("====================")
        print("1. Fecha")
        print("2. Categoria")
        print("3. Todos los gastos")
        print("4. Volver al menu principal")

        opcion = input("Ingrese opcion: ")

        match opcion:

            case "1":

                filtrar = input("¿Quieres filtrar por dia o por mes?: ").lower()

                if filtrar == "dia":

                    categoria = input("Ingrese la categoria: ").lower()

                    try:
                        fechapedida = input("Ingrese la fecha: ")

                        for gasto in data["gastos"][categoria]:

                            if gasto["fecha"] == fechapedida:
                                print(gasto)

                    except KeyError:
                        print("Categoria invalida")

                elif filtrar == "mes":

                    categoria = input("Ingrese la categoria: ").lower()

                    try:
                        fechapedida = input("Ingrese el mes (ej: 2026-05): ")

                        for gasto in data["gastos"][categoria]:

                            if gasto["fecha"].startswith(fechapedida):
                                print(gasto)

                    except KeyError:
                        print("Categoria invalida")

                else:
                    print("Filtro invalido")

            case "2":

                categoria = input(
                    "¿Que categoria quieres listar?: "
                ).lower()

                try:
                    for gasto in data["gastos"][categoria]:
                        print(gasto)

                except KeyError:
                    print("Categoria invalida")

            case "3":

                for categoria in data["gastos"]:

                    print(f"\n--- {categoria.upper()} ---")

                    for gasto in data["gastos"][categoria]:
                        print(gasto)

            case "4":
                return

            case _:
                print("Opcion invalida")


# =========================
# CALCULAR GASTOS
# =========================

def calcular_gastos():

    eleccion = 0

    while eleccion != "3":

        print("\n=======================")
        print("     CALCULAR GASTOS")
        print("=======================")
        print("1. Gastos totales")
        print("2. Gastos por categoria")
        print("3. SALIR")

        eleccion = input("Ingrese lo que quieres hacer: ")

        match eleccion:

            case "1":

                total = 0

                for categoria in data["gastos"]:

                    for gastos in data["gastos"][categoria]:

                        total += (gastos["precio"] *gastos["cantidad"])

                print(f"El total fue {total}")

            case "2":

                categoria = input("Ingrese la categoria que quieres calcular: ").lower()

                total = 0

                try:

                    for gastos in data["gastos"][categoria]:

                        total += (gastos["precio"] *gastos["cantidad"])

                    print(f"El total fue {total}")

                except KeyError:
                    print("Categoria invalida")

            case "3":
                break

            case _:
                print("Opcion invalida")


# =========================
# REPORTE DE GASTOS
# =========================

def reporte_gastos():

    eleccion = 0

    while eleccion != "3":

        print("\n======================")
        print("     REPORTE GASTOS")
        print("======================")
        print("1. En pantalla")
        print("2. Archivo Json")
        print("3. SALIR")

        eleccion = input("Ingrese lo que quieres hacer: ")

        match eleccion:

            case "1":

                try:

                    with open("datos.json", "r") as D:
                        data = json.load(D)

                    tabla = []
                    total_general = 0

                    for categoria in data["gastos"]:

                        subtotal = 0

                        for gasto in data["gastos"][categoria]:

                            subtotal += (gasto["precio"] *gasto["cantidad"])

                        total_general += subtotal

                        tabla.append([categoria,subtotal])

                    print("\nREPORTE DE GASTOS\n")

                    print(tabulate(
                        tabla,
                        headers=["Categoria", "Total"],
                        tablefmt="grid"
                    ))

                    print("\nTotal general:", total_general)

                except:
                    print("Error al generar el reporte")

            case "2":

                try:

                    with open("datos.json", "r") as D:
                        data = json.load(D)

                    total_general = 0

                    reporte = {
                        "totales_por_categoria": {},
                        "total_general": 0
                    }

                    for categoria in data["gastos"]:

                        subtotal = 0

                        for gasto in data["gastos"][categoria]:

                            subtotal += (gasto["precio"] *gasto["cantidad"])

                        reporte["totales_por_categoria"][categoria] = subtotal

                        total_general += subtotal

                    reporte["total_general"] = total_general

                    with open("reporte.json", "w") as R:
                        json.dump(reporte, R, indent=4)

                    print(
                        "\nReporte guardado en reporte.json"
                    )

                except:
                    print("Error al crear el reporte")

            case "3":
                break

            case _:
                print("Opcion invalida")
