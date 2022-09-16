from game_state import GameState

class GameManager():
    """
        Responsible for handling game state, process and players
    """
    def __init__(self, game_title, game_version):
        self.game_title = game_title
        self.game_version = game_version
        self.game_state = GameState.NONE
    
    def start(self):
        """Starts game. Shows game info to the user"""
        print(f"{self.game_title} v{self.game_version}")
        print("Game started.")
        self.game_state = GameState.START