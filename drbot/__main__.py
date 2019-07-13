from botbuilder import BotBuilder
import os.path

# Testing setup
class MyBot(BotBuilder):
    # def __init__(self, username, password):
    #     super().__init__(username, password)
    
    def onNotif(self, type, content):
        print(type, content)

# Fetch password from config file
password = ""
with open(os.path.expanduser("~") + "/.devdnspasswd", "r") as fp:
    password = fp.read()
    fp.close()

# Create a new bot
my_bot = MyBot("devDNS", password)

my_bot.start(10)