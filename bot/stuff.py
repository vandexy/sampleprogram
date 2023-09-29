#    This file is part of the CompressorQueue distribution.
#    Copyright (c) 2021
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/> .

from .worker import *


async def up(event):
    if not event.is_private:
        return
    stt = dt.now()
    ed = dt.now()
    v = ts(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"🌋Pɪɴɢ = {ms}ms"
    await event.reply(v + "\n" + p)


async def start(event):
    await event.reply(
        f"Hi `{event.sender.first_name}`\nDo I Need To Say Something?",
        buttons=[
            [Button.inline("HELP", data="ihelp")],
            [
                Button.url("Modified", url="https://t.me/tomanguy"),
                Button.url("DEVELOPER", url="t.me/tomanguy"),
            ],
        ],
    )


async def help(event):
    await event.reply(
        "This Bot Is Not Public**\n\n✔️Only Authenticated Users Will Use This Bot"
    )


async def ihelp(event):
    await event.edit(
        "This Bot Is Not Public**\n\n✔️Only Authenticated Users Will Use This Bot",
        buttons=[Button.inline("BACK", data="beck")],
    )


async def beck(event):
    await event.edit(
        f"Hi `{event.sender.first_name}`\nThis Bot Is Not Public**\n\n✔️Only Authenticated Users Will Use This Bot",
        buttons=[
            [Button.inline("HELP", data="ihelp")],
            [
                Button.url("Modified", url="https://t.me/tomanguy"),
                Button.url("DEVELOPER", url="t.me/tomanguy"),
            ],
        ],
    )
