while True:
    entrada = input("Ingrese número de VLAN (o 's' para salir): ")
    if entrada.lower() == "s":
        print("Saliendo del programa.")
        break
    if not entrada.isdigit():
        print("Ingrese solo números o la letra 's'.")
        continue
    vlan = int(entrada)
    if 1 <= vlan <= 1005:
        print("VLAN Normal")
    elif 1006 <= vlan <= 4094:
        print("VLAN Extendida")
    else:
        print("VLAN fuera de rango")
