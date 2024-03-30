import os
import sys
import asyncio
try:
    from pyrogram import Client
except:
    print("Intalling telethon")
    os.system("pip install Telethon")
    os.system('cls') if os.name == 'nt' else os.system('clear')
    from pyrogram import Client

API_KEY = int(input('Enter API KEY: '))
API_HASH = input('Enter API HASH: ')
with Client(name='USS', api_id=API_KEY, api_hash=API_HASH, in_memory=True) as app:
    os.system('cls') if os.name == 'nt' else os.system('clear')
    print("Here is your session")
    print(app.export_session_string())
