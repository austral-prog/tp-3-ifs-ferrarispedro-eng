def password():
    """
    Ejercicio 10 - Validador de Contraseña

    Leer una contraseña mediante input(). Validar que cumpla con los siguientes requisitos:
    1. Debe tener al menos 8 caracteres de longitud
    2. Debe contener al menos un número (usar el operador in para verificar cada dígito del 0 al 9)

    Si cumple ambos requisitos, imprimir "Contraseña valida".
    Si no cumple, imprimir cuál requisito falta.

    Ejemplo:
        Para la entrada "abc12345", la salida esperada es:
        Contraseña valida

        Para la entrada "abc123", la salida esperada es:
        Contraseña muy corta

        Para la entrada "abcdefgh", la salida esperada es:
        Debe contener un numero

        Para la entrada "abc", la salida esperada es:
        Contraseña muy corta
        Debe contener un numero
    """

    #contrasenia= input("Ingrese su contraseña: ")
    contrasenia= input()

    if len (contrasenia) < 8 and ("1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0") not in contrasenia:
       print (f"Contraseña muy corta\nDebe contener un numero")
    elif len (contrasenia) < 8:
        print("Contraseña muy corta")
    elif ("1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0") not in contrasenia:
        print("Debe contener un numero")
    else:
        print("Contraseña valida")


#password()