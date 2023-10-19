from deep_translator import GoogleTranslator
from os import listdir
from os.path import isfile, join

# Constants declarations
ORIGINAL_PATH = "engLanguageORG" # Path with the original files in english
RESULT_PATH = "engLanguage" # Path to save the new files in spanish

print("START")

# Get filenames list
filesList = [f for f in listdir(ORIGINAL_PATH) if isfile(join(ORIGINAL_PATH, f))]

# Create translator
translator = GoogleTranslator(source='en', target='es')

# Filename list loop
for fileName in filesList:
    
    # Reading original file in list
    orgFile = open(ORIGINAL_PATH + "\\" + fileName, "r", encoding="utf-8")
    lines = orgFile.readlines()
    # Creating new file with same filename in list
    newFile = open(RESULT_PATH + "\\" + fileName, "w", encoding="utf-8")

    print("Translating file:" + fileName)
    for line in lines:
        # Split original line format 'ENGLISH|JAPANESE'
        splitLine = line.split("|")
        # Translate to spanish and save line in new file
        translateLine = str(translator.translate(splitLine[0])) + "|" + str(splitLine[1]) 
        newFile.write(translateLine)
    orgFile.close()
    newFile.close()

print("END")