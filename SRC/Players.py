from SRC.Dice import Dice

#Creamnos la clase Personaje
class Character:

    #Definimos atributos
    __name = ""           #nombre del personaje
    __health = 0              #numero de puntos de vida, baja -1 por ataque efectuado exitosamente
    __attack = 0            #numero de lanzamientos de dado para atacar
    __defense = 0           #numero de tiradas de dado para defender
    itsAlive = True    #indica si el personaje sigue vivo
    
    #Constructor
    def __init__(self, name, health, attack, defense):
        self.__name = name
        self.__health = health
        self.__attack = attack
        self.__defense = defense
        print(f"Player {self.__name} created!")
    
    #String. Define los atributos del personaje
    def __str__(self):
        return f"Player {self.name}:\n Health  > {self.__health} pt\n Attack  > {self.__attack} pt\n Defense > {self.__defense} pt"
    
    #Metodo guardado Log personaje
    def logInfo(self):
        return f"\n- Health    > {self.__health} pt\n- Atack  > {self.__attack} pt\n- Defense > {self.__defense} pt"
    
    #Metodo guardado log sys
    def logSys(self):
        return f"{self.__health}, {self.__attack}, {self.__defense}"
    
    #Metodo para verificar el estado del personaje. En caso de tener vida positiva el estado sera "vivo", en caso de vida negativa o cero el estado será "muerto".
    def ItsAlive(self):
        if self.__health > 0:
            self.itsAlive = True
        elif self.__health <= 0:
            self.itsAlive = False
        return self.itsAlive
     
    #Metodo para atacar. Se lanza un dado virtual de 6 caras x numero de veces. Si el numero es mayor a 3 se asigna 1 punto de ataque esa ronda. Acumulable.
    def Attack(self):
        AttackNumber = 0
        for x in range(self.__attack):
            Throw = Dice.GlobalDice()
            if Throw > 3:
                AttackNumber += 1
            x += 1
        return AttackNumber
    
    #Definimos Getters
    @property
    def name(self):
        return self.__name
    @property
    def health(self):
        return self.__health   
    @property
    def attack(self):
        return self.__attack    
    @property
    def defense(self):
        return self.__defense
    
    #Definimos Setters
    @name.setter
    def name(self, new):
        self.__name = new       
    @health.setter
    def health(self, new):
        self.__health = new        
    @attack.setter
    def attack(self, new):
        self.__attack = new       
    @defense.setter
    def defense(self, new):
        self.__defense = new
    
#Creamos la clase heredada de Personajes llamada momia        
class Player(Character):
    
    #Constructor
    def __init__(self, PlayerID, name_player, health_player, attack_player, defense_player):
        super().__init__(name_player, health_player, attack_player, defense_player)
        self.__PlayerID = PlayerID
               
    #Definimos Getters
    @property
    def name_player(self):
        return self.name_player   
    @property
    def health_player(self):
        return self.health_player   
    @property
    def attack_player(self):
        return self.attack_player   
    @property
    def defense_player(self):
        return self.defense_player
    @property
    def PlayerID(self):
        return self.__PlayerID
    
    #Definimos Setters
    @name_player.setter
    def name_player(self, new):
        name_player = new       
    @health_player.setter
    def health_player(self, new):
        health_player = new      
    @attack_player.setter
    def attack_player(self, new):
        attack_player = new    
    @defense_player.setter
    def defense_player(self, new):
        defense_player = new
    @PlayerID.setter
    def PlayerID(self, new):
        self.__PlayerID = new
 
    #Metodo para defender. Se tira un dado de 6 caras vitrual x numero de veces. Si sale 6 gana un punto de defensa esa ronda. (Acumulable)
    def Defense(self, AttackNumber):
        DefenseNumber = 0
        for x in range(self.defense):
            Throw = Dice.GlobalDice()
            if Throw == 6:
                DefenseNumber += 1
        x += 1
        
        #Comparamos si las defensas superan, igualan o son menores que los ataques a defender
        if AttackNumber <= DefenseNumber:
            print(f"[BLOCKED] Player {self.PlayerID} {self.name} blocked the attacks and is left with {self.health} health pt")
            #Si logra defender, no pierde vida
        elif AttackNumber > DefenseNumber:
            StrikeNumber = AttackNumber - DefenseNumber
            NewPlayerHealth = self.health - StrikeNumber
            self.health = NewPlayerHealth
            print(f"[HIT]\t  Player {self.PlayerID} {self.name} didn't block {StrikeNumber} attacks and is left with {self.health} health pt")
            #Si no logra defender, pierde los puntos de vida equivalentes a los ataques sin defender