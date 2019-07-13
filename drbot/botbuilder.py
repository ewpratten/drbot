from api.api import API
from threading import Thread
import time
from enum import Enum

class NotifType():
    UPVOTE = 1
    COMMENT  =1
    MENTION = 3
    SUBSCRIPTION = 4

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

            # Clear notifs

            # Call onNotif with new data

            # Sleep for interval
            time.sleep(self.__interval)
