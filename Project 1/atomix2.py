import pygame
import pygame_gui
import sys
import time
from atomState import atomState
import copy
from datetime import datetime

import HeurClusters
from algorithms import GreedyAlgorithm

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
                pygame.quit()
                sys.exit()
            manager.process_events(event)

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == play_button:
                    filepath = "level3.txt"
                    filename = filepath.split("/")[-1]
                    stuff = initState(filename)
                    solution = stuff[0]
                    boardgame = stuff[1]
                    atoms = stuff[2]
                    visited = stuff[3]
                    
                    path = visited
                    
                    start_time = time.time()
                    path = bfs(atoms,boardgame,solution,visited,path)
                    total_time = time.time() - start_time
                    
                    print_results(path, total_time, boardgame)
                    
                    path = [path[0]]
                    heuristic = HeurClusters.heur_clusters
                    algorithm = GreedyAlgorithm(boardgame, atoms, solution, 
                                                heuristic)

                    start_time = time.time()
                    path += algorithm.solve()
                    total_time = time.time() - start_time
                    
                    print_results(path, total_time, boardgame)
                    
                    
"""=======

                    print(len(solution))
                    print(len(atoms))
                    print(len(boardgame))

                    time1 = datetime.now()
                    path = bfs(atoms,boardgame,solution,visited,path)
                    time2 = datetime.now()

                    total_time = time2 - time1

                    print("Time: ", total_time)
                    print("Number of moves: ", len(path) - 1)
                    print("Visited states: ", len(visited))

                    for i in path:
                        printBoard(boardgame,i)
                        print(" ")

                    for i in path[-1]:
                        print("O átomo {} na posição ({},{}) tem: \n - {} ligação/ões para cima \n - {} ligação/ões para baixo \n - {} ligação/ões para a esquerda \n - {} ligação/ões para a direita".format(i.s,i.x,i.y,i.c_u,i.c_d,i.c_l,i.c_r))
                        print(" ")
>>>>>>> c17a6f3003d6e6233546cff1418cb700a69e97e0

                    print("Time: ", total_time)
                    print("Number of moves: ", eval_function(path))
                    print("Visited states: ", len(visited))"""

                    

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == settings_button:
                    print('Hello')

        manager.update(time_delta)

        screen.blit(background, (0,0))
        manager.draw_ui(screen)

        pygame.display.update()

def eval_function(path):
    return len(path) - 1

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

    visited = [atoms]

    return [solution, boardgame, atoms,visited]

def printBoard(boardgame,atoms): #recebe em boardgame um tabuleiro sem átomos e em atoms o conjunto de átomos que tem de escrever
    boardgame3 = copy.deepcopy(boardgame)

    for i in range(0,len(atoms)):
        boardgame3[atoms[i].y][atoms[i].x] = atoms[i].s

    for i in boardgame3:
        line = ""
        for j in i:
            line += j
        print(line)

    print(" ")

def move_up(i,atoms,boardgame):
    if (boardgame[atoms[i].y-1][atoms[i].x] != " ") : return []
    
    tmp1 = []
    for k in atoms:
        tmp2 = atomState()
        tmp2.set_x(k.x)
        tmp2.set_y(k.y)
        tmp2.set_s(k.s)
        tmp2.set_c_u(k.c_u)
        tmp2.set_c_d(k.c_d)
        tmp2.set_c_l(k.c_l)
        tmp2.set_c_r(k.c_r)
        tmp1.append(tmp2)

    for k in range(0,len(atoms)):
        if(k != i): boardgame[atoms[k].y][atoms[k].x] = atoms[k].s

    x1 = tmp1[i].x
    y1 = tmp1[i].y

    for k in range(y1-1,0,-1):
        if boardgame[k][x1] == " ":
            tmp1[i].set_y(k)
        else:
            break

    for k in range(0,len(atoms)):
        if(k != i): boardgame[atoms[k].y][atoms[k].x] = " "


    return [tmp1]

def move_down(i,atoms,boardgame):
    if (boardgame[atoms[i].y+1][atoms[i].x] != " ") : return []

    tmp1 = []
    for k in atoms:
        tmp2 = atomState()
        tmp2.set_x(k.x)
        tmp2.set_y(k.y)
        tmp2.set_s(k.s)
        tmp2.set_c_u(k.c_u)
        tmp2.set_c_d(k.c_d)
        tmp2.set_c_l(k.c_l)
        tmp2.set_c_r(k.c_r)
        tmp1.append(tmp2)

    for k in range(0,len(atoms)):
        if(k != i): boardgame[atoms[k].y][atoms[k].x] = atoms[k].s

    x1 = tmp1[i].x
    y1 = tmp1[i].y

    for k in range(y1+1,len(boardgame)):
        if boardgame[k][x1] == " ":
            tmp1[i].set_y(k)
        else:
            break

    for k in range(0,len(atoms)):
        if(k != i): boardgame[atoms[k].y][atoms[k].x] = " "

    return [tmp1]

def move_left(i,atoms,boardgame):
    if (boardgame[atoms[i].y][atoms[i].x-1] != " ") : return []

    tmp1 = []
    for k in atoms:
        tmp2 = atomState()
        tmp2.set_x(k.x)
        tmp2.set_y(k.y)
        tmp2.set_s(k.s)
        tmp2.set_c_u(k.c_u)
        tmp2.set_c_d(k.c_d)
        tmp2.set_c_l(k.c_l)
        tmp2.set_c_r(k.c_r)
        tmp1.append(tmp2)

    for k in range(0,len(atoms)):
        if(k != i): boardgame[atoms[k].y][atoms[k].x] = atoms[k].s

    x1 = tmp1[i].x
    y1 = tmp1[i].y

    for k in range(x1-1,0,-1):
        if boardgame[y1][k] == " ":
            tmp1[i].set_x(k)
        else:
            break

    for k in range(0,len(atoms)):
        if(k != i): boardgame[atoms[k].y][atoms[k].x] = " "

    return [tmp1]

def move_right(i,atoms,boardgame):
    if (boardgame[atoms[i].y][atoms[i].x+1] != " ") : return []

    tmp1 = []
    for k in atoms:
        tmp2 = atomState()
        tmp2.set_x(k.x)
        tmp2.set_y(k.y)
        tmp2.set_s(k.s)
        tmp2.set_c_u(k.c_u)
        tmp2.set_c_d(k.c_d)
        tmp2.set_c_l(k.c_l)
        tmp2.set_c_r(k.c_r)
        tmp1.append(tmp2)

    for k in range(0,len(atoms)):
        if(k != i): boardgame[atoms[k].y][atoms[k].x] = atoms[k].s

    x1 = tmp1[i].x
    y1 = tmp1[i].y

    for k in range(x1+1,len(boardgame[y1])):
        if boardgame[y1][k] == " ":
            tmp1[i].set_x(k)
        else:
            break

    for k in range(0,len(atoms)):
        if(k != i): boardgame[atoms[k].y][atoms[k].x] = " "

    return [tmp1]

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

def equal_atoms(atom1,atom2): #return 0 if equal and 1 if not
    if (atom1.s == atom2.s):
        if (atom1.x == atom2.x):
            if (atom1.y == atom2.y):
                if (atom1.c_u == atom2.c_u):
                    if (atom1.c_d == atom2.c_d):
                        if (atom1.c_l == atom2.c_l):
                            if (atom1.c_r == atom2.c_r) : return 0
                            else: return 1
                        else: return 1
                    else: return 1
                else: return 1
            else: return 1
        else: return 1
    else: return 1
                             

def equal_states(atoms1,atoms2): #return 0 if equal and 1 if not
    for i in range(0,len(atoms1)):
        if (equal_atoms(atoms1[i],atoms2[i]) == 1) : return 1
    return 0

def is_visited(atoms, visited): #return 0 if visited and 1 if not
    for i in visited:
        if(equal_states(i,atoms) == 0) : return 0
        else: continue
    return 1

def bfs(atoms,boardgame,solution,visited,path):
    neighbors = []
    for i in range(0,len(atoms)):
        move = move_up(i,atoms,boardgame)
        if (len(move) > 0):
            if (is_visited(move[0],visited) == 1):
                if(verify_solution(solution,move[0]) == 0):
                    path.append(move[0])
                    return path
                else:
                    neighbors.append(move[0])
                    visited.append(move[0])
        move = move_down(i,atoms,boardgame)
        if (len(move) > 0):
            if (is_visited(move[0],visited) == 1):
                if(verify_solution(solution,move[0]) == 0):
                    path.append(move[0])
                    return path
                else:
                    neighbors.append(move[0])
                    visited.append(move[0])
        move = move_left(i,atoms,boardgame)
        if (len(move) > 0):
            if (is_visited(move[0],visited) == 1):
                if(verify_solution(solution,move[0]) == 0):
                    path.append(move[0])
                    return path
                else:
                    neighbors.append(move[0])
                    visited.append(move[0])
        move = move_right(i,atoms,boardgame)
        if (len(move) > 0):
            if (is_visited(move[0],visited) == 1):
                if(verify_solution(solution,move[0]) == 0):
                    path.append(move[0])
                    return path
                else:
                    neighbors.append(move[0])
                    visited.append(move[0])

    for i in neighbors:
        path_cp = copy.deepcopy(path)
        path_cp.append(i)
        path_cp = bfs(i,boardgame,solution,visited,path_cp)
        if(len(path_cp) > 0): return path_cp

    return []

def print_results(path, total_time, board):
    for i in path:
        printBoard(board,i)
        print(" ")

    print("Esta solução tem {} passos e demorou {} segundos.\n".format(len(path),total_time))

    for i in path[-1]:
        print("O átomo {} na posição ({},{}) tem: \n - {} ligação/ões para cima \n - {} ligação/ões para baixo \n - {} ligação/ões para a esquerda \n - {} ligação/ões para a direita".format(i.s,i.x,i.y,i.c_u,i.c_d,i.c_l,i.c_r))
        print(" ")

main()
