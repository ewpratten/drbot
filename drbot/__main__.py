from botbuilder import BotBuilder, NotifType
import os.path

# Testing setup
class MyBot(BotBuilder):
        
    def onNotif(self, type, content):
        
        if type == NotifType.MENTION:
            self.api.postComment(content["rant_id"], f"Hello @{content['username']}\n-------------\n\n{content}")
            print(self.api.getComment(content["comment_id"]))
        else:
            print(type, content)

# Fetch password from config file
password = ""
with open(os.path.expanduser("~") + "/.n4xuspasswd", "r") as fp:
    password = fp.read()
    fp.close()

# Create a new bot
my_bot = MyBot("n4xus", password)

my_bot.start(10)