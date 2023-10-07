from SRC.Dice import Dado

#Creamnos la clase Personaje
class Personaje:

    #Definimos atributos
    __nombre = ""           #nombre del personaje
    __vida = 0              #numero de puntos de vida, baja -1 por ataque efectuado exitosamente
    __ataque = 0            #numero de lanzamientos de dado para atacar
    __defensa = 0           #numero de tiradas de dado para defender
    personajeVivo = True    #indica si el personaje sigue vivo
    
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
    
    #Definimos Getters
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
    
    #Definimos Setters
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
               
    #Definimos Getters
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
    
    #Definimos Setters
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
        
    #Definimos Getters
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
    
    #Definimos Setters
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