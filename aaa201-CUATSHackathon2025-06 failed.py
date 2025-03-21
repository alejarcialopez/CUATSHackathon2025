from typing import List


def dfs(board, rows, cols, start, word):
    dRow = [0, 1, 0, -1]
    dCol = [-1, 0, 1, 0]
    visited = []
    stack = [start]
    if word[0] != board[start[0]][start[1]]:
        return False
    bWord = ""
    wordIndex = 0
    if bWord == word:
            return True
    
    addedNewNode = 1
    steps = -1
    dead=[]
    while len(stack) > 0:

        if addedNewNode == 0:
            dead.append((cRow, cCol))
            
            for _ in range(steps):
                bWord = bWord[:-1]
                wordIndex -= 1  
                visited.pop()
            steps = 0
        elif addedNewNode > 1:
            steps = 0 
        curr = stack.pop(0)
        cRow = curr[0]
        cCol = curr[1]
       
        if (((cRow, cCol) in visited) or cRow < 0 or cCol < 0 or cRow >= rows or cCol >= cols):
            continue
        
        

        steps +=1

        visited.append((cRow, cCol))

        if board[cRow][cCol] == word[wordIndex]:
            bWord += word[wordIndex]
            wordIndex += 1
        else:
            bWord = bWord[:-1]
            wordIndex -= 1  
            visited.pop()

        if bWord == word:
            return True

        addedNewNode = 0
        for i in range(4):
            adjRow = cRow + dRow[i]
            adjCol = cCol + dCol[i]
            if (0 <= adjRow < rows) and (0 <= adjCol < cols) and ((adjRow, adjCol) not in visited) and ((adjRow, adjCol) not in dead):
                adjLetter = board[adjRow][adjCol]
                if adjLetter == word[wordIndex]:
                    stack.insert(0, [adjRow, adjCol])
                    addedNewNode += 1

    return False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        return dfs(board, rows, cols, [4,0], word)


b= [["a","a","A","a","a","a"],["a","a","a","a","A","a"],["a","a","a","a","A","A"],["A","A","a","A","a","A"],["a","a","a","a","A","a"],["A","a","a","A","a","a"]]
w="aAAaAaaaAaAaAAA"
print(Solution().exist(b, w))