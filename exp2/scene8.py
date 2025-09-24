print("soham sonawane")
import re

class EmailFilterIterator:
    def __init__(self, items):
        self.items = items
        self.index = 0
        self.email_regex = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.items):
            item = self.items[self.index]
            self.index += 1
            if self.email_regex.match(item):
                return item
        raise StopIteration

# Test the iterator
strings = ["user@example.com", "invalidemail@", "test.user@mail.net", "hello@world", "admin@site.org"]
email_iterator = EmailFilterIterator(strings)

print("Valid emails:")
for email in email_iterator:
    print(email)
