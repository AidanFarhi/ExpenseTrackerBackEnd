import os
from flask import Flask, request
from database import Database
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
db = Database(os.getenv('DB_URI'))


# DEVELOPMENT ROUTE ONLY
@app.route('/exp-tracker/api/v1/get-users', methods=['GET'])
def get_users():
    return db.get_users()


if __name__ == '__main__':
    app.run(debug=True)
