# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for purging unneeded messages(usually spam or ot). """

from asyncio import sleep

from telethon.errors import rpcbaseerrors

from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP
from userbot.utils import register, errors_handler


@register(outgoing=True, pattern="^.purge$")
@errors_handler
async def fastpurger(purg):
    """ For .purge command, purge all messages starting from the reply. """
    chat = await purg.get_input_chat()
    msgs = []
    count = 0

    async for msg in purg.client.iter_messages(chat,
                                               min_id=purg.reply_to_msg_id):
        msgs.append(msg)
        count = count + 1
        msgs.append(purg.reply_to_msg_id)
        if len(msgs) == 100:
            await purg.client.delete_messages(chat, msgs)
            msgs = []

    if msgs:
        await purg.client.delete_messages(chat, msgs)
    done = await purg.client.send_message(
        purg.chat_id,
        "`Messaggi cancellati velocemente!\n`Cancellati " + str(count) + " messaggi.",
    )

    if BOTLOG:
        await purg.client.send_message(
            BOTLOG_CHATID,
            "Cancellati in " + str(count) +)
    await sleep(2)
    await done.delete()


@register(outgoing=True, pattern="^.purgeme")
@errors_handler
async def purgeme(delme):
    """ For .purgeme, delete x count of your latest message."""
    message = delme.text
    count = int(message[9:])
    i = 1

    async for message in delme.client.iter_messages(delme.chat_id,
                                                    from_user='me'):
        if i > count + 1:
            break
        i = i + 1
        await message.delete()

    smsg = await delme.client.send_message(
        delme.chat_id,
        "`Messaggi cancellati velocemente!\n`Cancellati " + str(count) + " messaggi.",
    )
    if BOTLOG:
        await delme.client.send_message(
            BOTLOG_CHATID,
           "Cancellati in " + str(count) +)
    await sleep(2)
    i = 1
    await smsg.delete()


@register(outgoing=True, pattern="^.del$")
@errors_handler
async def delete_it(delme):
    """ For .del command, delete the replied message. """
    msg_src = await delme.get_reply_message()
    if delme.reply_to_msg_id:
        try:
            await msg_src.delete()
            await delme.delete()
            if BOTLOG:
                await delme.client.send_message(
                    BOTLOG_CHATID, "Messaggio cancellato")
        except rpcbaseerrors.BadRequestError:
            if BOTLOG:
                await delme.client.send_message(
                    BOTLOG_CHATID, "Non posso cancellare questo messaggio")


@register(outgoing=True, pattern="^.edit")
@errors_handler
async def editer(edit):
    """ For .editme command, edit your last message. """
    message = edit.text
    chat = await edit.get_input_chat()
    self_id = await edit.client.get_peer_id('me')
    string = str(message[6:])
    i = 1
    async for message in edit.client.iter_messages(chat, self_id):
        if i == 2:
            await message.edit(string)
            await edit.delete()
            break
        i = i + 1
    if BOTLOG:
        await edit.client.send_message(BOTLOG_CHATID,
                                       "La query di modifica è stata eseguita correttamente")


@register(outgoing=True, pattern="^.sd")
@errors_handler
async def selfdestruct(destroy):
    """ For .sd command, make seflf-destructable messages. """
    message = destroy.text
    counter = int(message[4:6])
    text = str(destroy.text[6:])
    await destroy.delete()
    smsg = await destroy.client.send_message(destroy.chat_id, text)
    await sleep(counter)
    await smsg.delete()
    if BOTLOG:
        await destroy.client.send_message(BOTLOG_CHATID,
                                          "sd query Con successo")


CMD_HELP.update({
    'purge':
    '.purge\
        \nFunzione: Tutti i messaggi da quello in replica.'
})

CMD_HELP.update({
    'purgeme':
    '.purgeme <x>\
        \nFunzione: cancella i tuoi messsaggi.'
})

CMD_HELP.update({"del": ".del\
\nFunzione: Cancella i messaggi che replichi."})

CMD_HELP.update({
    'edit':
    ".edit <newmessage>\
\nFunzione: Edita il tuo messaggio con <NuovoMessaggio>."
})

CMD_HELP.update({
    'sd':
    '.sd <x> <message>\
\nFunzione: Crea un messaggio con autodistruzione.\
\nMantieni i secondi sotto i 100 poiché mette il tuo bot in stato di stop.'
})
