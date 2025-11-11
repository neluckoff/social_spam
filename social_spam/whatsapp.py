from alive_progress import alive_bar
from pathlib import Path


class WhatsApp:

    def __init__(self) -> None:
        """
        Class for working with messages in WhatsApp
        using the module pywhatkit
        """
        self.phones = None
        self.image = None
        self.message = None
        self.document = None
        self._pywhatkit = None

    @property
    def pywhatkit(self):
        """Lazy import of pywhatkit to avoid connection check at import time"""
        if self._pywhatkit is None:
            import pywhatkit
            self._pywhatkit = pywhatkit
        return self._pywhatkit

    def send_message(self,
                     phone: str = None,
                     text: str = None,
                     image: str = None
                     ) -> None:
        """
        Normally send a message to a user

        Args:
            phone (str): recipient number
            text (str): set a text message
            image (str): set image to message
        """
        if phone is not None:
            self.phones = phone
        if text is not None:
            self.message = text
        if image is not None:
            self.image = image

        if self.image is None:
            self.pywhatkit.sendwhatmsg_instantly(phone_no=self.phones, message=self.message,
                                                 tab_close=True, close_time=1, wait_time=6)
        else:
            self.pywhatkit.sendwhats_image(receiver=self.phones, img_path=self.image, caption=self.message,
                                           tab_close=True, close_time=1, wait_time=6)

    def start_bombing(self,
                      phone_number: str,
                      amount: int,
                      text: str = None,
                      image: str = None,
                      wait_time: int = 6,
                      close_time: int = 1
                      ) -> None:
        """
        Start bombarding one user with messages

        Args:
            phone_number (str): recipient number
            amount (int): number of sent messages
            text (str): message text
            image (str): message image
            wait_time (int): time to wait before sending (seconds)
            close_time (int): time before closing tab (seconds)
        """
        if text is not None:
            self.message = text
        if image is not None:
            self.image = image

        with alive_bar(amount, force_tty=True) as bar:
            for i in range(amount):
                self.pywhatkit.sendwhatmsg_instantly(phone_no=phone_number, message=self.message,
                                                     tab_close=True, close_time=close_time, wait_time=wait_time)
                bar()

    def start_spamming(self,
                       phones: list = None,
                       text: str = None,
                       image: str = None,
                       wait_time: int = 6,
                       close_time: int = 1
                       ) -> None:
        """
        Start mailing to all elements of the array (1 message each)

        Args:
             phones (list): list of recipient numbers
             text (str): message text
             image (str): message image
             wait_time (int): time to wait before sending (seconds)
             close_time (int): time before closing tab (seconds)
        """
        if phones is not None:
            self.phones = phones
        if text is not None:
            self.message = text
        if image is not None:
            self.image = image

        with alive_bar(range(len(self.phones)), force_tty=True) as bar:
            for phone in self.phones:
                self.pywhatkit.sendwhatmsg_instantly(phone_no=phone, message=self.message,
                                                     tab_close=True, close_time=close_time, wait_time=wait_time)
                bar()

    def set_message(self, message: str) -> None:
        """
        Set the message to be used in further mailing

        Args:
            message (str): message text
        """
        self.message = message

    def set_file_message(self, path: str) -> None:
        """
        Get message text from .txt or .md file

        Args:
            path (str): path to file
        """
        if Path(path).is_file() and (Path(path).suffix == ".txt" or Path(path).suffix == ".md"):
            md_str = ''
            with open(path, "r", encoding="utf-8") as file:
                for line in file:
                    md_str += line
            self.message = md_str

    def set_image(self, path) -> None:
        """
        Attach image to message

        Args:
            path (str): image path
        """
        self.image = path

    def set_document(self, path: str) -> None:
        """
        Attach document to message

        Args:
            path (str): document path
        """
        if Path(path).is_file():
            self.document = path

    def set_phone(self, phone_number: str) -> None:
        """
        Specify the number of one recipient

        Args:
            phone_number (str): recipient number
        """
        self.phones = phone_number

    def set_phones(self, phone_numbers: list) -> None:
        """
        Set a list of recipient numbers

        Args:
            phone_numbers (list): list of recipient numbers
        """
        self.phones = phone_numbers
