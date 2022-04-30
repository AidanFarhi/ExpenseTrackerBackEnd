import os
from flask import Flask, request
from database import Database
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
db = Database(os.getenv('DB_URI'))


@app.route('/exp-tracker/api/v1/get-user-transactions', methods=['GET'])
def get_user_transactions():
    user_id = request.args.get('user-id')
    return db.get_user_transactions(user_id)

@app.route('/exp-tracker/api/v1/create-transaction', methods=['POST'])
def create_transaction():
    data = request.form.to_dict()
    return db.create_new_transaction(data)


if __name__ == '__main__':
    app.run(debug=True)
