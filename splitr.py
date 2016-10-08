# -*- coding: utf-8 -*-
"""
script to take the clipboard's contents and send to a new cbz folder with the
name assigned in the script
[you can grab file paths of selected
files in windows explorer, for windows 7+ at least, by shift-right-clicking
and hitting 'copy paths']

proposed workflow:
- unzip/unrar a file containing a compilation of comics
- run script
- select one issue of comic files, then do that shift-right click trick
- alt-tab over to the python console, run a batch and type in a name
- rinse and repeat
"""

import pyperclip
from zipfile import ZipFile
import os


def runThisThing(name, issue):
    if input('\n\ncopy paths to clipboard and then hit enter to build a new cbz; "x" to quit').lower() == 'x':
        pass
    else:
        a, b = turnIntoCBZ(pyperclip.paste(), name, issue)
        runThisThing(a, b)

def turnIntoCBZ(paths, name, issue):
    files = paths.splitlines()
    dir = os.path.dirname(files[0].strip('"'))
    q = input('''Assuming this is {} #{}. Hit ENTER to accept, or hit "t"
to change the title, or "n" to change the numbering, or "b" for both! '''.format(name, issue)).lower()
    if q == 'b' or q == 't':
        name = input('Enter new name: ')
    elif q == 'b' or q == 'n':
        issue = int(input('Enter new number: '))
    cbzfile = os.path.join(dir, name + ' #' + str(issue) + '.cbz')
    with ZipFile(cbzfile, 'x') as myzip:
        for x in files:
            myzip.write(x.strip('"'), arcname=os.path.basename(x.strip('"')))
        print('{} created!'.format(os.path.basename(cbzfile)))
    for x in files:
        os.remove(x.strip('"'))
    issue += 1
    return name, issue


def nameThisThing():
    name = input('Name of this comic: ')
    issue = int(input('First issue number: '))
    return name, issue

if __name__ == "__main__":
    name, issue = nameThisThing()
    runThisThing(name, issue)
