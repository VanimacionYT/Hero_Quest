import random
import os

class Dice():
    __DIGlobalDiceMinFaces = 0
    __DIGlobalDiceMaxFaces = 0
    __DIHealthDiceMinFaces = 0
    __DIHealthDiceMaxFaces = 0
    __DIAttackDiceMinFaces = 0
    __DIAttackDiceMaxFaces = 0
    __DIDefenseDiceMinFaces = 0
    __DIDefenseDiceMaxFaces = 0
    
    def DiceInitiator(self):
        with open('Log/LogDices.txt', 'r') as DiceLog:
            DiceIndividualSettings = DiceLog.readline().split(".")
            self.__DIGlobalDiceMinFaces = int(DiceIndividualSettings[0].split("-")[0])
            self.__DIGlobalDiceMaxFaces = int(DiceIndividualSettings[0].split("-")[1])
            self.__DIHealthDiceMinFaces = int(DiceIndividualSettings[1].split("-")[0])
            self.__DIHealthDiceMaxFaces = int(DiceIndividualSettings[1].split("-")[1])
            self.__DIAttackDiceMinFaces = int(DiceIndividualSettings[2].split("-")[0])
            self.__DIAttackDiceMaxFaces = int(DiceIndividualSettings[2].split("-")[1])
            self.__DIDefenseDiceMinFaces = int(DiceIndividualSettings[3].split("-")[0])
            self.__DIDefenseDiceMaxFaces = int(DiceIndividualSettings[3].split("-")[1])

    def GlobalDice(self):
        Dice = (random.randint(self.__DIGlobalDiceMinFaces, self.__DIGlobalDiceMaxFaces))
        return Dice
    
    def DiceHealth(self):
        Dice = (random.randint(self.__DIHealthDiceMinFaces, self.__DIHealthDiceMaxFaces))
        return Dice
    
    def DiceAttack(self):
        Dice = (random.randint(self.__DIAttackDiceMinFaces, self.__DIAttackDiceMaxFaces))
        return Dice
    
    def DiceDefense(self):
        Dice = (random.randint(self.__DIDefenseDiceMinFaces, self.__DIDefenseDiceMaxFaces))
        return Dice
    
    def FirstPlayerTurn():
        DiceFaces = 2
        Dice = (random.randint(1,DiceFaces))
        return Dice
    
    def SetDices():
        os.system('cls' if os.name == 'nt' else 'clear')
        open('Log/LogDices.txt', 'w').close
        try:
            MinGlobalSet = int(input("Play Dice Min Number (Default 1)\n"))
            if type(MinGlobalSet) != int:
                raise ValueError()
            MaxGlobalSet = int(input("Play Dice Max Number (Default 6)\n"))
            if type(MinGlobalSet) != int:
                raise ValueError()
            MinHealthSet = int(input("Min Health Pt (Default 3)\n"))
            if type(MinGlobalSet) != int:
                raise ValueError()
            MaxHealthSet = int(input("Max Health Pt (Default 15)\n"))
            if type(MinGlobalSet) != int:
                raise ValueError()
            MinAttackSet = int(input("Min Attack Pt (Default 1)\n"))
            if type(MinGlobalSet) != int:
                raise ValueError()
            MaxAttackSet = int(input("Max Attack Pt (Default 10)\n"))
            if type(MinGlobalSet) != int:
                raise ValueError()
            MinDeffenseSet = int(input("Min Deffense Pt (Default 1)\n"))
            if type(MinGlobalSet) != int:
                raise ValueError()
            MaxDeffenseSet = int(input("Max Deffense Pt (Default 10)\n"))
            if type(MinGlobalSet) != int:
                raise ValueError()
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Wrong Value!")
            Dice.SetDices()
        with open('Log/LogDices.txt', 'w') as DiceLog:
            DiceLog.write(f"{MinGlobalSet}-{MaxGlobalSet}.{MinHealthSet}-{MaxHealthSet}.{MinAttackSet}-{MaxAttackSet}.{MinDeffenseSet}-{MaxDeffenseSet}")    
        
    
    def ResetDices():
        os.system('cls' if os.name == 'nt' else 'clear')
        open('Log/LogDices.txt', 'w').close
        with open('Log/LogDices.txt', 'w') as DiceLog:
            DiceLog.write("1-6.3-15.1-10.1-10")