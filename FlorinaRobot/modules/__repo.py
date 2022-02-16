import os
from pyrogram import Client, filters
from pyrogram.types import *

from FlorinaRobot.conf import get_str_key
from FlorinaRobot import pbot

REPO_TEXT = "**A Powerful [Robot](https://telegra.ph/file/bbaa5ef130c385e8333f8.jpg) to Make Your Groups Secured and Organized ! \n\n↼ Øwñêr ⇀ : 『 [OWNER](t.me/hehe860) 』\n╭──────────────\n┣─ » Python ~ 3.8.6\n┣─ » Update ~ Recently\n╰──────────────\n\n»»» @ALEXIA_SUPPORT «««"
  
BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("⚡ 𝗦𝗼𝘂𝗿𝗰𝗲🔥", url=f"https://github.com/KUNAL12459/FlorinaRobot"),
        InlineKeyboardButton(" 𝗝𝗢𝗜𝗡 🤖", url=f"https://t.me/ALEXIA_SUPPORT"),
      ],[
        InlineKeyboardButton("𝗕𝗢𝗧 𝗢𝗪𝗡𝗘𝗥🇮🇳", url="https://t.me/Saur12p"),
        InlineKeyboardButton("𝗦𝗨𝗣𝗣𝗢𝗥𝗧 💬", url="https://t.me/ALEXIA_SUPPORT"),
      ],[
        InlineKeyboardButton("📡 𝗨𝗣𝗗𝗔𝗧𝗘𝗦 📡", url="https://t.me/ALEXIA_UPDATE"),
        InlineKeyboardButton("𝗗𝗘𝗩𝗟𝗢𝗣𝗘𝗥 ➽", url="https://t.me/Saur12p"),
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
