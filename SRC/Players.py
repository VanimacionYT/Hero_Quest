from SRC.Dice import Dice

class Character:
    __name = ""
    __health = 0
    __attack = 0
    __defense = 0
    itsAlive = True
    
    def __init__(self, name, health, attack, defense):
        self.__name = name
        self.__health = health
        self.__attack = attack
        self.__defense = defense
        print(f"Player {self.__name} created!")
    
    def __str__(self):
        return f"Player {self.name}:\n Health  > {self.__health} pt\n Attack  > {self.__attack} pt\n Defense > {self.__defense} pt"
    
    def logInfo(self):
        return f"\n- Health    > {self.__health} pt\n- Attack  > \t{self.__attack} pt\n- Defense > \t{self.__defense} pt"
    
    def logSys(self):
        return f"{self.__health}, {self.__attack}, {self.__defense}"

    def ItsAlive(self):
        if self.__health > 0:
            self.itsAlive = True
        elif self.__health <= 0:
            self.itsAlive = False
        return self.itsAlive

    def Attack(self):
        AttackNumber = 0
        for x in range(self.__attack):
            Throw = Dice.GlobalDice(Dice)
            if Throw > 3:
                AttackNumber += 1
            x += 1
        return AttackNumber
    
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
       
class Player(Character):

    def __init__(self, PlayerID, name_player, health_player, attack_player, defense_player):
        super().__init__(name_player, health_player, attack_player, defense_player)
        self.__PlayerID = PlayerID

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

    def Defense(self, AttackNumber):
        DefenseNumber = 0
        for x in range(self.defense):
            Throw = Dice.GlobalDice(Dice)
            if Throw == 6:
                DefenseNumber += 1
        x += 1
        if AttackNumber <= DefenseNumber:
            print(f"[BLOCKED] Player {self.PlayerID} {self.name} blocked the attacks and is left with {self.health} health pt")
        elif AttackNumber > DefenseNumber:
            StrikeNumber = AttackNumber - DefenseNumber
            NewPlayerHealth = self.health - StrikeNumber
            self.health = NewPlayerHealth
            print(f"[HIT]\t  Player {self.PlayerID} {self.name} didn't block {StrikeNumber} attacks and is left with {self.health} health pt")