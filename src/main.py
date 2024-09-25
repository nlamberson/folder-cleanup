import os
import re

class AutoSpacer:
    def addSpacesToString(filename: str) -> str:
        name, extenstion = os.path.splitext(filename)[0], os.path.splitext(filename)[1]

        # Remove any underscores used for spaces
        name = name.replace("_", "")

        # Regex split the filename itself then add the extension back onto it
        return re.sub(r"(?<=\w)([A-Z0-9])", r" \1", name) + extenstion
    
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