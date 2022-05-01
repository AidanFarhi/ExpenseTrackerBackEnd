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
        try:
            with self.engine.begin() as conn:
                return [{
                    'id': r.id,
                    'amount': r.amount,
                    'trans_type': r.trans_type,
                    'user_id': r.user_id,
                    'description': r.description,
                    'category': r.category,
                    'trans_date': r.trans_date
                } for r in conn.execute(
                    text('SELECT * FROM transaction WHERE user_id = :id'),
                    {'id': user_id})]
        except Exception:
            return []

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
        try:
            with self.engine.begin() as conn:
                conn.execute(
                    text('''
                        INSERT INTO transaction(amount, trans_type, user_id, description, category)
                        VALUES (:amt, :trns_type, :usr_id, :desc, :cat)
                    '''), {
                        'amt': transaction['amount'],
                        'trns_type': transaction['trans_type'],
                        'usr_id': transaction['user_id'],
                        'desc': transaction['description'],
                        'cat': transaction['category']
                    })
            return True
        except Exception:
            return False

    def delete_transaction(self, transaction_id: int) -> bool:
        """Delete transaction from database with given id
        
        Args:
            transaction_id: id of transaction to delete

        Returns:
            True if successfull | False if not
        """
        try:
            with self.engine.begin() as conn:
                res = conn.execute(
                    text('DELETE FROM transaction WHERE id = :id'),
                    {'id': transaction_id})
            if res.rowcount > 0:
                return True
            return False
        except Exception as e:
            return False
