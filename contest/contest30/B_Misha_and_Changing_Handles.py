input_len  = int(input())
map_old = {}
map_new = {}

for _ in range(input_len):
  old, new = list(input().split())

  found = False
  for key, value in map_new.items():
    if value == old:
      map_new[key] = new;
      found = True
      break;

  map_old[old] = new

  if not found:
    map_new[old] = new


print(len(map_new))
for key, value in map_new.items():
  print(key,  value)
  

  