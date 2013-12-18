#encoding=utf-8
#cat -- short for category
#catTokenTable 为每类的TokenTable
#catProbTable 由每个catTokenTable直接计算出来
#catPHTTable 为计算公式一得出的Table
#公式一的调用返回catPHTTable
#公式二的调用返回运算概率结果


import os
import jieba
import jieba.posseg as pseg

#把file中逐行读取生成一个list
def readFileToList(fileName):
    fileList = list()
    file = open(fileName, "r")
    for line in file:
        fileList.append(line)
    return fileList

#生成对应每一类型的catProbTable
def listToCatTokenTable(list):
    tokenTable = dict()
    for str in list:
        tokenList = stringToToken(str) #call
        createTableWithTokenList(tokenList, tokenTable) #call
    proTable = catTokenTableToProTable(tokenTable)
    return proTable

#Caller: listToCatTokenTable
#执行cut以及按词性筛选的功能
def stringToToken(str):
    token_table = list()
    words = pseg.cut(str)
    for w in words:
    #print w.word, w.flag
        #if w.flag == 'v' or w.flag == 'a':
        #if w.flag == 'v' or w.flag == 'a' or w.flag == 'n':
        if w.flag == 'n' and w.flag != 'nr' and w.flag != 'ns' and w.flag != 'nt' and w.flag != 'nrt' and w.flag != 'nz' and w.flag != 'ng' or w.flag == 'v':
        #if w.flag == 'v':
            token_table.append(w.word)
    return token_table

#Caller: listToCatTokenTable
#把tokenList加入tokenTable
def createTableWithTokenList(tokenList, tokenTable):
    for token in tokenList:
        token = token.encode("UTF-8", errors="strict")
        if (tokenTable.has_key(token)):
            tokenTable[token] += 1
        else:
            tokenTable[token] = 1

#最终步骤：把catTokenTable转换成catProTable
def catTokenTableToProTable(catTokenTable):
    total = 0
    for token in catTokenTable.keys():
        if catTokenTable[token] > 1:
            #print token,catTokenTable[token]
            total += catTokenTable[token]
    catProTable = dict()
    for token in catTokenTable.keys():
        if catTokenTable[token] > 1:
            catProTable[token] = catTokenTable[token] / float(total)

    return catProTable

#公式一部分
def proFromCatProTable(key, catProTable):
    if key in catProTable.keys():
        return catProTable[key]
    else:
        return 0

def sumOfCatProTables(key, allCatProTable):
    sum = 0
    for catProTable in allCatProTable.values():
        sum += proFromCatProTable(key, catProTable)
    return sum

def catPHTTableFromFormulaOne(catProTable, allCatProTable):
    catPHTTable = dict()
    #对于A表格中的每个token -- key 做P的计算
    for key in catProTable.keys():
        catPHTTable[key] = catProTable[key] / sumOfCatProTables(key, allCatProTable)
        if catPHTTable[key] == 1:
            catPHTTable[key] = 0.95
    return catPHTTable

#公式二部分
def ResultFromEveryTokenDict(str, catPHTTable):

    tokens = stringToToken(str)
    probList = list()
    for token in tokens:
        #print token
        token = token.encode('utf-8')
        if token in catPHTTable:
            #print token
            probList.append(catPHTTable[token])

    m = 1
    n = 1
    for p in probList:
        #print p
        m = p * m
        #print "m:", m
        n = (1 - p) * n
        #print "n:", n
    return m / (m + n)
    #return m


Romantic = "RomanticMovie.txt"
Horror = "HorrorFilm.txt"
ScienceFiction = "ScienceFictionFilm.txt"
TestFileName = "Sample.txt"

RomanticList = readFileToList(Romantic)
HorrorList = readFileToList(Horror)
ScienceList = readFileToList(ScienceFiction)
TestList = readFileToList(TestFileName)


RomanticCatTable = listToCatTokenTable(RomanticList)
HorrorCatTable = listToCatTokenTable(HorrorList)
ScienceCatTable = listToCatTokenTable(ScienceList)

probability_table_dic = dict()
probability_table_dic['RomanticMovie'] = RomanticCatTable
probability_table_dic['HorrorFilm'] = HorrorCatTable
probability_table_dic['ScienceFictionFilm'] = ScienceCatTable

#把TestList中的内容加入到一个TestCaseList中
testCaseList = list()
tempString = ""
for item in TestList:
    if item != "\n":
        tempString += item
    else:
        testCaseList.append(tempString)
        tempString = ""
if tempString != "":
    testCaseList.append(tempString)

print "Begin the test cases"
print "----------------------------------"
for item in testCaseList:
    print "The test story is: ", item
    probability_table = catPHTTableFromFormulaOne(ScienceCatTable, probability_table_dic)
    print "Possibility of being a scientific story: ", ResultFromEveryTokenDict(item, probability_table)
    probability_table2 = catPHTTableFromFormulaOne(RomanticCatTable, probability_table_dic)
    print "Possibility of being a romantic story: ", ResultFromEveryTokenDict(item, probability_table2)
    probability_table3 = catPHTTableFromFormulaOne(HorrorCatTable, probability_table_dic)
    print "Possibility of being a horrible story: ", ResultFromEveryTokenDict(item, probability_table3)
    print "----------------------------------"
