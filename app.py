from flask import Flask
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
if __name__ == '__main__':
    app.run()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://etsh:3894@127.0.0.1:5432/todo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Task(db.Model):
    __tablename__ = 'Tasks'
    id = db.Column(db.Integer, primay_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'ID:{self.id}, Description: {self.description}'


db.create_all()


@app.route("/")
def index():
    return render_template("index.html", data=[
        {'description': 'Todo 1'},
        {'description': 'Todo 2'},
        {'description': 'Todo 3'},
    ])
