# Imports the Flask class from the Flask library.
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

#Creates a new Flask web application instance. __name__ tells Flask where to look for resources.
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return '<Task %r>' % self.id

#Defines a route ('/', the homepage) and a function (home) that runs when someone visits that route. 
#It returns the text "Hello, World!" to the browser.
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)   