import pyrogram

import config

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)



from pyrogram import Client, idle
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "ShowJson",
        bot_token=config.BOT_TOKEN,
        api_id=config.API_ID,
        api_hash=config.API_HASH,
        plugins=dict(root="plugins"),
        workers=100
    )
app.start()
uname = (app.get_me()).username
print(f"@{uname} Deployed Successfully !")

idle()
