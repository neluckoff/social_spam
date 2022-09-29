import json
import tempfile
import time

from pyrogram import Client
from random import randint
from pathlib import Path
from alive_progress import alive_bar
from pyrogram.types import InputPhoneContact


class Telegram:

    def __init__(self) -> None:
        """
        This class is based on the module pyrogram
        """
        self.user = None
        self.message = None
        self.image = None

    def connect_user(self,
                     api_id: int,
                     api_hash: str,
                     phone_number: str
                     ) -> None:
        """
        Method for connecting an account

        Args:
            api_id (int):
            api_hash (str):
            phone_number (str): your phone number

        api_id and api_hash can be obtained from this link by
        creating an application:
            https://my.telegram.org/auth
        """
        self.user = Client("my_account",
                           api_id=api_id,
                           api_hash=api_hash,
                           phone_number=phone_number
                           ).start()

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
        if Path(path).is_file() and (Path(path).suffix == ".md" or Path(path).suffix == ".txt"):
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
        if Path(path).is_file() and (Path(path).suffix == ".png" or Path(path).suffix == ".jpg"
                                     or Path(path).suffix == ".jpeg"):
            self.image = path

    def check_message(self) -> None:
        """
        Check the finished message

        Sends a ready-made text to himself
        in private messages
        """
        if self.image is None:
            self.user.send_message('me', self.message)
        else:
            self.user.send_photo('me', self.image, caption=self.message)

    def get_chats(self) -> list:
        """
        Get a list of all chats with their name and id

        Return:
            list: id list
        """
        chats = []
        for dialog in self.user.get_dialogs():
            chats.append({'dialog': dialog.chat.first_name or dialog.chat.title, 'id': dialog.chat.id})
        return chats

    def get_me(self) -> Client:
        """
        Get your user class Client from pyrogram

        Return:
             Client: class from pyrogram module
        """
        return self.user

    def start_selective_spam(self,
                             chats: list,
                             message: str = None,
                             image: str = None,
                             delay_time: float = 1.5
                             ) -> None:
        """
        Start mailing to all elements of the array (1 message each)

        Args:
            chats (list): ID of all users
            message (str): set a text message
            image (str): set image to message
            delay_time (float): delay time between sending emails
        """
        if message is not None:
            self.set_message(message)
        if image is not None:
            self.set_image(image)

        with alive_bar(len(chats), force_tty=True) as bar:
            for id in chats:
                if str(id).isdigit():
                    if self.image is not None:
                        self.user.send_photo(id, self.image, caption=self.message)
                        time.sleep(delay_time)
                        bar()
                    else:
                        self.user.send_message(id, self.message)
                        time.sleep(delay_time)
                        bar()
                else:
                    print(f'{id} is not ID')

    def start_all_spam(self,
                       message: str = None,
                       image: str = None,
                       delay_time: float = 1.5
                       ) -> None:
        """
        Start sending to all chats you've ever interacted in

        Args:
            message (str): set a text message
            image (str): set image to message
            delay_time (float): delay time between sending emails
        """
        if message is not None:
            self.set_message(message)
        if image is not None:
            self.set_image(image)

        all_chats = self.get_chats()
        with alive_bar(len(all_chats), force_tty=True) as bar:
            for chat in all_chats:
                if self.image is None:
                    self.user.send_message(chat['id'], self.message)
                    time.sleep(delay_time)
                    bar()
                else:
                    self.user.send_photo(chat['id'], self.image, caption=self.message)
                    time.sleep(delay_time)
                    bar()

    def start_bombing(self,
                      user_id: int,
                      amount: int,
                      message: str = None,
                      image: str = None,
                      delay_time: float = 1.5
                      ) -> None:
        """
        Start bombarding one user with messages

        Args:
             user_id (int): user ID
             amount (int): number of sent messages
             message (str): set a text message
             image (str): set image to message
             delay_time (float): delay time between sending emails
        """
        if message is not None:
            self.set_message(message)
        if image is not None:
            self.set_image(image)

        with alive_bar(amount, force_tty=True) as bar:
            for i in range(amount):
                if self.image is not None:
                    self.user.send_photo(user_id, self.image, caption=self.message)
                    time.sleep(delay_time)
                    bar()
                else:
                    self.user.send_message(user_id, self.message)
                    time.sleep(delay_time)
                    bar()

    def send_message(self,
                     user_id: int,
                     message: str = None,
                     image: str = None
                     ) -> None:
        """
        Normally send a message to a user

        Args:
            user_id (int): user ID
            message (str): set a text message
            image (str): set image to message
        """
        if message is not None:
            self.set_message(message)
        if image is not None:
            self.set_image(image)

        if self.image is not None:
            self.user.send_photo(user_id, self.image, caption=self.message)
        else:
            self.user.send_message(user_id, self.message)

    def get_id_by_phone(self, phone_num: str) -> int:
        """
        Method for getting a user's ID by his number (adds this contact to you in telegram chats,
        and then deletes it - it's better not to test on your contacts)

        Args:
            phone_num (str): phone number of interest
        Return:
            str: ID by number
        """
        temp_contact_name = tempfile.NamedTemporaryFile().name.split('\\')[-1]
        good_res = list()
        self.user.import_contacts([InputPhoneContact(phone=phone_num, first_name=temp_contact_name)])
        contacts = self.user.get_contacts()
        for contact in contacts:
            contact_data = json.loads(str(contact))
            if contact_data['first_name'] == temp_contact_name:
                good_res.append(contact_data)
                self.user.delete_contacts(contact_data['id'])

        try:
            good_res = int(good_res[0]['id'])
        except:
            good_res = None

        return good_res
