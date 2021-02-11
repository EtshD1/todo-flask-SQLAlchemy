from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
if __name__ == '__main__':
    app.run()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://etsh:3894@127.0.0.1:5432/todo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
