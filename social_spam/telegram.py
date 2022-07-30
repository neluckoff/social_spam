import time

from pyrogram import Client
from random import randint
from pathlib import Path
from alive_progress import alive_bar


class Telegram:

    def __init__(self):
        self.user = None
        self.message = None
        self.image = None

    def connect_user(self, api_id: int, api_hash: str, phone_number: str):
        self.user = Client("my_account", api_id=api_id, api_hash=api_hash, phone_number=phone_number).start()

    def set_message(self, message: str):
        self.message = message

    def set_file_message(self, path):
        if Path(path).is_file() and (Path(path).suffix == ".md" or Path(path).suffix == ".txt"):
            md_str = ''
            with open(path, "r", encoding="utf-8") as file:
                for line in file:
                    md_str += line
            self.message = md_str

    def set_image(self, path):
        if Path(path).is_file() and (Path(path).suffix == ".png" or Path(path).suffix == ".jpg"
                                     or Path(path).suffix == ".jpeg"):
            self.image = path

    def check_message(self):
        if self.image is None:
            self.user.send_message('me', self.message)
        else:
            self.user.send_photo('me', self.image, caption=self.message)

    def get_chats(self):
        chats = []
        for dialog in self.user.get_dialogs():
            chats.append({'dialog': dialog.chat.first_name or dialog.chat.title, 'id': dialog.chat.id})
        return chats

    def get_user(self):
        return self.user

    def start_selective_spam(self, chats: list):
        print('[Telegram] Starting selective spamming...')
        with alive_bar(len(chats), force_tty=True) as bar:
            for id in chats:
                if str(id).isdigit():
                    if self.image is not None:
                        self.user.send_photo(id, self.image, caption=self.message)
                        time.sleep(randint(1, 3))
                        bar()
                    else:
                        self.user.send_message(id, self.message)
                        time.sleep(randint(1, 3))
                        bar()
            else:
                print(f'{id} is not ID')

    def start_all_spam(self):
        print('[Telegram] Start spamming all chats...')
        all_chats = self.get_chats()
        with alive_bar(len(all_chats), force_tty=True) as bar:
            for chat in all_chats:
                if self.image is None:
                    self.user.send_message(chat['id'], self.message)
                    time.sleep(randint(1, 3))
                    bar()
                else:
                    self.user.send_photo(chat['id'], self.image, caption=self.message)
                    time.sleep(randint(1, 3))
                    bar()

    def start_bombing(self, user_id: int, amount: int):
        print(f'[Telegram] Start bombing {user_id}')
        with alive_bar(amount, force_tty=True) as bar:
            for i in range(amount):
                if self.image is not None:
                    self.user.send_photo(chat['id'], self.image, caption=self.message)
                    time.sleep(1.5)
                    bar()
                else:
                    self.user.send_message(chat['id'], self.message)
                    time.sleep(1.5)
                    bar()

    def send_message(self, user_id: int):
        if self.image is not None:
            self.user.send_photo(user_id, self.image, caption=self.message)
        else:
            self.user.send_message(user_id, self.message)
