#Importamos librerias
import locale
from datetime import datetime

#Creamos Funciones para almacenar los Logs de la partida y los personajes.
def LogPersonajes(Personaje1, Atributos1, Personaje2, Atributos2):
    # Colocamos un timestamp
    locale.setlocale(locale.LC_ALL, 'C')
    dt = datetime.now()
    LogPeDate =  (dt.strftime("[-- Characters Log Created At: %d/%m/%Y - %H:%M:%S --]"))
    LogPe = ("\n{}\n{} con los atributos: {}\n{} con los atributos {}\n--------------------------------------------------------".format(LogPeDate, Personaje1, Atributos1, Personaje2, Atributos2))
    #Cargamos el .excel que registra los datos, los cargamos y lo cerramos
    ArchivoLogPE = open('Log/LogPersonajes.txt', 'a')
    ArchivoLogPE.write(LogPe)
    ArchivoLogPE.close()
    
def LogPartida(Personaje1,Personaje1Name, Personaje2, Personaje2Name,opcion, TurnosElejidos, TurnosJugados, Resultado):
    #Comprobamos el metodo de asignacion de valores.
    Metodo = ""
    if opcion == "1":
        Metodo = "Automático"
    elif opcion == "2":
        Metodo = "Manual"
        
    # Colocamos un timestamp
    locale.setlocale(locale.LC_ALL, 'C')
    dt = datetime.now()
    LogPaDate = (dt.strftime("[-- Game Log Created At: %d/%m/%Y - %H:%M:%S --]"))    
    LogPa = ("\n{}\nPersonaje 1 | {}:{}\nPersonaje 2 | {}:{}\nMétodo de elección = {}\nTurnos [Elejidos/Jugados] = {}/{}\nResultado:{}\n--------------------------------------------------".format(LogPaDate, Personaje1Name, Personaje1, Personaje2Name, Personaje2, Metodo, TurnosElejidos, TurnosJugados, Resultado))
    #Cargamos el .excel que registra los datos, los cargamos y lo cerramos
    ArchivoLogPA = open('Log/LogPartidas.txt', 'a')
    ArchivoLogPA.write(LogPa)
    ArchivoLogPA.close()
