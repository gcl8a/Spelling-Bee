words = {}

# center letter must come first
letters = 'twoghur'

sum = 0

def calcScore(word):
    score = len(word)
    if score < 4:
        score = 0
    
    if score == 4:
        score = 1

    for l in word:
        if l not in letters:
            score = 0

    if letters[0] not in word:
        score = 0

    pangram = 7
    for l in letters:
        if l not in word:
            pangram = 0

    score += pangram

    if pangram: print("\nPangram!")
    print(word, "is worth", score, "points.")

    return score

def calcTotal(words):
    sum = 0
    print()
    for word in sorted(words):
        print(words[word], '\t', word)
        sum += words[word]

    print("-----------------")
    print(len(words), "words")
    print(sum, 'points')
    print()
    printHive()

    return sum

def printHive():
    upperCase = letters.upper()
    print('    ', upperCase[1], ' ', upperCase[2])
    print()
    print('  ', upperCase[3], ' ', upperCase[0], ' ', upperCase[4])    
    print()
    print('    ', upperCase[5], ' ', upperCase[6])
    print()

inFile = open("words.txt")
for line in inFile:
    word = line.strip()
    score = calcScore(word)
    words[word] = score
inFile.close()

calcTotal(words)

while True:
    word = input("Enter a word: ")
    if word == '': 
        break

    if word.startswith('-'):
        wordToDrop = word.strip('-')
        if wordToDrop in words:
            words.pop(wordToDrop)

    score = calcScore(word)

    if score:
        words[word] = score

    calcTotal(words)

calcTotal(words)

outFile = open("words.txt", 'w')

for w in sorted(words):
    outFile.write(w + "\n")
outFile.close()