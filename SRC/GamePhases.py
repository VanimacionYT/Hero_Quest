import locale
import time
from IPython.display import clear_output
from datetime import datetime
from SRC.Dice import Dice
from SRC.Players import Player
from SRC.Logs import LogPlayers, LogGames, RemoveLogs, CheckLogs, LogSystem
from SRC.Control.Current import CurrentState
from SRC.Control.Global import GlobalState





def Title():
    #Titulo
    print("----------------------------")
    print("--------[HERO QUEST]--------")
    print("----------------------------\n----------------------V2.8.0\n")

    #Sistema para iniciar
    print("Press 'ENTER' to start!")
    input()

    #Borrar lo anterior
    clear_output()
    GlobalState.GlobalGame = CurrentState.MENU
    return

def Menu():
    #Se crea un menu para elegir si jugar o borrar logs
        menu = True
        while menu == True:
            print("<---<-MAIN MENU->--->\n\nPlay HQ: 1\t|\tCheck Logs: 2\t\t|\tDelete Logs: 3\t\t|\tExit: 4\n")
            Selection = input()
            
            if Selection == "1":
                menu = False
                GlobalState.GlobalGame = CurrentState.GAME

            elif Selection == "2":
                CheckLogs()

            elif Selection == "3":
                clear_output()
                print("¿Are you sure you want to delete the logs?\nYes, I'm sure: 1\t|\tNo, I don't want to delete them: 2")
                Confirmation = input()
                
                if Confirmation == "1":
                    RemoveLogs()
                elif Confirmation == "2":
                    clear_output()
                    menu = True

            elif Selection == "4":
                quit()

def Game():
     #Mediante un if se selecciona la opcion de parametroa aleatorios o manuales
        print("What player stats selection mode do you want?\n\nRandom: 1\t|\tManual:2\n")
        ParameterSelection = input()

        #Tras seleccionar se limpia la pantalla
        clear_output()

        #Si es aletorio se hace uso del objeto Dado() con sus respectivos metodos
        if ParameterSelection == "1":
            print("\tLet's Create PLAYER 1") 
            print("PLAYER 1 Name: ")
            Player1Name = input()
            Player1Health = Dice.DiceHealth()
            Player1Attack = Dice.DiceAttack()
            Player1Defense = Dice.DiceDefense()
            Player1 = Player("1", Player1Name, Player1Health, Player1Attack, Player1Defense)
            
            print("\tLet's Create PLAYER 2") 
            print("PLAYER 2 Name: ")
            Player2Name = input()
            Player2Health = Dice.DiceHealth()
            Player2Attack = Dice.DiceAttack()
            Player2Defense = Dice.DiceDefense()
            Player2 = Player("2", Player2Name, Player2Health, Player2Attack, Player2Defense)

        #Si es manual, el usuario por medio de imputs() selecciona los datos
        elif ParameterSelection == "2":    
            print("\tLet's Create PLAYER 1") 
            print("PLAYER 1 Name: ")
            Player1Name = input()
            print("PLAYER 1 Health: ")
            Player1Health = int(input())
            print("PLAYER 1 Attack: ")
            Player1Attack = int(input())
            print("PLAYER 1 Defense: ")
            Player1Defense = int(input())
            Player1 = Player("1", Player1Name, Player1Health, Player1Attack, Player1Defense)

            print("\tLet's Create PLAYER 2") 
            print("PLAYER 2 Name: ")
            Player2Name = input()
            print("PLAYER 2 Health: ")
            Player2Health = int(input())
            print("PLAYER 2 Attack: ")
            Player2Attack = int(input())
            print("PLAYER 2 Defense: ")
            Player2Defense = int(input())
            Player2 = Player("2", Player2Name, Player2Health, Player2Attack, Player2Defense)
        else:
            print("¡ERROR!\nSelect a valid option")
            
        #Se borran los textos
        clear_output()

        #Se muestran los parametros de cada personaje y las opciones de la partida y se guardan en los logs
        if ParameterSelection == "1":
            print("Parameter Selection: Random")
        elif ParameterSelection == "2":
            print("Parameter Selection: Manual")
        print("\n", Player1)
        print("\n", Player2)
        Player1LogSys = Player1.logSys()
        Player2LogSys = Player2.logSys()
        LogPlayers(Player1.name, Player1.logInfo(), Player2.name, Player2.logInfo())

        #Se indican los turnos
        print("\nHow many game turns do you want to play?: ")
        GameTurns = int(input())
        #Se asigna los valores para el sistema de turnos. J1 es la momia y J2 es el barbaro.
        
        if Dice.FirstPlayerTurn() == 1:
            Attacker = "Player1"
            Defensor = "Player2"
        else:
            Attacker = "Player2"
            Defensor = "Player1"

        PlayedTurn = 0
        for x in range(GameTurns):
            PlayedTurn += 1
            #Mediante un bucle y varios If deternminamos los turnos
            time.sleep(1) #implentamos un timesleep(x) para poder hacer que los bucles tengan pausa de x segundos.
            if Attacker == "Player2":
                Attacker = "Player1"
            elif Attacker == "Player1":
                Attacker = "Player2"
            if Defensor == "Player2":
                Defensor = "Player1"
            elif Defensor == "Player1":
                Defensor = "Player2"
            turnolog = ("\n<<< TURN {} | {} attacks {} >>>".format(x + 1, Attacker, Defensor))
            print(turnolog)
            #Dependiendo de quien es el Jugador 1 (atacante) se ejecutara el .atacar de un jugador u otro
            if Attacker == "Player1":
                AttackNumber = Player1.Attack()
                Player1.Defense(AttackNumber)
            elif Attacker == "Player2":
                AttackNumber = Player2.Attack()
                Player2.Defense(AttackNumber)
            #tras los ataques se revisa si los jugadores estan vivos
            Player1.ItsAlive()
            Player2.ItsAlive()
            #Dependiendo de lo que devuelva .personajeVivo() se sigue o no con el combate
            if Player1.ItsAlive() == False:
                Result = (f"The winner is Player {Player2.PlayerID} {Player2.name}")
                break
            if Player2.ItsAlive() == False:
                Result = (f"The winner is Player {Player1.PlayerID} {Player1.name}")
                break
        if Player1.ItsAlive() == True and Player2.ItsAlive() == True:
            Result = ("It's a Tie! Both players survive!")
        print(f"\n\t{Result}")

        #Se muestra por pantalla los resultados y se guardan los logs de la partida.        
        Player1Result = (f"\n\tPlayer1:   {Player1.name} stays at {Player1.health} health pt.")
        Player2Result = (f"\n\tPlayer2:   {Player2.name} stays at {Player2.health} health pt.")
        GameResult = (Player1Result + Player2Result)
        print(GameResult)
        LogGames(Player1.logInfo(), Player1.name, Player2.logInfo(), Player2.name, ParameterSelection, PlayedTurn, GameTurns, GameResult, Player1.PlayerID, Player2.PlayerID)
        LogSystem(Player1.name, Player1LogSys, Player2.name, Player2LogSys, Result, Player1.PlayerID, Player2.PlayerID)
        GlobalState.GlobalGame = CurrentState.END

def End():
    print("\n-- Play Again: 1\t|\tReturn to Menu: 2\t|\tExit: 3 --\n")
    GameOver = input()
    while True:
        if GameOver == "1":
            GlobalState.GlobalGame = CurrentState.GAME
            break
        if GameOver == "2":
            GlobalState.GlobalGame = CurrentState.MENU
            break
        if GameOver== "3":
            quit()