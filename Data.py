from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """πHey!

 ** I am Font Gen Bot**with many advanced features. 
 Just send your Text and see what happens...π
 
 
 Devoloper : [π―πππ π°πππππ](https://t.me/ImDark_Empire)
 Powered by :[Team SL Botsπ±π°](https://t.me/SLBotOfficial)


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
    home_button = [[InlineKeyboardButton(text="ποΈ Return Home ποΈ", callback_data="home")]]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("π€ Bot Status and More Bots π€", url="https://t.me/SLBotOfficial/28")],
        [
            InlineKeyboardButton("β How to Use β", callback_data="help"),
            InlineKeyboardButton("βΎοΈ About βΎοΈ", callback_data="about")
        ],
        [InlineKeyboardButton("β₯ More Amazing bots β₯", url="https://t.me/SLBotOfficial")],
        [InlineKeyboardButton("π« Support Group π«", url="https://t.me/SLBotsChat")],
    ]
