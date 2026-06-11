""" Принципы ООП: """

"""  Наследование  """
# class Animal:
#     def eat(self):
#         print("Животное ест")
#     def breath(self):
#         print("Животное дышит")
#
# class Cat(Animal):
#     def meow(self):
#         print("Кот мяукает")
#
# c = Cat()
# c.eat()
# c.breath()
# c.meow()
#
# class Dog(Animal):
#     def gav(self):
#         print("Собака гавкает")
#
# d = Dog()
# d.eat()
# d.breath()
# d.gav()

# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#
#     def get_info(self):
#         return f"Name {self.name}, Email: {self.email}"
#
# class Teacher(User):
#     def __init__(self, name, email, subject):
#         super().__init__(name, email)
#         self.subject = subject
#
#     def teach(self):
#         return f"{self.name} teaches {self.subject}"
#
# class Admin(User):
#     def ban_user(self, user_name):
#         return f"{self.name} banned {user_name.name}"
#
# t = Teacher("Alice", "alice@gmail.com", "history")
# b = Admin("Bob", "bob@gmail.com")
#
# print(t.get_info())
# print(t.teach())
# print(b.get_info())
# print(b.ban_user(t))


"""  Полиморфизм  """
# class PaymentMethod():
#     def pay(self, payment):
#         pass
#
# class CardPayment(PaymentMethod):
#     def pay(self, payment):
#         print(f"Оплата {payment} руб. картой")
#
# class CashPayment(PaymentMethod):
#     def pay(self, payment):
#         print(f"Оплата {payment} руб. наличными")
#
# class CryptPayment(PaymentMethod):
#     def pay(self, payment):
#         print(f"Оплата {payment} руб. криптовалютой")
#
# def process_payment(payment_method, payment):
#     payment_method.pay(payment)
#
# card = CardPayment()
# cash = CashPayment()
# crypt = CryptPayment()
#
# process_payment(card, 1000)
# process_payment(cash, 500)
# process_payment(crypt, 2000)

""" Task """
class Notification:
    def __init__(self, user, message):
        self.user = user
        self.message = message
    def send(self):
        pass

class  EmailNotification(Notification):
    def send(self):
        print(f"Email: For {self.user}\n     {self.message}")

class SMSNotification(Notification):
    def send(self):
        print(f"SMS: For {self.user}\n     {self.message}")

class TelegramNotification(Notification):
    def send(self):
        print(f"Telegram: For {self.user}\n     {self.message}")

def notify_all(notifications):
    for notification in notifications:
        notification.send()


email = EmailNotification("Jack", "Good Morning Jack!")
sms = SMSNotification("Bob", "How are you?")
tg = TelegramNotification("Ali", "How old are you?")

arr = [email, sms, tg]

notify_all(arr)