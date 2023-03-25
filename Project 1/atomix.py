import pygame
import pygame_gui
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Atomix')

manager = pygame_gui.UIManager((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()
is_running = True

background = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
background.fill(pygame.Color('#000000'))

play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, 200), (100, 50)), text='Play', manager=manager)
settings_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, 275), (100, 50)), text='Settings', manager=manager)

while is_running:
    time_delta = clock.tick(60)/1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        manager.process_events(event)

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == play_button:
                print('Hello')

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == settings_button:
                print('Hello')

    manager.update(time_delta)

    screen.blit(background, (0,0))
    manager.draw_ui(screen)


    pygame.display.update()

def initialState(filename):
    boardgame = []
    solution = []
    f = open(filename,'r')
    line = f.readline().strip()

    while line[0] == '#':
        tmp = []
        for i in range(1,len(line)):
            tmp.append(i)
        solution.append(tmp)
        line = f.readline().strip()
    
    line = f.readline().strip()

    while line != "":
        tmp = []
        for i in line:
            tmp.append(i)
        boardgame.append(tmp)
        line = f.readline().strip()
    
    return [solution, boardgame]

def printBoard(boardgame):
    for i in boardgame:
        line = ""
        for j in i:
            line += j
        print(line)

class atomState:
    x = 0
    y = 0
    s = ''

    def set_x(x1):
        x = x1

    def set_y(y1):
        y = y1

    def set_s(s1):
        s = s1


def move_up(atom,boardgame):
    x1 = atom.x
    y1 = atom.y

    boardgame[y1][x1] = " "

    for i in range(y1-1,0):
        if boardgame[i][x1] == " ":
            atom.set_y(i)
        else:
            break

    boardgame[atom.y][atom.x] = atom.s

    return boardgame

def move_down(atom,boardgame):
    x1 = atom.x
    y1 = atom.y

    boardgame[y1][x1] = " "

    for i in range(y1+1,len(boardgame)):
        if boardgame[i][x1] == " ":
            atom.set_y(i)
        else:
            break

    boardgame[atom.y][atom.x] = atom.s

    return boardgame

def move_left(atom,boardgame):
    x1 = atom.x
    y1 = atom.y

    boardgame[y1][x1] = " "

    for i in range(x1-1,0):
        if boardgame[y1][i] == " ":
            atom.set_x(i)
        else:
            break
    
    boardgame[atom.y][atom.x] = atom.s

    return boardgame

def move_down(atom,boardgame):
    x1 = atom.x
    y1 = atom.y

    boardgame[y1][x1] = " "

    for i in range(x1+1,len(boardgame[y1])):
        if boardgame[y1][i] == " ":
            atom.set_x(i)
        else:
            break
    
    boardgame[atom.y][atom.x] = atom.s

    return boardgame