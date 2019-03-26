from flask import Flask, render_template, request
app = Flask(__name__)

'''
cipher imports
'''
import base64



@app.route('/ciphers', methods=['GET'])
def cipher_lib(input):
    '''
    Call list for ciphers:
    base64
    ROT47
    ROT13
    Caeser Cipher
    Affine
    Atbash
    Morse
    QuipQuip
    '''
    '''

    base64_decoded = base64(input)
    rot47_decoded = rot47(input)
    rot13_decoded = rot13(input)
    caesar_decoded = caesar(input)
    affine_decoded = affine(input)
    atbash_decoded = atbash(input)
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

def rot47(input):
    return "test"

def runRot(input):
    return "aasd"

def runCaesar(input):
    return "asd"