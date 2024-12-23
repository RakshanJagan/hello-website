from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello\n' * 5

if __name__ == '__main__':
    app.run(debug=True)
