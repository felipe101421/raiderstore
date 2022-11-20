
import cx_Oracle

# Validando si la tabla existe en la base de datos
def validadorTablas(tablename):
    # connstr = "riderStore/RiderCore22@localhost:1521/XEPDB1" # Acceso BBDD PC escritorio
    connstr = "SYSTEM/Password.2022@192.168.56.1:1521/XEPDB1" # Acceso BBDD Notebook
    conn = cx_Oracle.connect(connstr)
    curs = conn.cursor()
    
    try:
        curs.execute("SELECT * FROM {}".format(tablename))
        return True
    except cx_Oracle.DatabaseError as e:
        x = e.args[0]
        if x.code == 942: ## Only catch ORA-00942: table or view does not exist error
            return False
        else:
            raise e
    finally:
        curs.close()

# Comprobando creacion de tablas: 
# Si existen, no se crean
# Si NO existen, se crean

# Conexion a base de datos
#connstr = "riderStore/RiderCore22@localhost:1521/XEPDB1" # Acceso BBDD PC escritorio
connstr = "SYSTEM/Password.2022@192.168.56.1:1521/XEPDB1" # Acceso BBDD Notebook
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()

# TABLA PERSONA
def tablaPersona():
    if validadorTablas('persona'):
        #print("Tabla 'PERSONA' existe en el sistema.")
        pass
    else:
        persona = '''CREATE TABLE persona(
            id INT PRIMARY KEY,
            nombre CHAR(20) NOT NULL,
            apellido_paterno CHAR(20),
            apellido_materno CHAR(20),
            rut CHAR(15) NOT NULL,
            direccion CHAR(50),
            ciudad CHAR(20),
            telefono INT,
            email CHAR(30)
        )'''
        curs.execute(persona)
        print("Se ha creado la tabla 'PERSONA'.")

# TABLA CLIENTE
def tablaCliente():
    if validadorTablas('cliente'):
        #print("Tabla 'CLIENTE' existe en el sistema.")
        pass
    else:
        cliente = '''CREATE TABLE cliente(
            id INT PRIMARY KEY,
            nombre CHAR(20) NOT NULL,
            apellido_paterno CHAR(20),
            telefono INT,
            email CHAR(30)
        )'''
        curs.execute(cliente)
        print("Se ha creado la tabla 'CLIENTE'.")

# TABLA COLABORADOR
def tablaColaborador():
    if validadorTablas('colaborador'):
        #print("Tabla 'COLABORADOR' existe en el sistema.")
        pass
    else:
        colaborador = '''CREATE TABLE colaborador(
            id INT PRIMARY KEY,
            nombre CHAR(20) NOT NULL,
            apellido_paterno CHAR(20),
            rut CHAR(15),
            telefono INT,
            prevision CHAR(10),
            cargo CHAR(30),
            jefe_directo CHAR(20),
            tipo_contrato CHAR(15),
            privilegio INT,
            contrasena CHAR(8)
        )'''
        curs.execute(colaborador)
        print("Se ha creado la tabla 'COLABORADOR'.")

# TABLA PRODUCTO
def tablaProducto():
    if validadorTablas('producto'):
        #print("Tabla 'PRODUCTO' existe en el sistema.")
        pass
    else:
        producto = '''CREATE TABLE producto(
            id INT PRIMARY KEY,
            nombre CHAR(20),
            descripcion CHAR(100),
            familia_producto CHAR(20),
            stock INT,
            unidad_venta CHAR(10),
            posicion CHAR(20),
            codigo_producto CHAR(30)
        )'''
        curs.execute(producto)
        print("Se ha creado la tabla 'PRODUCTO'.")

# Ejecucion de base de datos
def dbExecute():
    tablaPersona()
    tablaCliente()
    tablaColaborador()
    tablaProducto()
