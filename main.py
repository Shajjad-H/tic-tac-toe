import numpy as np


from tensorflow.keras.models import Sequential

class PlayerAgent:

    def __init__(self, game) -> None:
        self.game = game
        self.network = None

    def action(self):
        pass


class Game:

    def __init__(self):
        self.grid = np.zeros(shape=(3, 3), dtype='int8')
        self.current_player = 1

    def action(self, x:int, y:int) -> int:
        assert(x < self.grid.shape[0] and y < self.grid.shape[1] and x >= 0 and y >= 0)

        if self.grid[x, y] > 0:
            return -2

        self.grid[x, y] = self.current_player

        if self.check_winner():
            return self.current_player

        if np.count_nonzero(self.grid) >= 9: # draw match
            return 0

        self.current_player = (self.current_player % 2) + 1

        return -1
        

    def check_winner(self) -> bool:

        if np.count_nonzero(self.grid) < 5:
            return False
        
        rows = self.grid[self.grid.all(axis=1)]
        
        cols = self.grid.T[self.grid.all(axis=0)]
        diagonal_left = np.reshape(np.diag(self.grid), (1, -1))
        diagonal_right = np.reshape(np.diag(np.fliplr(self.grid)), (1, -1))

        rows_cols_diags = np.concatenate([rows, cols, diagonal_left, diagonal_right])

        return np.any(np.all(rows_cols_diags == self.current_player, axis=1))
        
    
    def run(self):
        while True:
            print(self.grid)
            print(f'paying: {self.current_player}')
            x = int(input('x: '))
            y = int(input('y: '))
            result = self.action(x, y)

            if result == 1 or result == 2:
                print(f'player {result} won')
                break

            if result == 0:
                print(f'draw match')
                break


        
    
        



if __name__ == "__main__":
    game = Game()
    game.run()