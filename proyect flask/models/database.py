import pyodbc
from config import Config

class Database:
    @staticmethod
    def get_connection():
        return Config(0)
    
    @staticmethod
    def execute_query(query, params=None):
        conn = None
        cursor = None
        try:
            conn = Database.get_connection()
            cursor = conn.cursor()
            
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
                
            if query.strip().upper().startswith('SELECT'):
                result = cursor.fetchall()
                return result
            else:
                conn.commit()
                return cursor.rowcount
                
        except Exception as e:
            if conn:
                conn.rollback()
            raise e
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()