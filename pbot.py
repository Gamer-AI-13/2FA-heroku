import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from otp import generate
Developedbots = Client(
    "Pyrogram-example-bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)


START_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('SOURCE CODE', url="https://github.com/Gamer-AI-13/2FA-heroku")
        ]]
    ) 
@Developedbots.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        f""" Hai {update.from_user.mention} I'm a heroku Multi-Factor Authentication helper bot""", 
        disable_web_page_preview=True,
        reply_markup=START_BUTTON
    )
@Developedbots.on_message(filters.private & filters.incoming)
async def code(bot, update):
    otpop =generate(update.text)
    await update.reply_text(
        f""" your otp is: {otpop}""", 
        disable_web_page_preview=True,
        reply_markup=START_BUTTON
    )

Developedbots.run()
