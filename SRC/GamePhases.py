import locale
import time
from IPython.display import clear_output
from datetime import datetime
from SRC.Dice import Dado
from SRC.Players import Momia, Barbaro
from SRC.Logs import LogPartida, LogPersonajes
from SRC.Control.Current import CurrentState
from SRC.Control.Global import GlobalState





def Titulo():
    #Titulo
    print("----------------------------")
    print("--------[HERO QUEST]--------")
    print("----------------------------\n----------------------V2.6.0\n")

    #Sistema para iniciar
    print("Presiona 'ENTER' para empezar!")
    input()

    #Borrar lo anterior
    clear_output()
    GlobalState.GlobalGame = CurrentState.menu
    return

def Menu():
    #Se crea un menu para elegir si jugar o borrar logs
        menu = True
        while menu == True:
            print("<---<-MAIN MENU->--->\n\nJugar HQ: 1\t|\tBorrar Logs: 2\t\t|\tSalir: 3\n")
            mainmenu = input()
            
            if mainmenu == "1":
                menu = False
                GlobalState.GlobalGame = CurrentState.juego

                #Si se elige borrar logs se aplica un texto de confirmación.
            elif mainmenu == "2":
                clear_output()
                print("¿Estas seguro de querer borrar los logs?\nSi, Estoy seguro: 1\t|\tNo, No quiero borrarlos: 2")
                confirmar = input()
                
                if confirmar == "1":
                    #Si elige borarlos se reescriben los logs con un mensaje que indica la fecha de la limpieza y se limpia la consola.
                    clear_output()
                    locale.setlocale(locale.LC_ALL, 'C')
                    dt = datetime.now()
                    LogRefreshDate =  (dt.strftime("[-- Refresh Created At: %d/%m/%Y - %H:%M:%S --]"))
                    ArchivoLogPE = open('Log/LogPersonajes.txt', 'w').close
                    ArchivoLogPE = open('Log/LogPersonajes.txt', 'w')
                    ArchivoLogPE.write("{}\nBienvenido al archivo de Log Personajes\n---------------------------------------".format(LogRefreshDate))
                    ArchivoLogPE.close()
                    ArchivoLogPA = open('Log/LogPartidas.txt', 'w').close
                    ArchivoLogPA = open('Log/LogPartidas.txt', 'w')
                    ArchivoLogPA.write("{}\nBienvenido al archivo de Log Partidas\n-------------------------------------".format(LogRefreshDate))
                    ArchivoLogPA.close()
                    print("¡Logs Reiniciados!")
                elif confirmar == "2":
                    clear_output()
                    menu = True
            elif mainmenu == "3":
                quit()

def Game():
     #Mediante un if se selecciona la opcion de parametroa aleatorios o manuales
        print("Quieres colocar parametros de personaje aleatorios o manuales?\n\nAleatorio: 1\t|\tManuales:2\n")
        opcion = input()

        #Tras seleccionar se limpia la pantalla
        clear_output()

        #Si es aletorio se hace uso del objeto Dado() con sus respectivos metodos
        if opcion == "1":
            print("\tVamos a definir el nombre de la MOMIA") 
            print("Nombre Momia")
            NomM = input()
            VidM = Dado.tirav()
            AtaM = Dado.tiraa()
            DefM = Dado.tirad()
            Momia1 = Momia(NomM, VidM, AtaM, DefM)
            
            print("\n\tVamos a definir el nombre del BARBARO")  
            print("Nombre Barbaro")
            NomB = input()
            VidB = Dado.tirav()
            AtaB = Dado.tiraa()
            DefB = Dado.tirad()
            Barbaro1 = Barbaro(NomB, VidB, AtaB, DefB)
        #Si es manual, el usuario por medio de imputs() selecciona los datos
        elif opcion == "2":    
            print("\tVamos a definir los valores de la MOMIA") 
            print("Nombre Momia")
            NomM = input()
            print("Vida Momia")
            VidM = int(input())
            print("Ataque Momia")
            AtaM = int(input())
            print("Defensa Momia")
            DefM = int(input())
            Momia1 = Momia(NomM, VidM, AtaM, DefM)

            print("\n\tVamos a definir los valores del BARBARO")  
            print("Nombre Barbaro")
            NomB = input()
            print("Vida Barbaro")
            VidB = int(input())
            print("Ataque Barbaro")
            AtaB = int(input())
            print("Defensa Barbaro")
            DefB = int(input())
            Barbaro1 = Barbaro(NomB, VidB, AtaB, DefB)
        else:
            print("¡ERROR!\nSelecciona una opcion valida")
            
        #Se borran los textos
        clear_output()

        #Se muestran los parametros de cada personaje y las opciones de la partida y se guardan en los logs
        if opcion == "1":
            print("Módo de elección de parámetros: Automático")
        elif opcion == "2":
            print("Módo de elección de parámetros: Manual")
        print("\n", Momia1)
        print("\n", Barbaro1)
        LogPersonajes(Momia1.nombre, Momia1.logInfo(), Barbaro1.nombre, Barbaro1.logInfo())

        #Se indican los turnos
        print("\n¿Cuántos turnos máximos quiere jugar?: ")
        turnos = int(input())
        #Se asigna los valores para el sistema de turnos. J1 es la momia y J2 es el barbaro.
        Atacante = "Bárbaro"
        Defensor = "Momia"
        turno = 0
        for x in range(turnos):
            turno += 1
            #Mediante un bucle y varios If deternminamos los turnos
            time.sleep(1) #implentamos un timesleep(x) para poder hacer que los bucles tengan pausa de x segundos.
            if Atacante == "Bárbaro":
                Atacante = "Momia"
            elif Atacante == "Momia":
                Atacante = "Bárbaro"
            if Defensor == "Bárbaro":
                Defensor = "Momia"
            elif Defensor == "Momia":
                Defensor = "Bárbaro"
            turnolog = ("\n<<< TURNO {} | {} ataca a {} >>>".format(x + 1, Atacante, Defensor))
            print(turnolog)
            #Dependiendo de quien es el Jugador 1 (atacante) se ejecutara el .atacar de un jugador u otro
            if Atacante == "Bárbaro":
                Numataques = Barbaro1.atacar()
                Momia1.defender(Numataques)
            elif Atacante == "Momia":
                Numataques = Momia1.atacar()
                Barbaro1.defender(Numataques)
            #tras los ataques se revisa si los jugadores estan vivos
            Barbaro1.estarVivo()
            Momia1.estarVivo()
            #Dependiendo de lo que devuelva .personajeVivo() se sigue o no con el combate
            if Barbaro1.personajeVivo == False:
                resultado = ("\n\tEl ganador del combate es la Momia {} con {} pt de vida".format(Momia1.nombre, Momia1.vida))
                break
            if Momia1.personajeVivo == False:
                resultado = ("\n\tEl ganador del combate es el Barbaro {} con {} pt de vida".format(Barbaro1.nombre, Barbaro1.vida))
                break
        if Barbaro1.personajeVivo == True and Momia1.personajeVivo == True:
            resultado = ("\n\tEl combate queda en un empate! Ambos jugadores sobreviven!")
        print(resultado)

        #Se muestra por pantalla los resultados y se guardan los logs de la partida.        
        ResultadoMomia = ("\n\tMOMIA:   {} queda con {} pt de vida.".format(Momia1.nombre, Momia1.vida))    
        ResultadoBarbaro = ("\n\tBARBARO: {} queda con {} pt de vida.".format(Barbaro1.nombre, Barbaro1.vida))
        ResultadoPartida = (ResultadoMomia + ResultadoBarbaro)
        print(ResultadoPartida)
        LogPartida(Momia1.logInfo(),Momia1.nombre, Barbaro1.logInfo(),Barbaro1.nombre, opcion, turno, turnos, ResultadoPartida)
        GlobalState.GlobalGame = CurrentState.fin

def End():
    print("\n-- Volver a jugar: 1\t|\tVolver al menu: 2\t|\tSalir: 3 --\n")
    GameOver = input()
    while True:
        if GameOver == "1":
            GlobalState.GlobalGame = CurrentState.juego
            break
        if GameOver == "2":
            GlobalState.GlobalGame = CurrentState.menu
            break
        if GameOver== "3":
            quit()