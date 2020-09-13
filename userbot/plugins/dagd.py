"""DA.GD helpers in @UniBorg
Available Commands:
.isup URL
.dns google.com
.url <long url>
.unshort <short url>"""
from telethon import events
import os
import requests
import json
from userbot.utils import admin_cmd


@borg.on(admin_cmd("dns (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/dns/{}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await event.edit("I record DNS di {} lo sono\n{}".format(input_str, response_api))
    else:
        await event.edit("non riesco a trovare {} su Internet".format(input_str))


@borg.on(admin_cmd("url (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url={}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await event.edit("Generato {} per {}.".format(response_api, input_str))
    else:
        await event.edit("qualcosa è sbagliato. per favore riprova più tardi.")


@borg.on(admin_cmd("unshort (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if not input_str.startswith("http"):
        input_str = "http://" + input_str
    r = requests.get(input_str, allow_redirects=False)
    if str(r.status_code).startswith('3'):
        await event.edit("URL di input: {} \nURL reindirizzato: {}".format(input_str, r.headers["Location"]))
    else:
        await event.edit("URL di input {} restituito status_code{}".format(input_str, r.status_code))
