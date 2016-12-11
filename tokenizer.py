biglst = []
#step 2 tokenizer
# FIRST PARAMETER IS JUST THE STEP1.TXT
# SECOND PARMETER IS THE DIRECTORY WE SUPPOSE TO USE
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
                for i in ilst:
                        hid = 0;
                        hflag = 0;
                        if(inHTML == 1):
                                
                                i = str(i)
                                if(i.lower() == "<title>" or i.lower() == "</title>" ):
                                        hid = 1
                                        hflag = 1
                                elif(i.lower() == "<a>" or i.lower() == "</a>" ):
                                        hid = 2
                                        hflag = 1
                                elif(len(i) > 3 and i[len(i)-1] == '>'):
                                        if(i.lower()[0] == '<' and i.lower()[1] == 'h' and i[2].isdigit()):
                                                hid = 3
                                                hflag = 1

                        if (hflag == 1):
                                
                                smlst = [oentry[2], i, count, hid]                        
                                biglst.append(smlst)              
                                count += 1
                        else:
                                if(checkword(i) == 0):
                                        count += 1
                                        continue
                                
                                smlst = [oentry[2], i, count, hid]                        
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


