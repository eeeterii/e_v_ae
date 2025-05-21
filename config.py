import os
import pickle
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

os.system("clear")
print("""\033[031m

█▀▀ █░█ ▄▀█   █▀ █▀█ █░█ █▀█ █▀▀ █▀▀
██▄ ▀▄▀ █▀█   ▄█ █▄█ █▄█ █▀▄ █▄▄ ██▄

𝐃𝐞𝐯: @e_v_ae
""")

api_id = '26107707'
api_hash = 'e3774389da1ff2e49f3cfb38c2105c87'
session_string = input("أدخل كود الجلسة: ")
client = TelegramClient(StringSession(session_string), api_id, api_hash)
client.start()

session_name = 'Eva surce'
response_file = 'responss.pkl'
published_messages_file = 'publihed_messages.pkl'
muted_users_file = 'mute_usrs.pkl'
time_update_status_file = 'time_pdate_status.pkl'
channel_link_file = 'channel_lnk.pkl'
image_folder = 'path_to_image_older'
response_file = 'path_to_respons_file'
last_message_time_file = 'path_to_last_esage_time_file'
last_message_id_file = 'path_to_last_mesage_id_file'
responses = {}
user_last_message_time = {}
user_last_message_id = {}
user_last_message_time_sent = {}
active_publishing_tasks = {}
image_folder = "iage"

if not os.path.exists(image_folder):
    os.makedirs(image_folder)

def load_pickle_file(file_path, default_value):
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            return pickle.load(f)
    return default_value

responses = load_pickle_file(response_file, {})
published_messages = load_pickle_file(published_messages_file, [])
muted_users = load_pickle_file(muted_users_file, {})
channel_link = load_pickle_file(channel_link_file, None)
time_update_status = load_pickle_file(time_update_status_file, {'enabled': False})

user_last_message_time = {}
user_last_message_id = {}
user_last_message_time_sent = {}
active_publishing_tasks = {}
active_timers = {}
countdown_messages = {}