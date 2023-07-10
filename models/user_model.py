from pyspark.sql import SparkSession
import mysql.connector

class UserModel:
    def __init__(self):
        self.spark = SparkSession.builder \
            .appName("SparkMySQLApp") \
            .getOrCreate()

        # MySQL connection details
        self.mysql_config = {
            'host': 'localhost',
            'database': 'employee',
            'user': 'root',
            'password': ''
        }

        # Create a MySQL connection
        self.conn = mysql.connector.connect(**self.mysql_config)

    def create_user(self, name, email):
        cursor = self.conn.cursor()
        insert_query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        values = (name, email)
        try:
            cursor.execute(insert_query, values)
            self.conn.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            cursor.close()
            return False

    def get_users(self):
        cursor = self.conn.cursor()
        select_query = "SELECT * FROM users"
        cursor.execute(select_query)
        rows = cursor.fetchall()
        users = []
        for row in rows:
            user = {'id': row[0], 'name': row[1], 'email': row[2]}
            users.append(user)
        cursor.close()
        return users

    def update_user(self, user_id, name, email):
        cursor = self.conn.cursor()
        update_query = "UPDATE users SET name=%s, email=%s WHERE id=%s"
        values = (name, email, user_id)
        try:
            cursor.execute(update_query, values)
            self.conn.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            cursor.close()
            return False

    def delete_user(self, user_id):
        cursor = self.conn.cursor()
        delete_query = "DELETE FROM users WHERE id=%s"
        values = (user_id,)
        try:
            cursor.execute(delete_query, values)
            self.conn.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            cursor.close()
            return False
