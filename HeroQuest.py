#Codigo del Juego

#Importamos librerias
from SRC.GamePhases import Titulo, Menu, Game, End
from SRC.Control.Current import CurrentState
from SRC.Control.Global import GlobalState       

while True:
    if GlobalState.GlobalGame == CurrentState.titulo:
        Titulo()
    elif GlobalState.GlobalGame == CurrentState.menu:
        Menu()
    elif GlobalState.GlobalGame == CurrentState.juego:
        Game()
    elif GlobalState.GlobalGame == CurrentState.fin:
        End()
#Comming soon English version!