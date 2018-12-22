from mycroft import MycroftSkill, intent_file_handler


class RedditNews(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('news.reddit.intent')
    def handle_news_reddit(self, message):
        self.speak_dialog('news.reddit')


def create_skill():
    return RedditNews()

