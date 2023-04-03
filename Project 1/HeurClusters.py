# -*- coding: utf-8 -*-

class HeurClusters:
    # This heuristic returns the number of solved clusters - 1.
    
    def __init__(self, atoms, solution):
        self.atoms = atoms
        self.solution = solution
        
    def getCost(self):
        ret = 0
        
        dlist = [[]]
        dlist[0][0] = self.atoms[0].x - self.solution[0].x
        dlist[0][1] = self.atoms[0].y - self.solution[0].y
        
        for i in range(1,len(self.solution)):
            belongs = False
            for ofs in dlist:
                if (self.solution[i].x + ofs[0] == self.atoms[i].x):
                    if(self.solution[i].x + ofs[1] == self.fatoms[i].x):
                        belongs = True
                        break
            
            if not belongs:
                new_ofs = []
                new_ofs[0] = self.atoms[i].x - self.solution[i].x
                new_ofs[1] = self.atoms[i].y - self.solution[i].y
                dlist.append(new_ofs)
                ret += 1
        
        return ret