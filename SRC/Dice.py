import random

#Creamos una clase llamada dado que servira para el sistema de turnos y para la creacion aleatoria de parametros de los personajes      
class Dice():
    #Metodo para los turnos
    def GlobalDice():
        DiceFaces = 6
        Dice = (random.randint(1, DiceFaces))
        return Dice
    #Metodo para generar puntos de vida aleatorios
    def DiceHealth():
        DiceFaces = 15
        Dice = (random.randint(3, DiceFaces))
        return Dice
    #Metodo para generar puntos de ataque aleatorios
    def DiceAttack():
        DiceFaces = 10
        Dice = (random.randint(1, DiceFaces))
        return Dice
    #Metodo para generar puntos de defensa aleatorios
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