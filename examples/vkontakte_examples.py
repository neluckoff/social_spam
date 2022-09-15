from social_spam import Vkontakte

user_token = 'AD12jsd1Ad23...'
# a personal token of your account with access to messages, friends and access at any time.

vk = Vkontakte()
vk.connect_user(token=user_token)
# The token can be obtained from the link: https://vkhost.github.io/

# Get information about all chats
vk.get_chats_id()

# The first variation of sending a message
vk.set_message('Hi!')
vk.set_image('./image.png')
vk.send_message(146653997)

# Get name by user ID
name = vk.get_name_by_id(146653997)['first_name']

# The second variation of sending a message
vk.send_message(146653997, message=f'Hi, {name}!', image='./image.png')

# Start spamming by user list
vk.start_selective_spam([146653997, 146653998, 146653999])
# Or so
vk.start_selective_spam([146653997, 146653998, 146653999], message='Hi!')

# Start spamming all users you've chatted with
vk.start_all_spam()

# Start bombarding one user with messages
vk.start_bombing(146653997, message='BOOM!')
