#Potential changes:
#When finding page number, keep searching until no integer is found instead of when a space is found

#Layer order of array: page number, 
organizedPacket = []

with open("15A_MS_Reg_2016.txt") as questionPacket:
    contents = questionPacket.readlines()

#Returns string starting from inputted index until it finds the endstring NOT including the endstring but including the startIndex
#Ex. readUntilString("hello world, how is it going", 2, "rld") returns "llo wo"
def readUntilString(sentence, startIndex, endString):
    iterate = 0
    word = ""
    endIndex = sentence.find(endString, startIndex)
    if (endIndex >= 0):
        return sentence[startIndex:endIndex] #return substring between the two indices
    else:
        return "NOTFOUND" #If endString not found
   
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

    def __init__ (self, roundNumber, pageNumber, questionNumber, questionTypeA, questionTypeB, questionCategory, questionText, questionAnswer):
        self.roundNumber = roundNumber
        self.pageNumber = pageNumber
        self.questionNumber = questionNumber
        self.questionTypeA = questionTypeA
        self.questionTypeB = questionTypeB
        self.questionCategory = questionCategory
        self.questionText = questionText
        self.questionAnswer = questionAnswer

for i in range(0,len(contents)):
    #Check if it is toss-up question
    newQuestion = Question(0, 0, 0, "", "", "", "", "")
    #print(contents[i])
    if ("TOSS-UP" in contents[i]):
        newQuestion.questionTypeA = "TOSS-UP"
    elif ("BONUS" in contents[i]):
        newQuestion.questionTypeA = "BONUS"
    if newQuestion.questionTypeA == "TOSS-UP" or newQuestion.questionTypeA == "BONUS":
        print(newQuestion.questionTypeA)
        newQuestion.questionNumber = contents[i+1][0]
        print(newQuestion.questionNumber)
        newQuestion.questionCategory = readUntilString(contents[i+1], 3, "–")
        print(newQuestion.questionCategory)
        startIndexOfQuestionType = contents[i+1].find("–") + 2#Assumes first hyphen is after category name, +2 accounts for space after hypen
        if (contents[i+1][startIndexOfQuestionType:startIndexOfQuestionType+15] == "Multiple Choice"): #There are 15 char in "Multiple Choice"
            newQuestion.questionTypeB = "Multiple Choice"
            print(newQuestion.questionTypeB)
            fullQuestion = contents[i+1] + contents[i+2] + contents[i+3] + contents[i+4] + contents[i+5]
            newQuestion.questionText = readUntilString(fullQuestion,startIndexOfQuestionType+15,"ANSWER")
            print(newQuestion.questionText)
            newQuestion.questionAnswer = fullQuestion[fullQuestion.find("Answer"):]
            print(newQuestion.questionAnswer)
        else:
            newQuestion.questionTypeB = "Short Answer"
            print(newQuestion.questionTypeB)
            newQuestion.questionText = readUntilString(contents[i+1] + contents[i+2],startIndexOfQuestionType+12,"ANSWER")
            print(newQuestion.questionText)
            newQuestion.questionAnswer = contents[i+2]
            print(newQuestion.questionAnswer)
        questions.append(newQuestion)
        print("\n\n")


