from riderStoreCore import *
import cx_Oracle
from registro import Usuario
# Conexion a la BBDD
#connstr = "riderStore/RiderCore22@localhost:1521/XEPDB1" # Acceso BBDD PC escritorio
connstr = "riderStore/RiderCore22@192.168.56.1:1521/XEPDB1" # Acceso BBDD Notebook
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()

# Menu principal
def menu():
    value = True
    while value:   
        try:
            print("""
                *** Bienvenido al Menú ***\n
                1.- Registrar usuario
                2.- Iniciar venta
                3.- Mostrar todas las ventas
                4.- Salir
                \n""")
            
            option = int(input("Ingrese su opción: "))
            
            if option < 1 or option > 4:
                print("\nLa opción ingresada esta fuera de rango!. \nIntente nuevamente...\n")
                value = True
            else:
                opcMenu(option)
        
        except ValueError:
            print("El dato ingresado no es un numero! \nIngrese nuevamente...\n")
            value = True


def opcMenu(opc):
    # Registrar usuario
    if opc == 1:
        print("us")
        Usuario.registro_usuario()













    
    # Iniciar venta
    elif opc == 2: 
        main = Producto()
        main.mostrarProducto()
    
    # Mostrar todas las ventas
    elif opc == 3:
        print("\n*** TODAS LAS VENTAS REALIZADAS ***\n")
        # Resumen de la compra realizada
        sql_ventas = "SELECT numero_boleta, nombre, descripcion, precio, iva, precio_total, metodo_pago\
            FROM producto\
            JOIN detalle_boleta USING (id_producto)\
            JOIN boleta USING (id_boleta)\
            ORDER BY id_boleta"
        curs.execute(sql_ventas)
        ventas = curs.fetchall()
        for venta in ventas:
            print(f"Boleta N°: {venta[0]}\n\
                Producto: {venta[1]}\n\
                Descripcion: {venta[2]}\n\
                Valor Producto: {venta[3]}\n\
                IVA %: {venta[4]}\n\
                Monto Pagado: {venta[5]}\n\
                Metodo de Pago: {venta[6]}\n")
        menu()
    
    # Salir
    elif opc == 4:
        print("Cerrando programa")
        exit()