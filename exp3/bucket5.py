print("soham Sonawane")
from abc import ABC, abstractmethod

# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

# Concrete Observer for Email notification
class EmailNotifier(Observer):
    def __init__(self, email):
        self.email = email

    def update(self, message):
        print(f"Email sent to {self.email}: {message}")

# Concrete Observer for SMS notification
class SMSNotifier(Observer):
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def update(self, message):
        print(f"SMS sent to {self.phone_number}: {message}")

# Subject class managing list of observers
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

# Demonstration:
if __name__ == "__main__":
    subject = Subject()

    email_observer = EmailNotifier("user@example.com")
    sms_observer = SMSNotifier("+1234567890")

    subject.attach(email_observer)
    subject.attach(sms_observer)

    subject.notify("New update available!")
