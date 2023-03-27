from game import check_win
def minimax(state,move_count,symbol,depth,maximizing):

    #construct all next_possible moves for this iteration
    available_moves = []
    for (i,s) in enumerate(state):
        if s != "X" and s != "Y":
            available_moves.append(i)
    
    positive_score = 1*(len(available_moves)+1)
    negative_score = -1*(len(available_moves)+1)

    #check if game is over
    win_state = check_win(state,move_count)
    if depth == 0 or win_state > 0:
        if symbol == "X":
            if win_state == 1:
                return (0,positive_score)
            if win_state == 2:
                return (0,negative_score)

        if symbol == "Y":
            if win_state == 2:
                return (0,positive_score)
            if win_state == 1:
                return (0,negative_score)

        return(0,0)
    
    
    if maximizing:
        best = (0,-1)
        for move in available_moves:
            next_state = state.copy()
            next_state[move] = symbol
            
            eval = minimax(next_state,move_count+1,symbol,depth-1,False)
            if eval[1] > best[1]:
                best = (move,eval[1])
        return best
    else:
        best = (0,1)
        for move in available_moves:
            next_state = state.copy()
            next_state[move] = symbol
            
            eval = minimax(next_state,move_count+1,symbol,depth-1,False)
            if eval[1] < best[1]:
                best = (move,eval[1])
        return best

