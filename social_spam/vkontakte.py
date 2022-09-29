import vk_api
import time

from pathlib import Path
from random import randint
from alive_progress import alive_bar


class Vkontakte:

    def __init__(self) -> None:
        """
        This class is based on the module vk_api
        """
        self.user = None
        self.vk = None
        self.message = None
        self.image = None

    def connect_user(self, token: str) -> None:
        """
        Method for connecting an account

        Args:
            token (str): a personal token of your account with
            access to messages, friends and access at any time.

        The token can be obtained from the link:
            https://vkhost.github.io/
        """
        self.user = vk_api.VkApi(token=token)
        self.vk = self.user.get_api()

    def get_chats_id(self) -> list:
        """
        Method for getting list of id of all messages

        Return:
            list: message id list
        """
        chats = []
        for chat in self.vk.messages.getConversations(extended=1)['items']:
            chats.append(chat['conversation']['peer']['id'])
        for chat in self.vk.messages.getConversations(extended=1)['profiles']:
            chats.append(chat['id'])
        return chats

    def get_name_by_id(self, user_id: int) -> list:
        """
        Method for obtaining data about a person by his ID

        Args:
            user_id (int): user ID

        Return:
            list: person information
        """
        user = self.user.method("users.get", {"user_ids": user_id})[0]
        return user

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

    def check_message(self) -> None:
        """
        Check the finished message

        Sends a ready-made text to himself
        in private messages
        """
        self.vk.messages.send(user_id=self.vk.users.get()[0]['id'], message=self.message, random_id=0)

    def get_me(self) -> list:
        """
        Get all information about yourself

        Return:
            list: account information
        """
        return self.vk.users.get()[0]

    def set_image(self, path: str) -> None:
        """
        Attach image to message

        Args:
            path (str): image path
        """
        if Path(path).is_file() and (Path(path).suffix == ".png" or Path(path).suffix == ".jpg"
                                     or Path(path).suffix == ".jpeg"):
            upload = vk_api.VkUpload(self.vk)
            photo = upload.photo_messages(path)
            owner_id = photo[0]['owner_id']
            photo_id = photo[0]['id']
            access_key = photo[0]['access_key']
            self.image = f'photo{owner_id}_{photo_id}_{access_key}'

    def start_selective_spam(self,
                             chats: list,
                             message: str = None,
                             image: str = None,
                             delay_time: float = 1
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
                if str(abs(id)).isdigit():
                    if self.image is None:
                        self.vk.messages.send(user_id=abs(id), message=self.message, random_id=0)
                        time.sleep(delay_time)
                        bar()
                    else:
                        self.vk.messages.send(user_id=abs(id), message=self.message, random_id=0,
                                              attachment=self.image)
                        time.sleep(delay_time)
                        bar()
                else:
                    print(f'{id} is not ID')

    def start_all_spam(self,
                       message: str = None,
                       image: str = None,
                       delay_time: float = 1
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

        chats = self.get_chats_id()
        with alive_bar(len(chats), force_tty=True) as bar:
            for chat in chats:
                if self.image is None:
                    self.vk.messages.send(user_id=abs(chat), message=self.message, random_id=0)
                    time.sleep(delay_time)
                    bar()
                else:
                    self.vk.messages.send(user_id=abs(chat), message=self.message, random_id=0,
                                          attachment=self.image)
                    time.sleep(delay_time)
                    bar()

    def start_bombing(self,
                      user_id: int,
                      amount: int,
                      message: str = None,
                      image: str = None,
                      delay_time: float = 1
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
                    self.vk.messages.send(user_id=abs(user_id), message=self.message, random_id=0,
                                          attachment=self.image)
                    time.sleep(delay_time)
                    bar()
                else:
                    self.vk.messages.send(user_id=abs(user_id), message=self.message, random_id=0)
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
            self.vk.messages.send(user_id=abs(user_id), message=self.message, random_id=0,
                                  attachment=self.image)
        else:
            self.vk.messages.send(user_id=abs(user_id), message=self.message, random_id=0)
