import urllib
#uWord = str(raw_input("Enter word to translate: "))

ufile=urllib.urlopen("https://www.morfix.co.il/dog")
text = ufile.readlines()

print text

printNext=0

for line in text:
        if printNext== 1:
                ans = line.split("<")[0]
                print ans.decode('utf-8')[::-1]
                printNext=0
        if "normal_translation_div" in line:
            printNext=1