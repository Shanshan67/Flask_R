from flask import Flask
from flask import jsonify
from flask_sqlalchemy import                    


app = Flask(__name__)


@app.route('/get', methods=['GET'])
def get_articles():
    return jsonify({'hello':'world'})




if __name__ == "__main__":
    app.run(debug=True)