class Puzzle:
    def __init__(self):
        self.direc = [[-1,0],[-1,-1],[-1,1],[0,-1],[0,1],[1,0],[1,-1],[1,1]]
        
    def search(self,grid,word,row,col):
        if grid[row][col] != word[0]:
            return False
        for x,y in self.direc:
            rd = row + x
            cd = col + y
            flag = True
            for k in range(1,len(word)):
                if (0<=rd<len(grid) and 0<=cd<len(grid[0]) and grid[rd][cd] == word[k]):
                    rd += x
                    cd += y
                else:
                    flag = False
                    break
            if flag:
                return True
        return False
            
    def puzzsearch(self,grid,word):
        R = len(grid)
        C = len(grid[0])
        
        for row in range(R):
            for col in range(C):
                if self.search(grid,word,row,col):
                    print("The word is found in grid at row:{0}, column:{1}".format(row,col))
                



if __name__ == "__main__":
    grid = ["PYTDKGSYEJ", "YRSJSWAGFN", "JSWAGUWNGO"]
    word = "SWAG"
    puzz = Puzzle()
    puzz.puzzsearch(grid,word)
