import pygame
import pygame_gui
import sys
from atomState import atomState 

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
                    stuff = initState(filename)
                    solution = stuff[0]
                    boardgame = stuff[1]
                    atoms = stuff[2]
                    visited = stuff[3]
                    printBoard(boardgame,atoms)
                    play_player(boardgame, atoms,solution)
                    print("you won")

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
        a = atomState()

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

        a = atomState()
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

    visited = atoms
    
    return [solution, boardgame, atoms, visited]

def printBoard(boardgame, atoms):
    for i in boardgame:
        line = ""
        for j in i:
            line += j
        print(line)

    print(" ")

    n = 1
    for i in atoms:
        print("Átomo {}".format(n))
        print("O átomo {} na posição ({},{}) tem: \n - {} ligação/ões para cima \n - {} ligação/ões para baixo \n - {} ligação/ões para a esquerda \n - {} ligação/ões para a direita".format(i.s,i.x,i.y,i.c_u,i.c_d,i.c_l,i.c_r))
        print(" ")
        n += 1

def move_up(atom,boardgame):
    x1 = atom.x
    y1 = atom.y

    boardgame[y1][x1] = " "

    for i in range(y1-1,0,-1):
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

    for i in range(x1-1,0,-1):
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

def verify_solution(solution,atoms):
    d_x = atoms[0].x - solution[0].x
    d_y = atoms[0].y - solution[0].y

    for i in range(1, len(solution)):
        if (solution[i].x + d_x != atoms[i].x):
            return 1
        else:
            if (solution[i].y + d_y != atoms[i].y):
                return 1
            
    return 0

def play_player(boardgame, atoms,solution) :
    a = int(input("Da lista de átomos acima, escolhe qual queres mover: "))
    if (a < 0 | a > atoms.len()):
            print("Esse valor não é válido")
            play_player(boardgame,atoms,solution)

    direction = input("Agora escolhe a direção em que queres mover o átomo (a,w,s,d): ")
    if (direction == "a"):
        x = atoms[a-1].x
        y = atoms[a-1].y

        if (boardgame[y][x-1] != " "):
            print("Não podes mover esse átomo nessa direção")
            play_player(boardgame,atoms,solution)
        else:
            move = move_left(atoms[a-1],boardgame)
            atoms[a-1] = move[1]
            printBoard(move[0],atoms)

            if (verify_solution(solution,atoms) == 0): return 0
            else: play_player(move[0],atoms,solution)
    elif (direction == "w") :
        x = atoms[a-1].x
        y = atoms[a-1].y

        if (boardgame[y-1][x] != " "):
            print("Não podes mover esse átomo nessa direção")
            play_player(boardgame,atoms)
        else:
            move = move_up(atoms[a-1],boardgame)
            atoms[a-1] = move[1]
            printBoard(move[0],atoms)

            if (verify_solution(solution,atoms) == 0): return 0
            else: play_player(move[0],atoms,solution)
    elif (direction == "s") :
        x = atoms[a-1].x
        y = atoms[a-1].y

        if (boardgame[y+1][x] != " "):
            print("Não podes mover esse átomo nessa direção")
            play_player(boardgame,atoms,solution)
        else:
            move = move_down(atoms[a-1],boardgame)
            atoms[a-1] = move[1]
            printBoard(move[0],atoms)

            if (verify_solution(solution,atoms) == 0): return 0
            else: play_player(move[0],atoms,solution)
    elif (direction == "d") :
        x = atoms[a-1].x
        y = atoms[a-1].y

        if (boardgame[y][x+1] != " "):
            print("Não podes mover esse átomo nessa direção")
            play_player(boardgame,atoms,solution)
        else:
            move = move_right(atoms[a-1],boardgame)
            atoms[a-1] = move[1]
            printBoard(move[0],atoms)

            if (verify_solution(solution,atoms) == 0): return 0
            else: play_player(move[0],atoms,solution)
    else:
        print("Essa direção não é válida")
        play_player(boardgame,atoms,solution)

main()

