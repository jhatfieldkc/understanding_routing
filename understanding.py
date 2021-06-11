from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'
    
@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def hello(name):
    print(name)
    return "Hello, " + name

@app.route('/repeat/<int:num>/<word>')
def repeat(num, word):
    print(word)
    return word * num

@app.errorhandler(404)
def catch_all(err):
    print(type(err))
    return "Sorry its broken"

if __name__=="__main__":
    app.run(debug=True)