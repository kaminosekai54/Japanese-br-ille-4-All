import unicodedata
import json
from dataManager import *



def translateHiraganaToRomaji(input, output):

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
                    print("eventuelle caracter special")
                    # checking if we have a composed symbol
                    if c+1 < len(line) and not line[c+1]  in ponctuation:
                        print(unicodedata.name(line[c+1]))
                        print("caracter suivant peu correspondre")
                        found = False
                        print(line[c+1])
                        print(unicodedata.name(line[c+1]))
                        #  Looping into our eventual list of composed symbol
                        for dic in specialChar[charName][0]:
                            print(dic)
                            if unicodedata.name(line[c + 1]) in dic.keys():
                                found = True
                                # print("association trouver")
                                transcriptedLine += dic[unicodedata.name(line[c+1])]
                                # print(transcriptedLine)
                                c += 2

                        if found == False:
                            if charName in HiraganasToRomaji.keys():
                                # print("hiragana trouver, char aucune correspondance special trouver")
                                transcriptedLine += HiraganasToRomaji[charName]
                                # print(transcriptedLine)
                                c+=1

                            elif charName in KatakanasToRomaji.keys():
                                # print("hiragana trouver, char aucune correspondance special trouver")
                                transcriptedLine += KatakanasToRomaji[charName]
                                # print(transcriptedLine)
                                c+= 1


# If  the special char seams to not be a composed symbol

# check if its an Hiraganas
                    elif charName in HiraganasToRomaji.keys():
                        # print("simple hiraganas après  special")
                        transcriptedLine += HiraganasToRomaji[charName]
                        # print(transcriptedLine)
                        c+=1

# Check if its a Katakanas



                    elif charName in KatakanasToRomaji.keys():
                        # print("simple hiraganas après  special")
                        transcriptedLine += KatakanasToRomaji[charName]
                        # print(transcriptedLine)
                        c+=1

# The char isn't a special char
# Check if its a Hiraganas
                elif charName in HiraganasToRomaji.keys():
                    # print("simple hiraganas")
                    transcriptedLine += HiraganasToRomaji[charName]
                    # print(transcriptedLine)
                    c+=1

# Check if its a Katakanas

                elif charName in KatakanasToRomaji.keys():
                    # print("simple hiraganas")
                    transcriptedLine += KatakanasToRomaji[charName]
                    # print(transcriptedLine)
                    c+=1
                else:
                    # print("correspond a rien de connu")
                    c+=1

            new_file.write('input : \n %s\n'%(line))   
            new_file.write('output : \n %s\n'%(transcriptedLine))   
        new_file.close()



def translateHiraganaToBraille(input, output):
    with open(input, encoding="utf8") as fileobj:
        new_file = open(output, 'w', encoding="utf-8")

        for line in fileobj:
            
            line = line.replace("\n","")
            print(line)
            transcriptedLine = ""
            c = 0
            while c < len(line):
                char = line[c]
                charName = unicodedata.name(char, "?")
                if charName == "?":
                    transcriptedLine+= "?"
                    c+=1
                if char in ponctuation:
                    transcriptedLine += char
                    # print("passe dans ponctuation")
                    # print(transcriptedLine)
                    c+=1

                elif charName in specialChar.keys():
                    # print("eventuelle caracter special")
                    if c+1 < len(line) and not line[c+1]  in ponctuation:
                        # print("caracter suivant peu correspondre")
                        found = False
                        # print(line[c+1])
                        # print(unicodedata.name(line[c+1]))
                        for dic in specialChar[charName][1]:
                            # print(dic)
                            if unicodedata.name(line[c+1]) in dic.keys():
                                found = True
                                # print("association trouver")
                                transcriptedLine += dic[unicodedata.name(line[c+1])]
                                # print(transcriptedLine)
                                c += 2

                        if found == False:
                            if charName in HiraganasToBraille.keys():
                                # print("hiragana trouver, char aucune correspondance special trouver")
                                transcriptedLine += HiraganasToBraille[charName]
                                # print(transcriptedLine)
                                c+=1


                    elif charName in HiraganasToBraille.keys():
                        # print("simple hiraganas après  special")
                        transcriptedLine += HiraganasToBraille[charName]
                        # print(transcriptedLine)
                        c+=1


                elif charName in HiraganasToBraille.keys():
                    # print("simple hiraganas")
                    transcriptedLine += HiraganasToBraille[charName]
                    # print(transcriptedLine)
                    c+=1

                else:
                    # print("correspond a rien de connu")
                    c+=1

            print(transcriptedLine)
            new_file.write('input : \n %s\n'%(line))   
            new_file.write('ouput : \n %s\n'%(transcriptedLine))     
        new_file.close()

translateHiraganaToRomaji("exemple.txt", "result.txt")
# translateHiraganaToBraille("exemple.txt", "result1.txt")