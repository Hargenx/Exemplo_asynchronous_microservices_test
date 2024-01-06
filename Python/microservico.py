from flask import Flask

app = Flask(__name__)

@app.route('/oi')
def oi():
    return 'Oi do Python microservice!'

if __name__ == '__main__':
    print('http://127.0.0.1:5000/oi')
    app.run(port=5000)
    