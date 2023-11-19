input_len = int(input())
for _ in range(input_len):
  start_times = []
  end_times = []
  n = int(input())
  for _ in range(n):
    start, end = list(map(int, input().split()))
    end_times.append(end)
    start_times.append(start)

  start_times.sort()
  end_times.sort()
  end_ptr = 0
  assistant = 0

  for star_ptr in range(len(start_times)):
    if start_times[star_ptr] < end_times[end_ptr]:
      assistant += 1
    else:
      end_ptr += 1
  print(assistant)