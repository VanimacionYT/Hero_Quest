from SRC.GamePhasesDef import *

def Title():
    TitleShow()

def Menu():    
    MainMenu()        

def Game():
    GamePlay(ParameterSelectionDef(), GameTurnsSelection())

def End():
    EndShow()