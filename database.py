from sqlalchemy import create_engine, text


class Database:
    """Returns an object to interact with database

    Args:
        db_uri: uri of db to connect to
    
    Returns:
        A database interaction object
    """

    def __init__(self, db_uri: str) -> dict:
        self.engine = create_engine(db_uri, echo=True, future=True)

    def get_user_transactions(self, user_id: int) -> list:
        """Get all transactions for a given user id
        
        Args:
            user_id: id of user 

        Returns:
            A list of dictionary objects representing each transaction
        """
        with self.engine.begin() as conn:
            return {
                'data': [{
                    'id': row.id,
                    'amount': row.amount,
                    'trans_type': row.trans_type,
                    'user_id': row.user_id,
                    'description': row.description,
                    'category': row.category,
                    'trans_date': row.trans_date
                } for row in conn.execute(
                    text('SELECT * FROM transaction WHERE user_id = :id'), {'id': user_id}
                )]
            }

    def create_new_transaction(self, transaction: dict) -> bool:
        """Get all transactions for a given user id
        
        Args:
            transaction: dict (
                'amount': float,
                'trans_type': str,
                'user_id': int,
                'description': str,
                'category': str
            )

        Returns:
            True if successfull | False if not
        """
        with self.engine.begin() as conn:
            res = conn.execute(
                text('''
                    INSERT INTO transaction(amount, trans_type, user_id, description, category)
                    VALUES (:amt, :trns_type, :usr_id, :desc, :cat)
                '''),
                {
                    'amt': transaction['amount'],
                    'trns_type': transaction['trans_type'],
                    'usr_id': transaction['user_id'],
                    'desc': transaction['description'],
                    'cat': transaction['category']
                }
            )
        return {'result': str(res)}
