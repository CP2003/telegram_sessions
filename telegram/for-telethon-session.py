try:
    from telethon import TelegramClient
    from telethon.sessions import StringSession 
    import asyncio
    import sys
except Exception as e:
    print(e)
    print('\nInstall pyrogram: pip install Telethon')
    exit(1)
    

print('Loading telethon session generator...')
API_KEY = int(input('Enter API KEY: '))
API_HASH = input('Enter API HASH: ')


async def starting_generator():
    client = TelegramClient(StringSession(), API_KEY, API_HASH)
    await client.start()
    async with client:
        session = client.session.save()
        message = f"Here is Your session string \n\n ```{session}```"
        await client.send_message('me', message)
        print("Done , Session string has been sent to your saved message. Now you can Close this")
        await asyncio.sleep(5)
        sys.exit()
        

async def main():
    try:
        await starting_generator()
    except:
        pass

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.create_task(main())
        loop.run_forever()
    finally:
        loop.close()
