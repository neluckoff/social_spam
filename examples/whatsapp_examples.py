from social_spam import WhatsApp

wp = WhatsApp()
# How not to log in, the browser opens

# The first variation of sending a message
wp.set_message('Test')
wp.set_image('C:/Users/user/Desktop/img.png')
wp.set_phone('+79266666666')
wp.send_message()

# The second variation of sending a message
wp.send_message(phone='+79266666666', text='Test', image='C:/Users/user/Desktop/img.png')

# The first variation of sending spam
wp.set_phones(['+79266666666', '+79266666667', '+79266666668'])
wp.set_message('Test')
wp.set_image('C:/Users/user/Desktop/img.png')
wp.start_spamming()

# The second variation of sending spam
phones = ['+79266666666', '+79266666667', '+79266666668']
wp.start_spamming(phones=phones, text='Test', image='C:/Users/user/Desktop/img.png')

# Start bombarding one user with messages
wp.start_bombing('+79266666666', 100)
# Or so
wp.start_bombing('+79266666666', 100, text='Hello')
