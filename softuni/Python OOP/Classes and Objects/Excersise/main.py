from guild.player import Player
from guild.guild import Guild

player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(player.player_info())
print(guild.kick_player('George'))
print(player.player_info())
print(guild.guild_info())