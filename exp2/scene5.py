print("soham sonawane")
class UserAccount:
    _count = 0  # class variable to track number of instances

    def __init__(self, username):
        self.username = username
        UserAccount._count += 1

    @classmethod
    def get_user_count(cls):
        return cls._count

# Create multiple user objects
user1 = UserAccount("alice")
user2 = UserAccount("bob")
user3 = UserAccount("charlie")

# Display total user accounts created
print("Total user accounts created:", UserAccount.get_user_count())
