## String permutation /////////////


def string_opration(char, count, result, level):
    if level == len(char):
        print(''.join(result))
    else:

        for i in range(0,len(char)):
            if count[i] == 0:
                continue
            else:
                result[level] = char[i]
                count[i] -=1
                string_opration(char, count, result, level + 1)
                count[i] += 1

def string_permutation(string):
    count = [1]*len(string)
    result = [0]*len(string)
    string_opration(string,count,result,0)



## BOGGLE Problem **************//////////////////////////

pathRow = [0,0,1,1,-1,1,-1,-1]
pathCol = [1,-1,-1,1,1,0,0,-1]

def IfValid(rowNew, colNew, visited):
    if rowNew >=0 and colNew >=0 and rowNew < len(visited) and colNew < len(visited) and not visited[rowNew][colNew]:
        return True
    else:
        return False

def findWord(board, visited, row, col, word, dictionary):
    if word in dictionary:
        print(word)

    if len(word) == 9:
        return

    for i in range(0, len(pathRow)):
        rowNew = row + pathRow[i]
        colNew = col + pathCol[i]
        if IfValid(rowNew, colNew, visited):
            visited[rowNew][colNew] = True
            findWord(board, visited, rowNew, colNew, word+board[rowNew][colNew], dictionary)
            visited[rowNew][colNew] = False



####### path finding Algorithm /////////////////////////////
moveRow = [0,0,1,-1]
moveCol = [1,-1,0,0]

def weCanMove(maze, visited, newRow, newCol):
    if newRow >=0 and newCol >= 0 and newRow < len(visited) and newCol < len(visited) and maze[newRow][newCol]==1 and visited[newRow][newCol]==0:
        return True
    else:
        return False

def findMazePath(maze, visited, row, col, desRow, desCol, move):
    if row == desRow and col == desCol:
        for i in range(0,len(visited)):
            for j in range(0, len(visited)):
                    if visited[i][j]==0:
                        print(end='  ')
                    else:
                        print(visited[i][j],end=' ')
            print("")
        print("Next Path")
    else:
        for i in range(0,len(moveRow)):
            newRow = row + moveRow[i]
            newCol = col + moveCol[i]
            if weCanMove(maze,visited,newRow,newCol):
                move +=1
                visited[newRow][newCol] = move
                findMazePath(maze,visited,newRow,newCol,desRow,desCol,move)
                move -=1
                visited[newRow][newCol] = 0



### Knight Tour ////////////////////////////////////////
knightRow = [2,1,-1,-2,-2,-1,1,2]
knightCol = [1,2,2,1,-1,-2,-2,-1]
def IfvalidMove(visited, newRow, newCol):
    if newRow>=0 and newCol>=0 and newRow<8 and newCol<8 and visited[newRow][newCol]==0:
        return True
    else:
        return False

def knightTour(visited, row, col, move):
    if move == 64:
        for i in range(0,8):
            for j in range(0,8):
                print(visited[i][j],end="  ")
            print(" ")
        return True
    else:
        for i in range (0,len(knightRow)):
            newRow = row + knightRow[i]
            newCol = col + knightCol[i]
            if IfvalidMove(visited,newRow, newCol):
                move +=1
                visited[newRow][newCol] = move
                if knightTour(visited,newRow,newCol,move):
                    return True
                move -=1
                visited[newRow][newCol] = 0
    return False

#### N Queen Problem ///////////////////////////////////
def IfValidCell(board, newRow, newCol, size):
    valid = True
    for i in range(0,size):
        if board[i][newCol]:
            valid = False
    row = newRow
    col = newCol
    while row >= 0 and col >= 0:
            if board[row][col]:
                valid = False
            row -= 1
            col -= 1
    row = newRow
    col = newCol
    while row >= 0 and col < size:
            if board[row][col]:
                valid = False
            row -= 1
            col += 1
    return valid
def nQueen(board, row, size):
    if row == size - 1:
        for i in range(0,size):
            for j in range(0,size):
                print(board[i][j],end="  ")
            print(" ")
        return True
    else:
        for newCol in range(0,size):
            newRow  = row + 1
            if IfValidCell(board, newRow, newCol, size):
                board[newRow][newCol] = True;
                if nQueen(board,newRow,size):
                    return True
                board[newRow][newCol] = False;
        return False


####### Unique Grid path ///////////////////////////////
def uniqeGridPath(n,m):
    if n == 1 or m == 1:
        return 1
    else:
        return uniqeGridPath(n,m-1) + uniqeGridPath(n-1,m)


##### Partition of given list ///////////////////////////

def count_partition(n,m):

    if n == 0:
        return 1
    elif m == 0 or n < 0:
        return 0
    else:
        return count_partition(n-m,m) + count_partition(n,m-1)




