from itertools import permutations
from typing import List
from collections import Counter 
#V2 borrowed from Spaulding_/ because I was getting TLE at 60/79th testcase

def equalPairs(self, grid: List[List[int]]) -> int:

        transpose = list(zip(*grid))

        gridC = Counter(map(tuple,grid))
        gridTC = Counter(transpose)
        
        return(sum(gridC[t]*gridTC[t] for t in gridTC))

#V1 written by me
def equalPairs(self, grid: List[List[int]]) -> int:
        if (len(grid)==1):
            return 1

        coord1D = list(range(len(grid)))
        unique_combinations = []
        tgrid = list(zip(*grid))
        count = 0
    
        permut = permutations(coord1D, 2)
    
        for comb in list(permut):
            if (comb[0], comb[0]) not in unique_combinations:
                unique_combinations.append((comb[0], comb[0]))
            unique_combinations.append(comb)
            
        for coord in unique_combinations:
            if hash(tuple(grid[coord[0]]))==hash(tgrid[coord[1]]):
                count+=1 

        return(count)
