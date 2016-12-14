import os

def invert(gdir):
    if not os.path.exists("step5files"):
        os.makedirs("step5files")
    
    s4file = open("step4.txt", 'r')
    s4text = s4file.read()
    s4lst = s4text.split('\n')
    s4file.close()
    
    for i in range(s4lst.count('')):
        s4lst.pop()

    s4orglst = []

    for i in s4lst:
        s4orglst.append(i.split())
 

    #convert to int
    for i in range(len(s4orglst)):
        for j in range(4):
            s4orglst[i][j] = int(s4orglst[i][j])

    for i in range(len(s4orglst)):
            temp = s4orglst[i][0]
            s4orglst[i][0] = s4orglst[i][1]
            s4orglst[i][1] = temp

    
    s4orglst.sort()
        
    lexfile = open("step4LEX.txt", 'r')
    lextext = lexfile.read()
    lexlst = lextext.split('\n')

    for i in range(lexlst.count('')):
        lexlst.pop()


    voclst = []
    #number of documents is wrong
    for i in range(len(lexlst)):
        ndocs = 1
        nhits = 0
        dflag = -1
        for j in range(len(s4orglst)):
            if (s4orglst[j][0] == i + 1):
                nhits += 1
                if (dflag != s4orglst[j][1]):
                    ndocs += 1
                    
            dflag = s4orglst[j][1]
            
        voclst.append([i+1, ndocs, nhits])

    
        
    vocfile = open('step5files/step5VOC.txt', 'w')
    for i in voclst:
        entry = ''
        for j in i:
            entry += str(j) + ' '
        vocfile.write(entry)
        vocfile.write('\n')
    
    vocfile.close()

    s5file = open('step5files/invertedIndex.txt', 'w')

    for i in s4orglst:
        entry = ''
        for j in i:
            entry += str(j) + ' '
        s5file.write(entry)
        s5file.write('\n')
    

invert(0)
