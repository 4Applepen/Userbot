#   Copyright 2019 - 2020 DarkPrinc3

#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at

#       http://www.apache.org/licenses/LICENSE-2.0

#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

# if you change credits, you get anal cancer and get murdered by russians in 3 days.
"""
Support chatbox for pmpermit.
Used by incoming messages with trigger as /start
Will not work for already approved people.
Credits: written by ༺αиυвιѕ༻ {@A_Dark_Princ3}
"""
import asyncio
import io 
import telethon.sync
from telethon.tl.functions.users import GetFullUserRequest
import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql
from telethon import events, errors, functions, types
from userbot import ALIVE_NAME, LESS_SPAMMY
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Settati un nome su heroku. ALIVE_NAME "
PREV_REPLY_MESSAGE = {}


@command(pattern=r"\/start", incoming=True)
async def _(event):
    chat_id = event.from_id
    userid = event.sender_id
    if not pmpermit_sql.is_approved(chat_id):
        chat = await event.get_chat()
        if event.fwd_from:
            return
        if event.is_private:
         Nudas = ("__Indica il tuo sesso.__\n"
                  "`1`. Femmina Homo-Sapien\n"
                  "`2`. Maschio Homo-Sapien\n"
                  "`3`. Altro\n")
         PM = ("`Ciao. Stai accedendo al menù disponibile del mio capo,`"
               f"{DEFAULTUSER}.\n"
               "__Facciamo veloce e fammi sapere perché sei qui.__\n"
               "**Scegli una di queste risposte:**\n\n"
               "`1`. Messaggiare con il mio capo\n"
               "`2`. Spammare al mio capo\n"
               "`3`. Inviare nudes.\n"
               "`4`. Chiedere qualcosa\n"
               "`5`. Per richiedere qualcosa\n")
         ONE = ("__La tua richiesta è stata registrata, attenti almeno 24 ore prima dicevere una risposta. e non spammare grazie.__\n\n"
                "**⚠️ Sei stato bloccato e reportatp per spam. ⚠️**\n\n"
                "__Usa__ `/start` __Per tornare indietro col menù.__")
         TWO = (" `███████▄▄███████████▄  \n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓███░░░░░░░░░░░░█\n██████▀▀▀█░░░░██████▀  \n░░░░░░░░░█░░░░█  \n░░░░░░░░░░█░░░█  \n░░░░░░░░░░░█░░█  \n░░░░░░░░░░░█░░█  \n░░░░░░░░░░░░▀▀ `\n\n**Sei stato bloccato, vai a disturbare qualcun'altro.**")
         FOUR = ("__Il mio padrone risponde sempre a tutti, non correre e aspetta. altrimenti sono costretto a bloccarti.**")
         FIVE = ("`Non disturbare ancora il mio padrone o sono costretto a bloccarti e reportarti per spam.**")
         LWARN = ("**Ultimo avviso NON mandare più messaggi o ti blocco e reporto per spam, usa /start per tornare indietro.__")
     
        async with borg.conversation(chat) as conv:
         await borg.send_message(chat, PM)
         chat_id = event.from_id
         response = await conv.get_response(chat)
         y = response.text
         if y == "1":
             await borg.send_message(chat, ONE)
             response = await conv.get_response(chat)
             await event.delete()
             if not response.text == "/start":
                 await response.delete()
                 await borg.send_message(chat, LWARN)
                 response = await conv.get_response(chat)
                 await event.delete()
                 await response.delete()
                 response = await conv.get_response(chat)
                 if not response.text == "/start":
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
         elif y == "2":
             await borg.send_message(chat, LWARN)
             response = await conv.get_response(chat)
             if not response.text == "/start":
                 await borg.send_message(chat, TWO)
                 await asyncio.sleep(3)
                 await event.client(functions.contacts.BlockRequest(chat_id))
         elif y == "3":
             await borg.send_message(chat, Nudas)
             response = await conv.get_response(chat)
             await event.delete()
             await response.delete()
             x = response.text
             if x == "1":
                 await borg.send_message(chat, "`Oh my, you're very much welcome here ;).\nPlease drop your offerings and let my master judge if you have good heart <3.`\n\n **Please don't flood my inbox, we'll have a nice convo once i come back ;D**")
                 response = await conv.get_response(chat)
                 if not response.text == "/start":
                     await borg.send_message(chat, LWARN)
                     response = await conv.get_response(chat)
                     await event.delete()
                     await response.delete()
                     response = await conv.get_response(chat)
                     if not response.text == "/start":
                         await borg.send_message(chat, TWO)
                         await asyncio.sleep(3)
                         await event.client(functions.contacts.BlockRequest(chat_id))
             elif x == "2":
                 await borg.send_message(chat, "**You nigga gay af to send a guy like my your male nudes. \nLeave immediately else you become the ultimate gayest gay the gay world has ever seen. I will reply you when i get online.**")
                 response = await conv.get_response(chat)
                 if not response.text == "/start":
                     await borg.send_message(chat, LWARN)
                     response = await conv.get_response(chat)
                     await event.delete()
                     await response.delete()
                     response = await conv.get_response(chat)
                     if not response.text == "/start":
                         await borg.send_message(chat, TWO)
                         await asyncio.sleep(3)
                         await event.client(functions.contacts.BlockRequest(chat_id))
             elif x == "3":
                 await borg.send_message(chat, "`Please decide a gender for yourself before sending your nudes here,\n not that i'm judging if you're a helicopter or a banana but yeah, If you are anything else than a female Homo-Sapien,\n Do not send more messages and let my master see for himself if he wants to talk with you.`")
                 response = await conv.get_response(chat)
                 if not response.text == "/start":
                     await borg.send_message(chat, LWARN)
                     response = await conv.get_response(chat)
                     await event.delete()
                     await response.delete()
                     response = await conv.get_response(chat)
                     if not response.text == "/start":
                         await borg.send_message(chat, TWO)
                         await asyncio.sleep(3)
                         await event.client(functions.contacts.BlockRequest(chat_id))
             else:
                 await borg.send_message(chat, "__You have entered an invalid command. Please send__ `/start` __again or do not send another message if you do not wish to be blocked and reported.__")
                 response = await conv.get_response(chat)
                 if not response.text.startswith("/start"):
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
         elif y == "4":
             await borg.send_message(chat, FOUR)
             response = await conv.get_response(chat)
             await event.delete()
             await response.delete()
             if not response.text == "/start":
                 await borg.send_message(chat, LWARN)
                 await event.delete()
                 response = await conv.get_response(chat)
                 if not response.text == "/start":
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
         elif y == "5":
             await borg.send_message(chat,FIVE)
             response = await conv.get_response(chat)
             if not response.text == "/start":
                 await borg.send_message(chat, LWARN)
                 response = await conv.get_response(chat)
                 if not response.text == "/start":
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
         else:
             await borg.send_message(chat, "`You have entered an invalid command. Please send /start again or do not send another message if you do not wish to be blocked and reported.`")
             response = await conv.get_response(chat)
             z = response.text
             if not z == "/start":
                 await borg.send_message(chat, LWARN)
                 await conv.get_response(chat)
                 if not response.text == "/start":
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))


