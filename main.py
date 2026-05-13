import funciones 
opcion=0

while opcion !="5": 
        print("")
        print("==========================================")
        print("                   Menu                   ")
        print("")
        print("1. Registrar Datos")
        print("2. Listar Datos")
        print("3. Calcular Gastos Totales/por Categoria")
        print("4. Generar Reporte")
        print("5. Salir")
        try:
            opcion= input("Ingrese una opcion: ")
            if opcion<"1" or opcion>"5":
                 print("ERROR: opccion incorrecta")
                 continue
            match opcion:
                case "1": funciones.registrar_gasto()
                case "2": funciones.listargastos()
                case "3": funciones.calcular_gastos()
                case "4": funciones.reporte_gastos()
                case "5": 
                    print("Saliendo...") 
                    break
        except ValueError:
             print("ERROR: Debe ingresar un numero")
