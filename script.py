# Script

import sys
import os
sys.path.insert(1, '/mnt/d/Journal/lib/')

from shared import *
from finishing import *
from starting import *

try:
    filename = sys.argv[1]
except IndexError as e:
    print("No filename provided")
    exit()

ENCRYPTED = 'encrypted'
PLAINTEXT = filename
CWD = os.getcwd()

if(exists(CWD + '/' + ENCRYPTED)):
    starting(PLAINTEXT)
elif(exists(CWD + '/' + PLAINTEXT)):
    finishing(PLAINTEXT)
else:
    print("No plaintext file")
    print("No encrypted file")
    print("Error: Nothing in this folder")
    print("Start by running `touch journal`")
    print("And then running the script again :-)")
