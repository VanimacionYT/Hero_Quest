#Codigo del Juego

#Importamos librerias
from SRC.GamePhases import Titulo, Menu, Game, End
from SRC.Control.Current import CurrentState
from SRC.Control.Global import GlobalState       

while True:
    if GlobalState.GlobalGame == CurrentState.titulo:
        Titulo()
        print(GlobalState.GlobalGame)
    elif GlobalState.GlobalGame == CurrentState.menu:
        Menu()
        print(GlobalState.GlobalGame)
    elif GlobalState.GlobalGame == CurrentState.juego:
        Game()
        print(GlobalState.GlobalGame)
    elif GlobalState.GlobalGame == CurrentState.fin:
        End()
        print(GlobalState.GlobalGame)
#Comming soon English version!