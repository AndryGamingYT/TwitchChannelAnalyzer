class Stream:
    __id: str
    __user_id: str
    __user_login: str
    __user_name: str
    __game_id: str
    __game_name: str
    __type: str
    __title: str
    __viewer_count: int
    __started_at: str
    __language: str
    __thumbnail_url: str
    __tag_ids: list[str]
    __is_mature: bool

    def __init__(self, id: str = None, user_id: str = None, user_login: str = None, user_name: str = None, game_id: str = None, game_name: str = None, type: str = None, title: str = None, viewer_count: int = None, started_at: str = None, language: str = None, thumbnail_url: str = None, tag_ids: list[str] = None, is_mature: bool = None):
        self.__id = id
        self.__user_id = user_id
        self.__user_login = user_login
        self.__user_name = user_name
        self.__game_id = game_id
        self.__game_name = game_name
        self.__type = type
        self.__title = title
        self.__viewer_count = viewer_count
        self.__started_at = started_at
        self.__language = language
        self.__thumbnail_url = thumbnail_url
        self.__tag_ids = tag_ids
        self.__is_mature = is_mature

    @property
    def id(self):
        return self.__id

    @property
    def user_id(self):
        return self.__user_id

    @property
    def user_login(self):
        return self.__user_login

    @property
    def user_name(self):
        return self.__user_name

    @property
    def game_id(self):
        return self.__game_id

    @property
    def game_name(self):
        return self.__game_name

    @property
    def type(self):
        return self.__type

    @property
    def title(self):
        return self.__title

    @property
    def viewer_count(self):
        return self.__viewer_count

    @property
    def started_at(self):
        return self.__started_at

    @property
    def language(self):
        return self.__language

    @property
    def thumbnail_url(self):
        return self.__thumbnail_url

    @property
    def tag_ids(self):
        return self.__tag_ids

    @property
    def is_mature(self):
        return self.__is_mature
