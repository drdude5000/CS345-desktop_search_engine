biglst = []
#step 2 tokenizer
# FIRST PARAMETER IS JUST THE STEP1.TXT
# SECOND PARMETER IS THE DIRECTORY WE ARE SUPPOSE TO USE
def token(s1file, gdir):

        #open step1file
        rawfile = open(s1file, 'r')
        s1text = rawfile.read()
        rawfile.close()        
        
        s1lst = s1text.split('\n')
        if (s1lst[len(s1lst)-1] == ""):
                s1lst.pop()

        for i in s1lst:
                xline(i)

                
        newfile = open('step2.txt', 'w')

        for i in biglst:
                entry = ""
                for j in i:
                        entry += str(j) + " "
                newfile.write(entry)
                newfile.write("\n")


#examine a step1 line provided by besho
#it parses ... slightly
def xline(entry):
        oentry = entry.split()
        if (oentry[1] == "TXT"):
                mfile = open(oentry[0], 'r')
                itext = mfile.read()
                mfile.close()
                ilst = itext.split()

                inHTML = 0
                if(oentry[0][-4:] == "html" or oentry[0][-3:] == "htm"):
                        inHTML = 1;

                count = 0
                
                hflag = [0]
                for i in ilst:
                        if(inHTML == 1):
                                
                                i = str(i)
                                if(i.lower() == "<title>" or i.lower() == "</title>" ):
                                        if(hflag[len(hflag) - 1] == 1):
                                                hflag.pop()
                                        else:
                                                hflag.append(1)
                                        
                                elif(i.lower() == "<a>" or i.lower() == "</a>" ):
                                        if(hflag[len(hflag) - 1] == 2):
                                                hflag.pop()
                                        else:
                                                hflag.append(2)
                                elif(len(i) > 3 and i[len(i)-1] == '>'):
                                        if(i.lower()[0] == '<' and i.lower()[1] == 'h' and i[2].isdigit()):
                                                if(hflag[len(hflag) - 1] == 1):
                                                        hflag.pop()
                                                else:
                                                        hflag.append(3)

                        if (inHTML == 1):
                                
                                if(checkword(i) == 0):
                                        count += 1
                                        continue
                                smlst = [oentry[2], i, count, hflag[len(hflag) - 1]]                        
                                biglst.append(smlst)              
                                count += 1
                        else:
                                if(checkword(i) == 0):
                                        count += 1
                                        continue
                                
                                smlst = [oentry[2], i, count, 0]                        
                                biglst.append(smlst)
                                count += 1





def checkword(word):
        word = str(word)
        if(word.isalpha()):
                return 1
        elif(word.isdigit()):
                return 2
        elif(word.isalnum()):
                if(word[0].isalpha()):
                        return 3
        return 0



def tokendebug():
	print("DEBUG")


