class Guild:
    def __init__(self, name):
        self.guild_name = name
        self.players = []

    def assign_player(self, player_name):
        if player_name.guild != "Unaffiliated":
            return f"Player {player_name.name} is in another guild."
        elif self.player_in_guild(player_name.name):
            return f'Player {player_name.name} is already in the guild.'

        self.players.append(player_name)
        player_name.guild = self.guild_name
        return f'Welcome player {player_name.name} to the guild {self.guild_name}'

    def kick_player(self, player_name: str):
        player_in_guild = self.player_in_guild(player_name)
        if not player_in_guild:
            return f"Player {player_name} is not in the guild."

        player_in_guild.guild = "Unaffiliated"
        self.players.remove(player_in_guild)
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        return f'Guild: {self.guild_name}\n' + '\n'.join([x.player_info() for x in self.players])

    def player_in_guild(self, name):
        for x in self.players:
            if x.name == name:
                return x
        return False
