import pygame
import pygame_gui
import sys

def main():
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
                    filepath = "level1.txt"
                    filename = filepath.split("/")[-1]
                    initState(filename)

                    

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == settings_button:
                    print('Hello')

        manager.update(time_delta)

        screen.blit(background, (0,0))
        manager.draw_ui(screen)


        pygame.display.update()

def initState(filename):
    boardgame = []
    solution = []
    atoms = []
    f = open(filename,'r')
    line = f.readline().strip()

    while line != "":
        tmp = line.split()
        a = atomState(0,0," ",0,0,0,0)

        a.set_s(tmp[1])
        a.set_x(int(tmp[2]))
        a.set_y(int(tmp[3]))
        
        for i in range(0,len(tmp[4])):
            if tmp[4][i] == "U" : a.set_c_u(a.c_u + 1)
            elif tmp[4][i] == "D" : a.set_c_d(a.c_d + 1)
            elif tmp[4][i] == "L" : a.set_c_l(a.c_l + 1)
            elif tmp[4][i] == "R" : a.set_c_r(a.c_r + 1)

        solution.append(a)
        line = f.readline().strip()

    line = f.readline().strip()

    while line != "":
        tmp = line.split()

        a = atomState(0,0," ",0,0,0,0)
        a.set_s(tmp[1])
        a.set_x(int(tmp[2]))
        a.set_y(int(tmp[3]))
        
        for i in range(0,len(tmp[4])):
            if tmp[4][i] == "U" : a.set_c_u(a.c_u + 1)
            elif tmp[4][i] == "D" : a.set_c_d(a.c_d + 1)
            elif tmp[4][i] == "L" : a.set_c_l(a.c_l + 1)
            elif tmp[4][i] == "R" : a.set_c_r(a.c_r + 1)

        atoms.append(a)
        line = f.readline().strip()

    line = f.readline().strip()

    while line != "":
        tmp = []
        for i in line:
            tmp.append(i)
        boardgame.append(tmp)
        line = f.readline().strip()

    for i in range(0,len(atoms)):
        boardgame[atoms[i].y][atoms[i].x] = atoms[i].s

    printBoard(boardgame)
    
    return [solution, boardgame, atoms]

def printBoard(boardgame):
    for i in boardgame:
        line = ""
        for j in i:
            line += j
        print(line)

class atomState:
    x = 0
    y = 0
    s = " "
    c_u = 0
    c_d = 0
    c_l = 0
    c_r = 0

    def __init__(self,x1,y1,s1,c1,c2,c3,c4):
        self.x = x1
        self.y = y1
        self.s = s1
        self.c_u = c1
        self.c_d = c2
        self.c_l = c3
        self.c_r = c4

    def set_x(self,x1):
        self.x = x1

    def set_y(self,y1):
        self.y = y1

    def set_s(self,s1):
        self.s = s1
    
    def set_c_u(self,c1):
        self.c_u = c1
    
    def set_c_d(self,c1):
        self.c_d = c1
    
    def set_c_l(self,c1):
        self.c_l = c1
    
    def set_c_r(self,c1):
        self.c_r = c1

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

    return [boardgame,atom]

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

    return [boardgame,atom]

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

    return [boardgame,atom]

def move_right(atom,boardgame):
    x1 = atom.x
    y1 = atom.y

    boardgame[y1][x1] = " "

    for i in range(x1+1,len(boardgame[y1])):
        if boardgame[y1][i] == " ":
            atom.set_x(i)
        else:
            break

    boardgame[atom.y][atom.x] = atom.s

    return [boardgame,atom]

def equals(atom1,atom2):
    if(atom1.s == atom2.s & atom1.c_u == atom2.c_u & atom1.c_d == atom2.c_d & atom1.c_l == atom2.c_l & atom1.c_r == atom2.c_r): return 0
    return 1

def verify_solution(solution,boardgame):
    d1 = 0
    d2 = 0

    for i in range(0,len(solution)):
        for j in range(0,len(solution[i])):
            if j == " ": continue
            else:
                for k in range(0,len(boardgame)):
                    for l in range(0,len(boardgame[k])):
                        if (l == " " | l == "X"): continue
                        elif equals(l,j) == 1 : return 1
                        else:
                            d1 = l - j
                            d2 = k - i

    for i in range(0,len(solution)):
        for j in range(0, len(solution[i])):
            if (solution[i][j] == " " & (boardgame[i+d2][j+d1] == " " | boardgame[i+d2][j+d1] == "X")):continue
            elif equals(solution[i][j],boardgame[i+d2][j+d1]) == 0 : continue
            else: return 1

    return 0


main()