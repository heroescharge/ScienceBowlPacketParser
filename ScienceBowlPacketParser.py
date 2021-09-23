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
        

splitApartPages(organizedPacket)
for page in organizedPacket:
    print(page)
    print("\n\n\n")
