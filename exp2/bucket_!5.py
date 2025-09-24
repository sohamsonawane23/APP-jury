class UserAccount:
    count = 0

    def __init__(self, username):
        self.username = username
        UserAccount.count += 1

    def __str__(self):
        return f"UserAccount: {self.username}"

    @classmethod
    def get_count(cls):
        return cls.count


u1 = UserAccount("Alice")
u2 = UserAccount("Bob")
u3 = UserAccount("Charlie")

print(u1)
print(u2)
print(u3)
print("Total user accounts created:", UserAccount.get_count())
D