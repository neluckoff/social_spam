from io import open
from setuptools import setup

version = '1.2.4'

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='social_spam',
    version=version,

    author='neluckoff',
    author_email='neluckoff@gmail.com',

    description=(
        u'Package for convenient work with messages in all popular instant messengers '
        u'On the current version, you have access to the following messengers: Telegram, WhatsApp, Vkontakte, Email '
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/neluckoff/social_spam/archive/main.zip',
    download_url='https://github.com/neluckoff/social_spam/archive/master.zip',

    license='MIT License, see LICENSE file',

    packages=['social_spam'],
    install_requires=['alive_progress', 'pyrogram', 'vk-api', 'pywhatkit', 'TgCrypto'],

    classifiers=[
        'License :: OSI Approved :: MIT License',
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)
