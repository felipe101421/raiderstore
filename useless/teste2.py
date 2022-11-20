import cx_Oracle

# Conexion a la BBDD
# connstr = "riderStore/RiderCore22@localhost:1521/XEPDB1" # Acceso BBDD PC escritorio
connstr = "SYSTEM/Password.2022@192.168.56.1:1521/XEPDB1" # Acceso BBDD Notebook
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()

nombre = "Pablo"
apellido_paterno = "Lizama"
apellido_materno = "Lizama"
rut = "19873123-9"
direccion = "satiago 210"
ciudad = "santiago"
telefono = 9821234112
email = "pablo@pablo.cl"

sql = "INSERT INTO persona(id, nombre, apellido_paterno, apellido_materno, rut, direccion, ciudad, telefono, email) VALUES(1,'" + nombre + \
    "','" + apellido_paterno + "','" + apellido_materno + "','" + rut + "','" + direccion + "','" + ciudad + "'," + str(telefono) + ",'" + email + "')"

print(sql)

curs.execute(sql)
conn.commit()

curs.close()
conn.close()
