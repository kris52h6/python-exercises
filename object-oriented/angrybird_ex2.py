class Bird:

    def __init__(self):
        self.pos = (2, 5)
        self.directions = ['w', 'n', 'e', 's']
        self.cur_dir = 'e'

    def move(self):
        if self.cur_dir == 'e':
            self.pos = (self.pos[0], self.pos[1] + 1)
        elif self.cur_dir == 's':
            self.pos = (self.pos[0] + 1, self.pos[1])
        elif self.cur_dir == 'w':
            self.pos = (self.pos[0], self.pos[1] - 1)
        elif self.cur_dir == 'n':
            self.pos = (self.pos[0] - 1, self.pos[1])


class Pig:

    def __init__(self):
        self.pos = (2, 8)


class Board:

    cols = 10
    rows = 10

    def __init__(self):
        self.board = [(i + 1, j + 1) for i in range(self.cols)
                      for j in range(self.rows)]
        self.bird = Bird()
        self.pig = Pig()

    def display(self):
        for i in range(self.cols):
            for j in range(self.rows):
                if self.bird.pos == (i + 1, j + 1):
                    print('B ', end='')
                elif self.pig.pos == (i + 1, j + 1):
                    print('P ', end='')
                else:
                    print('* ', end='')
            print('*')


class Workspace:

    def commands(self):
        print('\nEnter "m" to move bird ', end='\n\n\n')


class Game:
    running = True
    workspace = Workspace()
    board = Board()
    board.display()

    workspace.commands()

    while running == True:
        user_input = input()

        if user_input == 'm':
            board.bird.move()
            board.display()
            if board.bird.pos == board.pig.pos:
                print('Bird wins')
                print(
                    f'Bird position: {board.bird.pos}, Pig position: {board.pig.pos}')
                running = False
        elif user_input == 'r':
            index = board.bird.directions.index(board.bird.cur_dir)
            print(f'index: {index}')
            if index == 3:
                board.bird.cur_dir = board.bird.directions[0]
                index = 0
            else:
                board.bird.cur_dir = board.bird.directions[index + 1]
        elif user_input == 'q':
            print('...Quitting program')
            running = False
