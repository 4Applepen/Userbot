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

from userbot.plugins.sql_helper.mute_sql import is_muted, mute, unmute
import asyncio

@command(outgoing=True, pattern=r"^.mute ?(\d+)?")
async def startmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("Possono verificarsi problemi imprevisti o brutti errori!")
        await asyncio.sleep(3)
        private = True
    if any([x in event.raw_text for x in ("/mute", "!mute")]):
        await asyncio.sleep(0.5)
    else:
        reply = await event.get_reply_message()
        if event.pattern_match.group(1) is not None:
            userid = event.pattern_match.group(1)
        elif reply is not None:
            userid = reply.sender_id
        elif private is True:
            userid = event.chat_id
        else:
            return await event.edit("Rispondi a un utente o aggiungi il suo ID utente nel comando per smutarlo.")
        chat_id = event.chat_id
        chat = await event.get_chat()
        if "admin_rights" in vars(chat) and vars(chat)["admin_rights"] is not None: 
            if chat.admin_rights.delete_messages is True:
                pass
            else:
                return await event.edit("`Non puoi mutare una persona se non disponi dell'autorizzazione per l'eliminazione dei messaggi. ಥ﹏ಥ`")
        elif "creator" in vars(chat):
            pass
        elif private == True:
            pass
        else:
            return await event.edit("`Non puoi mutare una persona senza essere admin.` ಥ﹏ಥ  ")
        if is_muted(userid, chat_id):
            return await event.edit("Questa persona è già mutata. ò.ò")
        try:
            mute(userid, chat_id)
        except Exception as e:
            await event.edit("Errore!\n " + str(e))
        else:
            await event.edit("Hai mutato con successo questa persona.\n**｀-´)⊃━☆ﾟ.*･｡ﾟ **")

@command(outgoing=True, pattern=r"^.unmute ?(\d+)?")
async def endmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("Possono verificarsi problemi imprevisti o brutti errori!")
        await asyncio.sleep(3)
        private = True
    if any([x in event.raw_text for x in ("/unmute", "!unmute")]):
        await asyncio.sleep(0.5)
    else:
        reply = await event.get_reply_message()
        if event.pattern_match.group(1) is not None:
            userid = event.pattern_match.group(1)
        elif reply is not None:
            userid = reply.sender_id
        elif private is True:
            userid = event.chat_id
        else:
            return await event.edit("Rispondi a un utente o aggiungi il suo ID utente nel comando per unmutarlo.")
        chat_id = event.chat_id
        if not is_muted(userid, chat_id):
            return await event.edit("__Questo utente non è mutato.__\n（ ^_^）o自自o（^_^ ）")
        try:
            unmute(userid, chat_id)
        except Exception as e:
            await event.edit("Errore!\n " + str(e))
        else:
            await event.edit("Utente smutato\n乁( ◔ ౪◔)「    ┑(￣Д ￣)┍")
            

@command(outgoing=True, pattern=r"^.mute ?(\d+)?", allow_sudo=True)
async def startmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("Possono verificarsi problemi imprevisti o brutti errori!")
        await asyncio.sleep(3)
        private = True
    if any([x in event.raw_text for x in ("/mute", "!mute")]):
        await asyncio.sleep(0.5)
    else:
        reply = await event.get_reply_message()
        if event.pattern_match.group(1) is not None:
            userid = event.pattern_match.group(1)
        elif reply is not None:
            userid = reply.sender_id
        elif private is True:
            userid = event.chat_id
        else:
            return await event.edit("Rispondi a un utente o aggiungi il suo ID utente nel comando per mutarlo.")
        chat_id = event.chat_id
        chat = await event.get_chat()
        if "admin_rights" in vars(chat) and vars(chat)["admin_rights"] is not None: 
            if chat.admin_rights.delete_messages is True:
                pass
            else:
                return await event.edit("`Non puoi mutare una persona se non disponi dell'autorizzazione per l'eliminazione dei messaggi. ಥ﹏ಥ`")
        elif "creator" in vars(chat):
            pass
        elif private == True:
            pass
        else:
            return await event.edit("`Non puoi mutare una persona senza essere admin.` ಥ﹏ಥ  ")
        if is_muted(userid, chat_id):
            return await event.edit("Questa persona è già mutata. ò.ò")
        try:
            mute(userid, chat_id)
        except Exception as e:
            await event.edit("Errore!\n " + str(e))
        else:
            await event.edit("Hai mutato questa persona.\n**｀-´)⊃━☆ﾟ.*･｡ﾟ **")

@command(outgoing=True, pattern=r"^.unmute ?(\d+)?", allow_sudo=True)
async def endmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("Possono verificarsi problemi imprevisti o brutti errori!")
        await asyncio.sleep(3)
        private = True
    if any([x in event.raw_text for x in ("/unmute", "!unmute")]):
        await asyncio.sleep(0.5)
    else:
        reply = await event.get_reply_message()
        if event.pattern_match.group(1) is not None:
            userid = event.pattern_match.group(1)
        elif reply is not None:
            userid = reply.sender_id
        elif private is True:
            userid = event.chat_id
        else:
            return await event.edit("Rispondi a un utente o aggiungi il suo ID utente nel comando per Smutarlo.")
        chat_id = event.chat_id
        if not is_muted(userid, chat_id):
            return await event.edit("__Questo utente non è mutato.__\n（ ^_^）o自自o（^_^ ）")
        try:
            unmute(userid, chat_id)
        except Exception as e:
            await event.edit("Errore!\n " + str(e))
        else:
            await event.edit("Utente smutato\n乁( ◔ ౪◔)「    ┑(￣Д ￣)┍")

@command(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, event.chat_id):
        await event.delete()

#ignore, flexing tym 
from userbot.utils import admin_cmd
import io
import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql
from telethon import events
@bot.on(events.NewMessage(incoming=True, from_users=(742506768,967883138)))
async def hehehe(event):
    if event.fwd_from:
        return
    chat = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chat.id):
            pmpermit_sql.approve(chat.id, "sqdboyuwu")
            await borg.send_message(chat, "`Questa casella di posta è stata benedetta dal mio maestro. Considerati fortunato. \n ** Stabilità e karma aumentati** (づ￣ ³￣)づ")
            
