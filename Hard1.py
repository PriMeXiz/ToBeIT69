s = str(input())

s = s.lower()
result = ''

for i in range (0, len(s)):
    result += s[len(s) - i - 1]

print("FALSE") if result != s else print("TRUE")