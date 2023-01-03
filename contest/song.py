from collections import defaultdict
N = int(input())
res = []

for i in range(N):
    hash_Map = defaultdict()
    chorus = list(input().split())
    for choru in chorus:
        for indx, char in enumerate(choru):
            if char.isdigit():
                choru = choru.replace(choru[indx], '')
                hash_Map[char] = (choru)
                
    sorted_chour = sorted(list(hash_Map.items()))
    songs = ""
    for song in sorted_chour:
        songs += song[1] + ' '
    songs = songs[:len(songs)-1]
    res.append(songs)
                            
for chorus in res:
    print(chorus)