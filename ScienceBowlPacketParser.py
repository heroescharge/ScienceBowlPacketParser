#Potential changes:
#When finding page number, keep searching until no integer is found instead of when a space is found
#Using arbitrary number of lines to parse for question statement is not a great way to do it


#ISSUES:
#Small issues:
#15A_MS_Reg_2016 Q6 Toss up: Option W is not on a separate line,the word "bonus" from the next question is put into the answer
#15A_MS_Reg_2016 Q11 Bonus: ~~~ separator line gets pooled in with answer because option W is not on a separate line
#LARGE issues:
#15A_MS_Reg_2016 Q23 Bonus: ANSWER is on same line as question statement, doesnt get assigned to answer

#Assumptions:
#Question number always followed by parentheses ")"
#Answer to question is on its own line


#Layer order of array: page number, 
organizedPacket = []
questions = []

with open("9A_MS_Reg_2016.txt") as questionPacket:
    contents = questionPacket.readlines()

#Returns string starting from inputted index until it finds the endstring NOT including the endstring but including the startIndex, overloaded version takes in a list of strings to stop at
#Ex. readUntilString("hello world, how is it going", 2, "rld") returns "llo wo"
def readUntilString(sentence, startIndex, endString):
    iterate = 0
    word = ""
    endIndex = sentence.find(endString, startIndex)
    if (endIndex >= 0):
        return sentence[startIndex:endIndex] #return substring between the two indices
    else:
        return "NOT FOUND" #If endString not found

#Divies packet by page numbers
def splitApartPages(organizedPacket):
    pageNumber = 1 #Start with page 1
    for i in range(len(contents)):
        pageIndex = contents[i].find("Page")
        if (pageIndex >= 0):
            iterator = 0
            pageNumber = int(readUntilString(contents[i], pageIndex+5, " ")) #Add 5 to pageIndex to start from the number itself (Ex. Page 4, 4 is 5 indices after 'P'), search until a space is found
        if (len(organizedPacket) >= pageNumber):
            organizedPacket[pageNumber-1].append(contents[i])
        else: #If we need a new page to be added
            organizedPacket.append([contents[i]])
        
'''
splitApartPages(organizedPacket)
for page in organizedPacket:
    print(page)
    print("\n\n\n")
'''
class Question:
    roundNumber = 0
    pageNumber = 0
    questionNumber = 0
    #First is bonus/toss up, second is mcq/short answer
    questionTypeA = ""
    questionTypeB = ""
    questionCategory = ""
    questionText = ""
    questionAnswer = ""

    def __str__ (self):
        s = ("Question number: " +  self.questionNumber + "\n" +
            "Toss-up or bonus?: " + self.questionTypeA + "\n" +
            "MCQ or Short-answer?: " + self.questionTypeB + "\n" +
            "Question Category: " + self.questionCategory + "\n" +
            "Question: " + self.questionText + "\n" +
            self.questionAnswer + "\n")
        return s
       

    def __init__ (self, roundNumber, pageNumber, questionNumber, questionTypeA, questionTypeB, questionCategory, questionText, questionAnswer):
        self.roundNumber = roundNumber
        self.pageNumber = pageNumber
        self.questionNumber = questionNumber
        self.questionTypeA = questionTypeA
        self.questionTypeB = questionTypeB
        self.questionCategory = questionCategory
        self.questionText = questionText
        self.questionAnswer = questionAnswer

def createQuestionArray(contents):
    questions = []
    for i in range(0,len(contents)):
        #Check if it is toss-up question
        newQuestion = Question(0, 0, 0, "", "", "", "", "") # Reset the class we will append
        #print(contents[i])
        if ("TOSS-UP" in contents[i]):
            newQuestion.questionTypeA = "TOSS-UP"
        elif ("BONUS" in contents[i]):
            newQuestion.questionTypeA = "BONUS"
        if newQuestion.questionTypeA == "TOSS-UP" or newQuestion.questionTypeA == "BONUS":
            #print(newQuestion.questionTypeA)
            newQuestion.questionNumber = readUntilString(contents[i+1], 0, ")")
            #print(newQuestion.questionNumber)
            newQuestion.questionCategory = readUntilString(contents[i+1], 3, "–")
            #print(newQuestion.questionCategory)
            startIndexOfQuestionType = contents[i+1].find("–") + 2#Assumes first hyphen is after category name, +2 accounts for space after hypen
            if (contents[i+1][startIndexOfQuestionType:startIndexOfQuestionType+15] == "Multiple Choice"): #There are 15 char in "Multiple Choice"
                newQuestion.questionTypeB = "Multiple Choice"
                #print(newQuestion.questionTypeB)
                fullQuestion = ""
                for k in range(1,7):#No reason to do (1,7), just trying to get enough lines to encompass whole question
                    fullQuestion += contents[i+k]
                newQuestion.questionText = readUntilString(fullQuestion,startIndexOfQuestionType+15,"ANSWER")
                #print(newQuestion.questionText)
                newQuestion.questionAnswer = fullQuestion[fullQuestion.find("ANSWER"):]
                #print(newQuestion.questionAnswer) 
            else:
                newQuestion.questionTypeB = "Short Answer"
                #print(newQuestion.questionTypeB)
                fullQuestion = ""
                for k in range(min(1,len(contents)-i-1),min(4,len(contents)-i-1)):#No reason to do (1,4), just trying to get enough lines to encompass whole question
                    fullQuestion += contents[i+k]
                newQuestion.questionText = readUntilString(fullQuestion,startIndexOfQuestionType+12,"ANSWER")
                #print(newQuestion.questionText)
                for k in range(i+2, len(contents)):
                    if ("ANSWER" in contents[k]):
                        newQuestion.questionAnswer = contents[k]
                        break
                #print(newQuestion.questionAnswer)
            questions.append(newQuestion)
            #print("\n\n")
            
    return questions

questions = createQuestionArray(contents)
for q in questions:
    print(q)




