#credits: @r4v4n4
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.utils import admin_cmd

@borg.on(admin_cmd("frybot ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```rispomdi ad un messaggio.```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.media:
       await event.edit("```rispondi a un messaggio di testo```")
       return
    chat = "@image_deepfrybot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```Rispondi al messaggio degli utenti effettivi.```")
       return
    await event.edit("```Processo```")
    async with borg.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=432858024))
              await borg.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Sblocca @sangmatainfo_bot e riprova```")
              return
          if response.text.startswith("Forward"):
              await event.edit("```puoi gentilmente disabilitare le tue impostazioni sulla privacy per sempre?```")
          else: 
              await borg.send_file(event.chat_id, response.message.media)
