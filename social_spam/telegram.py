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
        self.document = None
        self.video = None
        self.audio = None
        self.parse_mode = None

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

    def set_document(self, path: str) -> None:
        """
        Attach document to message

        Args:
            path (str): document path (any file type)
        """
        if Path(path).is_file():
            self.document = path

    def set_video(self, path: str) -> None:
        """
        Attach video to message

        Args:
            path (str): video path (mp4, avi, mkv, etc.)
        """
        if Path(path).is_file() and (Path(path).suffix in [".mp4", ".avi", ".mkv", ".mov", ".flv"]):
            self.video = path

    def set_audio(self, path: str) -> None:
        """
        Attach audio to message

        Args:
            path (str): audio path (mp3, wav, ogg, etc.)
        """
        if Path(path).is_file() and (Path(path).suffix in [".mp3", ".wav", ".ogg", ".m4a", ".flac"]):
            self.audio = path

    def set_parse_mode(self, mode: str = None) -> None:
        """
        Set text formatting mode
        
        Args:
            mode (str): 'markdown', 'html', or None for plain text
        """
        if mode and mode.lower() in ['markdown', 'html']:
            self.parse_mode = mode.lower()
        else:
            self.parse_mode = None

    def check_message(self) -> None:
        """
        Check the finished message

        Sends a ready-made text to himself
        in private messages
        """
        kwargs = {'parse_mode': self.parse_mode} if self.parse_mode else {}
        
        if self.image:
            self.user.send_photo('me', self.image, caption=self.message, **kwargs)
        elif self.video:
            self.user.send_video('me', self.video, caption=self.message, **kwargs)
        elif self.document:
            self.user.send_document('me', self.document, caption=self.message, **kwargs)
        elif self.audio:
            self.user.send_audio('me', self.audio, caption=self.message, **kwargs)
        else:
            self.user.send_message('me', self.message, **kwargs)

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
                             document: str = None,
                             video: str = None,
                             audio: str = None,
                             parse_mode: str = None,
                             delay_time: float = 1.5
                             ) -> None:
        """
        Start mailing to all elements of the array (1 message each)

        Args:
            chats (list): ID of all users
            message (str): set a text message
            image (str): set image to message
            document (str): set document to message
            video (str): set video to message
            audio (str): set audio to message
            parse_mode (str): 'markdown', 'html', or None
            delay_time (float): delay time between sending emails
        """
        if message is not None:
            self.set_message(message)
        if image is not None:
            self.set_image(image)
        if document is not None:
            self.set_document(document)
        if video is not None:
            self.set_video(video)
        if audio is not None:
            self.set_audio(audio)
        if parse_mode is not None:
            self.set_parse_mode(parse_mode)

        kwargs = {'parse_mode': self.parse_mode} if self.parse_mode else {}

        with alive_bar(len(chats), force_tty=True) as bar:
            for id in chats:
                if str(id).isdigit():
                    if self.image:
                        self.user.send_photo(id, self.image, caption=self.message, **kwargs)
                    elif self.video:
                        self.user.send_video(id, self.video, caption=self.message, **kwargs)
                    elif self.document:
                        self.user.send_document(id, self.document, caption=self.message, **kwargs)
                    elif self.audio:
                        self.user.send_audio(id, self.audio, caption=self.message, **kwargs)
                    else:
                        self.user.send_message(id, self.message, **kwargs)
                    time.sleep(delay_time)
                    bar()
                else:
                    print(f'{id} is not ID')

    def start_all_spam(self,
                       message: str = None,
                       image: str = None,
                       document: str = None,
                       video: str = None,
                       audio: str = None,
                       parse_mode: str = None,
                       delay_time: float = 1.5
                       ) -> None:
        """
        Start sending to all chats you've ever interacted in

        Args:
            message (str): set a text message
            image (str): set image to message
            document (str): set document to message
            video (str): set video to message
            audio (str): set audio to message
            parse_mode (str): 'markdown', 'html', or None
            delay_time (float): delay time between sending emails
        """
        if message is not None:
            self.set_message(message)
        if image is not None:
            self.set_image(image)
        if document is not None:
            self.set_document(document)
        if video is not None:
            self.set_video(video)
        if audio is not None:
            self.set_audio(audio)
        if parse_mode is not None:
            self.set_parse_mode(parse_mode)

        kwargs = {'parse_mode': self.parse_mode} if self.parse_mode else {}
        all_chats = self.get_chats()
        
        with alive_bar(len(all_chats), force_tty=True) as bar:
            for chat in all_chats:
                if self.image:
                    self.user.send_photo(chat['id'], self.image, caption=self.message, **kwargs)
                elif self.video:
                    self.user.send_video(chat['id'], self.video, caption=self.message, **kwargs)
                elif self.document:
                    self.user.send_document(chat['id'], self.document, caption=self.message, **kwargs)
                elif self.audio:
                    self.user.send_audio(chat['id'], self.audio, caption=self.message, **kwargs)
                else:
                    self.user.send_message(chat['id'], self.message, **kwargs)
                time.sleep(delay_time)
                bar()

    def start_bombing(self,
                      user_id: int,
                      amount: int,
                      message: str = None,
                      image: str = None,
                      document: str = None,
                      video: str = None,
                      audio: str = None,
                      parse_mode: str = None,
                      delay_time: float = 1.5
                      ) -> None:
        """
        Start bombarding one user with messages

        Args:
             user_id (int): user ID
             amount (int): number of sent messages
             message (str): set a text message
             image (str): set image to message
             document (str): set document to message
             video (str): set video to message
             audio (str): set audio to message
             parse_mode (str): 'markdown', 'html', or None
             delay_time (float): delay time between sending emails
        """
        if message is not None:
            self.set_message(message)
        if image is not None:
            self.set_image(image)
        if document is not None:
            self.set_document(document)
        if video is not None:
            self.set_video(video)
        if audio is not None:
            self.set_audio(audio)
        if parse_mode is not None:
            self.set_parse_mode(parse_mode)

        kwargs = {'parse_mode': self.parse_mode} if self.parse_mode else {}

        with alive_bar(amount, force_tty=True) as bar:
            for i in range(amount):
                if self.image:
                    self.user.send_photo(user_id, self.image, caption=self.message, **kwargs)
                elif self.video:
                    self.user.send_video(user_id, self.video, caption=self.message, **kwargs)
                elif self.document:
                    self.user.send_document(user_id, self.document, caption=self.message, **kwargs)
                elif self.audio:
                    self.user.send_audio(user_id, self.audio, caption=self.message, **kwargs)
                else:
                    self.user.send_message(user_id, self.message, **kwargs)
                time.sleep(delay_time)
                bar()

    def send_message(self,
                     user_id: int,
                     message: str = None,
                     image: str = None,
                     document: str = None,
                     video: str = None,
                     audio: str = None,
                     parse_mode: str = None
                     ) -> None:
        """
        Normally send a message to a user

        Args:
            user_id (int): user ID
            message (str): set a text message
            image (str): set image to message
            document (str): set document to message
            video (str): set video to message
            audio (str): set audio to message
            parse_mode (str): 'markdown', 'html', or None
        """
        if message is not None:
            self.set_message(message)
        if image is not None:
            self.set_image(image)
        if document is not None:
            self.set_document(document)
        if video is not None:
            self.set_video(video)
        if audio is not None:
            self.set_audio(audio)
        if parse_mode is not None:
            self.set_parse_mode(parse_mode)

        kwargs = {'parse_mode': self.parse_mode} if self.parse_mode else {}

        if self.image:
            self.user.send_photo(user_id, self.image, caption=self.message, **kwargs)
        elif self.video:
            self.user.send_video(user_id, self.video, caption=self.message, **kwargs)
        elif self.document:
            self.user.send_document(user_id, self.document, caption=self.message, **kwargs)
        elif self.audio:
            self.user.send_audio(user_id, self.audio, caption=self.message, **kwargs)
        else:
            self.user.send_message(user_id, self.message, **kwargs)

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

    def get_user_info(self, user_id: int) -> dict:
        """
        Get information about a user by their ID

        Args:
            user_id (int): user ID
        Return:
            dict: user information (first_name, last_name, username, phone, etc.)
        """
        try:
            user = self.user.get_users(user_id)
            return {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'username': user.username,
                'phone': user.phone_number,
                'is_bot': user.is_bot,
                'is_verified': user.is_verified,
                'is_premium': user.is_premium if hasattr(user, 'is_premium') else False
            }
        except Exception as e:
            print(f"Error getting user info: {e}")
            return None
