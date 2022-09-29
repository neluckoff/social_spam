import mimetypes
import smtplib
import time
import os
from email import encoders
from email.mime.application import MIMEApplication
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage

from email.mime.multipart import MIMEMultipart
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
        self.message = MIMEMultipart()

    def set_message(self, header: str, message: str, attachments: list = None) -> None:
        """
        Create messages for further sending in a letter

        Args:
             header (str): header of your message
             message (str): message text
             attachments (list): add attachments to email
        """
        self.message.attach(MIMEText(message, 'plain', 'utf-8'))
        self.message['Subject'] = Header(header, 'utf-8')
        if attachments:
            self.__attach_attachments(attachments=attachments)

    def set_message_html(self, header: str, html_path: str, attachments: list = None):
        """
        Creating a letter according to the layout from the html file

        Args:
             header (str): header of your message
             html_path (str): path to html file
             attachments (list): add attachments to email
        """
        try:
            with open(html_path) as file:
                html_template = file.read()
        except IOError:
            html_template = None

        self.message['Subject'] = Header(header, 'utf-8')
        self.message.attach(MIMEText(html_template, "html"))
        if attachments:
            self.__attach_attachments(attachments=attachments)

    def __attach_attachments(self, attachments: list) -> None:
        """
        Function for attaching attachments to a letter

         Args:
              attachments (list): add attachments to email
        """
        for attach in attachments:
            file_name = os.path.basename(attach)
            ftype, encoding = mimetypes.guess_type(attach)
            file_type, subtype = ftype.split("/")

            if file_type == "text":
                with open(attach, encoding="utf-8") as f:
                    file = MIMEText(f.read())
            elif file_type == "image":
                with open(attach, "rb") as f:
                    file = MIMEImage(f.read(), subtype)
            elif file_type == "audio":
                with open(attach, "rb") as f:
                    file = MIMEAudio(f.read(), subtype)
            elif file_type == "application":
                with open(attach, "rb") as f:
                    file = MIMEApplication(f.read(), subtype)
            else:
                with open(attach, "rb") as f:
                    file = MIMEBase(file_type, subtype)
                    file.set_payload(f.read())
                    encoders.encode_base64(file)

            file.add_header('content-disposition', 'attachment', filename=file_name)
            self.message.attach(file)

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
        self.message["From"] = username

    def send_message(self, mail_receiver: str) -> None:
        """
        Normally send a message to a user

        Args:
            mail_receiver (str): email
        """
        self.server.login(self.username, self.password)
        self.server.sendmail(self.username, mail_receiver, self.message.as_string())
        self.server.quit()

    def spam_messages(self, mail_receiver: list, delay_time: float = 1) -> None:
        """
        Start mailing to all elements of the array (1 message each)

        Args:
            mail_receiver (list): everyone's email
            delay_time (float): delay time between sending emails
        """
        self.server.login(self.username, self.password)
        with alive_bar(len(mail_receiver), force_tty=True) as bar:
            for user in mail_receiver:
                self.server.sendmail(self.username, user, self.message.as_string())
                time.sleep(delay_time)
                bar()
        self.server.quit()

    def bombing_message(self, mail_receiver: str, amount: int, delay_time: float = 1) -> None:
        """
        Start bombarding one user with messages

        Args:
             mail_receiver (str): email
             amount (int): number of sent messages
             delay_time (float): delay time between sending emails
        """
        self.server.login(self.username, self.password)
        with alive_bar(amount, force_tty=True) as bar:
            for i in range(amount):
                self.server.sendmail(self.username, mail_receiver, self.message.as_string())
                time.sleep(delay_time)
                bar()
        self.server.quit()
