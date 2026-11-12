
from mysql import connector
from datetime import datetime

class BloodDonorManager:
    def __init__(self):
        self.connection = connector.connect(
            user="root",
            port=3307,
            password="bt21jk",
            database="blood_db_aug_2026",
            host="localhost"
        )
        print("Connected successfully....!")
    def get_object(self, id=None):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Donor WHERE id=%s"
            values = (id,)
            cursor.execute(query, values)
            record = cursor.fetchone()
            return record
        except Exception as e:
            print(e)
            return None

    def post(self, **kwargs):
        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO Donor
                (name, blood_group, phone, city, last_donation)
                VALUES (%s, %s, %s, %s, %s)
            """
            values = (
                kwargs["name"],
                kwargs["blood_group"],
                kwargs["phone"],
                kwargs["city"],
                kwargs["last_donation"]
            )
            cursor.execute(query, values)
            self.connection.commit()

            print("Data inserted successfully...!")
            return True
        except Exception as e:
            print(e)
            self.connection.rollback()
            return False
    def get(self):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Donor"
            cursor.execute(query)
            records = cursor.fetchall()
            return records
        except Exception as e:
            print(e)
            return []
    def retrieve(self, id=None):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Donor WHERE id=%s"
            values = (id,)
            cursor.execute(query, values)
            record = cursor.fetchone()
            if record:
                return record
            else:
                return None
        except Exception as e:
            print(e)
            return None
    def put(self, id=None, **kwargs):
        try:
            record = self.get_object(id=id)
            if record is not None:
                allowed_columns = {
                    "name",
                    "blood_group",
                    "phone",
                    "city",
                    "last_donation"
                }
                if not kwargs or not set(kwargs).issubset(allowed_columns):
                    return False, "Invalid update fields...!"
                self.cursor = self.connection.cursor()
                placeholder = ""
                for k in kwargs.keys():
                    placeholder += k + "=%s, "
                placeholder = placeholder.rstrip(", ")
                query = f"UPDATE Donor SET {placeholder} WHERE id=%s"
                values = [v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query, values)
                self.connection.commit()
                return True, "Donor updated successfully...!"
            else:
                return False, "No donors found...!"
        except Exception as e:
            print(e)
            self.connection.rollback()
            return False, "Error while updating donor...!"
    def close(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Connection closed successfully...!")
