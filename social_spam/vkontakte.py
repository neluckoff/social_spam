import vk_api
import time

from pathlib import Path
from random import randint
from alive_progress import alive_bar


class Vkontakte:

    def __init__(self) -> None:
        self.user = None
        self.vk = None
        self.message = None
        self.image = None

    def connect_user(self, token: str) -> None:
        self.user = vk_api.VkApi(token=token)
        self.vk = self.user.get_api()

    def get_chats_id(self) -> list:
        chats = []
        for chat in self.vk.messages.getConversations(extended=1)['items']:
            chats.append(chat['conversation']['peer']['id'])
        for chat in self.vk.messages.getConversations(extended=1)['profiles']:
            chats.append(chat['id'])
        return chats

    def set_message(self, message: str) -> None:
        self.message = message

    def set_file_message(self, path) -> None:
        if Path(path).is_file() and (Path(path).suffix == ".txt" or Path(path).suffix == ".md"):
            md_str = ''
            with open(path, "r", encoding="utf-8") as file:
                for line in file:
                    md_str += line
            self.message = md_str

    def check_message(self) -> None:
        self.vk.messages.send(user_id=self.vk.users.get()[0]['id'], message=self.message, random_id=0)

    def get_user(self) -> list:
        return self.vk.users.get()[0]

    def set_image(self, path) -> None:
        if Path(path).is_file() and (Path(path).suffix == ".png" or Path(path).suffix == ".jpg"
                                     or Path(path).suffix == ".jpeg"):
            upload = vk_api.VkUpload(self.vk)
            photo = upload.photo_messages(path)
            owner_id = photo[0]['owner_id']
            photo_id = photo[0]['id']
            access_key = photo[0]['access_key']
            self.image = f'photo{owner_id}_{photo_id}_{access_key}'

    def start_selective_spam(self, chats: list) -> None:
        print('[Vkontakte] Starting selective spamming...')
        with alive_bar(len(chats), force_tty=True) as bar:
            for id in chats:
                if str(abs(id)).isdigit():
                    if self.image is None:
                        self.vk.messages.send(user_id=abs(id), message=self.message, random_id=0)
                        time.sleep(randint(1, 3))
                        bar()
                    else:
                        self.vk.messages.send(user_id=abs(id), message=self.message, random_id=0,
                                              attachment=self.image)
                        time.sleep(randint(1, 3))
                        bar()
                else:
                    print(f'{id} is not ID')

    def start_all_spam(self) -> None:
        print('[Vkontakte] Start spamming all chats...')
        chats = self.get_chats_id()
        with alive_bar(len(chats), force_tty=True) as bar:
            for chat in chats:
                if self.image is None:
                    self.vk.messages.send(user_id=abs(chat), message=self.message, random_id=0)
                    time.sleep(randint(1, 3))
                    bar()
                else:
                    self.vk.messages.send(user_id=abs(chat), message=self.message, random_id=0,
                                          attachment=self.image)
                    time.sleep(randint(1, 3))
                    bar()

    def start_bombing(self, user_id: int, amount: int) -> None:
        print(f'[Vkontakte] Start bombing {user_id}')
        with alive_bar(amount, force_tty=True) as bar:
            for i in range(amount):
                if self.image is not None:
                    self.vk.messages.send(user_id=abs(user_id), message=self.message, random_id=0,
                                          attachment=self.image)
                    time.sleep(1.5)
                    bar()
                else:
                    self.vk.messages.send(user_id=abs(user_id), message=self.message, random_id=0)
                    time.sleep(1.5)
                    bar()

    def send_message(self, user_id: int) -> None:
        if self.image is not None:
            self.vk.messages.send(user_id=abs(user_id), message=self.message, random_id=0,
                                  attachment=self.image)
        else:
            self.vk.messages.send(user_id=abs(user_id), message=self.message, random_id=0)

