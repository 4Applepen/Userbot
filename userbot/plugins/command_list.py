from telethon import events
import subprocess
import asyncio
import time


@command(pattern="^.cmds", outgoing=True)
async def install(event):
    if event.fwd_from:
        return
    cmd = "ls userbot/plugins"
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    _o = o.split("\n")
    o = "\n".join(_o)
    OUTPUT = f"**Elenco dei plugin: ** \n {o} \n \n ** SUGGERIMENTO: ** __Se vuoi conoscere i comandi per un plugin, esegui: -__ \n `.help <nome plugin>` ** senza il <>. **"
    await event.edit(OUTPUT)
