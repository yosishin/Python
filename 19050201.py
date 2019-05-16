import os

try:
    os.mkdir('c:\\users\\hackeru\\desktop\\newDir')
except:
    pass

os.listdir('c:\\users\\hackeru\\desktop\\newDir')

print os.path.exists('c:\\users\\hackeru\\desktop\\newDir')
