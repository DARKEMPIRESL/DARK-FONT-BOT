import random
from pyrogram import Client, filters


STICKERS = ["CAACAgUAAxkBAAEBH8Bin1OzuCzYzLOa9ZBiwK7026VX_QACCwUAAqp1AAFVU_BXBmgkKpwkBA", "CAACAgUAAxkBAAEBH8xin1P4sM9rspV0wcd9uAvHLFkoSwAC_wcAAs6U-FR6JwIKrfGfvCQE"]


# Help Message
@Client.on_message(filters.private & filters.command(["help"]))
async def _help(_, msg):
	STICKER = random.choice(STICKERS)
	await msg.reply_sticker(STICKER)
