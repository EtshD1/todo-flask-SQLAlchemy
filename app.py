import sys
from flask import Flask, request
from flask.json import jsonify
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, static_folder='public')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://etsh:3894@127.0.0.1:5432/todo'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db, 'migrations')


class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'ID:{self.id}, Description: {self.description}, Completed: {self.completed}'


# Read Task
@app.route("/")
def index():
    return render_template("index.html", data=Task.query.order_by('id').all())


# Create Task
@app.route("/add", methods=["POST"])
def add():
    try:
        data = request.form["description"]
        newTodo = Task(description=data)
        db.session.add(newTodo)
        db.session.commit()
        return jsonify(status=True, description=data, id=newTodo.id)
    except:
        db.session.rollback()
        print(sys.exc_info())
        return jsonify(status=False)
    finally:
        db.session.close()


# Delete
@app.route("/delete", methods=["DELETE"])
def remove():
    try:
        data = request.form["id"]
        db.session.delete(Task.query.get(data))
        db.session.commit()
        return jsonify(status=True)
    except:
        db.session.rollback()
        print(sys.exc_info())
        return jsonify(status=False)
    finally:
        db.session.close()


# Delete
@app.route("/update", methods=["PUT"])
def update():
    try:
        id = request.form["id"]
        data = parse_bool(request.form["data"])
        Task.query.get(id).completed = data
        db.session.commit()
        return jsonify(status=True)
    except:
        db.session.rollback()
        print(sys.exc_info())
        return jsonify(status=False)
    finally:
        db.session.close()


def parse_bool(str):
    if str.lower() == 'false':
        return False
    elif str.lower() == 'true':
        return True
    else:
        return None


if __name__ == '__main__':
    app.run()
