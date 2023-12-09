try:
    from telethon.sync import TelegramClient
    from telethon.sessions import StringSession
except Exception as e:
    print(e)
    print('\nInstall pyrogram: pip install Telethon')
    exit(1)

print('Loading telethon session generator...')
API_KEY = int(input('Enter API KEY: '))
API_HASH = input('Enter API HASH: ')
with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
    print(client.session.save())
