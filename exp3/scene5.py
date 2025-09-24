print("SY - 5,Soham Sonawane, Enrollment no- ADT24SOCB1178")
from abc import ABC, abstractmethod

# Base Notification interface
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

# Concrete Notification classes
class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending Email notification: {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS notification: {message}")

class PushNotification(Notification):
    def send(self, message):
        print(f"Sending Push notification: {message}")

# Notification Factory
class NotificationFactory:
    @staticmethod
    def create_notification(notification_type):
        notification_type = notification_type.lower()
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        elif notification_type == "push":
            return PushNotification()
        else:
            raise ValueError(f"Unknown notification type: {notification_type}")

# Demonstration
if __name__ == "__main__":
    factory = NotificationFactory()

    notif = factory.create_notification("email")
    notif.send("Hello via Email!")

    notif = factory.create_notification("sms")
    notif.send("Hello via SMS!")

    notif = factory.create_notification("push")
    notif.send("Hello via Push Notification!")
