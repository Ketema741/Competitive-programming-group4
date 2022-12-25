# Enter your code here. Read input from STDIN. Print output to STDOUT
num_english = int(input())
roll_english = set(input().split())

num_french = int(input())
roll_french = set(input().split())

print(len(roll_english - roll_french))