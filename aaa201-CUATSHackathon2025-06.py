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
    
    addedNewNode = True
    while len(stack) > 0:


        curr = stack.pop(0)
        cRow = curr[0]
        cCol = curr[1]
       
        if (((cRow, cCol) in visited) or cRow < 0 or cCol < 0 or cRow >= rows or cCol >= cols):
            continue
        
        if not addedNewNode:
            while board[cRow][cCol] != bWord[wordIndex]:
                bWord = bWord[:-1]
                wordIndex -= 1  
                visited.pop()
        
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

        addedNewNode = False
        for i in range(4):
            adjRow = cRow + dRow[i]
            adjCol = cCol + dCol[i]
            if (0 <= adjRow < rows) and (0 <= adjCol < cols) and ((adjRow, adjCol) not in visited):
                adjLetter = board[adjRow][adjCol]
                if adjLetter == word[wordIndex]:
                    stack.insert(0, [adjRow, adjCol])
                    addedNewNode = True

    return False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        return dfs(board, rows, cols, [1,1], word)

    
print(Solution().exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"))