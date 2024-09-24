
def send_email(message, recipient, sender="university.help@gmail.com"):
    if ('@' not in recipient and sender) and (".com",".ru",".net" not in recipient and sender):
        print("11")


send_email('Это сообщение для проверки связи', 'vasyok1337gmail.com')