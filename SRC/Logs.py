import locale
from IPython.display import clear_output
from datetime import datetime

def CheckLogs():
    clear_output()
    with open('Log/LogSystem.txt', 'r') as ArchivoLogSys:
        clear_output()
        lines = len(ArchivoLogSys.readlines())
        ArchivoLogSys.seek(0)
    for x in range(lines):
        Linea = ArchivoLogSys.readline()
        Linea = Linea.split(", ")
        print(f"\nGame {x + 1} Date  >>> {Linea[9]}\nPlayer {Linea[10]} {Linea[0]}:\n\tHealth  >> {Linea[1]}\n\tAttack  >> {Linea[2]}\n\tDefense >> {Linea[3]}\nPlayer {Linea[11]} {Linea[4]}:\n\tHealth  >> {Linea[5]}\n\tAttack  >> {Linea[6]}\n\tDefense >> {Linea[7]}\nWinner: {Linea[8]}\n--------------------------------------------------")


def RemoveLogs():
    clear_output()
    locale.setlocale(locale.LC_ALL, 'C')
    Date = datetime.now()
    LogRefreshDate =  Date.strftime("[-- Refresh Created At: %d/%m/%Y - %H:%M:%S --]")    
    open('Log/LogPlayers.txt', 'w').close
    with open('Log/LogPlayers.txt', 'w') as PlayerLogFile:
        PlayerLogFile.write(f"{LogRefreshDate}\nWelcome to the Player Log File\n---------------------------------------")
    open('Log/LogGames.txt', 'w').close
    with open('Log/LogGames.txt', 'w') as GameLogFile:
        GameLogFile.write(f"{LogRefreshDate}\nWelcome to the Game Log File\n-------------------------------------")
    open('Log/LogSystem.txt', 'w').close   
    print("¡Logs Reseted!")

def LogPlayers(Player1, Player1Stats, Player2, Player2Stats):
    locale.setlocale(locale.LC_ALL, 'C')
    Date = datetime.now()
    LogPlayersDate =  (Date.strftime("[-- Characters Log Created At: %d/%m/%Y - %H:%M:%S --]"))
    LogPlayers = (f"\n{LogPlayersDate}\n{Player1} with atributes: {Player1Stats}\n{Player2} with atributes {Player2Stats}\n--------------------------------------------------------")
    with open('Log/LogPlayers.txt', 'a') as PlayerLogFile:
        PlayerLogFile.write(LogPlayers)
    
def LogGames(Player1Stats,Player1Name, Player2Stats, Player2Name, ParameterSelection, SelectedTurns, PlayedTurns, Result, Player1ID, Player2ID):
    if ParameterSelection == "1":
        ParameterSelection = "Random"
    elif ParameterSelection == "2":
        ParameterSelection = "Manual"
    locale.setlocale(locale.LC_ALL, 'C')
    dt = datetime.now()
    LogGamesDate = (dt.strftime("[-- Game Log Created At: %d/%m/%Y - %H:%M:%S --]"))    
    LogGames = f"\n{LogGamesDate}\nPlayer {Player1ID} | {Player1Name}:{Player1Stats}\nPlayer {Player2ID} | {Player2Name}:{Player2Stats}\nParameter Selection = {ParameterSelection}\nTurns [Selected/Played] = {SelectedTurns}/{PlayedTurns}\nResult:{Result}\n--------------------------------------------------"
    with open('Log/LogGames.txt', 'a') as GameLogFile:
        GameLogFile.write(LogGames)

def LogSystem(Player1Name, Player1, Player2Name, Player2, Winner, Player1ID, Player2ID):
    locale.setlocale(locale.LC_ALL, 'C')
    dt = datetime.now()
    LogSysDate =  dt.strftime("%d/%m/%Y - %H:%M:%S")
    DataList = f"{Player1Name}, {Player1}, {Player2Name}, {Player2}, {Winner}, {LogSysDate}, {Player1ID}, {Player2ID}"
    with open('Log/LogSystem.txt', 'a') as ArchivoLogSys:
        ArchivoLogSys.write(f"{DataList}, \n")

