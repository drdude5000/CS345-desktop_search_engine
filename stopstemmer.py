

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
    count = 0
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
    

stopword(5)
