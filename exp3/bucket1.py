print("soham Sonawane")
class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            # Initialize any attributes here
            cls._instance.connection = "Database Connection Established"
        return cls._instance

    @classmethod
    def get_instance(cls):
        return cls()

    def get_connection_info(self):
        return self.connection


# Demonstration
db1 = DatabaseConnection.get_instance()
db2 = DatabaseConnection.get_instance()

print(db1.get_connection_info())  # Output: Database Connection Established
print(db2.get_connection_info())  # Output: Database Connection Established
print("Are both instances the same?", db1 is db2)  # Output: True
