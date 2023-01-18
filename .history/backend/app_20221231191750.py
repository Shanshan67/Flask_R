from flask import Flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy     
import datetime            


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////Users/jiangzihui/Downloads/React_Flask/backend/flask.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text())
    date = db.Column(db.Datetime, default=datetime.datetime.now)

    def __init__(self, title, body):
        self.title=title
        self.body=body

@app.route('/get', methods=['GET'])
def get_articles():
    return jsonify({'hello':'world'})




if __name__ == "__main__":
    app.run(debug=True)