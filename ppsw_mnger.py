import os
fileName = 'ProyectoFinal/ppsw_mnger.txt'

def master_ppsw():
    master = 'contrasena1234'
    tries = 3
    while True:
        question = input('Ingrese la contraseña maestra para ver los datos: ')
        if question.lower() == master:
            menu()
        else:
            if tries == 1:
                print('- FIN DEL PROGRAMA -')
                quit()
            else:
                tries -= 1
                print(f'Error, contraseña incorrecta. Tenes {tries} intentos más.')

def is_it_empty():
    if os.path.getsize(fileName) == 0:
        print('El archivo esta vacio. Primero cargue datos.\n')
    else:
        return True

def options():
    # Ver si el punto 4 y 5 puede ir en un solo punto o si es conveniente separarlos.
    # Ver si el punto 6 conviene. Podria hacerse con bajas logicas, quizas ocupe mucho espacio. Preguntar.
    print('1. Mostrar todos los usuarios y contraseñas.')
    print('2. Buscar contraseña por usuario.')
    print('3. Agregar un nuevo usuario y contraseña.')
    print('4. Cambiar un usuario.')
    print('5. Cambiar una contraseña.')
    print('6. Mostrar usuarios y contraseñas (nuevas y viejas). ')
    print('7. Salir.')

def menu():
    while True:
        options()
        opt = int(input('Ingrese una opcion: '))
        if opt >= 1 and opt <= 6:
            if opt == 1:
                show()
            elif opt == 2:
                search_by_user()
            elif opt == 3:
                add()
            elif opt == 4:
                print('Punto 4.')
            elif opt == 5:
                print('Punto 5.')
            elif opt == 6:
                print('Punto 6.')
        elif opt == 7:
            print('- FIN DEL PROGRAMA -')
            quit()
        else:
            print('ERROR. Vuelva a ingresar un numero entre 1 y 7: ')

def show():
    if is_it_empty():
        with open(fileName, 'rt') as file:
            for line in file.readlines():
                tokens = line.split('###')
                print(f'Plataforma: {tokens[0]}')
                print(f'Usuario: {tokens[1]}')
                print(f'Contraseña: {tokens[2]}')
        file.close()

# Preguntar como puedo re-utilizar el show() para que me muestre de esa forma pero solo lo que el usuario quiere buscar
"""def search_by_user():
    if is_it_empty():
        search_user = input('Nombre de usuario a buscar: ')
        with open(fileName, 'rt') as file:
            for line in file.readlines():
                tokens = line.split('###')
                if search_user.lower() in line.lower():
                    show(line)
                else:
                    print(f'No existe el usuario: {search_user}')
        file.close()"""


def add():
    plat = input('Plataforma: ')
    user = input('Usuario: ')
    ppsw = input('Contraseña:')
    with open(fileName, 'a') as file:
        file.write(plat + '###' + user + '###' + ppsw)
        file.write('\n')
        file.close()
    print('¡Datos cargados exitosamente!\n')

master_ppsw()