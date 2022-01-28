# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from telethon.errors import (
    BotMethodInvalidError,
    ChatSendInlineForbiddenError,
    ChatSendMediaForbiddenError,
)

from . import LOG_CHANNEL, LOGS, Button, asst, eor, get_string, ultroid_cmd

REPOMSG = """
• **ULTROID USERBOT** •\n
• Repo - [Click Here](https://github.com/PredatorHackerzZ/Renamer-Bot)
• Addons - [Click Here](https://t.me/TellyFun_Official)
• Support - @TeleRoid14
"""

RP_BUTTONS = [
    [
        Button.url(get_string("bot_3"), "https://github.com/PredatorHackerzZ/Ultroid-UB"),
        Button.url("Addons", "https://t.me/TeleRoidGroup"),
    ],
    [Button.url("Support Group", "https://t.me/TeleRoid14")],
]

ULTSTRING = """🎇 **Thanks for Deploying Userbot!**

• Here, are the Some Basic stuff from, where you can Know, about its Usage."""


@ultroid_cmd(
    pattern="repo$",
    manager=True,
)
async def repify(e):
    try:
        q = await e.client.inline_query(asst.me.username, "")
        await q[0].click(e.chat_id)
        return await e.delete()
    except (
        ChatSendInlineForbiddenError,
        ChatSendMediaForbiddenError,
        BotMethodInvalidError,
    ):
        pass
    except Exception as er:
        LOGS.info("Error while repo command : " + str(er))
    await e.eor(REPOMSG)


@ultroid_cmd(pattern="ultroid$")
async def useUltroid(rs):
    button = Button.inline("Start >>", "initft_2")
    msg = await asst.send_message(
        LOG_CHANNEL,
        ULTSTRING,
        file="https://telegra.ph/file/cda94d1fd7e6519cdc1c9.jpg",
        buttons=button,
    )
    await eor(rs, f"**[Click Here]({msg.message_link})**")
