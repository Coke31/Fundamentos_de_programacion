def ingresar_dato ():
    nombre = input("¿Cual es tu nombre?")
    telefono = int(input("¿Cual es tu numero de telefono?"))
    email = input("¿Cual es tu email?")
    edad = int(input("¿Cual es tu edad?"))
    fichas = {
        'nombre' : nombre,
        'telefono' : telefono,
        'email' : email,
        'edad' : edad,
    }
    ficha.append(fichas)
def ver_ficha():
    print("---FICHA---")
    for sficha in ficha:
        print(f"Nombre:{sficha['nombre']}")
        print(f"telefono:{sficha['telefono']}")
        print(f"email:{sficha['email']}")
        print(f"edad:{sficha['edad']}")
        print()
def actualizar_ficha ():
    dato = input("¿Que dato quieres cambiar? (nombre, telefono, email, edad)").lower()
    if dato == "nombre":
        nombre = input("¿Cual es el nombre que andas buscando?")
        encontrada = False
        for sficha in ficha:
            if nombre == sficha['nombre']:
                nuevo_nombre = input("¿Cual es el nuevo nombre?")
                sficha['nombre'] = nuevo_nombre
                encontrada = True
                print("Dato actualizado")
                break
        if not encontrada:
            print("nombre no encontrado")
    elif dato == "telefono":
        nombre = input("¿Cual es el nombre de la ficha que andas buscando?")
        encontrada = False
        for sficha in ficha:
            if nombre == sficha['nombre']:
                nuevo_telefono = int(input("¿Cual es el nuevo telefono?"))
                sficha['telefono'] = nuevo_telefono
                encontrada = True
                print("Dato actualizado")
                break
        if not encontrada:
            print("Nombre de la ficha no encontrada")
    elif dato == "email":
        nombre = input("¿Cual es el nombre de la ficha que andas buscando?")
        encontrada = False
        for sficha in ficha:
            if nombre == sficha['nombre']:
                nuevo_email = input("¿Cual es el nuevo email?")
                sficha['email'] = nuevo_email
                encontrada = True
                print("Dato actualizado")
                break
        if not encontrada:
            print("Nombre de la ficha no encontrada")
    elif dato == "edad":
        nombre = input("¿Cual es el nombre de la ficha que andas buscando?")
        encontrada = False
        for sficha in ficha:
            if nombre == sficha['nombre']:
                nuevo_edad = int(input("¿Cual es el nuevo edad?"))
                sficha['edad'] = nuevo_edad
                encontrada = True
                print("Dato actualizado")
                break
        if not encontrada:
            print("Nombre de la ficha no encontrada")
            
def eliminar_dato():
    nombre = input("¿Cual es el nombre de la ficha que andas buscando?")
    encontrada = False
    for sficha in ficha:
        if nombre == sficha['nombre']:
            ficha.remove(sficha)
            encontrada = True
            print("Dato actualizado")
            break
    if not encontrada:
        print("Nombre de la ficha no encontrada")            
def salir():
    print("Hasta luego")
    
                        
    

ficha = []

while True:
    try:
        opcion = int(input("[1] Ingresar Dato ficha \n [2] Ver ficha \n [3] Actualizar ficha \n [4] Eliminar contacto \n [5] Salir : "))
        if opcion == 1:
            ingresar_dato()
        elif opcion == 2:
            ver_ficha()
        elif opcion == 3:
            actualizar_ficha()
        elif opcion == 4:
            eliminar_dato()
        elif opcion == 5:
            salir()
            break
        else:
            print("Escoger una opcion correcta")
    except:
        print("error, dato no numerico")
        
        