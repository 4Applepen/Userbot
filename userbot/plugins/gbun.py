# This is a troll indeed ffs *facepalm*
import asyncio
from telethon import events
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.utils import admin_cmd


@borg.on(admin_cmd("gbun"))
async def gbun(event):
    if event.fwd_from:
        return
    gbunVar = event.text
    gbunVar = gbunVar[6:]
    mentions = "`Attenzione!! Utente 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 dall'admin!!...\n`"
    no_reason = "__Motivo: Hai meno diritti di una donna normale. __"
    await event.edit("**Evocando le Gungnir ❗️⚜️☠️**")
    asyncio.sleep(3.5)
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.from_id))
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.from_id
        # make meself invulnerable cuz why not xD
        if idd == 742506768:
            await reply_message.reply("`Aspetta un secondo, questo è il mio padrone! `\n ** Come osi minacciare di bandire il mio padrone negro! ** \n \n__Il tuo account è stato violato! Paga 69 $ al mio padrone__ [sqdboyuwu] (tg://user?Id=1229604694) __per liberare il tuo account__😏")
        else:
            jnl=("`Warning!! `"
                  "[{}](tg://user?id={})"
                  "` 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 By Admin...\n\n`"
                  "**First Name: ** __{}__\n"
                  "**ID : ** `{}`\n"
                ).format(firstname, idd, firstname, idd)
            if usname == None:
                jnl += "**Nome utente della vittima Nigga: ** `Non possiede un nome utente!`\n"
            elif usname != "None":
                jnl += "**Vittima username** : @{}\n".format(usname)
            if len(gbunVar) > 0:
                gbunm = "`{}`".format(gbunVar)
                gbunr = "**Motivo: **"+gbunm
                jnl += gbunr
            else:
                jnl += no_reason
            await reply_message.reply(jnl)
    else:
        mention = "`Attenzione!! Utente 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 dall'admin!!...\nMotivo: Hai meno diritti di una donna normale. `"
        await event.reply(mention)
    await event.delete()
