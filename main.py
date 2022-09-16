from level_select import show_levels_select
from game_manager import GameManager
from game_state import GameState

def intro():
    """Function asks for user name to play game."""
    
    print("Введіть ім'я:")
    name = input()
    print(f"Привіт: {name}")
    
def show_game_info(title, version):
    """Shows game info to the user"""
    print(f"{title} v{version}")

# Show game info
game_manager = GameManager("My game", 1)
game_manager.start()

if game_manager.game_state == GameState.START:
    print(game_manager.game_state)
    
    # Show user intro
    intro()

    # Ask user to select game level
    level = show_levels_select()
    print(f'Ви вибрали рівень: {level}')
else:
    print("Game already started.")