
#OBJECT-----------------------------------------------------------------------------------------------------------------------------------------------------------
class File:

    import csv
    import os
    
    #Initializing / Instance Attributes (CONSTRUCTOR)
    def __init__(self, test):
        self.test = test
            
    def fileNames(self):
        global file1
        global file2#pgw
        global file3#tn
        global file4#jems
        global answer
        
        answer = input("Choose from the following options and type the number for your selection. Press enter when ready.:\n(1)- Run analysis for PGW, TouchNet, and JEMS users\n(2)- Run analysis for PGW\n(3)- Run analysis for TouchNet\n(4)- Run analysis for JEMS\n> ")#(5)- Run analysis for FAME\n> ") 
        if answer == '1':
            file1 = input("\nEnter the file name for ServiceLink Terminations:(HAS TO INCLUDE THE END: '.csv.txt')\n(press enter when ready): ")
            file2 = input("Enter the file name for PGW: (HAS TO INCLUDE THE END: '.csv.txt')\n(press enter when ready): ")
            file3 = input("Enter the file name for TouchNet: (HAS TO INCLUDE THE END: '.csv.txt')\n(press enter when ready): ")
            file4 = input("Enter the file name for JEMS: (HAS TO INCLUDE THE END: '.csv.txt')\n(press enter when ready): ")
            #file5 = input("Enter the file name for FAME: (HAS TO INCLUDE THE END: '.csv.txt')\n(press enter when ready): ")
            return int(answer)
        if answer == '2':
            file1 = input("\nEnter the file name for ServiceLink Terminations:(HAS TO INCLUDE THE END: '.csv.txt')\n(press enter when ready): ")
            file2 = input("Enter the file name for PGW: (HAS TO INCLUDE THE END: '.csv.txt')\n(press enter when ready): ")
            return int(answer)
        elif answer == '3':
            file1 = input("\nEnter the file name for ServiceLink Terminations:(HAS TO INCLUDE THE END: '.csv.txt')\n(press enter when ready): ")
            file3 = input("Enter the file name for TouchNet: (HAS TO INCLUDE THE END: '.csv.txt')\n(press enter when ready): ")
            return int(answer)
        elif answer == '4':
            file1 = input("\nEnter the file name for ServiceLink Terminations:(HAS TO INCLUDE THE END: '.csv.txt')\n(press enter when ready): ")
            file4 = input("Enter the file name for JEMS: (HAS TO INCLUDE THE END: '.csv.txt')\n(press enter when ready): ")
            return int(answer)
        else:
            return answer

    def parsing_of_doc(self, file):
    
        data = file.read()
        
        data2 = data.split('\n')

        hold = []

        skip = 0 
        for line in data2:
            skip += 1
            if skip == 1: #This is because of weird tranlation of data and weird encoding appearing on the first line
                pass
            else:
                datasplit = line.split('\t')
                hold.append(datasplit)
        return hold

    def nthOccur(self, n, searchString, theString): #This method is to find the nth occurence of a substring in a string
        return len(searchString.join(theString.split(searchString,n)[:n]))
        
   #---------------------------------------------------------------------------------------------FORMATTING DOCUMENTS----------------------------------------------------------------- 
    def serviceLinkFormat(self):
        doc = open('J:\FSM\Maria Restrepo\PROGRAMS\TERMINATIONS PROGRAM\ServiceLink\\'+file1)
        global SLfinaldoc 
        SLfinaldoc = self.parsing_of_doc(doc) #returning parsed data as a list 
        return SLfinaldoc
        doc.close()
        

    def pgwFormat(self):
        doc = open('J:\FSM\Maria Restrepo\PROGRAMS\TERMINATIONS PROGRAM\PGW\\'+file2)
        global PGWfinaldoc
        PGWfinaldoc = self.parsing_of_doc(doc) #returning parsed data as a list
        return PGWfinaldoc
        doc.close()
        
    def touchNetFormat(self):
        doc = open('J:\FSM\Maria Restrepo\PROGRAMS\TERMINATIONS PROGRAM\Touchnet\\'+file3)
        global TNfinaldoc
        TNfinaldoc = self.parsing_of_doc(doc) #returning parsed data as a list// Calling method within method (self. is calling parsing_of_doc method with a reference to the class object)
        return TNfinaldoc
        doc.close()
    
    def jemsFormat(self):
        doc = open('J:\FSM\Maria Restrepo\PROGRAMS\TERMINATIONS PROGRAM\JEMS\\'+file4)
        global Jfinaldoc
        Jfinaldoc = self.parsing_of_doc(doc) #returning parsed data as a list
        return Jfinaldoc
        doc.close()

    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------FILE COMPARISON----------------------------------------------------------------
    def SLcomparison(self):
        global slNames
        slNames = []

        global descrip
        descrip =[]

        global date
        date = input("\nEnter today's date (MM-DD-YY), it will be added to the end of the files created. (press enter when ready): ")
        
        doc = open('J:\FSM\Maria Restrepo\PROGRAMS\TERMINATIONS PROGRAM\W NUMBERS\\W Names'+date+'.csv.txt','w',encoding='utf8')
        doc.write("In the file exported from ServiceLink ...\nThese lines do not have an N number.\n")

        #GETTING THE NAMES OUT FROM THE SERVICELINK FILE 
        for row in SLfinaldoc:
            try:
                nIndex = row[10].find('N')
                processedIndex = row[10].find('Processed')

                if (nIndex == -1): #-1 means not found
                    doc.write(row[10]+'\n')
                    try:
                        
                        fourthSpace = self.nthOccur(4,' ', row[10])
                        sixthSpace = self.nthOccur(6, ' ',row[10])
##                        print(row[10][fourthSpace+1:sixthSpace])
                    
                    except:
                        print("An exception was raised and it wasn't because the person had a W number.")
                    else:
                        slNames.append(row[10][fourthSpace+1:sixthSpace])#ADDING NAMES WITH W NUMBERS TO THE LIST THAT IS BEING RETURNED
                else:
                    slNames.append(row[10][nIndex+10:processedIndex-1])
                    #print(row[10][nIndex+10:processedIndex-1])
            except:
                pass ##AN EXCEPTION WILL RISE BUTS IT B/C THE LAST LINE IN THE FILE IS BLANK SO IT WILL SAY OUT OF RANGE FOR ROW[10]

##        for row in slNames:
##            print(row)

        #GETTING THE TERMINATION DESCRIPTION FROM THE SERVICELINK FILE
        for row in SLfinaldoc:
            try:
                descrip.append(row[10])

            except:
                if row[0] == '':
                    pass
                else:
                    print("Issue raised in SLcomparison.")

##        for row in descrip:
##            print(row)
        
                    
    def PGWcomparison(self):
        global pgwNames
        pgwNames = []

        global pgwNetID
        pgwNetID = []
        
        #GETTING THE NAMES OUT FROM THE PGW FILE 
        for row in PGWfinaldoc:
            try:
                parenIndex1 = row[0].find('(')
                parenIndex2 = row[0].find(')')
                
##                print(row)
##                print("index:"+str(parenIndex))
                if parenIndex1 == -1 or parenIndex2 == -1:
                    pass
                else:
                    pgwNames.append(row[0][0:parenIndex1])
                    pgwNetID.append(row[0][parenIndex1+2:parenIndex2-1])
   
            except:
                if (row[0] == ''): 
                    #THE LAST LINE IS EMPTY SO THIS TAKES CARE OF THE EXCEPTION IT RAISES
                    #print("None")
                    pass
                else:
                    print("Error raised in function PGWcomparison. (1)")                 
              
##        for row in pgwNames:
##            print(row)


    def TNcomparison(self):
        global tnNames
        tnNames = []

        global tnNetID
        tnNetID = []
        
        #print('TN')
        
        for row in TNfinaldoc:
            try:  
                if (row[7] == "Disabled" or row[1] == ''): #THERE ARE ROWS WITH NO NAMES AND THOSE ARE ALWAYS DISACTIVE
                    pass

                else:
                    join = row[-8]+" "+row[1]#join names
                    tnNames.append(join) #add names to tnNames list
                
                    try:
                        atSignIndex = row[9].find('@')#find @ sign in email column
                        
                        if (atSignIndex == -1):
                            pass #I checked, those that don't have emails don't have names.It is blank
                        
                        else: #if there is an @ sign then add the substring that has the netid to the tnNetId list
                            tnNetID.append(row[9][0:atSignIndex])
                            
                    except:
                        print("Could not find @")
            except:
                if row[0] == '':
                    pass #EXCEPTION FOR LAST ROW BECAUSE ITS BLANK || INDEX IS 0 BECAUSE IN AN EMPTY ROW THE EMPTINESS WILL BE INDEX 0 ->['']
                else:
                    print(row)
                    print("Error raised in TN comparison.")
            
##        for row in tnNames:
##            print(row)
        
    
    def JEMScomparison(self):
        global jemsNames
        jemsNames = []

        global jemsNetID
        jemsNetID = []
        
        for row in Jfinaldoc:
            try:
                jemsNames.append(row[1])
                jemsNetID.append(row[0])
                
            except:
                if row[0] == '': #EXCEPTION FOR LAST ROW BECAUSE ITS BLANK || INDEX IS 0 BECAUSE IN AN EMPTY ROW THE EMPTINESS WILL BE INDEX 0 ->['']
                    pass
                else:
                    print(row)
                    print("Exception raised in JEMScomparison.") 
    
    def finalComparison(self):
        global finalDocument
        global finalList
        finalList = []
        finalDocName = 'J:\FSM\Maria Restrepo\PROGRAMS\TERMINATIONS PROGRAM\TerminationsToBeDone\\Terminations To Be Done '+date+'.csv.txt'

        finalDocument = open(finalDocName,'w',encoding='utf8')
        #finalDocument.write("Name"+'\t'+"Net ID"+'\t'+"Termination Notice"+'\t'+'System'+'\n')
        finalDocumentList = []
        if int(answer) == 1:

            for row in pgwNames: 

                index_of_person_pgw = pgwNames.index(row)#getting index of name in pgwNames so I can then use it to get the netID from the pgwNetID list

                if row in slNames: #FOR NAME IN PGWNAMES, IF IT IS IN SERVICELINK PARSED LIST THEN FLAG IT BECAUSE IT SHOULDNT BE THERE, THEY SHOULD BE TERMINATED
                    #print(row)
                    finalList.append(row)
                    index_of_terminated_person = slNames.index(row)#getting index of name found in pgwNames in the slNames list
                    finalDocument.write(row+'\t'+pgwNetID[index_of_person_pgw]+'\t'+descrip[index_of_terminated_person]+'\t'+'Payment Gateway'+'\n')
            
            for row in tnNames: 

                index_of_person_tn = tnNames.index(row)#getting index of name in tnNames so I can then use it to get the netID from the tnNetID list
                
                if row in slNames: #FOR NAME IN TNNAMES, IF IT IS IN SERVICELINK THEN FLAG IT BUT MAKE SURE IT ISNT ALREADY THERE, TO AVOID DUPLICATES 
                    if row in finalList: #FINAL LIST IS A LIST OF THE NAMES IN THE FILE ITSELF. ITS A COPY OF THE DATA BUT IT IS EASIER TO COMPARE EQUALITY USING LISTS. SO HERE WE ARE AVOINDING DUPLICATES. 
                        pass
                        
                    else:
                        index_of_terminated_person = slNames.index(row)#getting index of name found in tnNames in the slNames list
                        finalDocument.write(row+'\t'+tnNetID[index_of_person_tn]+'\t'+descrip[index_of_terminated_person]+'\t'+'TouchNet'+'\n')
            
            for row in jemsNames:

                index_of_person_jems = jemsNames.index(row)#getting index of name in jemsNames so I can then use it to get the netID from the jemsNetID list
                        
                if row in slNames:
                    if row in finalList:
                        pass
                        
                    else:
                        index_of_terminated_person = slNames.index(row)#getting index of name found in jemsNames in the slNames list
                        finalDocument.write(row+'\t'+jemsNetID[index_of_person_jems]+'\t'+descrip[index_of_terminated_person]+'\t'+'Jems'+'\n')
                            
            print("\nAll Done!")
            finalDocument.close()
            
        elif int(answer) == 2:
            for row in pgwNames: 

                index_of_person_pgw = pgwNames.index(row)#getting index of name in pgwNames so I can then use it to get the netID from the pgwNetID list

                if row in slNames:
                    #print(row)
                    finalList.append(row)
                    index_of_terminated_person = slNames.index(row)#getting index of name found in pgwNames in the slNames list
                    #finalDocument.write(row+'\t'+pgwNetID[index_of_person_pgw]+'\t'+descrip[index_of_terminated_person]+'\t'+'Payment Gateway'+'\n')
                    
            print("\nAll Done!")
            finalDocument.close()
            
        elif int(answer) == 3:
            for row in tnNames:
                
                index_of_person_tn =tnNames.index(row)#getting index of name in tnNames so I can then use it to get the netID from the tnNetID list
                
                if row in slNames:
                    if row in finalList: #FINAL LIST IS A LIST OF THE NAMES IN THE FILE ITSELF. ITS A COPY OF THE DATA BUT IT IS EASIER TO COMPARE EQUALITY USING LISTS. SO HERE WE ARE AVOINDING DUPLICATES. 
                        pass
                    else:
                        finalList.append(row)
                        index_of_terminated_person = slNames.index(row)#getting index of name found in tnNames in the slNames list
                        finalDocument.write(row+'\t'+tnNetID[index_of_person_tn]+'\t'+descrip[index_of_terminated_person]+'\t'+'TouchNet'+'\n')
                        
                        
            print("\nAll Done!")
            finalDocument.close()

        elif int(answer) == 4:
            for row in jemsNames: 

                index_of_person_jems = jemsNames.index(row)#getting index of name in jemsNames so I can then use it to get the netID from the jemsNetID list

                if row in slNames:
                    #print(row)
                    finalList.append(row)
                    index_of_terminated_person = slNames.index(row)#getting index of name found in jemsNames in the slNames list
                    finalDocument.write(row+'\t'+jemsNetID[index_of_person_jems]+'\t'+descrip[index_of_terminated_person]+'\t'+'Jems'+'\n')
                                           
            print("\nAll Done!")
            finalDocument.close()

        else:
            print("here")
            
        
#-------------------------------------------------------------PROGRAM-----------------------------------------------------------------------------------------
test = File("test")
usersChoice = test.fileNames()
try:
    if (usersChoice == 1): #ALl SYSTEMS
        test.serviceLinkFormat()
        test.SLcomparison()
        test.pgwFormat()
        test.PGWcomparison()
        test.touchNetFormat()
        test.TNcomparison()
        test.jemsFormat()
        test.JEMScomparison()
        test.finalComparison()
        
    elif (usersChoice == 2): #PGW
        test.serviceLinkFormat()
        test.SLcomparison()
        test.pgwFormat()
        test.PGWcomparison()
        test.finalComparison()
        
    elif (usersChoice == 3): #TN 
        test.serviceLinkFormat()
        test.SLcomparison()
        test.touchNetFormat()
        test.TNcomparison()
        test.finalComparison()

    elif (usersChoice == 4): #JEMS
        test.serviceLinkFormat()
        test.SLcomparison()
        test.jemsFormat()
        test.JEMScomparison()
        test.finalComparison()
    
    else:
            print("Invalid Response. Please try again.")
