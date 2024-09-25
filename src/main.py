import os
import re

class AutoSpacer:
    def addSpacesToString(filename: str) -> str:
        return re.sub(r"(?<=\w)([A-Z])", r" \1", filename)
    
def main():
    folderPath = os.getcwd() + "/"
    for filename in os.listdir(folderPath):
        if filename == "main.py":
            print("Ignoring python script file.")
            return
        newFileName = AutoSpacer.addSpacesToString(filename)
        os.rename(folderPath+filename, folderPath+newFileName)
        print("Renamed file: \"" + filename + "\" to: \"" + newFileName + "\"")

if __name__ == '__main__':
    main()