import smtplib
import time

from email.mime.text import MIMEText
from email.header import Header
from alive_progress import alive_bar


class Mail:

    def __init__(self) -> None:
        self.mail_receiver = None
        self.username = None
        self.password = None
        self.server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
        self.message = None

    def set_message(self, header: str, message: str) -> None:
        self.message = MIMEText(message, 'plain', 'utf-8')
        self.message['Subject'] = Header(header, 'utf-8')

    def set_server(self, smtp: str, port: int) -> None:
        self.server = smtplib.SMTP_SSL(smtp, port)

    def connect_mail(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def send_message(self, mail_receiver: str) -> None:
        self.server.login(self.username, self.password)
        self.server.sendmail(self.username, mail_receiver, self.message.as_string())
        self.server.quit()

    def spam_messages(self, mail_receiver: list) -> None:
        self.server.login(self.username, self.password)
        with alive_bar(len(mail_receiver), force_tty=True) as bar:
            for user in mail_receiver:
                self.server.sendmail(self.username, user, self.message.as_string())
                time.sleep(1)
                bar()
        self.server.quit()

    def bombing_message(self, mail_receiver: str, amount: int) -> None:
        self.server.login(self.username, self.password)
        with alive_bar(amount, force_tty=True) as bar:
            for i in range(amount):
                self.server.sendmail(self.username, mail_receiver, self.message.as_string())
                time.sleep(1)
                bar()
        self.server.quit()
