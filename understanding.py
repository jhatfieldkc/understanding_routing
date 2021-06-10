from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/dojo')
def dojo():
    return 'Dojo!'
@app.route('/say/<name>')
def hello(name):
    print(name)
    return "Hello, " + str(name)
@app.route('/repeat/<num>/<word>')
def repeat(num, word):
    print(word)
    return word * int(num)
@app.route('/<path:path>')
def catch_all(path):
    return 'Sorry!  No response.  Try again.'

if __name__=="__main__":
    app.run(debug=True)