from api.api import API
from threading import Thread
import time
from enum import Enum

class NotifType():
    UNKNOWN = 0
    UPVOTE = 1
    COMMENT  =1
    MENTION = 3
    SUBSCRIPTION = 4

NotifType_conversion = {
    "content_vote": NotifType.UPVOTE,
    "comment_content": NotifType.COMMENT,
    "comment_mention": NotifType.MENTION,
    "subscription": NotifType.SUBSCRIPTION
}

def toNotifType(type_str: str):
    """ Convert API type to NotifType """

    # Check if type is valid
    if type_str in NotifType_conversion:
        return NotifType_conversion[type_str]
    else:
        return NotifType.UNKNOWN

class BotBuilder:
    """ A tool for building devRant bots. Extend this class """

    __runner_thread: Thread
    running: bool

    __username: str
    __password: str

    __interval: int

    __raw_notifs: list

    def __init__(self, username: str, password: str):
        self.api = API()

        self.__username = username
        self.__password = password

        self.api.login(username, password)

    def onNotif(self, type: NotifType, content: dict):
        pass

    def start(self, interval_secs: int, threaded=False):
        self.running = True
        self.__interval = interval_secs
        
        # Create a thread for the bot
        self.__runner_thread = Thread(target=self.__run)

        # Start the bot thread
        self.__runner_thread.start()

        # Check if we should join the bot thread or not
        if not threaded:
            self.__runner_thread.join()
    
    def stop(self):
        self.running = False

    def __run(self):
        while self.running:
            # Check for expired auth
            if self.api.hasAuthExpired():
                # Log in again
                self.api.login(self.username, self.password)

            # Fetch notifs
            self.__raw_notifs = self.api.getNotifs()

            # Clear notifs
            self.api.clearNotifs()

            # Convert raw notif data to something more useful
            notif_feed = []

            for notif in self.__raw_notifs:
                # skip if already read
                if notif["read"]:
                    continue

                # Just doing some type conversion
                del notif["read"]
                notif["type"] = toNotifType(notif["type"])

                # Convert a user ID to a username
                notif["username"] = self.api.getUsername(notif["uid"])
                del notif["uid"]

                # Add to list
                notif_feed.append(notif)

            # Call onNotif with new data
            for notif in notif_feed:
                # Store type in buffer
                notif_type = notif["type"]

                # Strip type from notif
                del notif["type"]

                # Call callback
                self.onNotif(notif_type, notif)

            # Sleep for interval
            time.sleep(self.__interval)
