import requests

from Channel import Channel
from Stream import Stream


class TwitchRequest:
    __BASE_URL = "https://api.twitch.tv/helix"

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.headers = {
            "Client-ID": self.client_id,
            "Authorization": "Bearer " + self.get_access_token()
        }

    def get_access_token(self):
        url = "https://id.twitch.tv/oauth2/token?client_id={}&client_secret={}&grant_type=client_credentials"
        response = requests.post(url.format(self.client_id, self.client_secret))
        return response.json()["access_token"]

    def get_user_data(self, user_id):
        url = self.__BASE_URL + "/users/" + user_id
        response = requests.get(url, headers=self.headers)
        return response.json()

    def search_channels(self, query: str, first: int = 20, live_only: bool = False):
        url = self.__BASE_URL + "/search/channels"
        data = {'query': query}
        data['first'] = first
        data['live_only'] = live_only
        response = requests.get(url, data, headers=self.headers)

        channels: list[Channel] = []
        for channel in response.json().get("data"):
            channels.append(Channel(
                channel.get("broadcaster_language"),
                channel.get("broadcaster_login"),
                channel.get("display_name"),
                channel.get("game_id"),
                channel.get("game_name"),
                channel.get("id"),
                channel.get("is_live"),
                channel.get("tags_ids"),
                channel.get("thumbnail_url"),
                channel.get("title"),
                channel.get("started_at"),
            ))

        return channels

    def get_streams(self, user_login: str):
        url = self.__BASE_URL + "/streams"
        response = requests.get(url, {'user_login': user_login}, headers=self.headers)

        streams: list[Stream] = []
        for stream in response.json().get("data"):
            streams.append(Stream(
                stream.get("id"),
                stream.get("user_id"),
                stream.get("user_login"),
                stream.get("user_name"),
                stream.get("game_id"),
                stream.get("game_name"),
                stream.get("type"),
                stream.get("title"),
                stream.get("viewer_count"),
                stream.get("started_at"),
                stream.get("language"),
                stream.get("thumbnail_url"),
                stream.get("tag_ids"),
                stream.get("is_mature"),
            ))

        return streams

    def get_follows(self, user_id: str):
        url = self.__BASE_URL + "/users/follows"
        response = requests.get(url, {'to_id': user_id}, headers=self.headers)
        return response.json().get("total")
