n, k = map(int, input().split())
ratings = list(map(int, input().split()))

def divide_and_conquer(start, count, k):
    # If there's only one player, return that player's index
    if count == 1:
        return [start]

    # Recursively divide the list of players in half and check the difference in ratings
    l_players = divide_and_conquer(start, count // 2, k)
    r_players = divide_and_conquer(start + (count // 2), count // 2, k)
    
    merged_players = []

    l_ptr = r_ptr = 0
    
    # Keep track of the lowest ratings in each half
    left_min = ratings[l_players[0]]
    right_min = ratings[r_players[0]]

    # Merge the two halves by comparing each player's rating
    while l_ptr < len(l_players) and r_ptr < len(r_players):
        
        if ratings[l_players[l_ptr]] <= ratings[r_players[r_ptr]]:
            if right_min - ratings[l_players[l_ptr]] <= k:
                merged_players.append(l_players[l_ptr])
            l_ptr += 1
        else:
            if left_min - ratings[r_players[r_ptr]] <= k:
                merged_players.append(r_players[r_ptr])
            r_ptr += 1
    
    # Add any remaining players from left or right halves while checking the rating difference
    while l_ptr < len(l_players) and right_min - ratings[l_players[l_ptr]] <= k:
        merged_players.append(l_players[l_ptr])
        l_ptr += 1
    
    while r_ptr < len(r_players) and left_min - ratings[r_players[r_ptr]] <= k:
        merged_players.append(r_players[r_ptr])
        r_ptr += 1

    return merged_players

# Find the players who can win the tournament and print their indices
winners = sorted(map(lambda x: x + 1, divide_and_conquer(0, len(ratings), k)))
print(*winners)