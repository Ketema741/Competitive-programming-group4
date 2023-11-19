n = int(input())
patterns= []
for i in range(n):
  patterns.append(input())

matches = ["?" for _ in range(len(patterns[0]))]
mismatch = set()

for pattern in patterns:
  for i, char in enumerate(pattern):
    if i in mismatch or char == "?":
      continue

    if matches[i] == "?":
      matches[i] = char
    elif char != matches[i]:
      mismatch.add(i)
      matches[i] = "?"

for i in range(len(matches)):
  if i not in mismatch and matches[i] == "?":
    matches[i] = "a"

print("".join(matches))