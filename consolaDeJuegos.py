import random
import os

def gamseNumeroAleatorio():
    intentos=0
    numeroRandom=random.randint(1, 10)
    clear()
    print("JUEGO DEL NUMERO ALEATORIO")
    print("Introduce un numero, dependiendo de el numero que introduzcas te mostrare si es mas alto o mas bajo\n")
    while (intentos<3):
        try:
            print(f"introduce un numero entre 1 y 10 (intento {intentos}/3):")
            numIntroducido= int(input())
            if (numIntroducido>numeroRandom):
                print(f"El numero es menor que {numIntroducido}")
                intentos+=1
            elif (numIntroducido<numeroRandom):
                print(f"El nummero es mayor que {numIntroducido}")
                intentos+=1
            else:
                print(f"Enorabuena el numero aleatorio era {numeroRandom}")
                print("Enter to continue")
                input()
                break
        except:
            print("ERROR: Hay que introducir un numero no caracteres")
    if (intentos==3):
        print(f"Vaya parece que ya has alcanzado el maximo de intentos el numero aleatorio era {numeroRandom}\nEnter to continue")
        input()
def gamsePiedraPapelTijera():
    clear()
    print("Juego de piedra, papelo o tijera")
    print("RECUERDA:")
    print("Piedra --> tijera")
    print("Palel --> piedra ")
    print("Tijera --> papel")
    print("\n")
    contadorBot=0
    contadorPlayer=0
    while (contadorPlayer!=3 and contadorBot!=3):
        opcBot = random.randint(1, 3)
        try:
            print(f"Player --> {contadorPlayer} BOT --> {contadorBot}")
            print("Opciones disponibles\n1-Piedra\n2-Papel\n3-Tijera")
            print("Introduce una opcion: ")
            opcPlayer = int(input())
            if (opcPlayer>=1 or opcPlayer<=3):
                if (opcBot==1 and opcPlayer==3):
                    contadorBot+=1
                elif(opcBot==2 and opcPlayer==1):
                    contadorBot+=1
                elif(opcBot==3 and opcPlayer==2):
                    contadorBot+=1
                elif (opcPlayer==1 and opcBot==3):
                    contadorPlayer+=1
                elif(opcPlayer==2 and opcBot==1):
                    contadorPlayer+=1
                elif(opcPlayer==3 and opcBot==2):
                    contadorPlayer+=1
            else:
                print("ERROR: Solo hay 3 opciones")
        except:
            print("ERROR: Solo es posible introducir 1, 2 o 3 (No caracteres)")
        print(f"jugada bot -->{opcBot} jugada player -->{opcPlayer}")
        print("Enter to continue")
        input()
        clear()
    print("Enorabuena has ganado") if contadorPlayer>contadorBot else print("Vaya mas suerte la proxima vez")
    print(f"{contadorPlayer}--> Player \n{contadorBot}-->Bot")
    print("Enter to continue")
    input()
        
def gameColgado():
    clear()
    print("Juegoo de el colgado")
    print("En este juego deveras de adivinar la palabra introduciendo un caracter, \ncada vez que introduzcas un caracter que no esta se restaran los intentos disponibles\ny si aciertas uno de los caracteres se mostraran todos los que existen con ese caracter\n")
    
    numeroRandom = random.randint(0, 30)
    rutaAbsoluta= "/Users/franciscomorales/Documents/Desarrollo_Aplicaciones_Web_2/Proyectos_PRO_INFO/P1 - PYTHON BÀSIC (AVALUABLE)/palabrasGuardadas.txt"
    arrayDatos = extraerDatos(rutaAbsoluta)
    palabraSeleccionada=arrayDatos[numeroRandom]
    intentos = len(palabraSeleccionada)*2
    palabraJuego=""
    salidaColgado=False
    for i in range(len(palabraSeleccionada)):
        palabraJuego+="_"
    while (salidaColgado==False):
        try:
            print(f"INTENTOS: {intentos}")
            print(palabraJuego)
            if (palabraSeleccionada==palabraJuego):
                    print("Enorabuena has adivinado la palabra")
                    print("Enter to continue")
                    input()
                    break
            elif (intentos==0):
                print(f"Vaya parece que no has adivinado la palara, en realidad era {palabraSeleccionada}")
                print("Enter to continue")
                input()
                break
            else:
                print("introduce un caracter:")
                opcColgado = str(input())
                if (len(opcColgado)!=1): 
                    print("ERROR: Solo esta permitido caracteres de longitud 1\nEnter to continue") 
                    input()
                else:
                    print(palabraSeleccionada)
                    for i in range(len(palabraSeleccionada)):
                        if (opcColgado==palabraSeleccionada[i]):
                            palabraJuego = palabraJuego[:i] + opcColgado + palabraJuego[i+1:]
                    intentos=intentos-1
        except:
            print("ERROR: Ha ocurrido un error inesperado")
                    
# funciones adicionales para consola
def extraerDatos(rutaArchivo):
    file = open(rutaArchivo, "r")
    data   = file.read()
    data   = data.split(';')
    return data   

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
while True:
    clear()
    print("JUEGOS DE CONSOLA")
    print("1 - Adivina el numero\n2 - Piedra papel o tijera\n3 - El colgado")
    try:
        print("Option:")
        opc=int(input())
        if opc== 0:
            exit()
        elif opc== 1:
            gamseNumeroAleatorio()
        elif opc== 2:
            gamsePiedraPapelTijera()
        elif opc== 3:
            gameColgado()
        else:
            print("ERROR: Solo hay 3 juegos disponibles")
            print("Enter to continue")
            input()
    except:
        print("ERROR: solo se puede utilizar numeros")
        print("Enter to continue")
        input()