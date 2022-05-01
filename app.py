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
    transactions = db.get_user_transactions(user_id)
    return {'data': transactions}


@app.route('/exp-tracker/api/v1/create-transaction', methods=['POST'])
def create_transaction():
    payload = request.form.to_dict()
    result = db.create_new_transaction(payload)
    return {'result': result}


@app.route('/exp-tracker/api/v1/delete-transaction', methods=['DELETE'])
def delete_transaction():
    transaction_id = request.form.get('transaction_id')
    result = db.delete_transaction(transaction_id)
    return {'result': result}


if __name__ == '__main__':
    app.run(debug=True)
