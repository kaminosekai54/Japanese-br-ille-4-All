import unicodedata
import json

romaji = []
braille = []
hiraganas = []
katakanas = []
specialChar = {}
ponctuation = [" ", ".", ",", "=", "/", "-","+","*",":",";","?","!", "\n","\\n", "$\n"]
with open("try.txt", encoding="utf8") as fileobj:
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


    KatakanasToRomaji = {}
    KatakanasToBraille = {}
    for indice in range(len(katakanas)):
        curKatakanaString = katakanas[indice]

        if len(curKatakanaString) == 1:
            KatakanasToRomaji[unicodedata.name(curKatakanaString)] = romaji[indice]
            KatakanasToBraille[unicodedata.name(curKatakanaString)] = braille[indice]

        elif len(curKatakanaString) == 2:
            if not unicodedata.name(curKatakanaString[0]) in specialChar.keys():
                Romaji = {}
                Braille = {}
                Katakana = {}

                specialChar[unicodedata.name(curKatakanaString[0])] = [[Romaji], [Braille], [Katakana]]
            tmp = {}
            tmp[unicodedata.name(curKatakanaString[1])] = romaji[indice]
            specialChar[unicodedata.name(curKatakanaString[0])][0].append(tmp)
            tmp = {}
            tmp[unicodedata.name(curKatakanaString[1])] = braille[indice]
            specialChar[unicodedata.name(curKatakanaString[0])][1].append(tmp)


def saveData(dict, file):
    data_file = open("./Data/" + file, "w")
    json.dump(dict, data_file)
    data_file.close()

def loadData(file):
    with open("./Data/" + file) as json_file:
        data = json.load(json_file)
        return data


    # data_file = open("./Data/" + file, "r")
    # dict = json.load()
    # print(dict)
    # data_file.close()
    # return dict

def main():
    saveData(HiraganasToBraille, "HiraganasToBraille.json")
    saveData(HiraganasToRomaji, "HiraganasToRomaji.json")
    saveData(KatakanasToBraille, "KatakanasToBraille.json")
    saveData(KatakanasToRomaji, "KatakanasToRomaji.json")
    saveData(specialChar, "specialChar.json")
    saveData(ponctuation, "ponctuation.json")

if __name__ == '__main__':
    main()