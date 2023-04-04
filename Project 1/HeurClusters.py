# -*- coding: utf-8 -*-

# This heuristic returns the inverse number of solution-aligned atoms
        
def heur_clusters(atoms, solution):
    ret = len(atoms)
    
    dlist = [[atoms[0].x - solution[0].x, atoms[0].y - solution[0].y]]
    
    for i in range(1,len(solution)):
        for ofs in dlist:
            if (solution[i].x + ofs[0] == atoms[i].x):
                if(solution[i].y + ofs[1] == atoms[i].y):
                    ret -= 1
                    break
    
    print(ret)
    return ret