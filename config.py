
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "" # integer value, dont use ""
    API_HASH = ""
    TOKEN = ""  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    SESSION ="BQArz2uKal5QtRmxtlSRokb2iGQ1g8LFKGhYe-sh_Eqb8Z_lCxyT1YMc5Rj8wftbp3kQxauyTM4D46KwMXsdRBelE8Gq5g5Dk0b799JlIOBw1YhR16aYUS_8i_vrBhrx0skdiUZoE13GZQ7SvjMPfPieen9tiEkgyJLyIsTRZF3cTDXTT64wvQ4dqs8UVOqkaG_-1sZRKB8nK4-OQuBkDWJ0ATsuzxNXElcuZ00aoYi28o8AIl7lJL00E3wlpmY9RU2nWp3mXrbfesre8C-rDPwWZHlnQIyJylmLj7cYHAE3y83rJ6Q6jYvAXnuWDBEAdn6zzD1Vq6kJtXKaOVKRdlRFcwgosAA"
    OWNER_ID = 1929914544 # If you dont know, run the bot and do /id in your private chat with it, also an integer
    SUPPORT_CHAT = "LovelyXSupport"  # Your own group for support, do not add the @
    START_IMG = "https://te.legra.ph/file/59d555afd67ff0d9bd224.mp4"
    PM_IMG = ""
    EVENT_LOGS = ()  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= ""
    # RECOMMENDED
    DATABASE_URL = ""  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        "NGJS76JQ28V2LRPF"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "5LB4TAKPEKZ0"  # Get your API key from https://timezonedb.com/api

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    CHATBOT_API = "1929914544-fallen-brff33ffrb"
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
