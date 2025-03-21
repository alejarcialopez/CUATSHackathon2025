def dfs(board, rows, cols, start, word, wordIndex, visited):
    dRow = [0, 1, 0, -1]
    dCol = [-1, 0, 1, 0]
    wordIndex += 1

    if wordIndex >= len(word):
        return True
    
    visited.add((start[0],start[1]))

    for i in range(4):
        adjRow = start[0] + dRow[i]
        adjCol = start[1] + dCol[i]
        if (0 <= adjRow < rows) and (0 <= adjCol < cols) and ((adjRow, adjCol) not in visited):
            adjLetter = board[adjRow][adjCol]
            targetLetter = word[wordIndex]
            if adjLetter == targetLetter:
                check = dfs(board, rows,cols, [adjRow, adjCol], word, wordIndex, visited)
                if check:
                    return True           
    
    visited.remove((start[0],start[1]))
    return False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = []
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(board, rows, cols, [i,j], word, 0, set()):
                        return True
        return False