def solution(dungeon, health):
    # TODO: Implement the solution
    n = len(dungeon)
    best_x = None
    best_loss = None
    
    for x in range(1, n + 1):
        pos = 0
        loss = 0
        
        while True:
            loss += dungeon[pos]
            
            if loss > health:
                break
                
            if pos == n - 1 or pos + x > n - 1:
                if best_x is None or loss < best_loss:
                    best_x = x
                    best_loss = loss
                break
                
            pos += x
            
            if pos > n - 1:
                break
                
    if best_x is None:
        return -1
    remaining = health - best_loss
    return best_x, best_loss, remaining
        

print(solution([0, 5, -2, 8, 3, 0, 10, 4, -1, 7], 20))