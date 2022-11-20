import cx_Oracle

# Conexion a la BBDD
#connstr = "riderStore/RiderCore22@localhost:1521/XEPDB1" # Acceso BBDD PC escritorio
connstr = "riderStore/RiderCore22@192.168.56.1:1521/XEPDB1" # Acceso BBDD Notebook
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()


class Persona:
    nombre = ''
    apellido_paterno = ''
    apellido_materno = ''
    rut = ''
    direccion = ''
    ciudad = ''
    telefono = 0
    email = ''

    def __init__(self, nombre, apellido_paterno, apellido_materno, rut, direccion, ciudad, telefono, email):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.rut = rut
        self.direccion = direccion
        self.ciudad = ciudad
        self.telefono = telefono
        self.email = email


class Cliente:
    nombre = ''
    apellido_paterno = ''
    telefono = 0
    email = ''
    
    def __init__(self, nombre, apellido_paterno, telefono, email):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.telefono = telefono
        self.email = email 


class Colaborador:
    nombre = ''
    apellido_paterno = ''
    rut = ''
    telefono = ''
    prevision = ''
    cargo = ''
    jefe_directo = ''
    tipo_contrato = ''
    
    def __init__(self, nombre, apellido_paterno, rut, telefono, prevision, cargo, jefe_directo, tipo_contrato):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.rut = rut
        self.telefono = telefono
        self.prevision = prevision
        self.cargo = cargo
        self.jefe_directo = jefe_directo
        self.tipo_contrato = tipo_contrato


class Producto:
    nombre = ''
    codigo_producto = ''
    precio = 0

    def __init__(self, nombre="", codigo_producto="", precio=0):
        self.nombre = nombre        
        self.codigo_producto = codigo_producto
        self.precio = precio


    def mostrarProducto(self):
        # Buscando producto en la tabla
        curs.execute("SELECT * FROM producto")
        
        # Mostrar productos en pantalla
        print("\n*** PRODUCTOS DISPONIBLES ***\n")
        viewProducts = curs.fetchall()
        value = True
        while value:
            for product in viewProducts:
                lista = [
                    "Nombre: " + product[1],
                    "Stock: " + str(product[4]),
                    "Precio: " + str(product[8]),
                    "Posición: " + product[6],
                    "Código: " + product[7]                    
                ]
                print(lista)
            
            try:
                busqueda = input("\nIngrese el codigo del producto: ")
                
                curs.execute("SELECT * FROM producto WHERE codigo_producto = '%s'"% busqueda.upper())
                products = curs.fetchall()
                
                if products == []:
                    print("\nProducto no encontrado!\n")
                else:
                    # Itera el ID de VENTAS
                    sql_id = "SELECT id_venta FROM venta"
                    curs.execute(sql_id)
                    ids = curs.fetchall()
                    for id in ids:
                        id
                    last_id = id[0]+1
                    
                    # Añadiendo el producto en VENTAS
                    for product in products:
                        print("\n** PRODUCTO SELECCIONADO **")
                        print(product)
                        idProducto = product[0]
                        self.nombre = product[1]
                        self.precio = product[8]
                        self.codigo_producto = product[7]
                        
                        sql = "INSERT INTO venta(id_venta, nombre_producto, precio_producto, codigo_producto, id_producto) VALUES("+\
                            str(last_id) + ",'" + self.nombre + "'," + str(self.precio) + ",'" + self.codigo_producto + "'," + str(idProducto) + ")"
                        
                        curs.execute(sql)
                        conn.commit()
                        
                        # Direccionando hacia DetalleBoleta
                        DetalleBoleta().metodoPago()
                        value = False
            
            except ValueError:
                    print("")


class Boleta:
    numero_boleta = 0
    
    def __init__(self, numero_boleta=0):
        self.numero_boleta = numero_boleta

    def generandoBoleta(self):
        
        # Generando numero de boleta
        sql = "SELECT id_boleta, numero_boleta FROM boleta ORDER BY id_boleta"
        curs.execute(sql)
        datos = curs.fetchall()
        for dato in datos:
            dato
        idBoleta = dato[0]+1
        self.numero_boleta = dato[1]+100
        
        # Insertando datos en tabla BOLETA
        sql_boleta = "INSERT INTO boleta(id_boleta, numero_boleta) VALUES("+str(idBoleta)+","+str(self.numero_boleta)+")"
        curs.execute(sql_boleta)
        #conn.commit()
        
        # Itera el ID de VENTA
        sql_id = "SELECT id_venta FROM venta ORDER BY id_venta"
        curs.execute(sql_id)
        ids = curs.fetchall()
        for id in ids:
            id
        last_id_venta = id[0]
        
        # Insertando NUMERO_BOLETA en DETALLE_BOLETA
        sql_detBol = "UPDATE venta SET numero_boleta="+str(self.numero_boleta) + " WHERE id_venta="+str(last_id_venta)
        curs.execute(sql_detBol)
        conn.commit()
        
        print("\n*** BOLETA GENERADA ***\n")
        
        # Resumen de la compra realizada
        print("### RESUMEN DE SU COMPRA ###\n")
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
        breakpoint

class DetalleBoleta(Boleta):
    precio_total = 0
    iva = 0
    metodo_pago = ""
    
    def __init__(self, precio_total=0, iva=0, metodo_pago=""):
        self.precio_total = precio_total
        self.iva = iva
        self.metodo_pago = metodo_pago
    
    def generarDetalleBoleta(self):
        
        # Itera el ID de VENTA
        sql_id = "SELECT id_venta FROM venta ORDER BY id_venta"
        curs.execute(sql_id)
        ids = curs.fetchall()
        for id in ids:
            id
        last_id_venta = id[0]
        
        # Itera ventas para extraer valores de la tabla VENTA
        sql_venta = "SELECT precio_total, iva, metodo_pago, id_producto FROM venta WHERE id_venta="+str(last_id_venta)
        curs.execute(sql_venta)
        datosVenta = curs.fetchall()
        for datos in datosVenta:
            datos
        self.precio_total = datos[0]
        self.iva = datos[1]
        self.metodo_pago = datos[2]
        idProducto = datos[3]
        
        # Itera el ID de DETALLE_BOLETA
        sql_id = "SELECT id_det_boleta FROM detalle_boleta ORDER BY id_det_boleta"
        curs.execute(sql_id)
        ids = curs.fetchall()
        for id in ids:
            id
        last_id_detBol = id[0]+1
        
        # Itera el ID de DETALLE_BOLETA (vinculo id_boleta)
        sql_idBoleta = "SELECT id_boleta FROM detalle_boleta ORDER BY id_boleta"
        curs.execute(sql_idBoleta)
        ids = curs.fetchall()
        for id in ids:
            id
        last_id_Bol = id[0]+1
        
        # Insertando datos en DETALLE_BOLETA
        sql_detBol = "INSERT INTO detalle_boleta(id_det_boleta, precio_total, iva, id_producto, metodo_pago, id_boleta) VALUES("+\
            str(last_id_detBol)+","+str(self.precio_total)+","+str(self.iva)+","+str(idProducto)+",'"+self.metodo_pago+"',"+str(last_id_Bol)+")"
        curs.execute(sql_detBol)
        conn.commit()
        
        # Direccionando a Boleta
        Boleta().generandoBoleta()
    
    def metodoPago(self):
        
        # Funcion local de metodoPago()
        def addToDBVentas(selectMetodoPago):
            
            # Itera el ID de VENTAS
            sql_id = "SELECT id_venta FROM venta ORDER BY id_venta"
            curs.execute(sql_id)
            ids = curs.fetchall()
            for id in ids:
                id
            last_id = id[0]
            
            self.metodo_pago = selectMetodoPago
            self.iva = 1.19
            curs.execute("SELECT precio_producto FROM venta WHERE id_venta = "+str(last_id))
            valor = curs.fetchall()
            for precio in valor:
                self.precio_total = precio[0]*self.iva
                
                sql = "UPDATE venta SET metodo_pago='"+self.metodo_pago+"', iva=19"+",precio_total="+str(self.precio_total)+\
                    "WHERE id_venta = "+str(last_id)
                curs.execute(sql)
                conn.commit()
            
            # Generando Detalle de Boleta
            self.generarDetalleBoleta()
        
        # Menu para seleccionar el Metodo de Pago
        bucle = True
        while bucle:
            try:
                print("""
                    ** METODOS DE PAGO **
                    1.- Efectivo
                    2.- Debito
                    3.- Credito
                    """)
                opc = int(input("Seleccione el metodo de pago: "))
                
                if opc == 1:
                    self.metodo_pago = 'Efectivo'
                    # Aqui funcion agregar a DB
                    addToDBVentas(self.metodo_pago)
                    bucle = False
                
                elif opc == 2:
                    self.metodo_pago = 'Debito'             
                    # Aqui funcion agregar a DB
                    addToDBVentas(self.metodo_pago)
                    bucle = False
                
                elif opc == 3:
                    self.metodo_pago = 'Credito'                    
                    # Aqui funcion agregar a DB
                    addToDBVentas(self.metodo_pago)
                    bucle = False
                
                else:
                    print("Opcion no valida!\n")
            
            except ValueError:
                print("Dato ingresado no es valido!\n")
            