import random
from IPython.display import clear_output

GlobalDiceMinFaces = 0
GlobalDiceMaxFaces = 0
HealthDiceMinFaces = 0
HealthDiceMaxFaces = 0
AttackDiceMinFaces = 0
AttackDiceMaxFaces = 0
DefenseDiceMinFaces = 0
DefenseDiceMaxFaces = 0

def DiceInitiator():
    with open('Log/LogDices.txt', 'r') as DiceLog:
        DiceIndividualSettings = DiceLog.readline().split(".")
        DIGlobalDiceMinFaces = int(DiceIndividualSettings[0].split("-")[0])
        DIGlobalDiceMaxFaces = int(DiceIndividualSettings[0].split("-")[1])
        DIHealthDiceMinFaces = int(DiceIndividualSettings[1].split("-")[0])
        DIHealthDiceMaxFaces = int(DiceIndividualSettings[1].split("-")[1])
        DIAttackDiceMinFaces = int(DiceIndividualSettings[2].split("-")[0])
        DIAttackDiceMaxFaces = int(DiceIndividualSettings[2].split("-")[1])
        DIDefenseDiceMinFaces = int(DiceIndividualSettings[3].split("-")[0])
        DIDefenseDiceMaxFaces = int(DiceIndividualSettings[3].split("-")[1])
        return DIGlobalDiceMinFaces,DIGlobalDiceMaxFaces,DIHealthDiceMinFaces,DIHealthDiceMaxFaces,DIAttackDiceMinFaces,DIAttackDiceMaxFaces,DIDefenseDiceMinFaces,DIDefenseDiceMaxFaces
    
    

class Dice():
    def GlobalDice():
        #DiceFaces = 6
        Dice = (random.randint(DiceInitiator()[0], DiceInitiator()[1]))
        return Dice
    
    def DiceHealth():
        #DiceFaces = 15
        Dice = (random.randint(DiceInitiator()[2], DiceInitiator()[3]))
        return Dice
    
    def DiceAttack():
        #DiceFaces = 10
        Dice = (random.randint(DiceInitiator()[4], DiceInitiator()[5]))
        return Dice
    
    def DiceDefense():
        #DiceFaces = 10
        Dice = (random.randint(DiceInitiator()[6], DiceInitiator()[7]))
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
            DiceLog.write("1-6.3-15.1-10.1-10")