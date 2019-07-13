# drbot
A Python3 library for easily building devRant bots

## Using
To make a bot, all you need to do is extend the `BotBuilder` class and define an `onNotif()` method

```python
from drbot.botbuilder import BotBuilder, NotifType

# Testing setup
class MyBot(BotBuilder):
        
    onNotif(self, type, content):
        # Handle notifs here
        pass

# Create a bot
my_bot = MyBot("username", "password")

# Set how long the bot should wait between notif queries (in seconds)
interval = 10

# Start the bot
my_bot.start(interval)
```

That's it!

## Using the API
Every `BotBuilder` class has a built in API wrapper. This can be accessed through `self.api`, and contains the following methods:
```python
getUserInfo(username: str) -> dict

getUsername(user_id: int) -> str

postRant(body: str, tags: str) -> None

postComment(rant_id: int, content: str) -> None

getComment(comment_id: int) -> dict
```

The `BotBuilder` automatically handles login, sessions, notif management, and some data parsing. If you are looking to override these, you may be interested in the following API methods:
```python
login(username: str, password: str) -> None

hasAuthExpired() -> bool

getNotifs() -> list

clearNotifs() -> None

getUserId(username: str) -> int
```

## Installing
This library is avalible on PYPI. 

With `python3.7` and `python3-pip` installed, run:
```
pip3 install drbot
```

to install `drbot`