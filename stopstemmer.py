
def stopword(gdir):
    stopfile = open('stopwords.txt', 'r')
    stoptxt = stopfile.read()
    stopfile.close()
    stoplst = stoptxt.split('\n')
    stoplst.pop()
    
    tokfile = open('step2.txt', 'r')
    toktxt = tokfile.read()
    tokfile.close()
    toklst = toktxt.split('\n')
    toklst.pop()

    orglst = []
    for i in toklst:
        
        orglst.append(i.split())
        if orglst[len(orglst)-1][1].lower() in stoplst:
            orglst.pop()

    newfile = open('step3.txt', 'w')

    for i in orglst:
        entry = ""
        for j in i:
            entry += j + ' '

        newfile.write(entry)
        newfile.write('\n')
    newfile.close()
    


def stem(gdir):
    s3file = open('step3.txt', 'r')
    s3txt = s3file.read()
    s3file.close()
    s3lst = s3txt.split('\n')

    for i in range(s3lst.count("")):
        s3lst.pop()
    
    s3orglst = []
    stemlst = []
    lex = []

    count = 0
    for i in s3lst:
        s3orglst.append(i.split())
        word = s3orglst[count][1]

        temp = ""
        sflag = 0

        if (len(word) > 3):
            if (word[-3:] == "ies" and (word[-4] != 'e' and word[-4] != 'a')):
                temp = word

                word = word[:-3] + 'y'

                stemlst.append([word, temp])
                sflag = 1
        if (len(word) > 2 and sflag == 0):
            if (word[-2:] == "es" and (word[-3] != 'e' and word[-3] != 'o')):
                temp = word

                word = word[:-2] + 'e'

                stemlst.append([word, temp])
                sflag = 1        
        if (len(word) > 1 and sflag == 0):
            if (word[-1:] == "s" and (word[-2] != 'u' and word[-2] != 's')):
                temp = word

                word = word[:-1]

                stemlst.append([word, temp])
                sflag = 1

        if (word not in lex):
            lex.append(word)
            

        s3orglst[count][1] = str(lex.index(word)+1)
        
        count += 1

    lexfile = open('step4LEX.txt', 'w')
    for i in lex:
        lexfile.write(i)
        lexfile.write('\n')
    lexfile.close()

    stemfile = open('step4STEM.txt', 'w')
    for i in stemlst:
        entry = ""
        for j in i:
            entry += j + " "
            
        stemfile.write(entry)
        stemfile.write('\n')
    stemfile.close()

    s5file = open('step4.txt', 'w')
    for i in s3orglst:
        entry = ""
        for j in i:
            entry += j + " "

        s5file.write(entry)
        s5file.write('\n')
    s5file.close()

