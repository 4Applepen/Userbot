# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""Filters
Available Commands:
.addblacklist
.listblacklist
.rmblacklist"""
import asyncio
import re
import userbot.plugins.sql_helper.blacklist_sql as sql
from telethon import events, utils
from telethon.tl import types, functions
from userbot.utils import admin_cmd


@borg.on(events.NewMessage(incoming=True))
async def on_new_message(event):
    # TODO: exempt admins from locks
    name = event.raw_text
    snips = sql.get_chat_blacklist(event.chat_id)
    for snip in snips:
        pattern = r"( |^|[^\w])" + re.escape(snip) + r"( |$|[^\w])"
        if re.search(pattern, name, flags=re.IGNORECASE):
            try:
                await event.delete()
            except Exception as e:
                await event.reply("Non ho l'autorizzazione CANCELLA in questa chat")
                sql.rm_from_blacklist(event.chat_id, snip.lower())
            break


@borg.on(admin_cmd("addblacklist ((.|\n)*)"))
async def on_add_black_list(event):
    text = event.pattern_match.group(1)
    to_blacklist = list(set(trigger.strip() for trigger in text.split("\n") if trigger.strip()))
    for trigger in to_blacklist:
        sql.add_to_blacklist(event.chat_id, trigger.lower())
    await event.edit("Fatto {} Aggiunto alla blacklist di questa chat.".format(len(to_blacklist)))


@borg.on(admin_cmd("listblacklist"))
async def on_view_blacklist(event):
    all_blacklisted = sql.get_chat_blacklist(event.chat_id)
    OUT_STR = "Blacklists in questa chat:\n"
    if len(all_blacklisted) > 0:
        for trigger in all_blacklisted:
            OUT_STR += f"👉 {trigger} \n"
    else:
        OUT_STR = "No blacklista, inizia con `.addblacklist`"
    if len(OUT_STR) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(OUT_STR)) as out_file:
            out_file.name = "blacklist.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption="BlackLists in questa chat",
                reply_to=event
            )
            await event.delete()
    else:
        await event.edit(OUT_STR)


@borg.on(admin_cmd("rmblacklist ((.|\n)*)"))
async def on_delete_blacklist(event):
    text = event.pattern_match.group(1)
    to_unblacklist = list(set(trigger.strip() for trigger in text.split("\n") if trigger.strip()))
    successful = 0
    for trigger in to_unblacklist:
        if sql.rm_from_blacklist(event.chat_id, trigger.lower()):
            successful += 1
    await event.edit(f"Rimosso {successful} / {len(to_unblacklist)} dalla blacklist")
