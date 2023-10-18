def menu():
    print("Datos Persona")
    print("1. Listar personas")
    print("2. Agregar personas")
    print("3. Salir\n")

def acceso():
    print("-- Bienvenido al sistema --")
    #Leer archivos
    txt_login = open("login.txt","rt",encoding="utf8")
    txt_clave = open("clave.txt","rt",encoding="utf8")
    datos_login = txt_login.read()
    datos_clave = txt_clave.read()
    txt_login.close()
    txt_clave.close()
    #Contador de intentos
    intentos = 0
    while intentos!=2:
        login = input("Ingrese login: ")
        clave = input("Ingrese clave: ")
        #Validar login y clave
        if (login != datos_login) or (clave != datos_clave):
            intentos += 1
            print("Login incorrecto y/o clave incorrecta\n")
            if intentos == 2:
                print("Ha excedido el número de intentos. Cerrando el sistema...")
        else:
            print("Mostrando menu...\n")
            menu()
            break
    
acceso()