#inicio de sesion
"""usuario=""
pwd=""
print("Bienvenido ingrese sus datos")
print("usuario:")
user= input()
print("contraseña:")
pwd=input()
if user==user and pwd==pwd:
    print("Bienvenido a rider store!")
else:
    print("usuario o contraseña inválido, intente nuevamente")"""

# registro

class Usuario:
    rut=""
    nombre=""
    contrasena=""
    email=""
    confirmar_contrasena=""

    def __init__(self, rut, nombre, contrasena, email,confirmar_contrasena):
        self.rut=rut
        self.nombre=nombre
        self.contrasena=contrasena
        self.email=email
        self.confirmar_contrasena=confirmar_contrasena
        
    def __str__(self):
        return str(self.__class__)+": "+str(self.__dict__)
        

    def registro_usuario():
    
        print("registre su usuarios")


        rut= input("ingrese su rut: ")
        nombre= input("ingrese su nombre: ")
        contrasena= input("cree una contraseña de 4 digitos: ")
        confirmar_contrasena= input("confirmar su contraseña: ")
        if contrasena!=confirmar_contrasena:
            print("su contraseña no coincide, compruebe nuevamente")
            return Usuario.registro_usuario()

        email=input("ingrese su email")


        us=Usuario(rut,nombre,contrasena, email,confirmar_contrasena)

        print(us)