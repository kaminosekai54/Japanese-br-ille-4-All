import unicodedata
import json

romaji = []
braille = []
hiraganas = []
katakanas = []
specialChar = {}
ponctuation = [" ", ".", ",", "=", "/", "-","+","*",":",";","?","!", "\n","\\n", "$\n"]
with open("try.txt", encoding="utf8") as fileobj:
# with open("Japanese braille for screen reader.odt") as fileobj:
    for line in fileobj:

        tmpLine = line.split("=")
        if len(tmpLine) > 0:
            romaji.append(tmpLine[0].replace("=", ""))
            braille.append(tmpLine[1].replace("=", "").replace("+", ""))
            hiraganas.append(tmpLine[3].replace("=", ""))
            katakanas.append(tmpLine[4].replace("=", ""))

    HiraganasToRomaji = {}
    HiraganasToBraille = {}
    for indice in range(len(hiraganas)):
        curHiraganaString = hiraganas[indice]

        if len(curHiraganaString) == 1:
            HiraganasToRomaji[unicodedata.name(curHiraganaString)] = romaji[indice]
            HiraganasToBraille[unicodedata.name(curHiraganaString)] = braille[indice]

        elif len(curHiraganaString) == 2:
            if not unicodedata.name(curHiraganaString[0]) in specialChar.keys():
                Romaji = {}
                Braille = {}
                Katakana = {}

                specialChar[unicodedata.name(curHiraganaString[0])] = [[Romaji], [Braille], [Katakana]]
            tmp = {}
            tmp[unicodedata.name(curHiraganaString[1])] = romaji[indice]
            specialChar[unicodedata.name(curHiraganaString[0])][0].append(tmp)
            tmp = {}
            tmp[unicodedata.name(curHiraganaString[1])] = braille[indice]
            specialChar[unicodedata.name(curHiraganaString[0])][1].append(tmp)

    # print(specialChar)
    # print(HiraganasToRomaji)


def translateHiraganaToRomaji(input, output):
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
                        for dic in specialChar[charName][0]:
                            # print(dic)
                            if unicodedata.name(line[c+1]) in dic.keys():
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


                    elif charName in HiraganasToRomaji.keys():
                        # print("simple hiraganas après  special")
                        transcriptedLine += HiraganasToRomaji[charName]
                        # print(transcriptedLine)
                        c+=1


                elif charName in HiraganasToRomaji.keys():
                    # print("simple hiraganas")
                    transcriptedLine += HiraganasToRomaji[charName]
                    # print(transcriptedLine)
                    c+=1

                else:
                    # print("correspond a rien de connu")
                    c+=1

            new_file.write('input : \n %s\n'%(line))   
            new_file.write('ouput : \n %s\n'%(transcriptedLine))   
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

# translateHiraganaToRomaji("exemple.txt", "result.txt")
translateHiraganaToBraille("exemple.txt", "result1.txt")