from level_select import show_levels_select

def intro():
    """Function asks for user name to play game."""
    
    print("Введіть ім'я:")
    name = input()
    print(f"Привіт: {name}")
    
def show_game_info(title, version):
    """Shows game info to the user"""
    print(f"{title} v{version}")

game_title = "My game"
game_version = 1.0

# Show game info
show_game_info(game_title, game_version)

# Show user intro
intro()

# Ask user to select game level
level = show_levels_select()
print(f'Ви вибрали рівень: {level}')