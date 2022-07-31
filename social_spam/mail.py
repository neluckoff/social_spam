import smtplib
import time

from email.mime.text import MIMEText
from email.header import Header
from alive_progress import alive_bar


class Mail:

    def __init__(self) -> None:
        """
        Class for sending messages from mail to mail
        """
        self.mail_receiver = None
        self.username = None
        self.password = None
        self.server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
        self.message = None

    def set_message(self, header: str, message: str) -> None:
        """
        Create messages for further sending in a letter

        Args:
             header (str): header of your message
             message (str): message text
        """
        self.message = MIMEText(message, 'plain', 'utf-8')
        self.message['Subject'] = Header(header, 'utf-8')

    def set_server(self, smtp: str, port: int) -> None:
        """
        Change SMTP server for sending messages
        Default: smtp.mail.ru:465

        Args:
            smtp (str): smtp address
            port (int): port to smtp
        """
        self.server = smtplib.SMTP_SSL(smtp, port)

    def connect_mail(self, username: str, password: str) -> None:
        """
        Connect your mail account
        * use a separate password for applications as a password

        Args:
            username (str): account login
            password (str): account password
        """
        self.username = username
        self.password = password

    def send_message(self, mail_receiver: str) -> None:
        """
        Normally send a message to a user

        Args:
            mail_receiver (str): email
        """
        self.server.login(self.username, self.password)
        self.server.sendmail(self.username, mail_receiver, self.message.as_string())
        self.server.quit()

    def spam_messages(self, mail_receiver: list) -> None:
        """
        Start mailing to all elements of the array (1 message each)

        Args:
            mail_receiver (list): everyone's email
        """
        self.server.login(self.username, self.password)
        with alive_bar(len(mail_receiver), force_tty=True) as bar:
            for user in mail_receiver:
                self.server.sendmail(self.username, user, self.message.as_string())
                time.sleep(1)
                bar()
        self.server.quit()

    def bombing_message(self, mail_receiver: str, amount: int) -> None:
        """
        Start bombarding one user with messages

        Args:
             mail_receiver (str): email
             amount (int): number of sent messages
        """
        self.server.login(self.username, self.password)
        with alive_bar(amount, force_tty=True) as bar:
            for i in range(amount):
                self.server.sendmail(self.username, mail_receiver, self.message.as_string())
                time.sleep(1)
                bar()
        self.server.quit()
