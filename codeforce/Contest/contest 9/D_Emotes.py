n, m, k = list(map(int, input().split()))
emots = sorted(list(map(int, input().split())))

sub_len = m//(k + 1) 
sub_sum = k*emots[-1] + emots[-2]
happiness = sub_len*sub_sum + (m - sub_len*(k + 1))*emots[-1]

print(happiness)