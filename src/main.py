import os
import re

class AutoSpacer:
    def addSpacesToString(filename: str) -> str:
        splitFilename = os.path.splitext(filename)

        # Remove any underscores used for spaces
        splitFilename[0].replace("_", "")

        # Regex split the filename itself then add the extension back onto it
        return re.sub(r"(?<=\w)([A-Z0-9])", r" \1", splitFilename[0]) + splitFilename[1]
    
def main():
    folderPath = os.getcwd() + "/"
    for filename in os.listdir(folderPath):
        if filename == "main.py":
            print("Ignoring python script file.")
            continue
        newFileName = AutoSpacer.addSpacesToString(filename)
        os.rename(folderPath+filename, folderPath+newFileName)
        print("Renamed file: \"" + filename + "\" to: \"" + newFileName + "\"")

if __name__ == '__main__':
    main()