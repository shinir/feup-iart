# -*- coding: utf-8 -*-

# import atomix2
from atomState import atomState
import math

class GreedyAlgorithm:
    def __init__(self, board, atoms, solution, heuristic):
        self._board = board
        self._atoms = atoms
        self._solution = solution
        self._heuristic = heuristic
    
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
                if len(temp) == 0: continue
                temp_heur = self._heuristic(temp[0], self._solution)
                
                if temp_heur < best_heur:
                    best_step = temp[0]
                    best_heur = temp_heur
                    
                if temp_heur == 0:
                    return [temp[0]]
        
        return [best_step] + self.__do_step(best_step)
    
    
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