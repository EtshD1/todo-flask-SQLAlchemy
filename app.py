from operator import methodcaller
import sys
from flask import Flask, request, redirect
from flask.helpers import url_for
from flask.json import jsonify
from flask.templating import render_template
from sqlalchemy.orm import backref
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
    list_id = db.Column(db.Integer, db.ForeignKey('list.id'), nullable=False)

    def __repr__(self):
        return f'ID:{self.id}, Description: {self.description}, Completed: {self.completed}'


class List(db.Model):
    __tablename__ = "list"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    tasks = db.relationship('Task',  cascade="all,delete",
                            backref="list", lazy=True)


@app.route("/list/<list_id>")
def get_list_tasks(list_id):
    return render_template("index.html", lists=List.query.all(), tasks=Task.query.filter_by(list_id=list_id).order_by('id').all())


@app.route("/list")
def get_lists():
    return render_template("index.html", lists=List.query.all(), tasks=[])


@app.route("/")
def index():
    firstList = List.query.first()
    if firstList == None:
        return redirect(url_for('get_lists'))
    else:
        return redirect(url_for('get_list_tasks'), list_id=firstList.id)


# Create List
@ app.route("/list", methods=["POST"])
def addList():
    try:
        data = request.form["name"]
        newList = List(name=data)
        db.session.add(newList)
        db.session.commit()
        return redirect(url_for('get_list_tasks', list_id=newList.id))
    except:
        db.session.rollback()
        print(sys.exc_info())
        return redirect("/")
    finally:
        db.session.close()


# Delete List
@ app.route("/delete-list", methods=["POST"])
def deleteList():
    try:
        data = request.form["id"]
        db.session.delete(List.query.get(data))
        db.session.commit()
        return jsonify(status=True)
    except:
        db.session.rollback()
        print(sys.exc_info())
        return jsonify(status=False)
    finally:
        db.session.close()


# Create Task
@ app.route("/list/<list_id>", methods=["POST"])
def addTask(list_id):
    try:
        data = request.form["description"]
        newTodo = Task(description=data, list_id=list_id)
        db.session.add(newTodo)
        db.session.commit()
        return jsonify(status=True, description=data, id=newTodo.id)
    except:
        db.session.rollback()
        print(sys.exc_info())
        return jsonify(status=False)
    finally:
        db.session.close()


# Delete Task
@ app.route("/delete", methods=["DELETE"])
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


# Update
@ app.route("/update", methods=["PUT"])
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
