# -*- coding: utf-8 -*-

# import atomix2
from atomState import atomState
import copy
import math

class GreedyAlgorithm:
    def __init__(self, board, atoms, solution, heuristic):
        self._board = board
        self._atoms = atoms
        self._solution = solution
        self._heuristic = heuristic
        self._visited = [atoms]
    
    def solve(self):
        # try:
        return self.__do_step(self._atoms)
        # except:
            # return None

    def __do_step(self, atoms):
        best_step = None
        best_heur = math.inf
        
        for i in range(len(atoms)):
            for action in (move_up, move_down,
                           move_left, move_right):
                temp = action(i, atoms, self._board)
                
                if (len(temp) == 0): 
                    continue
            
                if (is_visited(temp[0], self._visited) == 0):
                    continue
            
                temp_heur = self._heuristic(temp[0], self._solution)
                
                self._visited.append(temp[0])
                
                if temp_heur < best_heur:
                    best_step = temp[0]
                    best_heur = temp_heur
                    
                if temp_heur == 0:
                    return [temp[0]]
        
        return [best_step] + self.__do_step(best_step)
    

class AStarAlgorithm:
    
    def __init__(self, board, atoms, solution, heur1, heur2):
        self._board = board
        self._atoms = atoms
        self._solution = solution
        self._heur1 = heur1
        self._heur2 = heur2
        
    
# TEMPORARY WEE WOOOOOOOOOO
    
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
    
def equal_states(atoms1,atoms2): #return 0 if equal and 1 if not
    for i in range(0,len(atoms1)):
        if (equal_atoms(atoms1[i],atoms2[i]) == 1) : return 1
    return 0

def is_visited(atoms, visited): #return 0 if visited and 1 if not
    for i in visited:
        if(equal_states(i,atoms) == 0) : return 0
        else: continue
    return 1

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