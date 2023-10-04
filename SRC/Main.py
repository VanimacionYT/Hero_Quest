#Codigo del Juego

#Creamnos la clase Personaje
class Personaje:
    
    #___ATRIBUTOS___#
    
    __nombre = ""
    __vida = 0 #numero de puntos de vida, baja -1 por ataque efectuado exitosamente
    __ataque = 0 #numero de lanzamientos de dado para atacar
    __defensa = 0 #numero de tiradas de dado para defender
    personajeVivo = True #indica si el personaje sigue vivo
    
    #___MÉTODOS___#
    
    #Constructor
    def __init__(self, nombre, vida, ataque, defensa):
        self.__nombre = nombre
        self.__vida = vida
        self.__ataque = ataque
        self.__defensa = defensa
        print("Personaje {} creado!".format(self.__nombre))
    
    #String. Define los atributos del personaje
    def __str__(self):
        return "Personaje {}:\n Vida  \t > {} pt\n Ataque  > {} pt\n Defensa > {} pt".format(self.__nombre, self.__vida, self.__ataque, self.__defensa)
    
    #Metodo guardado Log personaje
    def logInfo(self):
        return "\n- Vida    > {} pt\n- Ataque  > {} pt\n- Defensa > {} pt".format(self.__vida, self.__ataque, self.__defensa)
    
    #Metodo para verificar el estado del personaje. En caso de tener vida positiva el estado sera "vivo", en caso de vida negativa o cero el estado será "muerto".
    def estarVivo(self):
        if self.__vida > 0:
            self.__personajeVivo = True
        elif self.__vida <= 0:
            self.personajeVivo = False
        return self.personajeVivo
    
    #Metodo para atacar. Se lanza un dado virtual de 6 caras x numero de veces. Si el numero es mayor a 3 se asigna 1 punto de ataque esa ronda. Acumulable.
    def atacar(self):
        numataques = 0
        for x in range(self.__ataque):
            Lanzamiento = Dado.tira()
            if Lanzamiento > 3:
                numataques += 1
            x += 1
        return numataques
                
    
    #___GETTERS___#
    
    @property
    def nombre(self):
        return self.__nombre
    @property
    def vida(self):
        return self.__vida   
    @property
    def ataque(self):
        return self.__ataque    
    @property
    def defensa(self):
        return self.__defensa
    
    #___SETTERS___#
    
    @nombre.setter
    def nombre(self, nuevo):
        self.__nombre = nuevo       
    @vida.setter
    def vida(self, nuevo):
        self.__vida = nuevo        
    @ataque.setter
    def ataque(self, nuevo):
        self.__ataque = nuevo       
    @defensa.setter
    def defensa(self, nuevo):
        self.__defensa = nuevo
    
#Creamos la clase heredada de Personajes llamada momia        
class Momia(Personaje):
    
    #Constructor
    def __init__(self, nombre_momia, vida_momia, ataque_momia, defensa_momia):
        super().__init__(nombre_momia, vida_momia, ataque_momia, defensa_momia)
               
    #___GETTERS___#
    
    @property
    def nombre_momia(self):
        return nombre_momia   
    @property
    def vida_momia(self):
        return vida_momia   
    @property
    def ataque_momia(self):
        return ataque_momia   
    @property
    def defensa_momia(self):
        return defensa_momia
    
    #___SETTERS___#
    
    @nombre_momia.setter
    def nombre_momia(self, nuevo):
        nombre_momia = nuevo       
    @vida_momia.setter
    def vida_momia(self, nuevo):
        vida_momia = nuevo      
    @ataque_momia.setter
    def ataque_momia(self, nuevo):
        ataque_momia = nuevo    
    @defensa_momia.setter
    def defensa_momia(self, nuevo):
        defensa_momia = nuevo
 
    #Metodo para defender. Se tira un dado de 6 caras vitrual x numero de veces. Si sale 6 gana un punto de defensa esa ronda. (Acumulable)
    def defender(self, Numataques):
        Numdefensas = 0
        for x in range(self.defensa):
            Lanzamiento = Dado.tira()
            if Lanzamiento == 6:
                Numdefensas += 1
        x += 1
        
        #Comparamos si las defensas superan, igualan o son menores que los ataques a defender
        if Numataques <= Numdefensas:
            print("BLOQUEADO: La momia {} ha defendido los ataques y se queda con {} pt de vida".format(self.nombre, self.vida))
            #Si logra defender, no pierde vida
        elif Numataques > Numdefensas:
            Numimpactos = Numataques - Numdefensas
            nueva_vida_momia = self.vida - Numimpactos
            self.vida = nueva_vida_momia
            print("IMPACTADO: La momia {} NO ha defendido {} ataques y se queda con {} pt de vida".format(self.nombre, Numimpactos, self.vida))
            #Si no logra defender, pierde los puntos de vida equivalentes a los ataques sin defender
      
#Creamos la clase heredada de Personajes llamada barbaro        
class Barbaro(Personaje):
    
    #Constructor
    def __init__(self, nombre_barbaro, vida_barbaro, ataque_barbaro, defensa_barbaro):
        super().__init__(nombre_barbaro, vida_barbaro, ataque_barbaro, defensa_barbaro)
        
    #___GETTERS___#
    
    @property
    def nombre_barbaro(self):
        return nombre_barbaro   
    @property
    def vida_barbaro(self):
        return vida_barbaro    
    @property
    def ataque_barbaro(self):
        return ataque_barbaro    
    @property
    def defensa_barbaro(self):
        return self.defensa_barbaro
    
    #___SETTERS___#
    
    @nombre_barbaro.setter
    def nombre_barbaro(self, nuevo):
        nombre_barbaro = nuevo        
    @vida_barbaro.setter
    def vida_barbaro(self, nuevo):
        vida_barbaro = nuevo       
    @ataque_barbaro.setter
    def ataque_barbaro(self, nuevo):
        ataque_barbaro = nuevo      
    @defensa_barbaro.setter
    def defensa_barbaro(self, nuevo):
        defensa_barbaro = nuevo
        
    #Metodo para defender. Se tira un dado de 6 caras vitrual x numero de veces. Si sale 6 gana un punto de defensa esa ronda. (Acumulable)
    def defender(self, Numataques):
        Numdefensas = 0
        for x in range(self.defensa):
            Lanzamiento = Dado.tira()
            if Lanzamiento == 6:
                Numdefensas += 1
        x += 1
        
        #Comparamos si las defensas superan, igualan o son menores que los ataques a defender
        if Numataques <= Numdefensas:
            print("BLOQUEADO: El barbaro {} ha defendido los ataques y se queda con {} pt de vida".format(self.nombre, self.vida))
            #Si logra defender, no pierde vida   
        elif Numataques > Numdefensas:
            Numimpactos = Numataques - Numdefensas
            nueva_vida_barbaro = self.vida - Numimpactos
            self.vida = nueva_vida_barbaro
            print("IMPACTADO: El barbaro {} NO ha defendido {} ataques y se queda con {} pt de vida".format(self.nombre, Numimpactos, self.vida))
            #Si no logra defender, pierde los puntos de vida equivalentes a los ataques sin defender  
        
#Creamos una clase llamada dado que servira para el sistema de turnos y para la creacion aleatoria de parametros de los personajes      
class Dado():
    #Metodo para los turnos
    def tira():
        caras = 6
        import random
        dado = (random.randint(1, caras))
        return dado
    #Metodo para generar puntos de vida aleatorios
    def tirav():
        caras = 15
        import random
        dado = (random.randint(3, caras))
        return dado
    #Metodo para generar puntos de ataque aleatorios
    def tiraa():
        caras = 10
        import random
        dado = (random.randint(1, caras))
        return dado
    #Metodo para generar puntos de defensa aleatorios
    def tirad():
        caras = 10
        import random
        dado = (random.randint(1, caras))
        return dado
    
#Creamos Funciones para almacenar los Logs de la partida y los personajes.
def LogPersonajes(Personaje1, Atributos1, Personaje2, Atributos2):
    # Colocamos un timestamp
    from datetime import datetime
    import pytz
    import locale
    locale.setlocale(locale.LC_ALL, 'C')
    dt = datetime.now()
    LogPeDate =  (dt.strftime("[-- Characters Log Created At: %d/%m/%Y - %H:%M:%S --]"))
    LogPe = ("\n{}\n{} con los atributos: {}\n{} con los atributos {}\n--------------------------------------------------------".format(LogPeDate, Personaje1, Atributos1, Personaje2, Atributos2))
    #Cargamos el .excel que registra los datos, los cargamos y lo cerramos
    ArchivoLogPE = open('Log/LogPersonajes.txt', 'a')
    ArchivoLogPE.write(LogPe)
    ArchivoLogPE.close()
    
def LogPartida(Personaje1,Personaje1Name, Personaje2, Personaje2Name,opcion, TurnosElejidos, TurnosJugados, Resultado):
    #Comprobamos el metodo de asignacion de valores.
    Metodo = ""
    if opcion == "1":
        Metodo = "Automático"
    elif opcion == "2":
        Metodo = "Manual"
        
    # Colocamos un timestamp
    from datetime import datetime
    import pytz
    import locale
    locale.setlocale(locale.LC_ALL, 'C')
    dt = datetime.now()
    LogPaDate = (dt.strftime("[-- Game Log Created At: %d/%m/%Y - %H:%M:%S --]"))    
    LogPa = ("\n{}\nPersonaje 1 | {}:{}\nPersonaje 2 | {}:{}\nMétodo de elección = {}\nTurnos [Elejidos/Jugados] = {}/{}\nResultado:{}\n--------------------------------------------------".format(LogPaDate, Personaje1Name, Personaje1, Personaje2Name, Personaje2, Metodo, TurnosElejidos, TurnosJugados, Resultado))
    #Cargamos el .excel que registra los datos, los cargamos y lo cerramos
    ArchivoLogPA = open('Log/LogPartidas.txt', 'a')
    ArchivoLogPA.write(LogPa)
    ArchivoLogPA.close()
    
#Titulo
print("--------------------")
print("----[HERO QUEST]----")
print("--------------------\t\t\t\tV2.5.1\n")

#Sistema para iniciar
print("Presiona 'ENTER' para empezar!")
input()

#Borrar lo anterior
from IPython.display import clear_output
clear_output()

#Se crea un menu para elegir si jugar o borrar logs
menu = True
while menu == True:
    print("<---<-MAIN MENU->--->\n\nJugar HQ: 1\t|\tBorrar Logs:2\n")
    opcion = input()
    #Tras seleccionar se limpia la pantalla
    clear_output()

#Si se elige borrar logs se aplica un texto de confirmación.
    if opcion == "2":
        print("¿Estas seguro de querer borrar los logs?\nSi, Estoy seguro: 1\t|\tNo, No quiero borrarlos: 2")
        borrar = input()
        if borrar == "1":
            #Si elige borarlos se reescriben los logs con un mensaje que indica la fecha de la limpieza y se limpia la consola.
            clear_output()
            from datetime import datetime
            import pytz
            import locale
            locale.setlocale(locale.LC_ALL, 'C')
            dt = datetime.now()
            LogRefreshDate =  (dt.strftime("[-- Refresh Created At: %d/%m/%Y - %H:%M:%S --]"))
            ArchivoLogPE = open('Log/LogPersonajes.txt', 'w').close
            ArchivoLogPE = open('Log/LogPersonajes.txt', 'w')
            ArchivoLogPE.write("{}\nBienvenido al archivo de Log Personajes\n---------------------------------------".format(LogRefreshDate))
            ArchivoLogPE.close()
            ArchivoLogPA = open('Log/LogPartidas.txt', 'w').close
            ArchivoLogPA = open('Log/LogPartidas.txt', 'w')
            ArchivoLogPA.write("{}\nBienvenido al archivo de Log Partidas\n-------------------------------------".format(LogRefreshDate))
            ArchivoLogPA.close()
            print("¡Logs Reiniciados!")
        elif borrar == "2":
            clear_output()
            menu = True
    elif opcion == "1":
        menu = False

#Mediante un if se selecciona la opcion de parametroa aleatorios o manuales
print("Quieres colocar parametros de personaje aleatorios o manuales?\n\nAleatorio: 1\t|\tManuales:2\n")
opcion = input()

#Tras seleccionar se limpia la pantalla
clear_output()

#Si es aletorio se hace uso del objeto Dado() con sus respectivos metodos
if opcion == "1":
    print("\tVamos a definir el nombre de la MOMIA") 
    print("Nombre Momia")
    NomM = input()
    VidM = Dado.tirav()
    AtaM = Dado.tiraa()
    DefM = Dado.tirad()
    Momia1 = Momia(NomM, VidM, AtaM, DefM)
    
    print("\n\tVamos a definir el nombre del BARBARO")  
    print("Nombre Barbaro")
    NomB = input()
    VidB = Dado.tirav()
    AtaB = Dado.tiraa()
    DefB = Dado.tirad()
    Barbaro1 = Barbaro(NomB, VidB, AtaB, DefB)
#Si es manual, el usuario por medio de imputs() selecciona los datos
elif opcion == "2":    
    print("\tVamos a definir los valores de la MOMIA") 
    print("Nombre Momia")
    NomM = input()
    print("Vida Momia")
    VidM = int(input())
    print("Ataque Momia")
    AtaM = int(input())
    print("Defensa Momia")
    DefM = int(input())
    Momia1 = Momia(NomM, VidM, AtaM, DefM)

    print("\n\tVamos a definir los valores del BARBARO")  
    print("Nombre Barbaro")
    NomB = input()
    print("Vida Barbaro")
    VidB = int(input())
    print("Ataque Barbaro")
    AtaB = int(input())
    print("Defensa Barbaro")
    DefB = int(input())
    Barbaro1 = Barbaro(NomB, VidB, AtaB, DefB)
else:
    print("¡ERROR!\nSelecciona una opcion valida")
    
#Se borran los textos
clear_output()

#Se muestran los parametros de cada personaje y las opciones de la partida y se guardan en los logs
if opcion == "1":
    print("Módo de elección de parámetros: Automático")
elif opcion == "2":
    print("Módo de elección de parámetros: Manual")
print("\n", Momia1)
print("\n", Barbaro1)
LogPersonajes(Momia1.nombre, Momia1.logInfo(), Barbaro1.nombre, Barbaro1.logInfo())

#Se indican los turnos
print("\n¿Cuántos turnos máximos quiere jugar?: ")
Turnos = int(input())
#Se asigna los valores para el sistema de turnos. J1 es la momia y J2 es el barbaro.
j1 = "B"
j2 = "M"
turno = 0
for x in range(Turnos):
    turno += 1
    #Mediante un bucle y varios If deternminamos los turnos
    import time #implentamos un import.time para poder hacer que los bucles tengan pausa
    time.sleep(1)
    if j1 == "B":
        j1 = "M"
    elif j1 == "M":
        j1 = "B"
    if j2 == "B":
        j2 = "M"
    elif j2 == "M":
        j2 = "B"
    print("\n<<< TURNO {} | {} vs {} >>>".format(x + 1, j1, j2))
    #Dependiendo de quien es el Jugador 1 (atacante) se ejecutara el .atacar de un jugador u otro
    if j1 == "B":
        Numataques = Barbaro1.atacar()
        Momia1.defender(Numataques)
    elif j1 == "M":
        Numataques = Momia1.atacar()
        Barbaro1.defender(Numataques)
    #tras los ataques se revisa si los jugadores estan vivos
    Barbaro1.estarVivo()
    Momia1.estarVivo()
    #Dependiendo de lo que devuelva .personajeVivo() se sigue o no con el combate
    if Barbaro1.personajeVivo == False:
        print("\n\tEl ganador del combate es la Momia {} con {} pt de vida".format(Momia1.nombre, Momia1.vida))
        break
    if Momia1.personajeVivo == False:
        print("\n\tEl ganador del combate es el Barbaro {} con {} pt de vida".format(Barbaro1.nombre, Barbaro1.vida))
        break
if Barbaro1.personajeVivo == True and Momia1.personajeVivo == True:
    print("\n\tEl combate queda en un empate! Ambos jugadores sobreviven!")

#Se muestra por pantalla los resultados y se guardan los logs de la partida.        
ResultadoMomia = ("\n\tMOMIA:   {} queda con {} pt de vida.".format(Momia1.nombre, Momia1.vida))    
ResultadoBarbaro = ("\n\tBARBARO: {} queda con {} pt de vida.".format(Barbaro1.nombre, Barbaro1.vida))
ResultadoPartida = (ResultadoMomia + ResultadoBarbaro)
print(ResultadoPartida)
LogPartida(Momia1.logInfo(),Momia1.nombre, Barbaro1.logInfo(),Barbaro1.nombre, opcion, turno, Turnos, ResultadoPartida)


#Comming soon English version!