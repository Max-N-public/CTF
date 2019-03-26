from flask import Flask, render_template, request
app = Flask(__name__)

import base64
from pprint import pprint


@app.route('/ciphers', methods=['GET'])
def cipher_lib(input):
    '''
    Call list for ciphers: (Only has really common ciphers --> use cyberchef for more rare)
    base64/32/16
    ROT47
    ROT26
    Caeser Cipher
    Morse
    QuipQuip
    '''

    '''
    base64_decoded = base64(input)
    rot47_decoded = rot47(input)
    rot26_decoded = rot26(input)
    caesar_decoded = caesar(input)
    morse_decoded = morse(input)
    quipquip_decoded = quipquip(input)
    '''
    #return render_template('output.html', 
    #)
    return "test"

'''
HEXBASE BLOCK----------------------------
'''
def base64_decode(input):
    return base64.b64decode(input)

def base32_decode(input):
    return base64.b32decode(input)

def base16_decode(input):
    return base64.b16decode(input)

def base64_encode(input):
    return base64.b64encode(input)

def base32_encode(input):
    return base64.b32encode(input)

def base16_encode(input):
    return base64.b16encode(input)

#--------------------------------------------

'''
ROT Block-------------------------------------
'''
def rot47(input):
    rot47_array = []
    return rot47_array.append([(str(33 + ((ord(j) + 14) mod 94))) for j in range(33,126)])

def rot26(input):
    rot26_array = []
    return rot_array26.append(['input'.decode('rot%d' % i) for i in range(1,26)])

#---------------------------------------------

def runRot(input):
    return "aasd"

def runCaesar(input):
    return "asd"