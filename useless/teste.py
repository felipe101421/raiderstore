import cx_Oracle

# Conexion a la BBDD
connstr = "riderStore/RiderCore22@localhost:1521/XEPDB1" # Acceso BBDD PC escritorio
#connstr = "SYSTEM/Password.2022@192.168.56.1:1521/XEPDB1" # Acceso BBDD Notebook
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()

#curs.execute("SELECT * FROM producto")
curs.execute("SELECT * FROM producto")

# Mostrar productos en pantalla
print("\n*** PRODUCTOS DISPONIBLES ***\n")
viewProducts = curs.fetchall()
for product in viewProducts:
    lista = [
        "Nombre: " + product[1],
        "Stock: " + str(product[4]),
        "Posición: " + product[6],
        "Código: " + product[7]
    ]
    print(lista)

# Pedir seleccion de producto al usuario
busqueda = input("\nIngrese el codigo del producto: ")
cantidad = int(input("¿Cuantos desea llevar?: "))
curs.execute("SELECT * FROM producto WHERE codigo_producto = '%s'"% busqueda.upper())
products = curs.fetchall()
for product in products:
    print(product)

print("""Desea agregar otro producto: 
    
    1.- Agregar otro
    2.- Continuar
    3.- Cancelar
    """)

opc = int(input("Ingrese su opcion: "))


# METODO DE PAGO
print("""
    *** METODO DE PAGO ***
    # Seleccione el metodo de pago
    
    1.- Efectivo
    2.- Debito
    3.- Credito
    """)

opc = int(input("Ingrese su opcion: "))
confirm = input(f"El metodo de pago seleccionado es: {opc}, ¿desea modificarlo (si/no)?: ")

# MOSTRANDO RESUMEN DE LA COMPRA
