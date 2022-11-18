from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify
import time
import json
import fasttext

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
content = ''
num_of_strings = 1
errors = 0
k = 0
seconds = 0
lpress = 0


def getFileViaPath(file_path):
    text_file = open(file_path, 'r')
    global content
    content = splitToStrings(text_file.read())
    text_file.close()


def parseTextToArrays(size_of_strings):
    global is_parsed
    global content
    data = []
    if is_parsed == '':
        is_parsed = 'true'
        data = splitToStrings(content, size_of_strings)
    return data

def splitToStrings(s, size_of_strings=30):
    print(s)
    return [s[i:i + size_of_strings] for i in range(0, len(s), size_of_strings)]


def getTextViaK(num_of_char):
    global k
    return splitToStrings(content[k])


def writeInputTextViaGUI(text):
    global content
    content = splitToStrings(text)


@app.route("/checkOfInput", methods=['GET', 'POST', 'DELETE', 'PUT'])
@cross_origin()
def checkOfInput():
    global lpress, seconds
    seconds += (time.time() - lpress)
    lpress = time.time()
    res = False
    global errors, k, content
    text = request.get_json()
    input_string = getTextViaK(k)[0]
    #input_string = input_string[:-2]
    current_string = ''.join(text['currentString'].split('\n'))
    print(len(input_string))
    print(len(current_string))
    if input_string[len(current_string) - 1] == current_string[len(current_string) - 1]:
        if len(current_string) == len(input_string):
            if k + num_of_strings >= len(content):
                return jsonify(boolRes=True, newString="new", errors=errors, messege="new", time=seconds)
            else:
                k += 1
                return jsonify(boolRes=res, newString=getTextViaK(k)[0], messege="new")
        else:
            return jsonify(boolRes=res, newString=text['currentString'], messege="old")
    else:
        errors += 1
        return jsonify(boolRes=res, newString=text['currentString'][:-1], messege="old")


@app.route("/getText", methods=['GET', 'POST', 'DELETE', 'PUT'])
@cross_origin()
def getText():
    global k
    text = request.get_json()
    writeInputTextViaGUI(text['value'])
    k = 0
    return jsonify(i='')

@app.route("/sendPath", methods=['GET', 'POST', 'DELETE', 'PUT'])
@cross_origin()
def sendPath():
    global num_of_strings
    text = request.get_json()
    num_of_strings = text['number']
    getFileViaPath(text['value'])


@app.route("/sendText", methods=['GET', 'POST', 'DELETE', 'PUT'])
@cross_origin()
def sendText():
    global lpress
    lpress = time.time()
    return jsonify(newString=getTextViaK(0)[0])


@app.route("/gettingTags", methods=['GET', 'POST', 'DELETE', 'PUT'])
@cross_origin()
def gettingTags():
    text = request.get_json()
    print(text['value'])
    result = '''searchingTheMostSimilarTwit(text['value'])'''
    return jsonify(hashtags=result)


def main():
    app.run(port=5050, debug=True)


if __name__ == "__main__":
    main()
