from mycroft import MycroftSkill, intent_handler
from adapt.intent import IntentBuilder
import requests
import json


class RedditNews(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder("").optionally("Pre").require("News").require("Reddit"))
    def handle_news_reddit(self, message):
        r = requests.get("https://reddit.com/r/worldnews/hot/.json", headers={"User-Agent": "mycroft:reddit-news-skill:v0.1 (by /u/makeworld)"})
        data = r.json()
        headlines = ""
        for post in data["data"]["children"][:5]:  # First five posts
            headline = post["data"]["title"]
            if headline[-1:] != ".":  # Add a period at the end to make mycroft pause
                headline += "."
            # Add a space at the end, because all headlines will be in one string
            headline += " "
            # Add it to the string of headlines
            headlines += headline
        self.speak_dialog('here.news', data={"headlines": headlines})


def create_skill():
    return RedditNews()

