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
        self.document = None
        self.video = None
        self.audio = None

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

    def set_document(self, path: str) -> None:
        """
        Attach document to message

        Args:
            path (str): document path
        """
        if Path(path).is_file():
            upload = vk_api.VkUpload(self.vk)
            doc = upload.document_message(path)
            owner_id = doc['doc']['owner_id']
            doc_id = doc['doc']['id']
            access_key = doc['doc']['access_key']
            self.document = f'doc{owner_id}_{doc_id}_{access_key}'

    def set_audio_message(self, path: str) -> None:
        """
        Attach audio message (voice message) to message

        Args:
            path (str): audio file path (mp3, ogg, etc.)
        """
        if Path(path).is_file():
            upload = vk_api.VkUpload(self.vk)
            audio = upload.audio_message(path)
            owner_id = audio['audio_message']['owner_id']
            audio_id = audio['audio_message']['id']
            access_key = audio['audio_message']['access_key']
            self.audio = f'audio_message{owner_id}_{audio_id}_{access_key}'

    def start_selective_spam(self,
                             chats: list,
                             message: str = None,
                             image: str = None,
                             document: str = None,
                             audio: str = None,
                             delay_time: float = 1
                             ) -> None:
        """
        Start mailing to all elements of the array (1 message each)

        Args:
            chats (list): ID of all users
            message (str): set a text message
            image (str): set image to message
            document (str): set document to message
            audio (str): set audio message to message
            delay_time (float): delay time between sending emails
        """
        if message is not None:
            self.set_message(message)
        if image is not None:
            self.set_image(image)
        if document is not None:
            self.set_document(document)
        if audio is not None:
            self.set_audio_message(audio)

        # Build attachment string
        attachment = None
        if self.image:
            attachment = self.image
        elif self.document:
            attachment = self.document
        elif self.audio:
            attachment = self.audio

        with alive_bar(len(chats), force_tty=True) as bar:
            for id in chats:
                if str(abs(id)).isdigit():
                    if attachment:
                        self.vk.messages.send(user_id=abs(id), message=self.message, random_id=0,
                                              attachment=attachment)
                    else:
                        self.vk.messages.send(user_id=abs(id), message=self.message, random_id=0)
                    time.sleep(delay_time)
                    bar()
                else:
                    print(f'{id} is not ID')

    def start_all_spam(self,
                       message: str = None,
                       image: str = None,
                       document: str = None,
                       audio: str = None,
                       delay_time: float = 1
                       ) -> None:
        """
        Start sending to all chats you've ever interacted in

        Args:
            message (str): set a text message
            image (str): set image to message
            document (str): set document to message
            audio (str): set audio message to message
            delay_time (float): delay time between sending emails
        """
        if message is not None:
            self.set_message(message)
        if image is not None:
            self.set_image(image)
        if document is not None:
            self.set_document(document)
        if audio is not None:
            self.set_audio_message(audio)

        # Build attachment string
        attachment = None
        if self.image:
            attachment = self.image
        elif self.document:
            attachment = self.document
        elif self.audio:
            attachment = self.audio

        chats = self.get_chats_id()
        with alive_bar(len(chats), force_tty=True) as bar:
            for chat in chats:
                if attachment:
                    self.vk.messages.send(user_id=abs(chat), message=self.message, random_id=0,
                                          attachment=attachment)
                else:
                    self.vk.messages.send(user_id=abs(chat), message=self.message, random_id=0)
                time.sleep(delay_time)
                bar()

    def start_bombing(self,
                      user_id: int,
                      amount: int,
                      message: str = None,
                      image: str = None,
                      document: str = None,
                      audio: str = None,
                      delay_time: float = 1
                      ) -> None:
        """
        Start bombarding one user with messages

        Args:
             user_id (int): user ID
             amount (int): number of sent messages
             message (str): set a text message
             image (str): set image to message
             document (str): set document to message
             audio (str): set audio message to message
             delay_time (float): delay time between sending emails
        """
        if message is not None:
            self.set_message(message)
        if image is not None:
            self.set_image(image)
        if document is not None:
            self.set_document(document)
        if audio is not None:
            self.set_audio_message(audio)

        # Build attachment string
        attachment = None
        if self.image:
            attachment = self.image
        elif self.document:
            attachment = self.document
        elif self.audio:
            attachment = self.audio

        with alive_bar(amount, force_tty=True) as bar:
            for i in range(amount):
                if attachment:
                    self.vk.messages.send(user_id=abs(user_id), message=self.message, random_id=0,
                                          attachment=attachment)
                else:
                    self.vk.messages.send(user_id=abs(user_id), message=self.message, random_id=0)
                time.sleep(delay_time)
                bar()

    def send_message(self,
                     user_id: int,
                     message: str = None,
                     image: str = None,
                     document: str = None,
                     audio: str = None
                     ) -> None:
        """
        Normally send a message to a user

        Args:
            user_id (int): user ID
            message (str): set a text message
            image (str): set image to message
            document (str): set document to message
            audio (str): set audio message to message
        """
        if message is not None:
            self.set_message(message)
        if image is not None:
            self.set_image(image)
        if document is not None:
            self.set_document(document)
        if audio is not None:
            self.set_audio_message(audio)

        # Build attachment string
        attachment = None
        if self.image:
            attachment = self.image
        elif self.document:
            attachment = self.document
        elif self.audio:
            attachment = self.audio

        if attachment:
            self.vk.messages.send(user_id=abs(user_id), message=self.message, random_id=0,
                                  attachment=attachment)
        else:
            self.vk.messages.send(user_id=abs(user_id), message=self.message, random_id=0)

    def get_friends(self) -> list:
        """
        Get list of friends

        Return:
            list: list of friends with their info (id, name, etc.)
        """
        try:
            friends = self.vk.friends.get(fields='first_name,last_name,nickname')
            return friends['items']
        except Exception as e:
            print(f"Error getting friends: {e}")
            return []

    def get_user_info(self, user_id: int) -> dict:
        """
        Get detailed information about a user

        Args:
            user_id (int): user ID
        Return:
            dict: user information
        """
        try:
            user = self.vk.users.get(user_ids=user_id, fields='photo_max,city,country,bdate,contacts')[0]
            return user
        except Exception as e:
            print(f"Error getting user info: {e}")
            return None
