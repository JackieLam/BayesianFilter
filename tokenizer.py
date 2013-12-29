import jieba.posseg as pseg

def readFileToList(fileName):
    fileList = list()
    file = open(fileName, "r")
    for line in file:
        fileList.append(line)
    return fileList

def writeListToFile(list, fileName):
    file = open(fileName, "w")
    for item in list:
        file.write("%s\n" % item)

def stringToToken(str):
    tokenList = list()
    words = pseg.cut(str)
    for w in words:
    #Choose only the noun, verb and adjective, excluding the names and the addresses, etc.
        if w.flag == 'n' and w.flag != 'nr' and w.flag != 'ns' and w.flag != 'nt' and w.flag != 'nrt' and w.flag != 'nz' and w.flag != 'ng' or w.flag == 'v' or w.flag == 'a':
            print w.word
            tokenList.append(w.word)
    return tokenList

def listToCatTokenTable(StringList):
    TokenSum = list()
    for str in StringList:
        TokenList = stringToToken(str) #call
        for token in TokenList:
            token = token.encode("UTF-8", errors="strict")
            TokenSum.append(token)
    return TokenSum

Romantic = "romanticResult"
RomanticList = readFileToList(Romantic)
RomanticTokenSum = listToCatTokenTable(RomanticList)
writeListToFile(RomanticTokenSum, "romanticResultToken.txt")

#Science = "scienceResult"
#ScienceList = readFileToList(Science)
#ScienceTokenSum = listToCatTokenTable(ScienceList)
#writeListToFile(ScienceTokenSum, "scienceResultToken.txt")

#Suspense = "suspenseResult"
#SuspenseList = readFileToList(Suspense)
#SuspenseTokenSum = listToCatTokenTable(SuspenseList)
#writeListToFile(SuspenseTokenSum, "suspenseResultToken.txt")