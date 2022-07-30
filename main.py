from social_spam import Telegram
from social_spam import Vkontakte

# tg = Telegram()
# tg.set_message("Проверка 2")
# tg.set_image('C:/Users/neluc/Desktop/img.png')
# tg.connect_user(api_id=10401485, api_hash="45cd83d78bf702173b8d875a62a7e12f", phone_number="89266715863")
# print(tg.get_chats())
# tg.start_selective_spam([358984161])

if __name__ == '__main__':
    vk = Vkontakte()
    vk.connect_user('vk1.a.V4yq6osDapxJUCAsnxhPtt5AGEJ-42A5vp3zfG94afFQTNDCIuhbcEhI9FrVj7TbrklIZEaB0D0xRugcGazNKIVfa--Zh7LTMNmCfLy2Vsvbh2DtH2D4KtCGE5M3AtPnlhiPAgldQNZrY0FgKqFnRfsTXCgs8Uz0OYadsO-Bpc0PLAf-x56V41ja0LFLCWoF')
    vk.set_message('Hi')
    vk.set_image('C:/Users/neluc/Desktop/img.png')
    # print(vk.get_chats_id())
    vk.start_selective_spam([146653997])
    # vk.start_all_spam()

