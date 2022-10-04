class Guild:
    def __init__(self, name):
        self.guild_name = name
        self.players = []

    def assign_player(self, player_name):
        if player_name.guild != "Unaffiliated":
            return f"Player {player_name.name} is in another guild."
        elif player_name not in self.players:
            self.players.append(player_name)
            player_name.guild = self.guild_name
            return f'Welcome player {player_name.name} to the guild {self.guild_name}'

        return f'Player {player_name.name} is already in the guild.'

    def kick_player(self, player_name: str):
        for x in self.players:
            if x.name == player_name:
                x.guild = "Unaffiliated"
                self.players.remove(x)
                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        return f'Guild: {self.guild_name}\n' + '\n'.join([x.player_info() for x in self.players])
