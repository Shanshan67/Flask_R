from flask import Flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy     
import datetime            


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////Users/jiangzihui/Downloads/React_Flask/backend/flask.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

@app.route('/get', methods=['GET'])
def get_articles():
    return jsonify({'hello':'world'})




if __name__ == "__main__":
    app.run(debug=True)