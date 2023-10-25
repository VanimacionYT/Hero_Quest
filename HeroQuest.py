from SRC.GamePhases import Title, Menu, Game, End
from SRC.Control.Current import CurrentState
from SRC.Control.Global import GlobalState       

while True:
    if GlobalState.GlobalGame == CurrentState.TITLE:
        Title()
    elif GlobalState.GlobalGame == CurrentState.MENU:
        Menu()
    elif GlobalState.GlobalGame == CurrentState.GAME:
        Game()
    elif GlobalState.GlobalGame == CurrentState.END:
        End()