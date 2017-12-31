from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///datasource/catalog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
@app.route('/hello')
def HelloWorld():
    return "Hello World"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
