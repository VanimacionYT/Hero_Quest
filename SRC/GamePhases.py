import time
import os
from IPython.display import clear_output
from SRC.Dice import Dice
from SRC.Players import Player
from SRC.Logs import LogPlayers, LogGames, RemoveLogs, CheckLogs, LogSystem
from SRC.Control.Current import CurrentState
from SRC.Control.Global import GlobalState
from SRC.Control.Exceptions import SameNameError, BadNameError

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
        print("<---<-MAIN MENU->--->\n\n\t- Play HQ: \t\t1\n\t- Check Logs: \t\t2\n\t- Delete Logs: \t\t3\n\t- Set Dice Values: \t4\n\t- Reset Dice Values: \t5\n\t- Exit: \t\t6\n")
        Selection = input()
        if Selection == "1":
            menu = False
            GlobalState.GlobalGame = CurrentState.GAME
        elif Selection == "2":
            CheckLogs()
        elif Selection == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("¿Are you sure you want to delete the logs?\nYes, I'm sure: 1\t|\tNo, I don't want to delete them: 2")
            Confirmation = input()                
            if Confirmation == "1":
                RemoveLogs()
            elif Confirmation == "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                menu = True
        elif Selection == "4":
            Dice.SetDices()
            Dice.DiceInitiator(Dice)
            menu = True
        elif Selection == "5":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("¿Are you sure you want to reset the dices?\nYes, I'm sure: 1\t|\tNo, I don't want to reset them: 2")
            Confirmation = input()                
            if Confirmation == "1":
                Dice.ResetDices()
            elif Confirmation == "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                menu = True
        elif Selection == "6":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("¿Are you sure you want to exit?\nYes: 1\t|\tNo: 2")
            Confirmation = input()                
            if Confirmation == "1":
                quit()
            elif Confirmation == "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                menu = True
        else:
            time.sleep(1)
            print("Wrong Option!\nChoose a valid option!")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            menu = True

def Game():
    print("What player stats selection mode do you want?\n\nRandom: 1\t|\tManual:2\n")
    ParameterSelection = input()
    os.system('cls' if os.name == 'nt' else 'clear')
    if ParameterSelection == "1":
        retry = 3
        for i in range(i):
            try:
                if i != 0:
                    print(f"Retry Number {i}/3\n")
                print("\tLet's Create PLAYER 1") 
                print("PLAYER 1 Name: ")
                Player1Name = input()
                if len(Player1Name) < 3:
                    raise BadNameError()
                Player1Health = Dice.DiceHealth(Dice)
                Player1Attack = Dice.DiceAttack(Dice)
                Player1Defense = Dice.DiceDefense(Dice)
                print("\tLet's Create PLAYER 2") 
                print("PLAYER 2 Name: ")
                Player2Name = input()
                if len(Player2Name) < 3:
                    raise BadNameError()
                if Player2Name == Player1Name:
                    raise SameNameError()
                Player2Health = Dice.DiceHealth(Dice)
                Player2Attack = Dice.DiceAttack(Dice)
                Player2Defense = Dice.DiceDefense(Dice)

            except SameNameError:
                time.sleep(1)
                print("¡Name Is Same as Player 1!")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Input a different name")
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                if i < retry:
                    continue
                else:
                    print("¡Error Limit Exceded!\n\nEnding Program")
                    time.sleep(2)
                    raise
            
            except BadNameError:
                time.sleep(1)
                print("¡Name Is Too Short!")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Input a 3 character name")
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                if i < retry:
                    continue
                else:
                    print("¡Error Limit Exceded!\n\nEnding Program")
                    time.sleep(2)
                    raise
            except:
                time.sleep(1)
                print("¡Wrong Value!")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Input a correct value")
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                if i < retry:
                    continue
                else:
                    print("¡Error Limit Exceded!\n\nEnding Program")
                    time.sleep(2)
                    raise

    elif ParameterSelection == "2":
        retry = 3
        for i in range(retry):
            if i != 0:
                print(f"Retry Number {i}/3\n")
            try:    
                print("\tLet's Create PLAYER 1") 
                print("PLAYER 1 Name: ")
                Player1Name = input()
                if len(Player1Name) < 3:
                    raise BadNameError()
                print("PLAYER 1 Health: ")
                Player1Health = int(input())
                print("PLAYER 1 Attack: ")
                Player1Attack = int(input())
                print("PLAYER 1 Defense: ")
                Player1Defense = int(input())
                print("\tLet's Create PLAYER 2") 
                print("PLAYER 2 Name: ")
                Player2Name = input()
                if len(Player1Name) < 3:
                    raise BadNameError()
                if Player2Name == Player1Name:
                    raise SameNameError()
                print("PLAYER 2 Health: ")
                Player2Health = int(input())
                print("PLAYER 2 Attack: ")
                Player2Attack = int(input())
                print("PLAYER 2 Defense: ")
                Player2Defense = int(input())

            except SameNameError:
                time.sleep(1)
                print("¡Name Is Same as Player 1!")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Input a different name")
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                if i < retry:
                    continue
                else:
                    print("¡Error Limit Exceded!\n\nEnding Program")
                    time.sleep(2)
                    raise
            
            except BadNameError:
                time.sleep(1)
                print("¡Name Is Too Short!")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Input a 3 character name")
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                if i < retry:
                    continue
                else:
                    print("¡Error Limit Exceded!\n\nEnding Program")
                    time.sleep(2)
                    raise

            except:
                time.sleep(1)
                print("¡Wrong Value!")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Input a correct value")
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                if i < retry:
                    continue
                else:
                    print("¡Error Limit Exceded!\n\nEnding Program")
                    time.sleep(2)
                    raise

    else:
        print("¡ERROR!\nSelect a valid option")
        os.system('cls' if os.name == 'nt' else 'clear')

    os.system('cls' if os.name == 'nt' else 'clear')
    Player1 = Player("1", Player1Name, Player1Health, Player1Attack, Player1Defense) 
    Player2 = Player("2", Player2Name, Player2Health, Player2Attack, Player2Defense)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    if ParameterSelection == "1":
        print("Parameter Selection: Random")
    elif ParameterSelection == "2":
        print("Parameter Selection: Manual")
    print("\n", Player1)
    print("\n", Player2)
    Player1LogSys = Player1.logSys()
    Player2LogSys = Player2.logSys()
    LogPlayers(Player1.name, Player1.logInfo(), Player2.name, Player2.logInfo())

    retry = 3
    for i in range(retry):
        if i != 0:
            print(f"Retry Number {i}/3\n")
    print("\nHow many game turns do you want to play?: ")
    try:
        GameTurns = int(input())
    except:
        time.sleep(1)
        print("¡Wrong Value!")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Input a correct value")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        if GameTurns == 0:
            GameTurns = 2147483647

    if Dice.FirstPlayerTurn() == 1:
        Attacker = "Player1"
        Defensor = "Player2"
    else:
        Attacker = "Player2"
        Defensor = "Player1"
    
    if GameTurns == 0:
        GameTurns = 2147483647
    PlayedTurn = 0
    for x in range(GameTurns):
        PlayedTurn += 1
        time.sleep(1)
        if Attacker == "Player2":
            Attacker = "Player1"
        elif Attacker == "Player1":
            Attacker = "Player2"
        if Defensor == "Player2":
            Defensor = "Player1"
        elif Defensor == "Player1":
            Defensor = "Player2"
        turnolog = (f"\n<<< TURN {x + 1} | {Attacker} attacks {Defensor} >>>")
        print(turnolog)
        if Attacker == "Player1":
            AttackNumber = Player1.Attack()
            Player2.Defense(AttackNumber)
        elif Attacker == "Player2":
            AttackNumber = Player2.Attack()
            Player1.Defense(AttackNumber)
        Player1.ItsAlive()
        Player2.ItsAlive()
        if Player1.ItsAlive() == False:
            Result = (f"The winner is Player {Player2.PlayerID} {Player2.name}")
            break
        if Player2.ItsAlive() == False:
            Result = (f"The winner is Player {Player1.PlayerID} {Player1.name}")
            break
    if Player1.ItsAlive() == True and Player2.ItsAlive() == True:
        Result = ("It's a Tie! Both players survive!")
    print(f"\n\t{Result}")
      
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
        else:
            time.sleep(1)
            print("¡Wrong Value!")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Input a correct value")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')