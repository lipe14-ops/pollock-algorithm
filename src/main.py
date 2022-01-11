import pygame
import random

SCREEN = pygame.display.set_mode()
WIDTH, HEIGHT = pygame.display.get_surface().get_size()
COLORS = {
    'white': (255, 255, 255),
    'green': (0, 255, 0),
    'red': (255, 0, 0),
    'blue': (0, 0, 255),
    'pink': (255, 0, 127),
    'yellow': (255, 255, 0),
    'cyan': (0, 255, 255),
    'black': (30, 30, 30),
    'orange': (255, 64, 0),
    'purple': (148, 0, 211),
    'gray': (150, 150, 150)
}


class Walker(object):
    """ creates the walker instance. """
    
    def __init__(self, x: int, y: int, size: int, color: int = None) -> None:
        """ Params:
                x (int): walker x position.
                y (int): walker y position.
                size (int): walker size walker body size.
                color (tuple): the player color.
        """
        
        self.x = x
        self.y = y
        self.size = size
        self.color = color
    
    def update(self) -> None:
        """ update the walker position. """
        
        self.x += random.randint(-1, 1) * self.size
        self.y += random.randint(-1, 1) * self.size
    
    def draw(self) -> None:
        """ render the walker. """
        
        color = self.color
        
        if not color:    
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 
        
        pygame.draw.rect(SCREEN, color, [self.x, self.y, self.size, self.size])


class GameManager(object):
    """ handle the game state. """
    
    def __init__(self) -> None:
        self.players: list[Walker] = []
    
    def add_player(self, player: Walker) -> None:
        """ adds a player from the game state.
        
        Params:
            player (Walker): the player that will be add.
        """
        
        self.players.append(player)
    
    def remove_player(self, player: Walker) -> None:
        """ removes a player from the game state.
        
        Params:
            player (Walker): the player that will be removed.
        """

        self.players.remove(player)
    
    def update_all_players(self) -> None:
        """ updates all player position in the game state. """
        
        for player in self.players:
            player.update()
    
    def draw_all_players(self) -> None:
        """ renders all players in the game state. """
        
        for player in self.players:
            player.draw()


def add_players(game_manager: GameManager, players_quantity: int) -> None:
    """ add a number n of players in the game state.
    
    Params:
        game_manager (GameManager): the game state manager.
        players_quantity (int): the number of players that will be add.
    """
    
    colors_values = list(COLORS.values())
    random_colors = random.sample(colors_values, players_quantity)
    
    x, y = WIDTH / 2, HEIGHT / 2
    size = 2
    
    for index, color in enumerate(random_colors, start=1):
        player = Walker(x, y, size, color)
        game_manager.add_player(player)
        
        if index == players_quantity:
            break


def main() -> None:
    is_running = True
    is_paused = True
    
    game = GameManager()
    
    add_players(game, 11)
    
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_paused = not is_paused
        
        if is_paused:
            continue
        
        game.update_all_players()
        game.draw_all_players()
        
        pygame.display.update()
    
    pygame.quit()    


if __name__ == '__main__':
    main()