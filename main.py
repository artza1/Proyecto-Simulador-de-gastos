import funciones 
opcion=0
while opcion !="6": 
    print("")
    print("==========================================")
    print("                   Menu                   ")
    print("")
    print("1. Registrar Datos")
    print("2. Listar Datos")
    print("3. Calcular Gastos Totales/por Categoria")
    print("4. Generar Reporte")
    print("5. Salir")
    opcion= input("Ingrese una opcion")
    match opcion:
        case "1": funciones.registrar_gasto()
        case "2": funciones.listargastos()
        case "3": funciones.calcular_gastos()
        case "4": funciones.reporte_gastos()
        case "5": break

        