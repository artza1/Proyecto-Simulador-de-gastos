import json
from tabulate import tabulate

with open("datos.json", "r") as D:
    data = json.load(D)

def registrar_gasto():

    Ndatos = int(input("Ingrese numero de datos que vas a ingresar"))
    for i in range(Ndatos):
        categoria = input("Ingrese categoria (comida, entretenimiento, transporte): ")
        nombre = input("Ingrese el nombre: ")
        precio = int(input("Ingrese el precio: "))
        cantidad = int(input("Ingrese la cantidad: "))
        fecha= (input("Ingrese la fecha del gasto"))
        if categoria=="comida":
            nuevo_gasto = {
                "comida": nombre,
                "precio": precio,
                "cantidad": cantidad,
                "fecha":fecha}
        if categoria == "entretenimiento":
            nuevo_gasto = {
                "entretenimiento": nombre,
                "precio": precio,
                "cantidad": cantidad,
                "fecha":fecha}
        if categoria == "transporte":
            nuevo_gasto = {
                "transporte": nombre,
                "precio": precio,
                "cantidad": cantidad,
                "fecha":fecha}     
        data["gastos"][categoria].append(nuevo_gasto)
        guardar= input("Ingrese 'S' para guardar o 'C' para Cancelar").upper()
        if guardar == "S": 
            with open("datos.json", "w") as D:
                json.dump(data, D, indent=4)
                print("Gasto guardado correctamente")
        elif guardar == "C":
            print("Se cancelo correctamente")
      

def listargastos():
    opcion= 0
    while opcion !="4":
        print("Listar POR:")
        print("1. Fecha")
        print("2. Categoria")
        print("3. Todos los gastos")
        print("4. Volver al menu principal")
        print("")
        opcion= input("Ingrese opcion: ")
        match opcion:
            case "1": 
                filtar= input("¿Quieres filtrar por dia o por mes? ")
                if filtar == "dia":
                    categoria = input("ingrese la categoria: ")
                    fechapedida= input("Ingrese la fecha desde la que quiere listar: ")
                    for gasto in data["gastos"][categoria]:
                     if gasto["fecha"] == fechapedida:
                        print(gasto)
                elif filtar == "mes":
                    categoria = input("ingrese la categoria: ")
                    fechapedida= input("Ingrese la fecha desde la que quiere listar: ")
                    for gasto in data["gastos"][categoria]:
                        if gasto["fecha"].startswith(fechapedida):
                            print(gasto)
            case "2":
                categoria= input("¿Que categoria quieres listar? ")
                for gasto in data["gastos"][categoria]:
                        print(gasto)
            case "3": 
                for gasto in data["gastos"]["comida"]:
                        print(gasto)

                for gasto in data["gastos"]["entretenimiento"]:
                        print(gasto)

                for gasto in data["gastos"]["transporte"]:
                        print(gasto)
            case "4":
                return
            
def calcular_gastos():
    eleccion = 0
    while eleccion !="3":
        print("=======================  ")
        print("     Calcular Gastos     ")
        print("1. Gastos totales")
        print("2. Gastos por categoria")
        print("3. SALIR")
        eleccion= input("Ingrese lo que quieres hacer: ")
        match eleccion:
            case "1": 
                total= 0
                for categoria in data["gastos"]:
                    for gastos in data["gastos"][categoria]:
                        total += gastos["precio"] * gastos["cantidad"]
                print(f"el total fue{total}")
                
            case "2":
                total= 0
                categoria= input("Ingrese la categoria que quieres calcular: ")
                for gastos in data["gastos"][categoria]:
                    total += gastos["precio"] * gastos["cantidad"]
                print(f"El total fue {total}")
            case "3":
                break

def reporte_gastos():
    eleccion=0
    while eleccion  !=3:
        print("======================")
        print("     Reporte Gastos   ")
        print("1. En pantalla")
        print("2. Archivo Json")
        print("3. SALIR")
        eleccion= input("Ingrese lo que quieres hacer: ")
        match eleccion:
            case "1":  
                with open("datos.json", "r") as D:
                    data = json.load(D)
                tabla = []
                total_general = 0
                for categoria in data["gastos"]:
                    subtotal = 0
                    for gasto in data["gastos"][categoria]:
                        subtotal += gasto["precio"] * gasto["cantidad"]
                    total_general += subtotal
                    tabla.append([categoria, subtotal])
        
                print("\nREPORTE DE GASTOS\n")

                print(tabulate(
                tabla,
                headers=["Categoria", "Total"],
                tablefmt="grid"
                    ))

                print("\nTotal general:", total_general)
            case "2": 
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
                        subtotal += gasto["precio"] * gasto["cantidad"]
                            
                    reporte["totales_por_categoria"][categoria] = subtotal
                    total_general += subtotal
                reporte["total_general"] = total_general
                        
                with open("reporte.json", "w") as R:
                    json.dump(reporte, R, indent=4)
                print("\nReporte guardado en reporte.json")
