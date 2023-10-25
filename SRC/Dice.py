import random
from IPython.display import clear_output


def DiceInitiator():
    with open('Log/LogDices.txt', 'r') as DiceLog:
        DiceIndividualSettings = DiceLog.readline().split(".")
        print(DiceIndividualSettings)
        GlobalDiceMinFaces = DiceIndividualSettings[0].split("-")[0]
        GlobalDiceMaxFaces = DiceIndividualSettings[0].split("-")[1]
        HealthDiceMinFaces = DiceIndividualSettings[1].split("-")[0]
        HealthDiceMaxFaces = DiceIndividualSettings[1].split("-")[1]
        AttackDiceMinFaces = DiceIndividualSettings[2].split("-")[0]
        AttackDiceMaxFaces = DiceIndividualSettings[2].split("-")[1]
        DefenseDiceMinFaces = DiceIndividualSettings[3].split("-")[0]
        DefenseDiceMaxFaces = DiceIndividualSettings[3].split("-")[1]
    return GlobalDiceMinFaces,GlobalDiceMaxFaces,HealthDiceMinFaces,HealthDiceMaxFaces,AttackDiceMinFaces,AttackDiceMaxFaces,DefenseDiceMinFaces,DefenseDiceMaxFaces
        

class Dice():
    def GlobalDice():
        #DiceFaces = 6
        Dice = (random.randint(GlobalDiceMinFaces, GlobalDiceMaxFaces))
        return Dice
    
    def DiceHealth():
        #DiceFaces = 15
        Dice = (random.randint(HealthDiceMinFaces, HealthDiceMaxFaces))
        return Dice
    
    def DiceAttack():
        #DiceFaces = 10
        Dice = (random.randint(AttackDiceMinFaces, AttackDiceMaxFaces))
        return Dice
    
    def DiceDefense():
        #DiceFaces = 10
        Dice = (random.randint(DefenseDiceMinFaces, DefenseDiceMaxFaces))
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