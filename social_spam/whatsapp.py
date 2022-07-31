import pywhatkit

from alive_progress import alive_bar


class WhatsApp:

    def __init__(self) -> None:
        """
        Class for working with messages in WhatsApp
        using the module pywhatkit
        """
        self.phones = None
        self.image = None
        self.message = None

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
            pywhatkit.sendwhatmsg_instantly(phone_no=self.phones, message=self.message,
                                            tab_close=True, close_time=1, wait_time=6)
        else:
            pywhatkit.sendwhats_image(receiver=self.phones, img_path=self.image, caption=self.message,
                                      tab_close=True, close_time=1, wait_time=6)

    def start_bombing(self,
                      phone_number: str,
                      amount: int,
                      text: str = None,
                      image: str = None
                      ) -> None:
        """
        Start bombarding one user with messages

        Args:
            phone_number (str): recipient number
            amount (int): number of sent messages
            text (str): message text
            image (str): message image
        """
        if text is not None:
            self.message = text
        if image is not None:
            self.image = image

        with alive_bar(amount, force_tty=True) as bar:
            for i in range(amount):
                pywhatkit.sendwhatmsg_instantly(phone_no=phone_number, message=self.message,
                                                tab_close=True, close_time=1, wait_time=6)
                bar()

    def start_spamming(self,
                       phones: list = None,
                       text: str = None,
                       image: str = None
                       ) -> None:
        """
        Start mailing to all elements of the array (1 message each)

        Args:
             phones (list): list of recipient numbers
             text (str): message text
             image (str): message image
        """
        if phones is not None:
            self.phones = phones
        if text is not None:
            self.message = text
        if image is not None:
            self.image = image

        with alive_bar(range(len(self.phones)), force_tty=True) as bar:
            for phone in self.phones:
                pywhatkit.sendwhatmsg_instantly(phone_no=phone, message=self.message,
                                                tab_close=True, close_time=1, wait_time=6)
                bar()

    def set_message(self, message: str) -> None:
        """
        Set the message to be used in further mailing

        Args:
            message (str): message text
        """
        self.message = message

    def set_image(self, path) -> None:
        """
        Attach image to message

        Args:
            path (str): image path
        """
        self.image = path

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
