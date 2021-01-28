import unicodedata
import json
from dataManager import *



def translateKanasToRomaji(input, output):

    # Loading the usefull dict
    ponctuation = loadData("ponctuation.json")
    specialChar = loadData("specialChar.json")
    HiraganasToRomaji = loadData("HiraganasToRomaji.json")
    KatakanasToRomaji = loadData("KatakanasToRomaji.json")

    # opening the file to read, and the file we gonna write in
    with open(input, encoding="utf8") as fileobj:
        new_file = open(output, 'w', encoding="utf-8")
        # Looping over each line of the file
        for line in fileobj:
            # cutting the endLine character indicator to avoid errors
            line = line.replace("\n","")
            #  Creating variables to store the transcription, and the current index of the char we want to translate
            transcriptedLine = ""
            c = 0
            #  Looping over our line until we reach the last characters
            while c < len(line):

                # Getting the current character and its Unicode Value
                # If no Unicode Value exist, the char will be "?"
                char = line[c]
                charName = unicodedata.name(char, "?")

                if charName == "?":
                    transcriptedLine+= "?"
                    c+=1

# Checking if the current char isn't a ponctuation symbol
                if char in ponctuation:
                    transcriptedLine += char
                    c+=1

# checking if the current char is a special char (composed symbole etc, etc)
                elif charName in specialChar.keys():
                    # checking if we have a composed symbol
                    if c+1 < len(line) and not line[c+1]  in ponctuation:
                        found = False
                        foundedDict = {}
                        #  Looping into our eventual list of composed symbol
                        for dict in specialChar[charName][0]:
                            if unicodedata.name(line[c+1]) in dict.keys():
                                found = True
                                foundedDict = dict

                        if found == True:
                            transcriptedLine += foundedDict[unicodedata.name(line[c+1])]
                            c += 2

                        elif found == False:
                            if charName in HiraganasToRomaji.keys():
                                transcriptedLine += HiraganasToRomaji[charName]
                                c+=1

                            elif charName in KatakanasToRomaji.keys():
                                transcriptedLine += KatakanasToRomaji[charName]
                                # print(transcriptedLine)
                                c+= 1


# If  the special char seams to not be a composed symbol
# check if its an Hiraganas
                    elif charName in HiraganasToRomaji.keys():
                        transcriptedLine += HiraganasToRomaji[charName]
                        c+=1

# Check if its a Katakanas
                    elif charName in KatakanasToRomaji.keys():
                        transcriptedLine += KatakanasToRomaji[charName]
                        c+=1

# The char isn't a special char
# Check if its a Hiraganas
                elif charName in HiraganasToRomaji.keys():
                    transcriptedLine += HiraganasToRomaji[charName]
                    c+=1

# Check if its a Katakanas
                elif charName in KatakanasToRomaji.keys():
                    transcriptedLine += KatakanasToRomaji[charName]
                    c+=1
                else:
                    # print("correspond a rien de connu")
                    c+=1

            new_file.write('input : \n %s\n'%(line))   
            new_file.write('output : \n %s\n'%(transcriptedLine))   
        new_file.close()





def translateKanasToJapaneseBraille(input, output):

    # Loading the usefull dict
    ponctuation = loadData("ponctuation.json")
    specialChar = loadData("specialChar.json")
    HiraganasToBraille = loadData("HiraganasToBraille.json")
    KatakanasToBraille = loadData("KatakanasToBraille.json")

    # opening the file to read, and the file we gonna write in
    with open(input, encoding="utf8") as fileobj:
        new_file = open(output, 'w', encoding="utf-8")
        # Looping over each line of the file
        for line in fileobj:
            # cutting the endLine character indicator to avoid errors
            line = line.replace("\n","")
            # print(line)
            #  Creating variables to store the transcription, and the current index of the char we want to translate
            transcriptedLine = ""
            c = 0
            #  Looping over our line until we reach the last characters
            while c < len(line):

                # Getting the current character and its Unicode Value
                # If no Unicode Value exist, the char will be "?"
                char = line[c]
                charName = unicodedata.name(char, "?")

                if charName == "?":
                    transcriptedLine+= "?"
                    c+=1

# Checking if the current char isn't a ponctuation symbol
                if char in ponctuation:
                    transcriptedLine += char
                    # print("passe dans ponctuation")
                    # print(transcriptedLine)
                    c+=1

# checking if the current char is a special char (composed symbole etc, etc)
                elif charName in specialChar.keys():
                    # checking if we have a composed symbol
                    if c+1 < len(line) and not line[c+1]  in ponctuation:
                        found = False
                        foundedDict = {}
                        #  Looping into our eventual list of composed symbol
                        for dict in specialChar[charName][1]:
                            if unicodedata.name(line[c+1]) in dict.keys():
                                found = True
                                foundedDict = dict

                        if found == True:
                            transcriptedLine += foundedDict[unicodedata.name(line[c+1])]
                            c += 2

                        elif found == False:
                            if charName in HiraganasToBraille.keys():
                                transcriptedLine += HiraganasToBraille[charName]
                                c+=1

                            elif charName in KatakanasToBraille.keys():
                                transcriptedLine += KatakanasToBraille[charName]
                                c+= 1


# If  the special char seams to not be a composed symbol
# check if its an Hiraganas
                    elif charName in HiraganasToBraille.keys():
                        transcriptedLine += HiraganasToBraille[charName]
                        c+=1

# Check if its a Katakanas
                    elif charName in KatakanasToBraille.keys():
                        transcriptedLine += KatakanasToBraille[charName]
                        c+=1

# The char isn't a special char
# Check if its a Hiraganas
                elif charName in HiraganasToBraille.keys():
                    transcriptedLine += HiraganasToBraille[charName]
                    c+=1

# Check if its a Katakanas
                elif charName in KatakanasToBraille.keys():
                    transcriptedLine += KatakanasToBraille[charName]
                    c+=1
                else:
                    # print("correspond a rien de connu")
                    c+=1

            new_file.write('input : \n %s\n'%(line))   
            new_file.write('output : \n %s\n'%(transcriptedLine))   
        new_file.close()




translateKanasToRomaji("exemple.txt", "result.txt")
translateKanasToJapaneseBraille("exemple.txt", "result1.txt")