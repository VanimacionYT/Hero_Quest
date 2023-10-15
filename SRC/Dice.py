import random

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
        pass