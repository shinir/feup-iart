# -*- coding: utf-8 -*-

import atomix

class BFSAlgorithm:
    def __init__(self, boardstate, solution):
        self._boardstate = boardstate
        self._solution = solution
    
    def solve(self):
        try:
            return self.__process_level([self._boardstate])
        except:
            # BFS limit reached; signal error.
            return None
    
    def __process_level(self, level_states):
        ret = []
        
        # Did we find a solution yet?
        for state in level_states:
            if atomix.verify_solution(self._solution, state[1]):
                ret.append(state)
        
        # No, we need to go a level deeper:
        next_level = []
            
        for state in level_states:
            next_level.append(atomix.move_up(state[1], state[0]))
            next_level.append(atomix.move_down(state[1], state[0]))
            next_level.append(atomix.move_left(state[1], state[0]))
            next_level.append(atomix.move_right(state[1], state[0]))
        
        return ret + self.__process_level(next_level)

    
        