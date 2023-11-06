from load_data import load

def master_ppsw():
    master = 'contrasena1234'
    tries = 3
    while True:
        attempt = input('Ingrese la contraseña maestra para ver los datos: ')
        if attempt.lower() == master:
            menu()
        else:
            if tries == 1:
                print('- FIN DEL PROGRAMA -')
                quit()
            else:
                tries -= 1
                print(f'Error, contraseña incorrecta. Tenes {tries} intentos más.')

def options():
    print('\n1. Mostrar todos los usuarios y contraseñas.')
    print('2. Buscar contraseña por usuario.')
    print('3. Agregar un nuevo usuario y contraseña.')
    print('4. Cambiar un usuario.')
    print('5. Cambiar una contraseña.')
    print('6. Salir.')

def menu():
    while True:
        options()
        opt = int(input('Ingrese una opcion: '))
        if opt >= 1 and opt <= 5:
            if opt == 1:
                pass
            elif opt == 2:
                pass
            elif opt == 3:
                load()
            elif opt == 4:
                print('Punto 4.')
            elif opt == 5:
                print('Punto 5.')
        elif opt == 6:
            print('- FIN DEL PROGRAMA -')
            quit()
        else:
            print('ERROR. Vuelva a ingresar un numero entre 1 y 7: ')

master_ppsw()
