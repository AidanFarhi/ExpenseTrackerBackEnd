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

    def get_users(self):
        """DEVELOPMENT ONLY"""
        with self.engine.begin() as conn:
            return {
                'data': [{
                    'id': row.id,
                    'username': row.username
                } for row in conn.execute(text('select * from app_user'))]
            }

    def get_user_transactions(self, user_id: int) -> list:
        """Get all transactions for a given user id
        
        Args:
            user_id: id of user 

        Returns:
            A list of dictionary objects representing each transaction
        """
        pass

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
        pass
