#PruebaBriamDjesusFPY005
import csv
import random
trabajadores = ["Juan Pérez","María García", "Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos = []

def sueldos_trabajadores(trabajadores):
    sueldos = {trabajador: random.randint(300000, 2500000) for trabajador in trabajadores}
    print ("Sueldos creados")
    for trabajador, sueldo in sueldos.items():
        print (f"{trabajador}: {sueldo}")
    return sueldos
        
def clasificar_sueldos(sueldos):
    clasificacion = {"sueldos menores a $800.000": [], "Sueldos entre $800.000 y $2.000.000": [], "Sueldos mayores a $2.000.000": []}
    for trabajador, sueldo in sueldos.items():
        if sueldo < 800000:
            clasificacion["Sueldos entre $800.000 y $2.000.000"].append((trabajador, sueldo))
        elif sueldo < 2000000:
            clasificacion["Sueldos mayores a $2.000.000"].append((trabajador, sueldo))
        else:
            clasificacion["Sueldos entre $800.000 y $2.000.000"].append((trabajador, sueldo))
            
    print ("clasificacion de sueldos lista:")
    
    for categoria, empleados in clasificacion.items():
        print(f"{categoria} - total: {len(empleados)}")
        for trabajador, sueldo in empleados:
            print(f"{trabajador}: {sueldo}")
    
    print (f"total sueldos: {sum(sueldos.values())}")

def estadisticas(sueldos):
    sueldo_MaAlto = max(sueldos.values())
    print (f"El sueldo mas alto es: {sueldo_MaAlto}")
    
    sueldo_MaBajo = min(sueldos.values())
    print (f"El sueldo mas bajo es: {sueldo_MaBajo}")
    
    promedio_sueldos = round(sum(sueldos.values()) / len(sueldos), 2)
    print (f"El promedio de los sueldos es: {promedio_sueldos}")    

def csv_sueldos(sueldos):
    with open("sueldos.csv", "w", newline='') as archive_csv:
        escritor_csv = csv.writer(archive_csv, delimiter=";")
        escritor_csv.writerow(["Nombre empleado", "Sueldo empleado", "Descuento salud", "Descuento AFP", "Sueldo liquido"])
        for trabajador, sueldo in sueldos.items():
            descuento_salud = round(sueldo * 0.07)
            descuento_afp = round(sueldo * 0.12)
            sueldo_liquido = round(sueldo - descuento_salud - descuento_afp)
            
            escritor_csv.writerow([trabajador, round(sueldo, 2), descuento_afp, descuento_salud, sueldo_liquido])
while True:
    
    print("Analizador de datos de trabajadores")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas.")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")
    
    opcion = input("Ingrese la opcion que desee realizar: ")
    
    if opcion == "1":
        sueldos = sueldos_trabajadores(trabajadores)
    elif opcion == "2":
        if sueldos:
            clasificar_sueldos(sueldos)
        else:
            print ("No se han generado sueldos, intente de nuevo")
    elif opcion == "3":
        if sueldos:
            estadisticas(sueldos)
        else:
            print ("No se han generado sueldos, intente de nuevo")
    elif opcion == "4":
        if sueldos:
            csv_sueldos(sueldos)
        else:
            print ("No se han generado sueldos, intente de nuevo")
    elif opcion == "5":
        print("Finalizando programa...")
        print("Desarrollado por Briam Djesus-seccion FPY005")
        print("Rut 26.267.996-9")
        break
    else:
        print("La opcion ingreseda no es valida")