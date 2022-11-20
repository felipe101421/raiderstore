import cx_Oracle
# Conexion a la BBDD
#connstr = "riderStore/RiderCore22@localhost:1521/XEPDB1" # Acceso BBDD PC escritorio
connstr = "riderStore/RiderCore22@192.168.56.1:1521/XEPDB1" # Acceso BBDD Notebook
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()

# Resumen de la compra realizada
sql_venta_realizada = "SELECT numero_boleta, nombre, descripcion, precio, iva, precio_total, metodo_pago\
    FROM producto\
    JOIN detalle_boleta USING (id_producto)\
    JOIN boleta USING (id_boleta)\
    ORDER BY id_boleta"

curs.execute(sql_venta_realizada)
ventaLista = curs.fetchall()

for venta in ventaLista:
    venta
print(f"Boleta N°: {venta[0]}\n\
        Producto: {venta[1]}\n\
        Descripcion: {venta[2]}\n\
        Valor Producto: {venta[3]}\n\
        IVA %: {venta[4]}\n\
        Monto Pagado: {venta[5]}\n\
        Metodo de Pago: {venta[6]}\n")

curs.close()
conn.close()
