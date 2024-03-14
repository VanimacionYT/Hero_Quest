import time
import os
from IPython.display import clear_output
from SRC.Dice import Dice
from SRC.Players import Player
from SRC.Logs import LogPlayers, LogGames, RemoveLogs, CheckLogs, LogSystem
from SRC.Control.Current import CurrentState
from SRC.Control.Global import GlobalState
from SRC.Control.Exceptions import SameNameError, BadNameError
from SRC.GamePhasesDef import *

def Title():
    os.system('cls' if os.name == 'nt' else 'clear')
    Dice.DiceInitiator(Dice)
    print(f"----------------------------\n--------[HERO QUEST]--------\n----------------------------\n----------------------------\tV{GlobalState.Version}\nPress 'ENTER' to start!")
    input()
    os.system('cls' if os.name == 'nt' else 'clear')
    GlobalState.GlobalGame = CurrentState.MENU
    return

def Menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    menu = True
    while menu == True:
        MainMenu()
        break        

def Game():
    GamePlay(ParameterSelectionDef(), GameTurnsSelection())

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
        else:
            time.sleep(1)
            print("¡Wrong Value!")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Input a correct value")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')