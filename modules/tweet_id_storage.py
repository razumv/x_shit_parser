import json
import os


class TweetIdStorage:
    LATEST_TWEETS_ID_PATH = "latest_tweets_id.json"

    def get_last_tweet_id(self, username: str) -> str:
        if os.path.exists(self.LATEST_TWEETS_ID_PATH):
            with open(self.LATEST_TWEETS_ID_PATH, "r") as file:
                data = json.loads(file.read())
        else:
            data = {}

        return data.get(username, None)

    def save_last_tweet_id(self, username: str, tweet_id: str):
        if os.path.exists(self.LATEST_TWEETS_ID_PATH):
            with open(self.LATEST_TWEETS_ID_PATH, "r") as file:
                data = json.loads(file.read())
        else:
            data = {}

        data[username] = tweet_id

        with open(self.LATEST_TWEETS_ID_PATH, "w") as file:
            file.write(json.dumps(data))
