n, t = map(int, input().split())
line_word = list(map(int, input().split()))
possible = False


current = 1

while current < t:
    current += line_word[current-1]
    if current == t:
        possible = True
        break

if possible:
    print("YES")
else:
    print("NO")
