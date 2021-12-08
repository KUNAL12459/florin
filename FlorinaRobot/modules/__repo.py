import os
from pyrogram import Client, filters
from pyrogram.types import *

from FlorinaRobot.conf import get_str_key
from FlorinaRobot import pbot

REPO_TEXT = "**A Powerful [FlorinaRobot](https://telegra.ph/file/bbaa5ef130c385e8333f8.jpg) to Make Your Groups Secured and Organized ! \n\n↼ Øwñêr ⇀ : 『 [OWNER](t.me/hehe860) 』\n╭──────────────\n┣─ » Python ~ 3.8.6\n┣─ » Update ~ Recently\n╰──────────────\n\n»»» @THN_BOTS_SUPPORT «««"
  
BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("⚡ ʀᴇᴘᴏꜱɪᴛᴏʀʏ🔥", url=f"https://github.com/KUNAL12459/FlorinaRobot"),
        InlineKeyboardButton(" ᴊᴏɪɴ 💫", url=f"https://t.me/florina_support"),
      ],[
        InlineKeyboardButton("florina owner ❣️", url="https://t.me/hehe860"),
        InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ ⚡", url="https://t.me/florina_support"),
      ],[
        InlineKeyboardButton("⚡ ᴜᴘᴅᴀᴛᴇꜱ ☑️", url="https://t.me/florina_channel"),
        InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ ➡️", url="https://t.me/hehe860"),
      ]]
    )
  
  
@pbot.on_message(filters.command(["repo"]))
async def repo(pbot, update):
    await update.reply_text(
        text=REPO_TEXT,
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
