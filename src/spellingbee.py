words = {}

# center letter must come first
letters = ''

def processWord(word):
    global letters ## not good practice
    if word.startswith('-'):
        wordToDrop = word.strip('-')
        if wordToDrop in words:
            words.pop(wordToDrop)

    if word.startswith('+'):
        letters = word.strip('+')

    score = calcScore(word)

    if score:
        words[word] = score

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

    if score: score += pangram

    if pangram: print("\nPangram!")
    print(word, "is worth", score, "points.")

    return score

def calcTotal(words):
    sum = 0
    print()
    for word in sorted(words):
        print(words[word], '\t', word)
        sum += words[word]

    print("--------------------")
    print(len(words), "words,", sum, 'points')
    print()

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
    print(word)
    processWord(word)
inFile.close()

calcTotal(words)
printHive()

while True:
    word = input("Enter a word: ")
    if word == '': 
        break

    processWord(word)

    calcTotal(words)
    printHive()

calcTotal(words)

outFile = open("words.txt", 'w')

outFile.write('+' + letters + '\n')
for w in sorted(words):
    outFile.write(w + "\n")
outFile.close()