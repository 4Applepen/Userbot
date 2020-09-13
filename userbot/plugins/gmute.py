from userbot.plugins.sql_helper.mute_sql import is_muted, mute, unmute
import asyncio

@command(outgoing=True, pattern=r"^.gmute ?(\d+)?")
async def startgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("Possono verificarsi problemi imprevisti o brutti errori!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit("Rispondi a un utente o aggiungilo al comando per disattivarlo.")
    chat_id = event.chat_id
    chat = await event.get_chat()
    if is_muted(userid, "gmute"):
        return await event.edit("Questo utente è già gmutato")
    try:
        mute(userid, "gmute")
    except Exception as e:
        await event.edit("Errore!\n " + str(e))
    else:
        await event.edit("Hai gmutato con successo")

@command(outgoing=True, pattern=r"^.ungmute ?(\d+)?")
async def endgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("Possono verificarsi problemi imprevisti o brutti errori!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit("Rispondi a un utente o aggiungilo al comando per riattivarlo.")
    chat_id = event.chat_id
    if not is_muted(userid, "gmute"):
        return await event.edit("Questo utente non è gmutato")
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await event.edit("Errore!\n " + str(e))
    else:
        await event.edit("Hai smutato questo utente.")

@command(outgoing=True, pattern=r"^.gmute ?(\d+)?", allow_sudo=True)
async def startgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("Possono verificarsi problemi imprevisti o brutti errori!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit("Rispondi a un utente o aggiungilo al comando per disattivarlo.")
    chat_id = event.chat_id
    chat = await event.get_chat()
    if is_muted(userid, "gmute"):
        return await event.edit("Questo utente è già gmutato")
    try:
        mute(userid, "gmute")
    except Exception as e:
        await event.edit("Errore!\n " + str(e))
    else:
        await event.edit("Utente gmutato con successo")

@command(outgoing=True, pattern=r"^.ungmute ?(\d+)?", allow_sudo=True)
async def endgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("Possono verificarsi problemi imprevisti o brutti errori!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit("Rispondi a un utente o aggiungilo al comando per riattivarlo.")
    chat_id = event.chat_id
    if not is_muted(userid, "gmute"):
        return await event.edit("Questo utente non è gmutato")
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await event.edit("Errore!\n " + str(e))
    else:
        await event.edit("Persona smutata con successo")

@command(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()
