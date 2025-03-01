usuarios = {}

def agregar_usuario():
    usuario = input("Ingrese el nombre de usuario: ")
    contrasena = input("Ingrese la contraseña: ")

    try:
        if usuario in usuarios:
            print("El usuario ya existe")
        else:
            usuarios[usuario] = contrasena
            print("Usuario agregado")
            main()
    except ValueError:  
        print("Error al agregar usuario")


def leer_info(usuarios):
    print("Los usuarios registrados son: ", usuarios)
    main()

def login():
    usuario = input("Ingrese el nombre de usuario: ")
    contrasena = input("Ingrese la contraseña: ")

    try:
        if usuario in usuarios and usuarios[usuario] == contrasena:
            print("Inicio de sesión exitoso")
            main()
        else:
            intentar = input("Usuario o contraseña incorrectos. Desea volver a intentar? (s/n): ")
            if intentar == "s":
                login()
            elif intentar == "n":
                main()
    except ValueError:
        print("Error al iniciar sesión")


# Menu principal
def main():
    try:
        print("")
        print("Bienvenido al sistema de usuarios")
        print("1. Agregar usuario")
        print("2. Leer información de los usuarios")
        print("3. Iniciar sesión")
        print("4. Salir")
        print("")

        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            agregar_usuario()
        elif opcion == 2:
            leer_info(usuarios)
        elif opcion == 3:
            login()
        elif opcion == 4:
            print("Gracias por usar el sistema")
        else:
            print("Opción no válida")
    except ValueError:
        print("Opción no válida")


# Comienzo del programa       
main()