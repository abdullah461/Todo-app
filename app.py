from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# creating the actual Database
db = SQLAlchemy(app)

# creating a module in our database that will inherit db.module
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

# with app.app_context():
#     db.create_all()

@app.route('/')
def index():
    
    #show all to-do's
    todo_list = Todo.query.all()
    print(todo_list)
    return render_template('base.html')

if __name__ == "__main__":
    db.create_all()
    new_todo = Todo(title='todo 1', complete=False)
    db.session.add(new_todo)
    db.session.commit()

    app.run(debug=True)