import pywhatkit

from alive_progress import alive_bar


class WhatsApp:

    def __init__(self) -> None:
        self.phones = None
        self.image = None
        self.message = None

    def send_message(self, text: str = None):
        if text is not None:
            self.message = text

        pywhatkit.sendwhatmsg_instantly(phone_no=self.phones, message=self.message,
                                        tab_close=True, close_time=1, wait_time=6)

    def start_bombing(self, phone_number: str, amount: int):
        with alive_bar(amount, force_tty=True) as bar:
            for i in range(amount):
                pywhatkit.sendwhatmsg_instantly(phone_no=phone_number, message=self.message,
                                                tab_close=True, close_time=1, wait_time=6)
                bar()

    def start_spamming(self):
        with alive_bar(range(len(self.phones)), force_tty=True) as bar:
            for phone in self.phones:
                pywhatkit.sendwhatmsg_instantly(phone_no=phone, message=self.message,
                                                tab_close=True, close_time=1, wait_time=6)

    def set_message(self, message: str):
        self.message = message

    def set_image(self, path):
        self.image = path

    def set_phone(self, phone_number: str):
        self.phones = phone_number

    def set_phones(self, phone_numbers: list):
        self.phones = phone_numbers
