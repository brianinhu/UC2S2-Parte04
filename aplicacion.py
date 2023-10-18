import gestion_personas as gp

def menu():
    print("Datos Persona")
    print("1. Listar personas")
    print("2. Agregar persona")
    print("3. Salir\n")

    opcion = int(input("Ingrese una opción: "))

    while True:
        if opcion == 1:
            listar()
        elif opcion == 2:
            agregar()
        elif opcion == 3:
            print("\nCerrando el sistema...")
            break
        else:
            print("\nOpción incorrecta\n")
        print("")
        print("Datos Persona")
        print("1. Listar personas")
        print("2. Agregar personas")
        print("3. Salir\n")
        opcion = int(input("Ingrese una opción: "))


def listar():
    gp.listarPersonas()

def agregar():
    dni = input("\nIngrese DNI: ")
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    gp.agregarPersona(dni, nombre, apellido)

def acceso():
    print("-- Bienvenido al sistema --")
    #Leer archivos
    txt_login = open("login.txt","rt",encoding="utf8")
    txt_clave = open("clave.txt","rt",encoding="utf8")
    datos_login = txt_login.read()
    datos_clave = txt_clave.read()
    txt_login.close()
    txt_clave.close()
    intentos = 0
    while intentos!=2:
        login = input("Ingrese login: ")
        clave = input("Ingrese clave: ")

        if (login != datos_login) or (clave != datos_clave):
            intentos += 1
            print("Login incorrecto y/o clave incorrecta\n")
            if intentos == 2:
                print("Ha excedido el número de intentos. Cerrando el sistema...")
        else:
            print("\nMostrando menu...\n")
            menu()
            break
    
acceso()