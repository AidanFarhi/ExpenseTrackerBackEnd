from flask import Flask, request
from database import engine, text

app = Flask(__name__)

@app.route('/get_users', methods=['GET'])
def get_transactions():
    with engine.begin() as conn:
        return {
            'data': [
                {'id': row.id, 'username': row.username} 
                for row in conn.execute(text('select * from app_user'))
            ]
        }

if __name__ == '__main__':
    app.run(debug=True)
