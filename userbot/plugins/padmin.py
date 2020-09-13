"""Emoji

Available Commands:

.padmin"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 20)

    input_str = event.pattern_match.group(1)

    if input_str == "fadmin":

        await event.edit(input_str)

        animation_chars = [
        
            "**Promuovo utente ad admin...**",
            "**Abilito tutti i permessi ad utente...**",
            "**(1) Mandare Messaggi: ☑️**",
            "**(1) Mandare Messaggi: ✅**",
            "**(2) Mandare Media: ☑️**",
            "**(2) Mandare Media: ✅**",
            "**(3) Mandare Stickers & GIFs: ☑️**",
            "**(3) Mandare Stickers & GIFs: ✅**",    
            "**(4) Mandare Sondaggi: ☑️**",
            "**(4) Mandare Sondaggi: ✅**",
            "**(5) Incorporare Links: ☑️**",
            "**(5) Incorporare Links: ✅**",
            "**(6) Aggiungere Utenti: ☑️**",
            "**(6) Aggiungere Utenti: ✅**",
            "**(7) Fissare Messaggi: ☑️**",
            "**(7) Fissare Messaggi: ✅**",
            "**(8) Cambiare info Gruppo: ☑️**",
            "**(8) Cambiare info Gruppo: ✅**",
            "**Permessi aggiunti con successo**",
            "**Promosso da @sqdboyuwu**"

 ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 20])
