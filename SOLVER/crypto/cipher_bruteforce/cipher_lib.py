from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def cipher_lib():
    return "hello world"

@app.route('/call_decoders')
def main():
    return 'text'

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