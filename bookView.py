import mysql.connector
class librarymanagement:
    def ___init_(self):
        self.connection=mysql.connector.connect(
            user="root",
            password="bt21jk",
            database="library_db",
            host="localhost",
            port=3307
        )
        print("connected successfully...!"