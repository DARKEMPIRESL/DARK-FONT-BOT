from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(bot, msg):
	user = await bot.get_me()
	mention = user["mention"]
  STICKERS = ["CAACAgUAAxkBAAEBH8Bin1OzuCzYzLOa9ZBiwK7026VX_QACCwUAAqp1AAFVU_BXBmgkKpwkBA", "CAACAgUAAxkBAAEBH8xin1P4sM9rspV0wcd9uAvHLFkoSwAC_wcAAs6U-FR6JwIKrfGfvCQE"]
    
  STICKER = random.choice(STICKERS)
    
await msg.reply_sticker(STICKER)
await bot.send_message(
		  msg.chat.id,
		  Data.START.format(msg.from_user.mention, mention),
		  reply_markup=InlineKeyboardMarkup(Data.buttons)
	                    )
