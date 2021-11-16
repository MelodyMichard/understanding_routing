from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'    

@app.route('/say/flask')
def flask():
    return 'Hi Flask!'    

@app.route('/say/michael')
def michael():
    return 'Hi Michael!' 

@app.route('/say/john')
def john():
    return 'Hi John!'

@app.route('/name/<username>')
def given_name(username):
    print(username)
    return "Hi " + username
    
@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    return f"{word * num}"

if __name__ == "__main__":
    app.run(debug=True)