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
        self.server = None
        self.smtp_host = 'smtp.mail.ru'
        self.smtp_port = 465
        self.use_tls = False
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

    def set_server(self, smtp: str, port: int, use_tls: bool = False) -> None:
        """
        Change SMTP server for sending messages
        Default: smtp.mail.ru:465 (SSL)

        Args:
            smtp (str): smtp address
            port (int): port to smtp
            use_tls (bool): use TLS instead of SSL (for ports like 587)
        """
        self.smtp_host = smtp
        self.smtp_port = port
        self.use_tls = use_tls
        # Reset server connection to use new settings
        if self.server is not None:
            try:
                self.server.quit()
            except:
                pass
            self.server = None

    def _get_server(self):
        """
        Get or create SMTP server connection

        Returns:
            smtplib.SMTP_SSL or smtplib.SMTP: SMTP server connection
        """
        if self.server is None:
            if self.use_tls:
                self.server = smtplib.SMTP(self.smtp_host, self.smtp_port)
                self.server.starttls()
            else:
                self.server = smtplib.SMTP_SSL(self.smtp_host, self.smtp_port)
        return self.server

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
        server = self._get_server()
        server.login(self.username, self.password)
        server.sendmail(self.username, mail_receiver, self.message.as_string())
        server.quit()
        self.server = None

    def spam_messages(self, mail_receiver: list, delay_time: float = 1) -> None:
        """
        Start mailing to all elements of the array (1 message each)

        Args:
            mail_receiver (list): everyone's email
            delay_time (float): delay time between sending emails
        """
        server = self._get_server()
        server.login(self.username, self.password)
        with alive_bar(len(mail_receiver), force_tty=True) as bar:
            for user in mail_receiver:
                server.sendmail(self.username, user, self.message.as_string())
                time.sleep(delay_time)
                bar()
        server.quit()
        self.server = None

    def bombing_message(self, mail_receiver: str, amount: int, delay_time: float = 1) -> None:
        """
        Start bombarding one user with messages

        Args:
             mail_receiver (str): email
             amount (int): number of sent messages
             delay_time (float): delay time between sending emails
        """
        server = self._get_server()
        server.login(self.username, self.password)
        with alive_bar(amount, force_tty=True) as bar:
            for i in range(amount):
                server.sendmail(self.username, mail_receiver, self.message.as_string())
                time.sleep(delay_time)
                bar()
        server.quit()
        self.server = None

    def set_priority(self, priority: str = 'normal') -> None:
        """
        Set message priority level

        Args:
            priority (str): 'urgent', 'normal', or 'low'
        """
        priority_values = {
            'urgent': ('1', 'urgent'),
            'normal': ('3', 'normal'),
            'low': ('5', 'non-urgent')
        }
        
        if priority.lower() in priority_values:
            x_priority, importance = priority_values[priority.lower()]
            self.message['X-Priority'] = x_priority
            self.message['Importance'] = importance
        else:
            raise ValueError("Priority must be 'urgent', 'normal', or 'low'")

    def set_cc_bcc(self, cc: list = None, bcc: list = None) -> None:
        """
        Set CC (Carbon Copy) and BCC (Blind Carbon Copy) recipients

        Args:
            cc (list): list of CC email addresses
            bcc (list): list of BCC email addresses
        """
        if cc:
            self.message['Cc'] = ', '.join(cc)
        if bcc:
            self.message['Bcc'] = ', '.join(bcc)

    def set_template_message(self, header: str, template: str, variables: dict, attachments: list = None) -> None:
        """
        Create message from template with variable substitution
        Use {{variable_name}} in template for substitution

        Args:
            header (str): header of your message
            template (str): message template with {{variables}}
            variables (dict): dictionary with variable values
            attachments (list): add attachments to email
            
        Example:
            template = "Hello {{name}}, your order {{order_id}} is ready!"
            variables = {"name": "John", "order_id": "12345"}
        """
        message_text = template
        for key, value in variables.items():
            message_text = message_text.replace('{{' + key + '}}', str(value))
        
        self.message.attach(MIMEText(message_text, 'plain', 'utf-8'))
        self.message['Subject'] = Header(header, 'utf-8')
        if attachments:
            self.__attach_attachments(attachments=attachments)

    def send_message_with_cc_bcc(self, to: str, cc: list = None, bcc: list = None) -> None:
        """
        Send message with CC and BCC support

        Args:
            to (str): primary recipient email
            cc (list): list of CC email addresses
            bcc (list): list of BCC email addresses
        """
        server = self._get_server()
        server.login(self.username, self.password)
        
        # Prepare all recipients
        all_recipients = [to]
        if cc:
            all_recipients.extend(cc)
            self.message['Cc'] = ', '.join(cc)
        if bcc:
            all_recipients.extend(bcc)
            # BCC is not added to message headers
        
        self.message['To'] = to
        server.sendmail(self.username, all_recipients, self.message.as_string())
        server.quit()
        self.server = None
