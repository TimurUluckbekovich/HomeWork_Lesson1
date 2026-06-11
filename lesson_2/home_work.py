"""  Task 1:  """
class Notification:
    def __init__(self, user, message):
        self.user = user
        self.message = message
    def send(self):
        pass

class  EmailNotification(Notification):
    def send(self):
        print(f"Email: For {self.user}\n     {self.message}\n")

class SMSNotification(Notification):
    def send(self):
        print(f"SMS: For {self.user}\n     {self.message}\n")

class TelegramNotification(Notification):
    def send(self):
        print(f"Telegram: For {self.user}\n     {self.message}\n")

def notify_all(notifications):
    for notification in notifications:
        notification.send()


email = EmailNotification("Jack", "Good Morning Jack!")
sms = SMSNotification("Bob", "How are you?")
tg = TelegramNotification("Ali", "How old are you?")

arr = [email, sms, tg]

notify_all(arr)

"""  Task 2:  """
class Transport:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    def move(self):
        pass

class Car(Transport):
    def move(self):
        print(f"Car: {self.name}\nSpeed: {self.speed}\n")

class Plane(Transport):
    def move(self):
        print(f"Plane: {self.name}\nSpeed: {self.speed}\n")

class Boat(Transport):
    def move(self):
        print(f"Boat: {self.name}\nSpeed: {self.speed}\n")

def start_trip(transports):
    for transport in transports:
        transport.move()

transports = [Car("BMW",120), Plane("Boeing", 900), Boat("Yacht", 60)]

start_trip(transports)

