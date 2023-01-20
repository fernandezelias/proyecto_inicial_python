# CODE:40

import csv
import random
import interfaz

# Funcion "leer_palabra_secreta"
def leer_palabra_secreta(csvfilename):

    csvfile = open('palabras.csv')

    lista_palabras = list(csv.DictReader(csvfile))
    
    for palabra in lista_palabras:
        lista_palabras_secretas = palabra['palabras']
        #print(lista_palabras_secretas)
    
    palabra_random = random.choice(lista_palabras)
    palabra_secreta = str(palabra_random['palabras'])
    return palabra_secreta


# Funcion "pedir_letra"
def pedir_letra(letras_usadas):

    letra = str(input('Ingrese una nueva letra: ').lower())

    while True:           
        if len(letra) > 1:
            print('¡Error! Debe ingresar una solo letra.')
        elif letra in letras_usadas:
            print(f'La letra "{letra}" ya ha sido ingresada.')
        elif letra.isalpha() == False:
            print(f'¡Error! Debe ingresar sólo letras.')
        elif len(letra) == 1 and letra not in letras_usadas:
            letras_usadas.append(letra)
        break

    return letra


# Funcion "verificar_letra"
def verificar_letra(letra, palabra_secreta):

    for i in palabra_secreta:
        if letra in palabra_secreta:
            print('¡CORRECTO! La letra escogida se encuentra en la palabra secreta.')
            return True
        else:
            print('¡INCORRECTO! La letra escogida no se encuentra en la palabra secreta.')
            return False


# Funcion "validar_palabra"
def validar_palabra(letras_usadas, palabra_secreta):

    for letra in palabra_secreta:
        if letra in letras_usadas:
            continue
        elif letra not in letras_usadas:
            return False
    return True


# Bloque principal del programa
if __name__ == "__main__":
    print("\n¡Aquí comienza el juego del ahorcado!\n")
    # Inicializo las variables y listas a utilizar.
    max_cantidad_intentos = 7
    intentos = 0
    letras_usadas = []
    es_ganador = False

    # Leer la palabra secreta de un archivo csv.
    palabra_secreta = leer_palabra_secreta('palabras.csv')
    
    # Esto se realiza para que el jugador pueda ver al principio
    # la cantidad de letras de la palabra a adivinar.
    interfaz.dibujar(palabra_secreta, letras_usadas, intentos)
    
    while intentos < max_cantidad_intentos == 7 and not es_ganador:
        # Pedir una nueva letra
        letra = pedir_letra(letras_usadas)

        # Verificar si la letra es parte de la palabra secreta        
        if verificar_letra(letra, palabra_secreta) == False:
            # En caso de no estar la letra ingresada en la palabra
            # a adivinar incremento en 1 la variable intentos.
            intentos += 1
        
        # Dibujar la interfaz
        interfaz.dibujar(palabra_secreta, letras_usadas, intentos)

        # Validar si la palabra secreta se ha adivinado
        if validar_palabra(letras_usadas, palabra_secreta) == True:
            es_ganador = True
            break

    if es_ganador:
        print(f'\n¡Usted ha ganado la partida!, palabra secreta {palabra_secreta}!\n')
    else:
        print('\n¡Ahorcado!')
        print(f'\n¡Usted ha perdido la partida!, palabra secreta {palabra_secreta}!\n')