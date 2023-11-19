def check_substrings(s):
    if "AB" in s and "BA" in s:
        if s.index("AB") + 1 < s.rindex("BA") or s.index("BA") + 1 < s.rindex("AB"):
            return "YES"
    return "NO"

s = input()

print(check_substrings(s))
