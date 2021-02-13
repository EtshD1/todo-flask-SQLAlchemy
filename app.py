from flask import Flask, request
from flask.json import jsonify
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='public')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://etsh:3894@127.0.0.1:5432/todo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'ID:{self.id}, Description: {self.description}'


db.create_all()


@app.route("/")
def index():
    return render_template("index.html", data=Task.query.all())


@app.route("/add", methods=["POST"])
def add():
    data = request.form["description"]
    newTodo = Task(description=data)
    db.session.add(newTodo)
    db.session.commit()
    return jsonify(status=True, description=data)


if __name__ == '__main__':
    app.run()
