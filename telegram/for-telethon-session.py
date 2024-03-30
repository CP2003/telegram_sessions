import os
import sys
import asyncio

try:
    from telethon import TelegramClient
    from telethon.sessions import StringSession 
except Exception as e:
    print("Intalling telethon")
    os.system("pip install Telethon")
    os.system('cls') if os.name == 'nt' else os.system('clear')
    from telethon import TelegramClient
    from telethon.sessions import StringSession 

    

print('Loading telethon session generator...')
API_KEY = int(input('Enter API KEY: '))
API_HASH = input('Enter API HASH: ')


async def starting_generator():
    os.system('cls') if os.name == 'nt' else os.system('clear')
    client = TelegramClient(StringSession(), API_KEY, API_HASH)
    await client.start()
    async with client:
        session = client.session.save()
        message = f"Here is Your session string \n\n ```{session}```"
        await client.send_message('me', message)
        os.system('cls') if os.name == 'nt' else os.system('clear')
        print("Done , Session string has been sent to your saved message. Now you can Close this")
        await client.disconnect()
        sys.exit(1)
        

async def main():
    try:
        await starting_generator()
    except:
        pass

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
