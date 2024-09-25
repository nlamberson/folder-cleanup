# Folder Cleanup Python Script

This was a personal project used to cleanup some folders with weird filenames on my PC.

This script will separate words found in a filename if the word starts with a capital letter.

## How to Run

To run the script, download the main.py file and put it into a directory that you want to edit filenames for.

Provided you have Python installed, simply open the folder in a terminal of your choice and run the following command

``` shell
python main.py
```

You should see the following output (based on the example files) for example:

``` shell
Renamed file: "textImage.PNG" to: "text Image.PNG"
Renamed file: "testFileEdit.txt" to: "test File Edit.txt"
Renamed file: "ThisIsAFilePlzRename.txt" to: "This Is A File Plz Rename.txt"
Renamed file: "Number3Test2.txt" to: "Number 3 Test 2.txt"
Ignoring python script file.
Renamed file: "test_underscore.txt" to: "testunderscore.txt"
```
