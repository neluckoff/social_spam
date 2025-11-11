"""
Telegram Examples for social_spam package

This file contains various examples of using the Telegram module.

Requirements:
- api_id and api_hash from https://my.telegram.org/auth
- Your Telegram phone number
- Pyrogram installed (installed automatically with social_spam)

Documentation: https://github.com/neluckoff/social_spam
"""

from social_spam import Telegram

# ============================================================================
# STEP 1: INITIALIZE AND CONNECT
# ============================================================================

tg = Telegram()

# Connect to your Telegram account
# Get api_id and api_hash from: https://my.telegram.org/auth
tg.connect_user(
    api_id=1234,                    # Your API ID
    api_hash="your_api_hash_here",  # Your API Hash
    phone_number="+1234567890"      # Your phone number with country code
)

# ============================================================================
# STEP 2: GET INFORMATION
# ============================================================================

# Get list of all your chats with IDs
all_chats = tg.get_chats()
print("Your chats:", all_chats)

# Get your own Telegram user info
me = tg.get_me()
print("My info:", me)

# ============================================================================
# STEP 3: BASIC MESSAGE SENDING
# ============================================================================

# Method 1: Set message first, then send
tg.set_message("Hi! I'm using social_spam package")
tg.send_message(user_id=123456789)

# Method 2: Send message directly
tg.send_message(
    user_id=123456789,
    message="Hello from social_spam!"
)

# ============================================================================
# STEP 4: SENDING WITH IMAGES
# ============================================================================

# Method 1: Set image and message separately
tg.set_message("Check out this image!")
tg.set_image('path/to/image.png')
tg.send_message(user_id=123456789)

# Method 2: Send with image directly
tg.send_message(
    user_id=123456789,
    message="Look at this!",
    image='path/to/image.jpg'
)

# ============================================================================
# STEP 5: ADVANCED - GET USER ID BY PHONE
# ============================================================================

# Get user ID by phone number (adds and removes temporary contact)
user_id = tg.get_id_by_phone('+79261234567')
if user_id:
    tg.send_message(user_id=user_id, message="Found you by phone!")
else:
    print("User not found")

# ============================================================================
# STEP 6: MASS MESSAGING - SELECTIVE SPAM
# ============================================================================

# Send message to specific list of users
users_list = [123456789, 987654321, 111222333]

# Option 1: With message parameter
tg.start_selective_spam(
    chats=users_list,
    message='Important announcement!',
    delay_time=2.0  # Wait 2 seconds between messages
)

# Option 2: Use pre-set message
tg.set_message("Hello everyone!")
tg.start_selective_spam(chats=users_list, delay_time=1.5)

# Option 3: With image
tg.start_selective_spam(
    chats=users_list,
    message='Check this out!',
    image='announcement.png',
    delay_time=2.0
)

# ============================================================================
# STEP 7: MASS MESSAGING - ALL CONTACTS
# ============================================================================

# Send message to ALL your contacts (use with caution!)
tg.start_all_spam(
    message='Mass announcement to everyone!',
    delay_time=3.0  # Longer delay to avoid rate limits
)

# ============================================================================
# STEP 8: MESSAGE BOMBING (Use Responsibly!)
# ============================================================================

# Send multiple messages to one user
tg.start_bombing(
    user_id=123456789,
    amount=10,                      # Number of messages
    message='Repeated message',
    delay_time=1.0                  # Delay between messages
)

# Bombing with image
tg.start_bombing(
    user_id=123456789,
    amount=5,
    message='Check this repeatedly!',
    image='important.png',
    delay_time=2.0
)

# ============================================================================
# STEP 9: ADVANCED - LOAD MESSAGE FROM FILE
# ============================================================================

# Load message from text file
tg.set_file_message('message.txt')  # .txt or .md file
tg.send_message(user_id=123456789)

# ============================================================================
# STEP 10: TEST YOUR MESSAGE
# ============================================================================

# Send test message to yourself
tg.set_message("Testing my message before mass send")
tg.set_image('test_image.png')  # Optional
tg.check_message()  # Sends to 'me' (yourself)

# ============================================================================
# BEST PRACTICES
# ============================================================================

"""
1. Rate Limiting:
   - Telegram allows ~20-30 messages per minute
   - Use delay_time >= 2 seconds for safety
   - Longer delays for mass operations

2. Security:
   - Never commit your api_id and api_hash to git
   - Use environment variables in production
   - Keep your session file (.session) private

3. Error Handling:
   try:
       tg.send_message(user_id, "Hello!")
   except Exception as e:
       print(f"Error: {e}")

4. Clean Up:
   - Session files are created automatically
   - Keep them safe, they contain your auth data
   - Add *.session to .gitignore
"""

# ============================================================================
# EXAMPLE: PRODUCTION-READY CODE
# ============================================================================

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Use environment variables for credentials
API_ID = os.getenv('TELEGRAM_API_ID')
API_HASH = os.getenv('TELEGRAM_API_HASH')
PHONE = os.getenv('TELEGRAM_PHONE')

if API_ID and API_HASH and PHONE:
    tg_prod = Telegram()
    tg_prod.connect_user(
        api_id=int(API_ID),
        api_hash=API_HASH,
        phone_number=PHONE
    )
    
    # Your production code here
    # tg_prod.send_message(...)
else:
    print("Please set environment variables: TELEGRAM_API_ID, TELEGRAM_API_HASH, TELEGRAM_PHONE")
