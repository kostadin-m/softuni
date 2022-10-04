class Player:
    def __init__(self,name,hp,mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill, cost):
        if skill not in self.skills:
            self.skills[skill] = cost
            return f"Skill {skill} added to the collection of the player {self.name}"
        return f"Skill already added"

    def player_info(self):
        return f'Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n' + \
               '\n'.join([f"==={skill} - {mana}" for skill, mana in self.skills.items()]) + '\n'




