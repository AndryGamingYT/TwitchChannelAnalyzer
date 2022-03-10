from datetime import datetime


class Channel:
    __broadcaster_language: str
    __broadcaster_login: str
    __display_name: str
    __game_id: str
    __game_name: str
    __id: str
    __is_live: bool
    __tags_ids: list[str]
    __thumbnail_url: str
    __title: str
    __started_at: datetime

    def __init__(self, broadcaster_language: str = None, broadcaster_login: str = None, display_name: str = None, game_id: str = None, game_name: str = None, id: str = None, is_live: bool = None, tags_ids: list[str] = None, thumbnail_url: str = None, title: str = None, started_at: datetime = None):
        self.__broadcaster_language = broadcaster_language
        self.__broadcaster_login = broadcaster_login
        self.__display_name = display_name
        self.__game_id = game_id
        self.__game_name = game_name
        self.__id = id
        self.__is_live = is_live
        self.__tags_ids = tags_ids
        self.__thumbnail_url = thumbnail_url
        self.__title = title
        self.started_at = started_at

    @property
    def broadcaster_language(self):
        return self.__broadcaster_language

    @property
    def broadcaster_login(self):
        return self.__broadcaster_login

    @property
    def display_name(self):
        return self.__display_name

    @property
    def game_id(self):
        return self.__game_id

    @property
    def game_name(self):
        return self.__game_name

    @property
    def id(self):
        return self.__id

    @property
    def is_live(self):
        return self.__is_live

    @property
    def tags_ids(self):
        return self.__tags_ids

    @property
    def thumbnail_url(self):
        return self.__thumbnail_url

    @property
    def title(self):
        return self.__title

    @property
    def started_at(self):
        return self.__started_at

    @started_at.setter
    def started_at(self, value: datetime):
        """
        Args:
            started_at (datetime): UTC datetime
        """
        self.__started_at = value

    @started_at.setter
    def started_at(self, value: str):
        """
        Args:
            started_at (str): UTC datetime
        """
        self.__started_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ") if value else ""
