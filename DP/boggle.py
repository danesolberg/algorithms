dictionary = set(["GEEKS", "FOR", "QUIZ", "GO"])
board = [['G', 'I', 'Z'],
         ['U', 'E', 'K'],
         ['Q', 'S', 'E']]

def dfs(board, dictionary, found_words, prefix, visited, i, j):
    visited.add((i, j))

    cur_letter = board[i][j]
    cur_word = prefix + cur_letter
    if cur_word in dictionary:
        found_words.append(cur_word)

    neighbors = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
    
    for i2, j2 in neighbors:
        if (i+i2, j+j2) not in visited and i+i2 >= 0 and j+j2 >= 0 and i+i2 < len(board) and j+j2 < len(board[0]):
            dfs(board, dictionary, found_words, cur_word, visited.copy(), i+i2, j+j2)

def find_words(board, dictionary):
    found_words = []
    if not dictionary or not board:
        return []
    
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            print(board[i][j])
            dfs(board, dictionary, found_words, "", set(), i, j)
            
    return found_words

print(find_words(board, dictionary))

#TODO: implement Trie and DP