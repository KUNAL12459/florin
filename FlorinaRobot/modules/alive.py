from telethon import events, Button, custom
import re, os
from FlorinaRobot.events import register
from FlorinaRobot import telethn as love
from FlorinaRobot import telethn as tgbot
PHOTO = "https://telegra.ph/file/63ec234e1be1f16345e69.jpg"
@register(pattern=("/alive"))
async def awake(event):
  FlorinaRobot = event.sender.first_name
  FlorinaRobot = "**𝗪𝗛𝗢 𝗔𝗠 𝗜 🥺❓** \n\n"
  FlorinaRobot += "**I'ᴍ FlorinaRobot💞, Yᴏᴜʀ Hᴇᴀʀᴛʙᴇᴀᴛ❤️🙈*\n\n"
  FlorinaRobot += "**I'ᴍ Wᴏʀᴋɪɴɢ Oɴ Lᴏᴠᴇ 😜**\n\n"
  FlorinaRobot += "**Mʏ Lᴏᴠᴇ 🥰 :**  [ 🇷 ØΜΔŇŦIĆ❤️ 🇸 ĦΔ¥ΔŘ 🇹 ỮŞĦΔŘ](t.me/TUSHAR204)\n\n"
  FlorinaRobot += "**Aʙᴏᴜᴛ Mʏ Lᴏᴠᴇ 🤩 :** [「ƬƲֆӇƛƦ ✘ ԼƠꪜЄԼƳ」🇮🇳](t.me/ABOUTVEDMAT)\n\n"
  BUTTON = [[Button.url("𝗦𝗨𝗣𝗣𝗢𝗥𝗧🙂", "https://t.me/florina_support"), Button.url("𝗨𝗣𝗗𝗔𝗧𝗘", "https://t.me/Florina_channel")]]
  await love.send_file(event.chat_id, PHOTO, caption=LOVELY,  buttons=BUTTON)
