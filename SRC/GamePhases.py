import time
from IPython.display import clear_output
from SRC.Dice import Dice
from SRC.Players import Player
from SRC.Logs import LogPlayers, LogGames, RemoveLogs, CheckLogs, LogSystem
from SRC.Control.Current import CurrentState
from SRC.Control.Global import GlobalState

def Title():
    Dice.DiceInitiator(Dice)
    print("----------------------------\n--------[HERO QUEST]--------\n----------------------------\n----------------------V2.8.0\nPress 'ENTER' to start!")
    input()
    clear_output()
    GlobalState.GlobalGame = CurrentState.MENU
    return

def Menu():
    menu = True
    while menu == True:
        print("<---<-MAIN MENU->--->\n\nPlay HQ: 1\t|\tCheck Logs: 2\t|\tDelete Logs: 3\t\t|\tSet Random Values: 4\t|\tExit: 5\n")
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
            Dice.SetDices()

        elif Selection == "5":
            Dice.ResetDices()

        elif Selection == "6":
            quit()

def Game():
    print("What player stats selection mode do you want?\n\nRandom: 1\t|\tManual:2\n")
    ParameterSelection = input()
    clear_output()
    if ParameterSelection == "1":
        print("\tLet's Create PLAYER 1") 
        print("PLAYER 1 Name: ")
        Player1Name = input()
        Player1Health = Dice.DiceHealth(Dice)
        Player1Attack = Dice.DiceAttack(Dice)
        Player1Defense = Dice.DiceDefense(Dice)
        Player1 = Player("1", Player1Name, Player1Health, Player1Attack, Player1Defense) 
        print("\tLet's Create PLAYER 2") 
        print("PLAYER 2 Name: ")
        Player2Name = input()
        Player2Health = Dice.DiceHealth(Dice)
        Player2Attack = Dice.DiceAttack(Dice)
        Player2Defense = Dice.DiceDefense(Dice)
        Player2 = Player("2", Player2Name, Player2Health, Player2Attack, Player2Defense)

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
        clear_output()

    if ParameterSelection == "1":
        print("Parameter Selection: Random")
    elif ParameterSelection == "2":
        print("Parameter Selection: Manual")
    print("\n", Player1)
    print("\n", Player2)
    Player1LogSys = Player1.logSys()
    Player2LogSys = Player2.logSys()
    LogPlayers(Player1.name, Player1.logInfo(), Player2.name, Player2.logInfo())

    print("\nHow many game turns do you want to play?: ")
    GameTurns = int(input())
        
    if Dice.FirstPlayerTurn() == 1:
        Attacker = "Player1"
        Defensor = "Player2"
    else:
        Attacker = "Player2"
        Defensor = "Player1"

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