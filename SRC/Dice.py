import random

#Creamos una clase llamada dado que servira para el sistema de turnos y para la creacion aleatoria de parametros de los personajes      
class Dado():
    #Metodo para los turnos
    def tira():
        caras = 6
        dado = (random.randint(1, caras))
        return dado
    #Metodo para generar puntos de vida aleatorios
    def tirav():
        caras = 15
        dado = (random.randint(3, caras))
        return dado
    #Metodo para generar puntos de ataque aleatorios
    def tiraa():
        caras = 10
        dado = (random.randint(1, caras))
        return dado
    #Metodo para generar puntos de defensa aleatorios
    def tirad():
        caras = 10
        dado = (random.randint(1, caras))
        return dado