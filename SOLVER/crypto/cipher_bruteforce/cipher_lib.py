from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def cipher_lib():
    return """Form decoding Schemes:
    <br>Caesar Cipher
    <br>Affine
    <br>Rail Fence
    <br>ROT47
    <br>ROT13
    <br>etc"""

@app.route('/admin_panel')
def main():
    return '<br><br><br><br><br><b>yur mum, gai<br><br><br>rekt</b>'

'''def base64_decode(input):
{
    return "test string"
}

def rot47(input)
{

}

def runRot(input)
{

}

def runCaesar(input)
{

}
'''