import requests
from exceptions import *
import time


class API:

    auth_token = {"id": "", "key": "", "user": "", "expiration": 0}

    def __init__(self, app=3, plat=2):
        self.app_id = app
        self.plat_id = plat

    def login(self, username: str, password: str):
        """ Authenticate with the devRant API """

        # Deal with newlines from reading files
        username = username.strip()
        password = password.strip()

        # Ask the API for tokens
        response = requests.post("https://devrant.com/api/users/auth-token", data={
                                 "username": username.lower(), "password": password, "app": self.app_id, "plat": self.plat_id}).json()
        print(response)

        # Check for a failed response
        if not response["success"]:
            # Check for invalid creds
            if response["error"] == "Invalid login credentials entered. Please try again.":
                raise FailedLoginException
            else:
                # Something else went wrong
                raise UnknownAPIException

        # Set auth data
        self.auth_token["id"] = response["auth_token"]["id"]
        self.auth_token["key"] = response["auth_token"]["key"]
        self.auth_token["user"] = response["auth_token"]["user_id"]
        self.auth_token["expiration"] = response["auth_token"]["expire_time"]

    def hasAuthExpired(self):
        """ Checks if the current time is past the auth token expiration time """
        return round(time.time()) >= self.auth_token["expiration"]

    def getUserId(self, username: str):
        """ Gets the API's database ID for a given user. This is rarely needed  """

        # Ask the API for an ID
        response = requests.get("https://devrant.com/api/get-user-id", params={
                                "username": username, "app": self.app_id, "plat": self.plat_id}).json()

        # Check that the user actually exists
        if not response["success"]:
            raise InvalidUserException

        # Return the id
        return response["user_id"]

    def getUserInfo(self, username: str):
        """ Get a user's profile information from the API """

        # Find the user id
        user_id = self.getUserId(username)

        # Ask the API for a profile
        response = requests.get(f"https://devrant.com/api/users/{user_id}", params={
                                "app": self.app_id, "plat": self.plat_id}).json()

        # Check for an error that should never exist
        if not response["success"]:
            raise UnknownAPIException

        # Return the user's profile
        return response["profile"]

    def getRantById(self, id: int):
        pass

    def postRant(self, body: str, tags: str):
        pass

    def postComment(self, content):
        pass

    def getNotifs(self):
        """ Get a list of Notifs from the API """

        # Ask the API for notif data
        response = requests.get("https://devrant.com/api/users/me/notif-feed", params={
                                "app": self.app_id, "plat": self.plat_id, "user_id": self.auth_token["user"], "token_id": self.auth_token["id"], "token_key": self.auth_token["key"]}).json()
        
        # Check for an error that should never exist
        if not response["success"]:
            raise UnknownAPIException

    def clearNotifs(self):
        pass
