input = input("enter your word i keyes: ")

word = []
temp = []

for index in range(0, len(input)):
    if (input[index] == " "):
        word.append(temp)
        temp = []
    elif (index == len(input) - 1):
        temp.append(input[index])
        word.append(temp)
    else:
        temp.append(input[index])

longest = []
longest.append(max(word, key=len))
word = ""

for i in range(0, len(longest)):
    word += ''.join(longest[i])

print(word)
