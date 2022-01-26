'''YTPlaylistDL, An Telegram Bot Project
Copyright (c) 2021 Anjana Madu <https://github.com/AnjanaMadu>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>'''

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

@Client.on_message(filters.command("start"))
async def start_msg(client, message):
	await message.reply_text(
		f"Hi {message.from_user.mention},If you need any help, Just click help button.\n\nProject by @Harp_Tech",
		reply_markup=InlineKeyboardMarkup(
                                [[
					InlineKeyboardButton("⭕ Channel ⭕", url="https://t.me/TeleRoidGroup"),
					InlineKeyboardButton("😇 Support", url="https://t.me/TeleRoid14")
				]],
				[[
					InlineKeyboardButton("🆘 Help", callback_data=f"help"),
					InlineKeyboardButton("👥 About", callback_data=f"about")
				]]
			),
		quote=True)


@Client.on_callback_query()
async def cb_handler(client, update):

    cb_data = update.data
    if "about" in cb_data:
        await update.message.edit(
            text=Translation.ABOUT_TEXT,
            parse_mode="html",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
					[
						InlineKeyboardButton("🆘 Help", callback_data="help"),
						InlineKeyboardButton("🐱 Github", url="https://t.me/MoviesFlixers_DL")
					],
					[
						InlineKeyboardButton("🔙 Back", callback_data="back") 
					]
	        ]
            )
        )

    elif "help" in cb_data:
        await update.message.edit(
            text=Translation.HELP_USER,
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                                        [
						InlineKeyboardButton("More Bots ", url="https://t.me/TheTeleRoid")
					],
					[
						InlineKeyboardButton("👥 About", callback_data="about"),
						InlineKeyboardButton("🔙 Back", callback_data="back")
					]
                ]
            )
        )

    elif "back" in cb_data:
        await update.message.edit(
            text=Translation.START_TEXT.format(update.from_user.mention),
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
						InlineKeyboardButton("⭕ Channel ⭕", url="https://t.me/TeleRoidGroup"),
						InlineKeyboardButton("😇 Support", url="https://t.me/TeleRoid14")
					],
					[
						InlineKeyboardButton("👥 About", callback_data="about"),
						InlineKeyboardButton("🆘 Help", callback_data="help")
					], 
                                        [
						InlineKeyboardButton("🐱 Follow Me ", url="https://GitHub.com/PredatorHackerzZ"),
						InlineKeyboardButton("🚸 Powered By", url="https://t.me/MoviesFlixers_DL")
	            ]
                ]
            )
        )

@Client.on_callback_query()
async def button(bot, update):
 
      if  'close'  in update.data:
                await update.message.delete()
