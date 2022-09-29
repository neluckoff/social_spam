from social_spam import Mail

mail = Mail()
mail.connect_mail('test@inbox.ru', 'my_password')
# use a separate password for applications as a password

mail.set_message('Message from luckoff', 'How are you?')
# Structure: set_message(header, message, attachments)
# or
mail.set_message('Message from luckoff', 'How are you?', ['tetx.txt', 'image.png'])
# or you can use html layout
mail.set_message_html('Click me', 'template.html')
# Structure: set_message_html(header, html_path, attachments)

# The second variation of sending a message
mail.send_message('friend@gmail.com')

# Start spamming by user list
mail.spam_messages(['friend1@gmail.com', 'friend2@gmail.com', 'friend3@gmail.com'], delay_time=1.5)

# Start bombarding one user with messages
mail.bombing_message('friend@gmail.com', 100)

# Change the server for sending the message (optional)
mail.set_server('smtp.mail.ru', 465)
