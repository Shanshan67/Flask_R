from flask import Flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy                 


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////Users/jiangzihui/Downloads/flask/api_resetpwd/resetpwd.db'


@app.route('/get', methods=['GET'])
def get_articles():
    return jsonify({'hello':'world'})




if __name__ == "__main__":
    app.run(debug=True)