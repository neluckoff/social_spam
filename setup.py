from io import open
from setuptools import setup

version = '1.3.0'

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
    install_requires=[
        'alive-progress>=3.0.0',
        'pyrogram>=2.0.0',
        'vk-api>=11.9.0',
        'pywhatkit>=5.0',
        'TgCrypto>=1.2.0'
    ],
    python_requires='>=3.8',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ]
)
