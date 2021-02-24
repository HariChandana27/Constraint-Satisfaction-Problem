''' Solving N-Queens Problem '''
global board,N

def print_board():
    print()
    for i in range(N):
        for j in range(N):
            print(board[i][j],end =' ')
        print()

def check_attack(m,n):
    global N

    #checking attack via row redundant since each row is passed to place_queen()
    #checking for attack via column
    for k in range(N):
        if(k!=m and board[k][n]=='1'):
            return True
   
    #checking for attack via right lower diagonal
    k = m
    l = n
    while(k<N and l<N):
        if(board[k][l]=='1'):
            return True
        k+=1
        l+=1
     
    #checking for attack via left lower diagonal
    k = m
    l = n
    while(k<N and l>=0):
        if(board[k][l]=='1'):
            return True
        k+=1
        l-=1
    
    #checking for attack via right upper diagonal
    k = m
    l = n
    while(k>=0 and l<N):
        if(board[k][l]=='1'):
            return True
        k-=1
        l+=1

    #checking for attack via right upper diagonal
    k = m
    l = n
    while(k>=0 and l>=0):
        if(board[k][l]=='1'):
            return True
        k-=1
        l-=1


def place_queen(m):
    global board
    
    #base case
    #if 'N' queens can be placed in all the rows, the goal is achieved and the recursion stops 
    if(m==N):
        return True
    
    #recursive case
    for i in range(N):
        if(check_attack(m,i)!=True):
            #places the queen in 'm'th row and 'i'th column
            #only if there is no attack by another queen
            board[m][i]='1'

            #the next row is recursively passed to place_queen()
            if(place_queen(m+1)==True):
                #if the function can place the remaining queens in all the rows,
                #it simply returns True and the current queen is remained placed in (m,i)
                return True
            else:
                #else, the function backtracks to the current posiotion (m,i)
                #and iteratively looks for another 'i'th place to place the first queen
                board[m][i]=0

    #if 'N' queens can not be placed in all the rows, the recursion stops
    return False       

#driver code
if __name__ == '__main__':
    N = int(input('Enter the size of row or column of the board \n'))
    board = [[0 for j in range(N)]for i in range(N)]
    possible = place_queen(0)

    #if solution is not found, the place_queen() returns False
    #this for 'N' values less than 4
    if (possible==False):
        print('No solution exists for',N)
    print_board()

    
