from social_spam import Telegram

tg = Telegram()
tg.connect_user(api_id=1234, api_hash="h1s2l3...", phone_number="89266666666")
# api_id and api_hash can be obtained from this link by creating an application:
# https://my.telegram.org/auth

# Get information about all chats
tg.get_chats()

# The first variation of sending a message
tg.set_message("Hi! I'm using social_spam package")
tg.set_image('C:/Users/user/Desktop/img.png')
tg.send_message(358984161)

# The second option for sending a message with ID taken by phone number
user_id = tg.get_id_by_phone('79269019999')
tg.send_message(user_id=user_id, message="Hi! I'm using social_spam package",
                image='C:/Users/user/Desktop/img.png')

# Start spamming by user list
users_list = [358984161, 358984162, 358984163, 358984164]
tg.start_selective_spam(users_list, message='Hi')
# Or so
tg.start_selective_spam(users_list)
# if the text you have already set

# Start spamming all users you've chatted with
tg.start_all_spam()

# Start bombarding one user with messages
tg.start_bombing(358984161, 100, message='Hey, bro!')
