from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """😎Hey!

 ** I am Font Gen Bot**with many advanced features. 
 Just send your Text and see what happens...😁
 
 
 Devoloper : [𝕯𝖆𝖗𝖐 𝕰𝖒𝖕𝖎𝖗𝖊](https://t.me/ImDark_Empire)
 Powered by :[Team SL Bots🇱🇰](https://t.me/SLBotOfficial)


"""

    # About Message
    ABOUT = """
**About This Bot** 
Bot created by @SLBotOfficial
Source Code : [Click Here](https://github.com/DARKEMPIRESL/DARK-FONT-BOT)
Framework : [Pyrogram](docs.pyrogram.org)
Language : [Python](www.python.org)
Developer : @ImDark_Empire
    """

    # Home Button
    home_button = [[InlineKeyboardButton(text="🏛️ Return Home 🏛️", callback_data="home")]]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🤖 Bot Status and More Bots 🤖", url="https://t.me/SLBotOfficial/28")],
        [
            InlineKeyboardButton("❔ How to Use ❔", callback_data="help"),
            InlineKeyboardButton("♾️ About ♾️", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/SLBotOfficial")],
        [InlineKeyboardButton("🛫 Support Group 🛫", url="https://t.me/SLBotsChat")],
    ]
