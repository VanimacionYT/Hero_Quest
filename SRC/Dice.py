import random
from IPython.display import clear_output

class Dice():
    def GlobalDice():
        DiceFaces = 6
        Dice = (random.randint(1, DiceFaces))
        return Dice
    
    def DiceHealth():
        DiceFaces = 15
        Dice = (random.randint(3, DiceFaces))
        return Dice
    
    def DiceAttack():
        DiceFaces = 10
        Dice = (random.randint(1, DiceFaces))
        return Dice
    
    def DiceDefense():
        DiceFaces = 10
        Dice = (random.randint(1, DiceFaces))
        return Dice
    
    def FirstPlayerTurn():
        DiceFaces = 2
        Dice = (random.randint(1,DiceFaces))
        return Dice
    
    def SetDices():
        pass
    
    def ResetDices():
        clear_output()
        open('Log/LogDices.txt', 'w').close
        with open('Log/LogDicess.txt', 'w') as DiceLog:
            DiceLog.write("6.15.10.10.2")